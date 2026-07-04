"""Generate the primary July 5 adaptive plan after v301-v320 scores.

The v301-v320 batch is already a composite plan: public COPD pruning,
mediastinum thymus/nodes, selected ASSOC/DIFF maps, and the v185 private KEEP
hedge. This generator treats those scored composites as sources and creates
controlled follow-ups by toggling one dimension at a time, instead of sending
the older post-ASSOC/DIFF generator through the same data twice.
"""
from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

try:
    from cohortx_ops import PlanItem, public_score, read_plan, read_submissions
    from v281_300_assoc_diff import (
        CONDITION_GROUPS,
        MEDIASTINUM,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )
except ModuleNotFoundError:
    from src.cohortx_ops import PlanItem, public_score, read_plan, read_submissions
    from src.v281_300_assoc_diff import (
        CONDITION_GROUPS,
        MEDIASTINUM,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
HIGH_VOLUME_SOFT_LIMIT = 1000
HIGH_VOLUME_PRIORITY_PENALTY = 0.004
HIGH_VOLUME_EXCESS_PENALTY_PER_100 = 0.001
BUCKETS = ("ASSOCIATION", "DIFF")
BASE_BEST = SUBMISSIONS / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
BASE_PRIVATE = SUBMISSIONS / "v185_private_kw.csv"
CKD = "CKD"
UTI = "UTI"
DIABETES = "Diabetes"
PNEUMONIA = "Pneumonia"
PRIVATE_KEEP_ALL = (CKD, UTI, DIABETES, PNEUMONIA)
PRIVATE_KEEP_GROUPS: tuple[tuple[str, tuple[str, ...], float], ...] = (
    ("v185keep", PRIVATE_KEEP_ALL, 0.020),
    ("no_v185keep", (), 0.018),
    ("v185_ckd_uti", (CKD, UTI), 0.016),
    ("v185_diab_pneu", (DIABETES, PNEUMONIA), 0.015),
    ("v185_ckd", (CKD,), 0.012),
    ("v185_uti", (UTI,), 0.011),
    ("v185_diabetes", (DIABETES,), 0.010),
    ("v185_pneumonia", (PNEUMONIA,), 0.009),
)
ASSOC_VARIANTS: tuple[tuple[str, tuple[str, ...] | None, tuple[str, ...] | None, float], ...] = (
    ("assocdiff", None, None, 0.020),
    ("assoc_only", ("ASSOCIATION",), None, 0.018),
    ("diff_only", ("DIFF",), None, 0.010),
    ("no_assocdiff", (), None, 0.008),
    ("pulmonary_assocdiff", None, CONDITION_GROUPS["pulmonary"], 0.014),
    ("cardiorenal_assocdiff", None, CONDITION_GROUPS["cardiorenal"], 0.014),
    ("endocrine_assocdiff", None, CONDITION_GROUPS["endocrine"], 0.012),
    ("ent_gi_derm_assocdiff", None, CONDITION_GROUPS["ent_gi_derm"], 0.011),
    ("neuro_rheum_assocdiff", None, CONDITION_GROUPS["neuro_rheum"], 0.010),
)
MED_VARIANTS: tuple[tuple[str, bool, float], ...] = (
    ("med_keep", False, 0.012),
    ("no_med_add", True, 0.010),
)


@dataclass(frozen=True)
class ScoredJuly4Item:
    item: PlanItem
    score: float
    delta: float


@dataclass(frozen=True)
class Candidate:
    source: Path
    slug: str
    message: str
    notes: str
    priority: float
    private_keep_conditions: tuple[str, ...]
    drop_mediastinum: bool = False
    assoc_buckets: tuple[str, ...] | None = None
    assoc_conditions: tuple[str, ...] | None = None


def safe_slug(value: str) -> str:
    value = re.sub(r"^v\d+_", "", value.removesuffix(".csv"))
    value = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return value[:58]


def scores_by_file() -> dict[str, float]:
    scores: dict[str, float] = {}
    for row in read_submissions():
        score = public_score(row)
        if score is None or row.get("status") != "complete":
            continue
        scores[row["fileName"]] = max(score, scores.get(row["fileName"], float("-inf")))
    return scores


def scored_items(plan_path: Path) -> list[ScoredJuly4Item]:
    scores = scores_by_file()
    anchor_score = scores.get(BASE_BEST.name)
    if anchor_score is None:
        raise RuntimeError(f"Missing public anchor score for {BASE_BEST.name}.")

    out: list[ScoredJuly4Item] = []
    missing: list[str] = []
    for item in read_plan(plan_path):
        score = scores.get(item.file.name)
        if score is None:
            missing.append(item.file.name)
            continue
        out.append(ScoredJuly4Item(item=item, score=score, delta=score - anchor_score))

    if missing:
        sample = ", ".join(missing[:5])
        raise RuntimeError(
            f"{len(missing)} planned submissions are not scored yet: {sample}. "
            "Run this after the July 4 batch is submitted and complete."
        )
    return out


def usable_sources(items: list[ScoredJuly4Item]) -> list[ScoredJuly4Item]:
    selected = [item for item in items if item.delta >= 0.0]
    selected.sort(key=lambda item: (item.delta, item.score, item.item.file.name), reverse=True)
    if not selected:
        raise RuntimeError(
            "No July 4 composite matched or beat the v296 public anchor. "
            "Use the July 5 public contingency instead of promoting a losing composite."
        )
    return selected[:8]


def apply_private_keep_choice(df: pd.DataFrame, base: pd.DataFrame, private: pd.DataFrame, conditions: tuple[str, ...]) -> None:
    selected = set(conditions)
    for condition in PRIVATE_KEEP_ALL:
        source = private if condition in selected else base
        set_codes(df, condition, "KEEP", get_codes(source, condition, "KEEP"))


def apply_assoc_choice(
    df: pd.DataFrame,
    source: pd.DataFrame,
    buckets: tuple[str, ...] | None,
    conditions: tuple[str, ...] | None,
) -> None:
    selected_buckets = set(BUCKETS if buckets is None else buckets)
    selected_conditions = None if conditions is None else set(conditions)
    for condition in df["Condition"]:
        for bucket in BUCKETS:
            if condition in PUBLIC_ASSOC_DIFF_EMPTY:
                set_codes(df, condition, bucket, [])
            elif bucket in selected_buckets and (selected_conditions is None or condition in selected_conditions):
                set_codes(df, condition, bucket, get_codes(source, condition, bucket))
            else:
                set_codes(df, condition, bucket, [])


def candidate_frame(candidate: Candidate) -> pd.DataFrame:
    source = pd.read_csv(candidate.source)
    base = pd.read_csv(BASE_BEST)
    private = pd.read_csv(BASE_PRIVATE)
    df = source.copy()
    if candidate.drop_mediastinum:
        set_codes(df, MEDIASTINUM, "KEEP", get_codes(base, MEDIASTINUM, "KEEP"))
    apply_private_keep_choice(df, base, private, candidate.private_keep_conditions)
    apply_assoc_choice(df, source, candidate.assoc_buckets, candidate.assoc_conditions)
    return df


def dataframe_change_volume(base: pd.DataFrame, candidate: pd.DataFrame) -> int:
    total = 0
    for condition in base["Condition"]:
        for bucket in ("KEEP", *BUCKETS):
            before = set(get_codes(base, condition, bucket))
            after = set(get_codes(candidate, condition, bucket))
            total += len(after - before) + len(before - after)
    return total


def high_volume_penalty(volume: int) -> float:
    if volume <= HIGH_VOLUME_SOFT_LIMIT:
        return 0.0
    excess_units = (volume - HIGH_VOLUME_SOFT_LIMIT) / 100.0
    return HIGH_VOLUME_PRIORITY_PENALTY + (excess_units * HIGH_VOLUME_EXCESS_PENALTY_PER_100)


def candidate_pool(items: list[ScoredJuly4Item]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for rank, source in enumerate(usable_sources(items), start=1):
        source_slug = safe_slug(source.item.file.name)
        rank_bonus = max(0.0, 0.010 - (rank * 0.001))
        for med_slug, drop_mediastinum, med_bonus in MED_VARIANTS:
            for private_slug, private_conditions, private_bonus in PRIVATE_KEEP_GROUPS:
                for assoc_slug, assoc_buckets, assoc_conditions, assoc_bonus in ASSOC_VARIANTS:
                    if med_slug == "med_keep" and private_slug == "v185keep" and assoc_slug == "assocdiff":
                        continue
                    slug = f"{source_slug}_{med_slug}_{private_slug}_{assoc_slug}"
                    message = f"{source_slug} {med_slug} {private_slug} {assoc_slug}"
                    notes = (
                        f"post-July4 source {source.item.file.name} ({source.score:.5f}, {source.delta:+.5f} vs v296); "
                        f"med={'drop' if drop_mediastinum else 'keep'}, "
                        f"private_keep={'+'.join(private_conditions) if private_conditions else 'none'}, "
                        f"assoc={assoc_slug}"
                    )
                    candidates.append(Candidate(
                        source=source.item.file,
                        slug=slug,
                        message=message,
                        notes=notes,
                        priority=source.delta + rank_bonus + med_bonus + private_bonus + assoc_bonus,
                        private_keep_conditions=private_conditions,
                        drop_mediastinum=drop_mediastinum,
                        assoc_buckets=assoc_buckets,
                        assoc_conditions=assoc_conditions,
                    ))
    base = pd.read_csv(BASE_BEST)
    volume_cache: dict[int, int] = {}

    def sort_key(candidate: Candidate) -> tuple[float, int, str]:
        volume = volume_cache.setdefault(
            id(candidate),
            dataframe_change_volume(base, candidate_frame(candidate)),
        )
        adjusted_priority = candidate.priority - high_volume_penalty(volume)
        return adjusted_priority, -volume, candidate.slug

    return sorted(candidates, key=sort_key, reverse=True)


def existing_versions() -> set[int]:
    versions: set[int] = set()
    for path in SUBMISSIONS.glob("v*.csv"):
        match = re.match(r"v(\d+)_", path.name)
        if match:
            versions.add(int(match.group(1)))
    return versions


def write_candidates(candidates: list[Candidate], start_version: int, out_plan: Path) -> list[Path]:
    target_versions = set(range(start_version, start_version + TARGET_COUNT))

    def local_version(path: Path) -> int | None:
        match = re.match(r"v(\d+)_", path.name)
        return int(match.group(1)) if match else None

    existing_keys = {
        dataframe_key(pd.read_csv(path))
        for path in SUBMISSIONS.glob("*.csv")
        if local_version(path) not in target_versions
    }
    used_versions = existing_versions() - target_versions
    remote_filenames = {row.get("fileName", "") for row in read_submissions()}
    rows: list[dict[str, str]] = []
    written: list[Path] = []
    seen_slugs: set[str] = set()
    version = start_version

    for candidate in candidates:
        if len(written) >= TARGET_COUNT:
            break
        if candidate.slug in seen_slugs:
            continue
        seen_slugs.add(candidate.slug)
        df = candidate_frame(candidate)
        key = dataframe_key(df)
        if key in existing_keys:
            continue
        while version in used_versions:
            version += 1
        path = SUBMISSIONS / f"v{version}_{candidate.slug}.csv"
        if path.exists() and path.name in remote_filenames:
            raise RuntimeError(f"Refusing to overwrite remotely submitted file: {path.relative_to(ROOT)}")
        if path.exists() and version not in target_versions:
            raise RuntimeError(f"Refusing to overwrite existing submission: {path.relative_to(ROOT)}")
        df.to_csv(path, index=False)
        existing_keys.add(key)
        used_versions.add(version)
        written.append(path)
        rows.append({
            "file": str(path.relative_to(ROOT)),
            "message": f"v{version}: {candidate.message}"[:120],
            "notes": candidate.notes,
        })
        version += 1

    if len(written) < TARGET_COUNT:
        raise RuntimeError(f"Only generated {len(written)} unique post-July4 candidates; expected {TARGET_COUNT}.")

    out_plan.parent.mkdir(parents=True, exist_ok=True)
    with out_plan.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["file", "message", "notes"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prior-plan", type=Path, default=ROOT / "plans" / "2026-07-04.csv")
    parser.add_argument("--out-plan", type=Path, required=True)
    parser.add_argument("--start-version", type=int, default=341)
    args = parser.parse_args()

    prior_plan = args.prior_plan if args.prior_plan.is_absolute() else ROOT / args.prior_plan
    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    items = scored_items(prior_plan)
    candidates = candidate_pool(items)
    written = write_candidates(candidates, args.start_version, out_plan)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        raise SystemExit(f"not_ready: {exc}") from exc
