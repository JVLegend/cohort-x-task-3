"""Generate a July 16 final-window contingency plan.

The preferred July 16 path should still be an adaptive plan from July 15
scores, so this fallback starts at v801 and leaves v781-v800 available for that
primary path. These candidates blend the strongest public anchor with final
private hedges: v185 KEEP slices, public-neutral hidden KEEP overlays, selected
KEEP prunes, and ASSOC-only maps. DIFF stays empty in this final fallback unless
an adaptive plan earns it from fresh scores.
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
        dataframe_key,
        drop_prefixes,
        expand_nodes,
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
        dataframe_key,
        drop_prefixes,
        expand_nodes,
        get_codes,
        load_code_order,
        set_codes,
    )


TARGET_COUNT = 20
BASE_BEST = SUBMISSIONS / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
MED_POSITIVE = SUBMISSIONS / "v300_med_add_thymus_nodes.csv"

ICP = "Intracranial Pressure"
GOUT = "Gout"
PLEURISY = "Pleurisy"
BRONCHITIS = "Bronchitis"
THYROIDITIS = "Thyroiditis"
NPC = "Nasopharyngeal Carcinoma"
CKD = "CKD"
HYPOTHYROIDISM = "Hypothyroidism"
HEMATEMESIS = "Hematemesis"
HEART_FAILURE = "Heart Failure"
HYPERGONADISM = "Hypergonadism"
UTI = "UTI"
DIABETES = "Diabetes"
ILD = "Interstitial Lung Disease"
HYPOPARATHYROIDISM = "Hypoparathyroidism"
HYPERTHYROIDISM = "Hyperthyroidism"
PNEUMONIA = "Pneumonia"
DERMATOMYCOSIS = "Dermatomycosis"

PRIVATE_KEEP_ALL = (CKD, UTI, DIABETES, PNEUMONIA)
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
class KeepPrune:
    condition: str
    prefixes: tuple[str, ...]


@dataclass(frozen=True)
class FinalBlendSpec:
    slug: str
    message: str
    notes: str
    add_mediastinum_positive: bool = False
    private_keep_conditions: tuple[str, ...] = ()
    zero_keep_conditions: tuple[str, ...] = ()
    add_keep_conditions: tuple[str, ...] = ()
    prune_edits: tuple[KeepPrune, ...] = ()
    assoc_family: str | None = None
    assoc_conditions: tuple[str, ...] | None = None


RENAL_METABOLIC_PRUNE = (
    KeepPrune(CKD, ("Q60", "Q61", "Q62")),
    KeepPrune(DIABETES, ("O24",)),
    KeepPrune(UTI, ("O23", "O86", "O03")),
)
CARDIO_PULM_PRUNE = (
    KeepPrune(CKD, ("I50",)),
    KeepPrune(HEART_FAILURE, ("I97",)),
    KeepPrune(ILD, ("J70",)),
)
THYROID_PRUNE = (
    KeepPrune(THYROIDITIS, ("E03",)),
    KeepPrune(HYPOTHYROIDISM, ("E04",)),
    KeepPrune(HYPERTHYROIDISM, ("E04", "E01", "E03", "P72")),
)
RESPIRATORY_PRUNE = (
    KeepPrune(PLEURISY, ("R09", "J95")),
    KeepPrune(BRONCHITIS, ("J43", "J68")),
    KeepPrune(PNEUMONIA, ("A37", "P23", "J84", "J85")),
)
SMALL_PRECISION_PRUNE = (
    KeepPrune(GOUT, ("E79",)),
    KeepPrune(CKD, ("I50",)),
    KeepPrune(HEART_FAILURE, ("I97",)),
    KeepPrune(UTI, ("N35",)),
    KeepPrune(ILD, ("J70",)),
    KeepPrune(HEMATEMESIS, ("R36", "K66")),
)
BROAD_PRIVATE_PRUNE = (
    KeepPrune(ICP, ("G96", "G94")),
    KeepPrune(GOUT, ("E79",)),
    KeepPrune(PLEURISY, ("R09", "J95")),
    KeepPrune(BRONCHITIS, ("J43", "J68")),
    KeepPrune(THYROIDITIS, ("E03",)),
    KeepPrune(NPC, ("D00", "C44", "D10")),
    KeepPrune(CKD, ("Q60", "Q61", "Q62", "I50")),
    KeepPrune(HYPOTHYROIDISM, ("E04",)),
    KeepPrune(HEMATEMESIS, ("R36", "K66")),
    KeepPrune(HEART_FAILURE, ("I97",)),
    KeepPrune(HYPERGONADISM, ("E27",)),
    KeepPrune(UTI, ("O23", "O86", "O03", "N35")),
    KeepPrune(DIABETES, ("O24", "Z79", "Z86", "P70")),
    KeepPrune(ILD, ("J70",)),
    KeepPrune(HYPOPARATHYROIDISM, ("E23", "E87", "P71", "E21")),
    KeepPrune(HYPERTHYROIDISM, ("E04", "E01", "E03", "P72")),
    KeepPrune(PNEUMONIA, ("A37", "P23", "J84", "J85")),
    KeepPrune(DERMATOMYCOSIS, ("B37",)),
)
NEURO_CKD_PRUNE = (
    KeepPrune(ICP, ("G96", "G94")),
    KeepPrune(GOUT, ("E79",)),
    KeepPrune(CKD, ("Q60", "Q61", "Q62")),
)


SPECS = [
    FinalBlendSpec("v296_final_med_v185_zero_thyroid_highconf_assoc", "v296 final med+v185 zero thyroid highconf ASSOC", "final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC", True, PRIVATE_KEEP_ALL, (HYPERTHYROIDISM, HYPOTHYROIDISM), (), (), "highconf"),
    FinalBlendSpec("v296_final_med_v185_zero_pulmonary_highconf_assoc", "v296 final med+v185 zero pulmonary highconf ASSOC", "final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC", True, PRIVATE_KEEP_ALL, (ILD, BRONCHITIS), (), (), "highconf"),
    FinalBlendSpec("v296_final_med_v185_zero_derm_npc_highconf_assoc", "v296 final med+v185 zero Derm/NPC highconf ASSOC", "final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC", True, PRIVATE_KEEP_ALL, (DERMATOMYCOSIS, NPC), (), (), "highconf"),
    FinalBlendSpec("v296_final_med_v185_add_hidden_highconf_assoc", "v296 final med+v185 add hidden highconf ASSOC", "final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC", True, PRIVATE_KEEP_ALL, (), (HEART_FAILURE, ILD, DERMATOMYCOSIS, NPC), (), "highconf"),
    FinalBlendSpec("v296_final_med_v185_prune_renal_metabolic_highconf_assoc", "v296 final med+v185 renal/metabolic prune highconf ASSOC", "final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC", True, PRIVATE_KEEP_ALL, (), (), RENAL_METABOLIC_PRUNE, "highconf"),
    FinalBlendSpec("v296_final_med_v185_prune_cardio_pulm_highconf_assoc", "v296 final med+v185 cardio/pulm prune highconf ASSOC", "final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC", True, PRIVATE_KEEP_ALL, (), (), CARDIO_PULM_PRUNE, "highconf"),
    FinalBlendSpec("v296_final_med_v185_prune_thyroid_highconf_assoc", "v296 final med+v185 thyroid prune highconf ASSOC", "final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC", True, PRIVATE_KEEP_ALL, (), (), THYROID_PRUNE, "highconf"),
    FinalBlendSpec("v296_final_med_v185_prune_resp_highconf_assoc", "v296 final med+v185 respiratory prune highconf ASSOC", "final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC", True, PRIVATE_KEEP_ALL, (), (), RESPIRATORY_PRUNE, "highconf"),
    FinalBlendSpec("v296_final_v185_zero_thyroid_broad_assoc", "v296 final v185 zero thyroid broad ASSOC", "final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC", False, PRIVATE_KEEP_ALL, (HYPERTHYROIDISM, HYPOTHYROIDISM), (), (), "broad"),
    FinalBlendSpec("v296_final_v185_zero_pulmonary_broad_assoc", "v296 final v185 zero pulmonary broad ASSOC", "final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC", False, PRIVATE_KEEP_ALL, (ILD, BRONCHITIS), (), (), "broad"),
    FinalBlendSpec("v296_final_v185_zero_derm_npc_broad_assoc", "v296 final v185 zero Derm/NPC broad ASSOC", "final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC", False, PRIVATE_KEEP_ALL, (DERMATOMYCOSIS, NPC), (), (), "broad"),
    FinalBlendSpec("v296_final_v185_add_hidden_broad_assoc", "v296 final v185 add hidden broad ASSOC", "final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC", False, PRIVATE_KEEP_ALL, (), (HEART_FAILURE, ILD, DERMATOMYCOSIS, NPC), (), "broad"),
    FinalBlendSpec("v296_final_v185_prune_renal_metabolic_broad_assoc", "v296 final v185 renal/metabolic prune broad ASSOC", "final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC", False, PRIVATE_KEEP_ALL, (), (), RENAL_METABOLIC_PRUNE, "broad"),
    FinalBlendSpec("v296_final_v185_prune_small_precision_broad_assoc", "v296 final v185 small precision prune broad ASSOC", "final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC", False, PRIVATE_KEEP_ALL, (), (), SMALL_PRECISION_PRUNE, "broad"),
    FinalBlendSpec("v296_final_v185_broad_private_prune_broad_assoc", "v296 final v185 broad private prune broad ASSOC", "aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty", False, PRIVATE_KEEP_ALL, (), (), BROAD_PRIVATE_PRUNE, "broad"),
    FinalBlendSpec("v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc", "v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC", "targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC", True, (CKD, UTI), (), (HEART_FAILURE, ILD), (), "broad", CONDITION_GROUPS["cardiorenal"]),
    FinalBlendSpec("v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc", "v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC", "targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC", True, (DIABETES, PNEUMONIA), (), (DERMATOMYCOSIS, NPC), (), "broad", CONDITION_GROUPS["pulmonary"]),
    FinalBlendSpec("v296_final_med_v185_zero_endocrine_endocrine_assoc", "v296 final med+v185 zero endocrine ASSOC", "targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only", True, PRIVATE_KEEP_ALL, (HYPERTHYROIDISM, HYPOTHYROIDISM), (), (), "broad", CONDITION_GROUPS["endocrine"]),
    FinalBlendSpec("v296_final_v185_ckd_uti_gout_ckd_neuro_assoc", "v296 final CKD/UTI neuro-rheum prune ASSOC", "targeted final fallback: CKD/UTI v185, ICP/Gout/CKD prune, neuro-rheum ASSOC", False, (CKD, UTI), (), (), NEURO_CKD_PRUNE, "broad", CONDITION_GROUPS["neuro_rheum"]),
    FinalBlendSpec("v296_final_v185_add_hidden_broad_private_no_assoc", "v296 final v185 hidden add broad private prune", "private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty", False, PRIVATE_KEEP_ALL, (), (HEART_FAILURE, ILD, DERMATOMYCOSIS, NPC), BROAD_PRIVATE_PRUNE),
]


def clear_assoc_diff(df: pd.DataFrame) -> None:
    for condition in df["Condition"]:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])


def copy_keep(df: pd.DataFrame, source: pd.DataFrame, condition: str) -> None:
    set_codes(df, condition, "KEEP", get_codes(source, condition, "KEEP"))


def apply_assoc_only(df: pd.DataFrame, spec: FinalBlendSpec, code_order: list[str]) -> None:
    if spec.assoc_family is None:
        return
    assoc_map = ASSOC_DIFF_HIGH_CONF if spec.assoc_family == "highconf" else ASSOC_DIFF_BROAD
    conditions = spec.assoc_conditions if spec.assoc_conditions is not None else tuple(assoc_map)
    for condition in conditions:
        if condition in PUBLIC_ASSOC_DIFF_EMPTY:
            continue
        if condition not in assoc_map:
            raise KeyError(f"missing ASSOC map for {condition}")
        nodes = assoc_map[condition]["ASSOCIATION"]
        set_codes(df, condition, "ASSOCIATION", expand_nodes(nodes, code_order))


def candidate_frame(
    base: pd.DataFrame,
    private: pd.DataFrame,
    med_positive: pd.DataFrame,
    zero_frames: dict[str, pd.DataFrame],
    add_frames: dict[str, pd.DataFrame],
    spec: FinalBlendSpec,
    code_order: list[str],
) -> pd.DataFrame:
    df = base.copy()
    if spec.add_mediastinum_positive:
        copy_keep(df, med_positive, MEDIASTINUM)
    for condition in spec.private_keep_conditions:
        copy_keep(df, private, condition)
    for condition in spec.zero_keep_conditions:
        copy_keep(df, zero_frames[condition], condition)
    for condition in spec.add_keep_conditions:
        copy_keep(df, add_frames[condition], condition)
    for edit in spec.prune_edits:
        set_codes(df, edit.condition, "KEEP", drop_prefixes(get_codes(df, edit.condition, "KEEP"), edit.prefixes))
    clear_assoc_diff(df)
    apply_assoc_only(df, spec, code_order)
    return df


def write_july16_final_blends(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    required_paths = {BASE_BEST, BASE_PRIVATE, MED_POSITIVE, *ZERO_SOURCES.values(), *ADD_SOURCES.values()}
    for path in required_paths:
        if not path.exists():
            raise FileNotFoundError(path)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_BEST)
    private = pd.read_csv(BASE_PRIVATE)
    med_positive = pd.read_csv(MED_POSITIVE)
    zero_frames = {condition: pd.read_csv(path) for condition, path in ZERO_SOURCES.items()}
    add_frames = {condition: pd.read_csv(path) for condition, path in ADD_SOURCES.items()}
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
        df = candidate_frame(base, private, med_positive, zero_frames, add_frames, spec, code_order)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 16 final blend candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-16-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=801)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july16_final_blends(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
