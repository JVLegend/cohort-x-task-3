"""Generate a July 5 public contingency plan.

The preferred July 5 path is still the adaptive plan generated from scored
v301-v320 results. This fallback deliberately starts at v361 so v341-v360 stay
available for that primary adaptive plan.
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
        ASSOC_DIFF_HIGH_CONF,
        BASE_PRIVATE,
        CONDITION_GROUPS,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        apply_assoc_diff,
        dataframe_key,
        get_codes,
        load_code_order,
        set_codes,
    )
except ModuleNotFoundError:
    from src.v281_300_assoc_diff import (
        ASSOC_DIFF_BROAD,
        ASSOC_DIFF_HIGH_CONF,
        BASE_PRIVATE,
        CONDITION_GROUPS,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        apply_assoc_diff,
        dataframe_key,
        get_codes,
        load_code_order,
        set_codes,
    )


TARGET_COUNT = 20
BASE_BEST = SUBMISSIONS / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
MED_POSITIVE = SUBMISSIONS / "v300_med_add_thymus_nodes.csv"
CKD = "CKD"
UTI = "UTI"
DIABETES = "Diabetes"
PNEUMONIA = "Pneumonia"
PRIVATE_KEEP_ALL = (CKD, UTI, DIABETES, PNEUMONIA)


@dataclass(frozen=True)
class ContingencySpec:
    slug: str
    message: str
    notes: str
    private_keep_conditions: tuple[str, ...] = ()
    add_mediastinum_positive: bool = False
    assoc_diff: dict[str, dict[str, tuple[str, ...]]] | None = None
    buckets: tuple[str, ...] = ("ASSOCIATION", "DIFF")
    conditions: tuple[str, ...] | None = None


SPECS = [
    ContingencySpec("v296_v185_keep_all", "v296 plus v185 private KEEP", "best public COPD prune plus all v185 hidden KEEP, no mediastinum add", private_keep_conditions=PRIVATE_KEEP_ALL),
    ContingencySpec("v296_v185_keep_ckd", "v296 plus v185 CKD KEEP", "isolates CKD private KEEP on the v296 public anchor", private_keep_conditions=(CKD,)),
    ContingencySpec("v296_v185_keep_uti", "v296 plus v185 UTI KEEP", "isolates UTI private KEEP on the v296 public anchor", private_keep_conditions=(UTI,)),
    ContingencySpec("v296_v185_keep_diabetes", "v296 plus v185 Diabetes KEEP", "isolates Diabetes private KEEP on the v296 public anchor", private_keep_conditions=(DIABETES,)),
    ContingencySpec("v296_v185_keep_pneumonia", "v296 plus v185 Pneumonia KEEP", "isolates Pneumonia private KEEP on the v296 public anchor", private_keep_conditions=(PNEUMONIA,)),
    ContingencySpec("v296_highconf_assoc", "v296 plus highconf ASSOC", "public anchor plus high-confidence ASSOC only, no private KEEP", assoc_diff=ASSOC_DIFF_HIGH_CONF, buckets=("ASSOCIATION",)),
    ContingencySpec("v296_broad_assoc", "v296 plus broad ASSOC", "public anchor plus broad ASSOC only, no private KEEP", assoc_diff=ASSOC_DIFF_BROAD, buckets=("ASSOCIATION",)),
    ContingencySpec("v296_pulmonary_assocdiff", "v296 plus pulmonary ASSOC/DIFF", "public anchor plus public-neutral pulmonary ASSOC/DIFF group", assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["pulmonary"]),
    ContingencySpec("v296_cardiorenal_assocdiff", "v296 plus cardiorenal ASSOC/DIFF", "public anchor plus public-neutral CKD/HF/Diabetes ASSOC/DIFF group", assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["cardiorenal"]),
    ContingencySpec("v296_highconf_assoc_v185keep", "v296 highconf ASSOC plus v185 KEEP", "v296 plus high-confidence ASSOC and all v185 hidden KEEP, no mediastinum add", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_HIGH_CONF, buckets=("ASSOCIATION",)),
    ContingencySpec("v296_broad_assoc_v185keep", "v296 broad ASSOC plus v185 KEEP", "v296 plus broad ASSOC and all v185 hidden KEEP, no mediastinum add", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_BROAD, buckets=("ASSOCIATION",)),
    ContingencySpec("v296_pulmonary_assocdiff_v185keep", "v296 pulmonary ASSOC/DIFF plus v185 KEEP", "public-neutral pulmonary ASSOC/DIFF plus all v185 hidden KEEP, no mediastinum add", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["pulmonary"]),
    ContingencySpec("v296_cardiorenal_assocdiff_v185keep", "v296 cardiorenal ASSOC/DIFF plus v185 KEEP", "public-neutral cardiorenal ASSOC/DIFF plus all v185 hidden KEEP, no mediastinum add", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["cardiorenal"]),
    ContingencySpec("v296_med_add_thymus_nodes", "v296 plus mediastinum thymus/nodes", "pure public combo of best COPD prune with small positive mediastinum add", add_mediastinum_positive=True),
    ContingencySpec("v296_med_add_thymus_nodes_highconf_assoc", "v296 mediastinum plus highconf ASSOC", "pure public combo plus high-confidence ASSOC only, no private KEEP", add_mediastinum_positive=True, assoc_diff=ASSOC_DIFF_HIGH_CONF, buckets=("ASSOCIATION",)),
    ContingencySpec("v296_med_add_thymus_nodes_broad_assoc", "v296 mediastinum plus broad ASSOC", "pure public combo plus broad ASSOC only, no private KEEP", add_mediastinum_positive=True, assoc_diff=ASSOC_DIFF_BROAD, buckets=("ASSOCIATION",)),
    ContingencySpec("v296_med_add_thymus_nodes_pulmonary_assocdiff", "v296 mediastinum plus pulmonary ASSOC/DIFF", "pure public combo plus pulmonary ASSOC/DIFF, no private KEEP", add_mediastinum_positive=True, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["pulmonary"]),
    ContingencySpec("v296_med_add_thymus_nodes_cardiorenal_assocdiff", "v296 mediastinum plus cardiorenal ASSOC/DIFF", "pure public combo plus cardiorenal ASSOC/DIFF, no private KEEP", add_mediastinum_positive=True, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["cardiorenal"]),
    ContingencySpec("v296_med_add_thymus_nodes_v185_keep_ckd_uti", "v296 mediastinum plus v185 CKD/UTI KEEP", "public combo plus renal/urinary hidden KEEP isolation", private_keep_conditions=(CKD, UTI), add_mediastinum_positive=True),
    ContingencySpec("v296_med_add_thymus_nodes_v185_keep_diab_pneumonia", "v296 mediastinum plus v185 Diabetes/Pneumonia KEEP", "public combo plus diabetes/pneumonia hidden KEEP isolation", private_keep_conditions=(DIABETES, PNEUMONIA), add_mediastinum_positive=True),
]


def copy_private_keep(df: pd.DataFrame, private: pd.DataFrame, conditions: tuple[str, ...]) -> None:
    for condition in conditions:
        if condition in PUBLIC_ASSOC_DIFF_EMPTY:
            continue
        set_codes(df, condition, "KEEP", get_codes(private, condition, "KEEP"))


def copy_mediastinum_positive(df: pd.DataFrame, med_positive: pd.DataFrame) -> None:
    set_codes(df, MEDIASTINUM, "KEEP", get_codes(med_positive, MEDIASTINUM, "KEEP"))


def candidate_frame(base: pd.DataFrame, private: pd.DataFrame, med_positive: pd.DataFrame, spec: ContingencySpec, code_order: list[str]) -> pd.DataFrame:
    df = base.copy()
    if spec.add_mediastinum_positive:
        copy_mediastinum_positive(df, med_positive)
    copy_private_keep(df, private, spec.private_keep_conditions)
    apply_assoc_diff(df, spec, code_order)
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_july5_contingency(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    for path in (BASE_BEST, BASE_PRIVATE, MED_POSITIVE):
        if not path.exists():
            raise FileNotFoundError(path)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_BEST)
    private = pd.read_csv(BASE_PRIVATE)
    med_positive = pd.read_csv(MED_POSITIVE)
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
        df = candidate_frame(base, private, med_positive, spec, code_order)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 5 contingency candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-05-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=361)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july5_contingency(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
