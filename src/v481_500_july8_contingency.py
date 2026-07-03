"""Generate a July 8 hidden-KEEP contingency plan.

The preferred July 8 path should be an adaptive plan from July 7 scores, so
this fallback starts at v481 and leaves v461-v480 available for that primary
path. Candidates use the current public anchor while toggling conditions that
were public-neutral in prior single-condition probes.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

try:
    from v281_300_assoc_diff import (
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )
except ModuleNotFoundError:
    from src.v281_300_assoc_diff import (
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
BASE_BEST = SUBMISSIONS / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
MED_POSITIVE = SUBMISSIONS / "v300_med_add_thymus_nodes.csv"

HEART_FAILURE = "Heart Failure"
HYPERTHYROIDISM = "Hyperthyroidism"
ILD = "Interstitial Lung Disease"
DERMATOMYCOSIS = "Dermatomycosis"
BRONCHITIS = "Bronchitis"
NPC = "Nasopharyngeal Carcinoma"
HYPOTHYROIDISM = "Hypothyroidism"

ZERO_SOURCES = {
    HEART_FAILURE: SUBMISSIONS / "v187_zero_hf.csv",
    HYPERTHYROIDISM: SUBMISSIONS / "v188_zero_hyperthyroid.csv",
    ILD: SUBMISSIONS / "v189_zero_ild.csv",
    DERMATOMYCOSIS: SUBMISSIONS / "v190_zero_derm.csv",
    BRONCHITIS: SUBMISSIONS / "v191_zero_bronchitis.csv",
    NPC: SUBMISSIONS / "v192_zero_npc.csv",
    HYPOTHYROIDISM: SUBMISSIONS / "v193_zero_hypothyroid.csv",
}
ADD_SOURCES = {
    HEART_FAILURE: SUBMISSIONS / "v196_add_hf_kw.csv",
    ILD: SUBMISSIONS / "v197_add_ild_kw.csv",
    DERMATOMYCOSIS: SUBMISSIONS / "v198_add_derm_kw.csv",
    NPC: SUBMISSIONS / "v200_add_npc_kw.csv",
}


@dataclass(frozen=True)
class ContingencySpec:
    slug: str
    message: str
    notes: str
    zero_keep_conditions: tuple[str, ...] = ()
    add_keep_conditions: tuple[str, ...] = ()
    add_mediastinum_positive: bool = False


SPECS = [
    ContingencySpec("v296_zero_hf", "v296 zero Heart Failure KEEP", "public-neutral zero probe v187 on v296 anchor", zero_keep_conditions=(HEART_FAILURE,)),
    ContingencySpec("v296_zero_hyperthyroid", "v296 zero Hyperthyroidism KEEP", "public-neutral zero probe v188 on v296 anchor", zero_keep_conditions=(HYPERTHYROIDISM,)),
    ContingencySpec("v296_zero_ild", "v296 zero ILD KEEP", "public-neutral zero probe v189 on v296 anchor", zero_keep_conditions=(ILD,)),
    ContingencySpec("v296_zero_derm", "v296 zero Dermatomycosis KEEP", "public-neutral zero probe v190 on v296 anchor", zero_keep_conditions=(DERMATOMYCOSIS,)),
    ContingencySpec("v296_zero_bronchitis", "v296 zero Bronchitis KEEP", "public-neutral zero probe v191 on v296 anchor", zero_keep_conditions=(BRONCHITIS,)),
    ContingencySpec("v296_zero_npc", "v296 zero NPC KEEP", "public-neutral zero probe v192 on v296 anchor", zero_keep_conditions=(NPC,)),
    ContingencySpec("v296_zero_hypothyroid", "v296 zero Hypothyroidism KEEP", "public-neutral zero probe v193 on v296 anchor", zero_keep_conditions=(HYPOTHYROIDISM,)),
    ContingencySpec("v296_add_hf_kw", "v296 add Heart Failure keyword KEEP", "public-neutral keyword add v196 on v296 anchor", add_keep_conditions=(HEART_FAILURE,)),
    ContingencySpec("v296_add_ild_kw", "v296 add ILD keyword KEEP", "public-neutral keyword add v197 on v296 anchor", add_keep_conditions=(ILD,)),
    ContingencySpec("v296_add_derm_kw", "v296 add Dermatomycosis keyword KEEP", "public-neutral keyword add v198 on v296 anchor", add_keep_conditions=(DERMATOMYCOSIS,)),
    ContingencySpec("v296_add_npc_kw", "v296 add NPC keyword KEEP", "public-neutral keyword add v200 on v296 anchor", add_keep_conditions=(NPC,)),
    ContingencySpec("v296_zero_endocrine_pair", "v296 zero thyroid pair KEEP", "paired public-neutral thyroid ablation", zero_keep_conditions=(HYPERTHYROIDISM, HYPOTHYROIDISM)),
    ContingencySpec("v296_zero_pulmonary_pair", "v296 zero ILD/Bronchitis KEEP", "paired public-neutral pulmonary hidden KEEP ablation", zero_keep_conditions=(ILD, BRONCHITIS)),
    ContingencySpec("v296_zero_derm_npc_pair", "v296 zero Derm/NPC KEEP", "paired public-neutral derm/NPC ablation", zero_keep_conditions=(DERMATOMYCOSIS, NPC)),
    ContingencySpec("v296_add_hidden_kw_group", "v296 add hidden keyword group", "combined public-neutral keyword additions from v196/v197/v198/v200", add_keep_conditions=(HEART_FAILURE, ILD, DERMATOMYCOSIS, NPC)),
    ContingencySpec("v296_med_zero_hf", "v296 mediastinum plus zero HF", "med positive plus public-neutral HF ablation", zero_keep_conditions=(HEART_FAILURE,), add_mediastinum_positive=True),
    ContingencySpec("v296_med_zero_endocrine_pair", "v296 mediastinum plus zero thyroid pair", "med positive plus public-neutral thyroid ablation", zero_keep_conditions=(HYPERTHYROIDISM, HYPOTHYROIDISM), add_mediastinum_positive=True),
    ContingencySpec("v296_med_zero_pulmonary_pair", "v296 mediastinum plus zero ILD/Bronchitis", "med positive plus public-neutral pulmonary ablation", zero_keep_conditions=(ILD, BRONCHITIS), add_mediastinum_positive=True),
    ContingencySpec("v296_med_zero_derm_npc_pair", "v296 mediastinum plus zero Derm/NPC", "med positive plus public-neutral derm/NPC ablation", zero_keep_conditions=(DERMATOMYCOSIS, NPC), add_mediastinum_positive=True),
    ContingencySpec("v296_med_add_hidden_kw_group", "v296 mediastinum plus hidden keyword group", "med positive plus combined public-neutral keyword additions", add_keep_conditions=(HEART_FAILURE, ILD, DERMATOMYCOSIS, NPC), add_mediastinum_positive=True),
]


def copy_mediastinum_positive(df: pd.DataFrame, med_positive: pd.DataFrame) -> None:
    set_codes(df, MEDIASTINUM, "KEEP", get_codes(med_positive, MEDIASTINUM, "KEEP"))


def copy_keep(df: pd.DataFrame, source: pd.DataFrame, condition: str) -> None:
    set_codes(df, condition, "KEEP", get_codes(source, condition, "KEEP"))


def candidate_frame(
    base: pd.DataFrame,
    med_positive: pd.DataFrame,
    zero_frames: dict[str, pd.DataFrame],
    add_frames: dict[str, pd.DataFrame],
    spec: ContingencySpec,
) -> pd.DataFrame:
    df = base.copy()
    if spec.add_mediastinum_positive:
        copy_mediastinum_positive(df, med_positive)
    for condition in spec.zero_keep_conditions:
        copy_keep(df, zero_frames[condition], condition)
    for condition in spec.add_keep_conditions:
        copy_keep(df, add_frames[condition], condition)
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_july8_contingency(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    required_paths = {BASE_BEST, MED_POSITIVE, *ZERO_SOURCES.values(), *ADD_SOURCES.values()}
    for path in required_paths:
        if not path.exists():
            raise FileNotFoundError(path)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_BEST)
    med_positive = pd.read_csv(MED_POSITIVE)
    zero_frames = {condition: pd.read_csv(path) for condition, path in ZERO_SOURCES.items()}
    add_frames = {condition: pd.read_csv(path) for condition, path in ADD_SOURCES.items()}
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
        df = candidate_frame(base, med_positive, zero_frames, add_frames, spec)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 8 contingency candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-08-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=481)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july8_contingency(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
