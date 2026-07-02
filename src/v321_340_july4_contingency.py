"""Generate a July 4 contingency plan if adaptive v301+ is not ready.

This plan deliberately uses v321-v340 so the normal adaptive generator can own
v301+ after the July 3 scores. It is a fallback, not the preferred primary.
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
        BASE_PUBLIC,
        CONDITION_GROUPS,
        COPD,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        apply_assoc_diff,
        apply_keep_edits,
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
        BASE_PUBLIC,
        CONDITION_GROUPS,
        COPD,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        apply_assoc_diff,
        apply_keep_edits,
        dataframe_key,
        get_codes,
        load_code_order,
        set_codes,
    )


TARGET_COUNT = 20
CKD = "CKD"
UTI = "UTI"
DIABETES = "Diabetes"
PNEUMONIA = "Pneumonia"


@dataclass(frozen=True)
class ContingencySpec:
    slug: str
    message: str
    notes: str
    private_keep_conditions: tuple[str, ...] = ()
    assoc_diff: dict[str, dict[str, tuple[str, ...]]] | None = None
    buckets: tuple[str, ...] = ("ASSOCIATION", "DIFF")
    conditions: tuple[str, ...] | None = None
    keep_remove: dict[str, tuple[str, ...]] | None = None
    keep_add: dict[str, tuple[str, ...]] | None = None


PRIVATE_KEEP_ALL = (CKD, UTI, DIABETES, PNEUMONIA)


SPECS = [
    ContingencySpec("v209_v185_keep_all", "v209 plus v185 private KEEP", "best public COPD prune plus v185 hidden KEEP hedge", private_keep_conditions=PRIVATE_KEEP_ALL),
    ContingencySpec("v209_v185_keep_ckd", "v209 plus v185 CKD KEEP", "isolates v185 CKD private KEEP on v209", private_keep_conditions=(CKD,)),
    ContingencySpec("v209_v185_keep_uti", "v209 plus v185 UTI KEEP", "isolates v185 UTI private KEEP on v209", private_keep_conditions=(UTI,)),
    ContingencySpec("v209_v185_keep_diabetes", "v209 plus v185 Diabetes KEEP", "isolates v185 Diabetes private KEEP on v209", private_keep_conditions=(DIABETES,)),
    ContingencySpec("v209_v185_keep_pneumonia", "v209 plus v185 Pneumonia KEEP", "isolates v185 Pneumonia private KEEP on v209", private_keep_conditions=(PNEUMONIA,)),
    ContingencySpec("v209_v185_keep_ckd_uti", "v209 plus v185 CKD/UTI KEEP", "paired renal/urinary private KEEP hedge", private_keep_conditions=(CKD, UTI)),
    ContingencySpec("v209_v185_keep_diab_pneumonia", "v209 plus v185 Diabetes/Pneumonia KEEP", "paired high-volume private KEEP hedge", private_keep_conditions=(DIABETES, PNEUMONIA)),
    ContingencySpec("v209_v185_keep_highconf_both", "v209 v185 KEEP plus highconf assoc/diff", "v185 private KEEP plus high-confidence ASSOC+DIFF", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_HIGH_CONF),
    ContingencySpec("v209_v185_keep_highconf_diff", "v209 v185 KEEP plus highconf DIFF", "v185 private KEEP plus high-confidence DIFF only", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_HIGH_CONF, buckets=("DIFF",)),
    ContingencySpec("v209_v185_keep_highconf_assoc", "v209 v185 KEEP plus highconf ASSOC", "v185 private KEEP plus high-confidence ASSOC only", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_HIGH_CONF, buckets=("ASSOCIATION",)),
    ContingencySpec("v209_v185_keep_pulmonary_assocdiff", "v209 v185 KEEP plus pulmonary assoc/diff", "v185 private KEEP plus pulmonary ASSOC/DIFF group", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["pulmonary"]),
    ContingencySpec("v209_v185_keep_cardiorenal_assocdiff", "v209 v185 KEEP plus cardiorenal assoc/diff", "v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["cardiorenal"]),
    ContingencySpec("v209_v185_keep_endocrine_assocdiff", "v209 v185 KEEP plus endocrine assoc/diff", "v185 private KEEP plus endocrine ASSOC/DIFF group", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["endocrine"]),
    ContingencySpec("v209_v185_keep_ent_gi_derm_assocdiff", "v209 v185 KEEP plus ENT/GI/derm assoc/diff", "v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["ent_gi_derm"]),
    ContingencySpec("v209_v185_keep_neuro_rheum_assocdiff", "v209 v185 KEEP plus neuro/rheum assoc/diff", "v185 private KEEP plus neuro/rheum ASSOC/DIFF group", private_keep_conditions=PRIVATE_KEEP_ALL, assoc_diff=ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["neuro_rheum"]),
    ContingencySpec("copd_no_j20_j45_j31", "COPD remove J20/J45/J31", "v209 plus J31 removal, isolating one extra positive public signal", keep_remove={COPD: ("J31",)}),
    ContingencySpec("copd_no_j20_j45_j98", "COPD remove J20/J45/J98", "v209 plus J98 removal, isolating one extra positive public signal", keep_remove={COPD: ("J98",)}),
    ContingencySpec("copd_no_j20_j45_j31_j81_j82_j93_j95", "COPD remove J20/J45/J31/J81/J82/J93/J95", "v209 plus strongest non-J96 COPD removals, excluding J98", keep_remove={COPD: ("J31", "J81", "J82", "J93", "J95")}),
    ContingencySpec("med_no_q34", "mediastinum remove Q34", "unsubmitted mediastinum family ablation on v209", keep_remove={MEDIASTINUM: ("Q34",)}),
    ContingencySpec("med_no_c78_d38_j85", "mediastinum remove C78/D38/J85", "small mediastinum false-positive ablation bundle on v209", keep_remove={MEDIASTINUM: ("C78", "D38", "J85")}),
]


def copy_private_keep(df: pd.DataFrame, private: pd.DataFrame, conditions: tuple[str, ...]) -> None:
    for condition in conditions:
        if condition in PUBLIC_ASSOC_DIFF_EMPTY:
            continue
        set_codes(df, condition, "KEEP", get_codes(private, condition, "KEEP"))


def candidate_frame(base: pd.DataFrame, private: pd.DataFrame, spec: ContingencySpec, code_order: list[str]) -> pd.DataFrame:
    df = base.copy()
    copy_private_keep(df, private, spec.private_keep_conditions)
    apply_assoc_diff(df, spec, code_order)
    apply_keep_edits(df, spec)
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_july4_contingency(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    if not BASE_PUBLIC.exists():
        raise FileNotFoundError(BASE_PUBLIC)
    if not BASE_PRIVATE.exists():
        raise FileNotFoundError(BASE_PRIVATE)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_PUBLIC)
    private = pd.read_csv(BASE_PRIVATE)
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
        df = candidate_frame(base, private, spec, code_order)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 4 contingency candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-04-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=321)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july4_contingency(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
