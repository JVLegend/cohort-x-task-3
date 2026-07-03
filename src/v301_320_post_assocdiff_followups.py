"""Generate adaptive follow-ups after the v281-v300 ASSOC/DIFF batch.

The July 3 plan tests whether curated ASSOC/DIFF nodes are public-neutral and
whether the new COPD/mediastinum public probes improve the v209 anchor. This
script turns those scored signals into v301-v320 candidates for the next quota:
combine public-safe ASSOC/DIFF variants with the best public-facing KEEP base
and with the v185 private KEEP hedge.
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
        BASE_PRIVATE,
        BASE_PUBLIC,
        COPD,
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
        BASE_PRIVATE,
        BASE_PUBLIC,
        COPD,
        MEDIASTINUM,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
PUBLIC_BASE_SLOTS = 6
ASSOC_DIFF_SLOTS = 10
BUCKETS = ("ASSOCIATION", "DIFF")


@dataclass(frozen=True)
class ScoredPlanItem:
    item: PlanItem
    score: float
    delta: float
    kind: str


@dataclass(frozen=True)
class Candidate:
    public_base: Path
    assoc_source: Path | None
    slug: str
    message: str
    notes: str
    priority: float
    public_keep_sources: tuple[Path, ...] = ()
    private_keep: bool = False
    buckets: tuple[str, ...] = BUCKETS


def safe_slug(value: str) -> str:
    value = re.sub(r"^v\d+_", "", value.removesuffix(".csv"))
    value = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return value[:42]


def scores_by_file() -> dict[str, float]:
    scores: dict[str, float] = {}
    for row in read_submissions():
        score = public_score(row)
        if score is None or row.get("status") != "complete":
            continue
        scores[row["fileName"]] = max(score, scores.get(row["fileName"], float("-inf")))
    return scores


def scored_items(plan_path: Path) -> list[ScoredPlanItem]:
    scores = scores_by_file()
    anchor_score = scores.get(BASE_PUBLIC.name)
    if anchor_score is None:
        raise RuntimeError(f"Missing public anchor score for {BASE_PUBLIC.name}.")

    out: list[ScoredPlanItem] = []
    missing: list[str] = []
    for item in read_plan(plan_path):
        score = scores.get(item.file.name)
        if score is None:
            missing.append(item.file.name)
            continue
        lower = item.file.name.lower()
        if "assocdiff" in lower:
            kind = "assocdiff"
        elif "copd" in lower or "_med_" in lower or "mediastinum" in lower:
            kind = "public_keep"
        else:
            kind = "other"
        out.append(ScoredPlanItem(item=item, score=score, delta=score - anchor_score, kind=kind))
    if missing:
        sample = ", ".join(missing[:5])
        raise RuntimeError(
            f"{len(missing)} planned submissions are not scored yet: {sample}. "
            "Run this after the ASSOC/DIFF batch is submitted and complete."
        )
    return out


def nonnegative(items: list[ScoredPlanItem], kind: str) -> list[ScoredPlanItem]:
    selected = [item for item in items if item.kind == kind and item.delta >= 0.0]
    return sorted(selected, key=lambda item: (item.delta, item.score, item.item.file.name), reverse=True)


def assoc_diff_candidates(items: list[ScoredPlanItem]) -> list[ScoredPlanItem]:
    selected = nonnegative(items, "assocdiff")[:ASSOC_DIFF_SLOTS]
    if selected:
        return selected
    raise RuntimeError(
        "No public-neutral ASSOC/DIFF candidate is available. "
        "Use the July 4 public contingency instead of promoting private-label probes."
    )


def public_base_candidates(items: list[ScoredPlanItem]) -> list[ScoredPlanItem]:
    selected = nonnegative(items, "public_keep")[:PUBLIC_BASE_SLOTS]
    anchor = ScoredPlanItem(
        item=PlanItem(file=BASE_PUBLIC, message="v209 anchor", notes="best public anchor"),
        score=0.0,
        delta=0.0,
        kind="public_keep",
    )
    return [anchor, *selected]


def public_condition(item: ScoredPlanItem) -> str | None:
    lower = item.item.file.name.lower()
    if "copd" in lower:
        return COPD
    if "_med_" in lower or "mediastinum" in lower:
        return MEDIASTINUM
    return None


def changed_public_conditions(source: pd.DataFrame, anchor: pd.DataFrame) -> list[str]:
    changed: list[str] = []
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        if get_codes(source, condition, "KEEP") != get_codes(anchor, condition, "KEEP"):
            changed.append(condition)
    return changed


def copy_changed_public_keep(df: pd.DataFrame, source: pd.DataFrame, anchor: pd.DataFrame) -> None:
    for condition in changed_public_conditions(source, anchor):
        set_codes(df, condition, "KEEP", get_codes(source, condition, "KEEP"))


def copy_assoc_diff(df: pd.DataFrame, source: pd.DataFrame, buckets: tuple[str, ...]) -> None:
    for condition in source["Condition"]:
        if condition in PUBLIC_ASSOC_DIFF_EMPTY:
            continue
        for bucket in buckets:
            set_codes(df, condition, bucket, get_codes(source, condition, bucket))
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        for bucket in BUCKETS:
            set_codes(df, condition, bucket, [])


def copy_private_keep(df: pd.DataFrame, private: pd.DataFrame) -> None:
    for condition in private["Condition"]:
        if condition in PUBLIC_ASSOC_DIFF_EMPTY:
            continue
        set_codes(df, condition, "KEEP", get_codes(private, condition, "KEEP"))


def candidate_frame(candidate: Candidate) -> pd.DataFrame:
    df = pd.read_csv(candidate.public_base)
    anchor = pd.read_csv(BASE_PUBLIC)
    for source_path in candidate.public_keep_sources:
        copy_changed_public_keep(df, pd.read_csv(source_path), anchor)
    if candidate.private_keep:
        copy_private_keep(df, pd.read_csv(BASE_PRIVATE))
    if candidate.assoc_source is not None:
        copy_assoc_diff(df, pd.read_csv(candidate.assoc_source), candidate.buckets)
    return df


def candidate_pool(items: list[ScoredPlanItem]) -> list[Candidate]:
    assoc_items = assoc_diff_candidates(items)
    public_bases = public_base_candidates(items)
    public_items = [item for item in public_bases if item.item.file != BASE_PUBLIC]
    copd_bases = [item for item in public_items if public_condition(item) == COPD][:4]
    med_bases = [item for item in public_items if public_condition(item) == MEDIASTINUM][:2]
    candidates: list[Candidate] = []

    for copd in copd_bases:
        copd_slug = safe_slug(copd.item.file.name)
        for med in med_bases:
            med_slug = safe_slug(med.item.file.name)
            candidates.append(Candidate(
                public_base=copd.item.file,
                public_keep_sources=(med.item.file,),
                assoc_source=None,
                slug=f"{copd_slug}_{med_slug}_v185keep",
                message=f"{copd_slug} plus {med_slug} and v185 KEEP",
                notes=(
                    f"public-public combo from {copd.item.file.name} ({copd.score:.5f}, {copd.delta:+.5f}) "
                    f"and {med.item.file.name} ({med.score:.5f}, {med.delta:+.5f}) plus v185 private KEEP"
                ),
                priority=copd.delta + med.delta + 0.045,
                private_keep=True,
            ))
            for assoc in assoc_items[:4]:
                assoc_slug = safe_slug(assoc.item.file.name)
                candidates.append(Candidate(
                    public_base=copd.item.file,
                    public_keep_sources=(med.item.file,),
                    assoc_source=assoc.item.file,
                    slug=f"{copd_slug}_{med_slug}_{assoc_slug}_v185keep",
                    message=f"{copd_slug} plus {med_slug} plus {assoc_slug} and v185 KEEP",
                    notes=(
                        f"public-public combo {copd.item.file.name} ({copd.score:.5f}, {copd.delta:+.5f}) "
                        f"+ {med.item.file.name} ({med.score:.5f}, {med.delta:+.5f}) "
                        f"+ public-neutral ASSOC/DIFF {assoc.item.file.name} ({assoc.score:.5f}, {assoc.delta:+.5f}) "
                        "plus v185 private KEEP"
                    ),
                    priority=copd.delta + med.delta + assoc.delta + 0.060,
                    private_keep=True,
                ))

    for assoc in assoc_items:
        assoc_slug = safe_slug(assoc.item.file.name)
        candidates.append(Candidate(
            public_base=BASE_PUBLIC,
            assoc_source=assoc.item.file,
            slug=f"v209_{assoc_slug}_v185keep",
            message=f"v209 {assoc_slug} plus v185 private KEEP",
            notes=f"public-neutral ASSOC/DIFF hedge {assoc.item.file.name} ({assoc.score:.5f}, {assoc.delta:+.5f}) plus v185 KEEP",
            priority=assoc.delta + 0.010,
            private_keep=True,
        ))
        for bucket in BUCKETS:
            candidates.append(Candidate(
                public_base=BASE_PUBLIC,
                assoc_source=assoc.item.file,
                slug=f"v209_{assoc_slug}_{bucket.lower()}_v185keep",
                message=f"v209 {assoc_slug} {bucket} plus v185 KEEP",
                notes=f"bucket isolation from {assoc.item.file.name} ({assoc.score:.5f}, {assoc.delta:+.5f})",
                priority=assoc.delta + 0.005,
                private_keep=True,
                buckets=(bucket,),
            ))

    for public in public_bases:
        public_slug = safe_slug(public.item.file.name)
        for assoc in assoc_items:
            assoc_slug = safe_slug(assoc.item.file.name)
            if public.item.file == BASE_PUBLIC:
                continue
            candidates.append(Candidate(
                public_base=public.item.file,
                assoc_source=assoc.item.file,
                slug=f"{public_slug}_{assoc_slug}",
                message=f"{public_slug} plus {assoc_slug}",
                notes=(
                    f"public KEEP base {public.item.file.name} ({public.score:.5f}, {public.delta:+.5f}) "
                    f"plus public-neutral ASSOC/DIFF {assoc.item.file.name} ({assoc.score:.5f}, {assoc.delta:+.5f})"
                ),
                priority=public.delta + assoc.delta + 0.020,
            ))
            candidates.append(Candidate(
                public_base=public.item.file,
                assoc_source=assoc.item.file,
                slug=f"{public_slug}_{assoc_slug}_v185keep",
                message=f"{public_slug} plus {assoc_slug} and v185 KEEP",
                notes=(
                    f"best public KEEP base {public.item.file.name} ({public.score:.5f}, {public.delta:+.5f}) "
                    f"plus ASSOC/DIFF hedge {assoc.item.file.name} and v185 private KEEP"
                ),
                priority=public.delta + assoc.delta + 0.030,
                private_keep=True,
            ))

    for public in public_bases:
        if public.item.file == BASE_PUBLIC:
            continue
        public_slug = safe_slug(public.item.file.name)
        candidates.append(Candidate(
            public_base=public.item.file,
            assoc_source=None,
            slug=f"{public_slug}_v185keep",
            message=f"{public_slug} plus v185 private KEEP",
            notes=f"public KEEP base {public.item.file.name} ({public.score:.5f}, {public.delta:+.5f}) plus v185 private KEEP",
            priority=public.delta + 0.015,
            private_keep=True,
        ))

    return sorted(candidates, key=lambda candidate: candidate.priority, reverse=True)


def existing_versions() -> set[int]:
    versions: set[int] = set()
    for path in SUBMISSIONS.glob("v*.csv"):
        match = re.match(r"v(\d+)_", path.name)
        if match:
            versions.add(int(match.group(1)))
    return versions


def write_candidates(candidates: list[Candidate], start_version: int, out_plan: Path) -> list[Path]:
    target_versions = set(range(start_version, start_version + TARGET_COUNT))
    remote_filenames = {
        row.get("fileName", "")
        for row in read_submissions()
    }

    def local_version(path: Path) -> int | None:
        match = re.match(r"v(\d+)_", path.name)
        return int(match.group(1)) if match else None

    existing_keys = {
        dataframe_key(pd.read_csv(path))
        for path in SUBMISSIONS.glob("*.csv")
        if local_version(path) not in target_versions
    }
    used_versions = existing_versions() - target_versions
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
        raise RuntimeError(f"Only generated {len(written)} unique post-ASSOC/DIFF candidates; expected {TARGET_COUNT}.")

    out_plan.parent.mkdir(parents=True, exist_ok=True)
    with out_plan.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["file", "message", "notes"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prior-plan", type=Path, default=ROOT / "plans" / "2026-07-03.csv")
    parser.add_argument("--out-plan", type=Path, required=True)
    parser.add_argument("--start-version", type=int, default=301)
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
