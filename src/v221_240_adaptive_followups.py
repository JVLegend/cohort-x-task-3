"""Generate adaptive follow-up probes after the v201-v220 public-mover batch.

The script is intentionally result-driven. It reads the previous daily plan,
pulls Kaggle public scores through cohortx_ops, ranks the COPD and mediastinum
variants, then writes cross-condition combinations for the next daily quota.
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
except ModuleNotFoundError:
    from src.cohortx_ops import PlanItem, public_score, read_plan, read_submissions


ROOT = Path(__file__).resolve().parents[1]
SUBMISSIONS = ROOT / "submissions"
BASE_PUBLIC = SUBMISSIONS / "v178_FINAL.csv"
BASE_PRIVATE = SUBMISSIONS / "v185_private_kw.csv"
COPD = "Chronic Obstructive Pulmonary Disease"
MEDIASTINUM = "Enlarged Mediastinum"
TARGET_COUNT = 20
PUBLIC_COMBO_SLOTS = 16
PRIVATE_COMBO_SLOTS = 4


@dataclass(frozen=True)
class ScoredPlanItem:
    item: PlanItem
    score: float
    condition: str


@dataclass(frozen=True)
class Candidate:
    changes: dict[str, list[str]]
    base: Path
    slug: str
    message: str
    notes: str
    priority: float = 0.0


def parse_codes(value: str) -> list[str]:
    if pd.isna(value) or value == "Not Applicable":
        return []
    return [code.strip() for code in str(value).split(";") if code.strip()]


def fmt(codes: list[str]) -> str:
    return "; ".join(codes) if codes else "Not Applicable"


def codes_for(path: Path, condition: str) -> list[str]:
    df = pd.read_csv(path)
    return parse_codes(df.loc[df["Condition"].eq(condition), "KEEP"].iloc[0])


def set_codes(df: pd.DataFrame, condition: str, codes: list[str]) -> None:
    df.loc[df["Condition"].eq(condition), "KEEP"] = fmt(codes)


def submission_key(path: Path) -> str:
    return pd.read_csv(path).to_csv(index=False)


def dataframe_key(df: pd.DataFrame) -> str:
    return df.to_csv(index=False)


def variant_condition(filename: str) -> str | None:
    lower = filename.lower()
    if "copd" in lower:
        return COPD
    if "mediastinum" in lower or re.search(r"(^|_)med_", lower):
        return MEDIASTINUM
    return None


def scores_by_file() -> dict[str, float]:
    scores: dict[str, float] = {}
    for row in read_submissions():
        score = public_score(row)
        if score is None or row.get("status") != "complete":
            continue
        name = row["fileName"]
        scores[name] = max(score, scores.get(name, float("-inf")))
    return scores


def scored_items(plan_path: Path) -> list[ScoredPlanItem]:
    scores = scores_by_file()
    out: list[ScoredPlanItem] = []
    missing: list[str] = []
    for item in read_plan(plan_path):
        name = item.file.name
        condition = variant_condition(name)
        if condition is None:
            continue
        score = scores.get(name)
        if score is None:
            missing.append(name)
            continue
        out.append(ScoredPlanItem(item=item, score=score, condition=condition))
    if missing:
        sample = ", ".join(missing[:5])
        raise RuntimeError(
            f"{len(missing)} planned submissions are not scored yet: {sample}. "
            "Run this after the prior batch is submitted and complete."
        )
    if not out:
        raise RuntimeError(f"No scored COPD/mediastinum variants found in {plan_path}.")
    return out


def top_by_condition(items: list[ScoredPlanItem], condition: str, limit: int) -> list[ScoredPlanItem]:
    selected = [item for item in items if item.condition == condition]
    return sorted(selected, key=lambda item: item.score, reverse=True)[:limit]


def safe_slug(value: str) -> str:
    value = re.sub(r"^v\d+_", "", value.removesuffix(".csv"))
    value = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return value[:48]


def combo_candidates(copd_top: list[ScoredPlanItem], med_top: list[ScoredPlanItem]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for c_item in copd_top[:5]:
        for m_item in med_top[:5]:
            c_slug = safe_slug(c_item.item.file.name)
            m_slug = safe_slug(m_item.item.file.name)
            priority = c_item.score + m_item.score
            changes = {
                COPD: codes_for(c_item.item.file, COPD),
                MEDIASTINUM: codes_for(m_item.item.file, MEDIASTINUM),
            }
            candidates.append(Candidate(
                changes=changes,
                base=BASE_PUBLIC,
                slug=f"combo_{c_slug}_{m_slug}",
                message=f"combo: {c_slug} + {m_slug}",
                notes=f"public combo from {c_item.item.file.name} ({c_item.score:.5f}) and {m_item.item.file.name} ({m_item.score:.5f})",
                priority=priority,
            ))
    return sorted(candidates, key=lambda candidate: candidate.priority, reverse=True)


def private_candidates(candidates: list[Candidate]) -> list[Candidate]:
    if not BASE_PRIVATE.exists():
        return []
    out: list[Candidate] = []
    for candidate in candidates[:10]:
        out.append(Candidate(
            changes=candidate.changes,
            base=BASE_PRIVATE,
            slug=f"private_{candidate.slug}",
            message=f"private hedge: {candidate.message}",
            notes=f"v185 hidden-condition hedge plus {candidate.notes}",
            priority=candidate.priority,
        ))
    return out


def standalone_candidates(items: list[ScoredPlanItem]) -> list[Candidate]:
    out: list[Candidate] = []
    for scored in items:
        condition = scored.condition
        slug = safe_slug(scored.item.file.name)
        out.append(Candidate(
            changes={condition: codes_for(scored.item.file, condition)},
            base=BASE_PRIVATE if BASE_PRIVATE.exists() else BASE_PUBLIC,
            slug=f"private_{slug}",
            message=f"private hedge: {slug}",
            notes=f"v185 hidden-condition hedge plus standalone {scored.item.file.name} ({scored.score:.5f})",
            priority=scored.score,
        ))
    return out


def candidate_pool(copd_top: list[ScoredPlanItem], med_top: list[ScoredPlanItem]) -> list[Candidate]:
    combos = combo_candidates(copd_top, med_top)
    private_combos = private_candidates(combos)
    standalones = standalone_candidates(copd_top + med_top)
    return (
        combos[:PUBLIC_COMBO_SLOTS]
        + private_combos[:PRIVATE_COMBO_SLOTS]
        + combos[PUBLIC_COMBO_SLOTS:]
        + private_combos[PRIVATE_COMBO_SLOTS:]
        + standalones
    )


def write_candidates(candidates: list[Candidate], start_version: int, out_plan: Path) -> list[Path]:
    existing_keys = {
        submission_key(path)
        for path in SUBMISSIONS.glob("*.csv")
    }
    rows: list[dict[str, str]] = []
    written: list[Path] = []
    version = start_version
    seen_slugs: set[str] = set()

    for candidate in candidates:
        if len(written) >= TARGET_COUNT:
            break
        slug = candidate.slug
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)

        df = pd.read_csv(candidate.base)
        for condition, codes in candidate.changes.items():
            set_codes(df, condition, codes)

        key = dataframe_key(df)
        if key in existing_keys:
            continue

        path = SUBMISSIONS / f"v{version}_{slug}.csv"
        df.to_csv(path, index=False)
        existing_keys.add(key)
        written.append(path)
        rows.append({
            "file": str(path.relative_to(ROOT)),
            "message": f"v{version}: {candidate.message}"[:120],
            "notes": candidate.notes,
        })
        version += 1

    if len(written) < TARGET_COUNT:
        raise RuntimeError(f"Only generated {len(written)} unique candidates; expected {TARGET_COUNT}.")

    out_plan.parent.mkdir(parents=True, exist_ok=True)
    with out_plan.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["file", "message", "notes"])
        writer.writeheader()
        writer.writerows(rows)

    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prior-plan", type=Path, default=ROOT / "plans" / "2026-07-02.csv")
    parser.add_argument("--out-plan", type=Path, required=True)
    parser.add_argument("--start-version", type=int, default=221)
    args = parser.parse_args()

    prior_plan = args.prior_plan if args.prior_plan.is_absolute() else ROOT / args.prior_plan
    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    items = scored_items(prior_plan)
    copd_top = top_by_condition(items, COPD, 6)
    med_top = top_by_condition(items, MEDIASTINUM, 6)
    if not copd_top or not med_top:
        raise RuntimeError("Need at least one scored COPD and one scored mediastinum variant.")

    candidates = candidate_pool(copd_top, med_top)
    written = write_candidates(candidates, args.start_version, out_plan)

    print(f"wrote_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        raise SystemExit(f"not_ready: {exc}") from exc
