"""Generate a private-hedge reserve plan for quota-risk days.

This is not the primary 2026-07-03 strategy. The adaptive v221-v240 generator
should run first after v201-v220 receive scores. These reserve files exist to
avoid wasting a daily quota if the adaptive plan is still not ready near reset.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SUBMISSIONS = ROOT / "submissions"
PLANS = ROOT / "plans"
BASE_PRIVATE = SUBMISSIONS / "v185_private_kw.csv"
TARGET_COUNT = 20


@dataclass(frozen=True)
class ReserveSpec:
    slug: str
    condition: str
    source: str
    message: str
    notes: str


SPECS = [
    ReserveSpec("reserve_zero_hf", "Heart Failure", "v187_zero_hf.csv", "reserve: v185 plus zero HF", "public-neutral v187 on top of v185 private hedge"),
    ReserveSpec("reserve_zero_hyperthyroid", "Hyperthyroidism", "v188_zero_hyperthyroid.csv", "reserve: v185 plus zero Hyperthyroidism", "public-neutral v188 on top of v185 private hedge"),
    ReserveSpec("reserve_zero_ild", "Interstitial Lung Disease", "v189_zero_ild.csv", "reserve: v185 plus zero ILD", "public-neutral v189 on top of v185 private hedge"),
    ReserveSpec("reserve_zero_derm", "Dermatomycosis", "v190_zero_derm.csv", "reserve: v185 plus zero Dermatomycosis", "public-neutral v190 on top of v185 private hedge"),
    ReserveSpec("reserve_zero_bronchitis", "Bronchitis", "v191_zero_bronchitis.csv", "reserve: v185 plus zero Bronchitis", "public-neutral v191 on top of v185 private hedge"),
    ReserveSpec("reserve_zero_npc", "Nasopharyngeal Carcinoma", "v192_zero_npc.csv", "reserve: v185 plus zero NPC", "public-neutral v192 on top of v185 private hedge"),
    ReserveSpec("reserve_zero_hypothyroid", "Hypothyroidism", "v193_zero_hypothyroid.csv", "reserve: v185 plus zero Hypothyroidism", "public-neutral v193 on top of v185 private hedge"),
    ReserveSpec("reserve_add_hf_kw", "Heart Failure", "v196_add_hf_kw.csv", "reserve: v185 plus HF keyword extras", "public-neutral v196 on top of v185 private hedge"),
    ReserveSpec("reserve_add_ild_kw", "Interstitial Lung Disease", "v197_add_ild_kw.csv", "reserve: v185 plus ILD keyword extras", "public-neutral v197 on top of v185 private hedge"),
    ReserveSpec("reserve_add_derm_kw", "Dermatomycosis", "v198_add_derm_kw.csv", "reserve: v185 plus Derm keyword extras", "public-neutral v198 on top of v185 private hedge"),
    ReserveSpec("reserve_add_npc_kw", "Nasopharyngeal Carcinoma", "v200_add_npc_kw.csv", "reserve: v185 plus NPC keyword extras", "public-neutral v200 on top of v185 private hedge"),
    ReserveSpec("reserve_derm_v148", "Dermatomycosis", "v148_enrich.csv", "reserve: v185 plus Derm v148 enrich", "v148 tied public with Dermatomycosis enrichment"),
    ReserveSpec("reserve_pleurisy_v148", "Pleurisy", "v148_enrich.csv", "reserve: v185 plus Pleurisy v148 enrich", "v148 tied public with Pleurisy enrichment"),
    ReserveSpec("reserve_bronchitis_v148", "Bronchitis", "v148_enrich.csv", "reserve: v185 plus Bronchitis v148 enrich", "v148 tied public with Bronchitis enrichment"),
    ReserveSpec("reserve_hematemesis_v148", "Hematemesis", "v148_enrich.csv", "reserve: v185 plus Hematemesis v148 enrich", "v148 tied public with Hematemesis enrichment"),
    ReserveSpec("reserve_thyroiditis_v153", "Thyroiditis", "v153_more_expand.csv", "reserve: v185 plus Thyroiditis v153 expand", "v153 tied public with Thyroiditis expansion"),
    ReserveSpec("reserve_hypothyroid_v153", "Hypothyroidism", "v153_more_expand.csv", "reserve: v185 plus Hypothyroidism v153 expand", "v153 tied public with Hypothyroidism expansion"),
    ReserveSpec("reserve_hypergonadism_v153", "Hypergonadism", "v153_more_expand.csv", "reserve: v185 plus Hypergonadism v153 expand", "v153 tied public with Hypergonadism expansion"),
    ReserveSpec("reserve_hypopara_v153", "Hypoparathyroidism", "v153_more_expand.csv", "reserve: v185 plus Hypoparathyroidism v153 expand", "v153 tied public with Hypoparathyroidism expansion"),
    ReserveSpec("reserve_hyperpara_v153", "Hyperparathyroidism", "v153_more_expand.csv", "reserve: v185 plus Hyperparathyroidism v153 expand", "v153 tied public with Hyperparathyroidism expansion"),
]


def parse_codes(value: str) -> list[str]:
    if pd.isna(value) or value == "Not Applicable":
        return []
    return [code.strip() for code in str(value).split(";") if code.strip()]


def fmt(codes: list[str]) -> str:
    return "; ".join(codes) if codes else "Not Applicable"


def get_codes(df: pd.DataFrame, condition: str) -> list[str]:
    rows = df.loc[df["Condition"].eq(condition), "KEEP"]
    if rows.empty:
        raise ValueError(f"condition not found: {condition}")
    return parse_codes(rows.iloc[0])


def set_codes(df: pd.DataFrame, condition: str, codes: list[str]) -> None:
    if not df["Condition"].eq(condition).any():
        raise ValueError(f"condition not found: {condition}")
    df.loc[df["Condition"].eq(condition), "KEEP"] = fmt(codes)


def dataframe_key(df: pd.DataFrame) -> str:
    return df.to_csv(index=False)


def reserve_frame(base: pd.DataFrame, spec: ReserveSpec) -> pd.DataFrame:
    source_path = SUBMISSIONS / spec.source
    if not source_path.exists():
        raise FileNotFoundError(source_path)
    source = pd.read_csv(source_path)
    df = base.copy()
    set_codes(df, spec.condition, get_codes(source, spec.condition))
    return df


def write_reserve(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    if not BASE_PRIVATE.exists():
        raise FileNotFoundError(BASE_PRIVATE)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_PRIVATE)
    target_paths = [SUBMISSIONS / f"v{start_version + idx}_{spec.slug}.csv" for idx, spec in enumerate(SPECS)]
    target_set = set(target_paths)
    existing_keys = {
        dataframe_key(pd.read_csv(path))
        for path in SUBMISSIONS.glob("*.csv")
        if path not in target_set
    }

    rows: list[dict[str, str]] = []
    written: list[Path] = []
    seen_keys: set[str] = set()
    for idx, spec in enumerate(SPECS):
        version = start_version + idx
        path = SUBMISSIONS / f"v{version}_{spec.slug}.csv"
        df = reserve_frame(base, spec)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate reserve candidate: {path.name}")
        seen_keys.add(key)
        rows.append({
            "file": str(path.relative_to(ROOT)),
            "message": f"v{version}: {spec.message}"[:120],
            "notes": spec.notes,
        })
        written.append(path)
        if not dry_run:
            df.to_csv(path, index=False)

    if not dry_run:
        out_plan.parent.mkdir(parents=True, exist_ok=True)
        with out_plan.open("w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["file", "message", "notes"])
            writer.writeheader()
            writer.writerows(rows)

    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-03-reserve.csv")
    parser.add_argument("--start-version", type=int, default=241)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_reserve(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
