"""Generate a July 9 ASSOC-isolation contingency plan.

The preferred July 9 path should be an adaptive plan from July 8 scores, so
this fallback starts at v521 and leaves v501-v520 available for that primary
path. Candidates isolate the ASSOC-only map that improved/tied public score in
v283/v286, one condition at a time, on the current v296 public anchor.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

try:
    from v281_300_assoc_diff import (
        ASSOC_DIFF_BROAD,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        expand_nodes,
        get_codes,
        load_code_order,
        set_codes,
    )
except ModuleNotFoundError:
    from src.v281_300_assoc_diff import (
        ASSOC_DIFF_BROAD,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        expand_nodes,
        get_codes,
        load_code_order,
        set_codes,
    )


TARGET_COUNT = 20
BASE_BEST = SUBMISSIONS / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"

EPISTAXIS = "Epistaxis"
GOUT = "Gout"
PLEURISY = "Pleurisy"
BRONCHITIS = "Bronchitis"
THYROIDITIS = "Thyroiditis"
CKD = "CKD"
HYPOTHYROIDISM = "Hypothyroidism"
HEMATEMESIS = "Hematemesis"
HEART_FAILURE = "Heart Failure"
ILD = "Interstitial Lung Disease"
HYPOPARATHYROIDISM = "Hypoparathyroidism"
HYPERPARATHYROIDISM = "Hyperparathyroidism"
HYPERTHYROIDISM = "Hyperthyroidism"
PNEUMONIA = "Pneumonia"
ICP = "Intracranial Pressure"
ADRENAL = "Latent Adrenal Insufficiency"
DERMATOMYCOSIS = "Dermatomycosis"
NPC = "Nasopharyngeal Carcinoma"
UTI = "UTI"
DIABETES = "Diabetes"


@dataclass(frozen=True)
class AssocIsolationSpec:
    slug: str
    condition: str

    @property
    def message(self) -> str:
        return f"v296 isolate {self.condition} ASSOC only"

    @property
    def notes(self) -> str:
        return "single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty"


SPECS = [
    AssocIsolationSpec("v296_assoc_epistaxis", EPISTAXIS),
    AssocIsolationSpec("v296_assoc_gout", GOUT),
    AssocIsolationSpec("v296_assoc_pleurisy", PLEURISY),
    AssocIsolationSpec("v296_assoc_bronchitis", BRONCHITIS),
    AssocIsolationSpec("v296_assoc_thyroiditis", THYROIDITIS),
    AssocIsolationSpec("v296_assoc_ckd", CKD),
    AssocIsolationSpec("v296_assoc_hypothyroidism", HYPOTHYROIDISM),
    AssocIsolationSpec("v296_assoc_hematemesis", HEMATEMESIS),
    AssocIsolationSpec("v296_assoc_hf", HEART_FAILURE),
    AssocIsolationSpec("v296_assoc_ild", ILD),
    AssocIsolationSpec("v296_assoc_hypoparathyroidism", HYPOPARATHYROIDISM),
    AssocIsolationSpec("v296_assoc_hyperparathyroidism", HYPERPARATHYROIDISM),
    AssocIsolationSpec("v296_assoc_hyperthyroidism", HYPERTHYROIDISM),
    AssocIsolationSpec("v296_assoc_pneumonia", PNEUMONIA),
    AssocIsolationSpec("v296_assoc_icp", ICP),
    AssocIsolationSpec("v296_assoc_adrenal", ADRENAL),
    AssocIsolationSpec("v296_assoc_derm", DERMATOMYCOSIS),
    AssocIsolationSpec("v296_assoc_npc", NPC),
    AssocIsolationSpec("v296_assoc_uti", UTI),
    AssocIsolationSpec("v296_assoc_diabetes", DIABETES),
]


def candidate_frame(base: pd.DataFrame, spec: AssocIsolationSpec, code_order: list[str]) -> pd.DataFrame:
    df = base.copy()
    nodes = ASSOC_DIFF_BROAD[spec.condition]["ASSOCIATION"]
    set_codes(df, spec.condition, "ASSOCIATION", expand_nodes(nodes, code_order))
    set_codes(df, spec.condition, "DIFF", [])
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_july9_assoc_isolations(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    if not BASE_BEST.exists():
        raise FileNotFoundError(BASE_BEST)
    missing = [spec.condition for spec in SPECS if spec.condition not in ASSOC_DIFF_BROAD]
    if missing:
        raise KeyError(f"missing ASSOC specs: {missing}")
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_BEST)
    code_order = load_code_order()
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
        df = candidate_frame(base, spec, code_order)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 9 ASSOC isolation candidate: {path.name}")
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
            writer = csv.DictWriter(fh, fieldnames=["file", "message", "notes"], lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-09-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=521)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july9_assoc_isolations(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
