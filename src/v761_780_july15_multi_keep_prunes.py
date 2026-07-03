"""Generate a July 15 multi-condition KEEP-prune contingency plan.

The preferred July 15 path should be an adaptive plan from July 14 scores, so
this fallback starts at v761 and leaves v741-v760 available for that primary
path. Candidates combine clinically related KEEP-prune edits in public-invisible
conditions on the v296 anchor while keeping ASSOC/DIFF empty. This is meant as
a final-window private hedge family, not a public leaderboard chase.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

try:
    from v281_300_assoc_diff import (
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        drop_prefixes,
        get_codes,
        set_codes,
    )
except ModuleNotFoundError:
    from src.v281_300_assoc_diff import (
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        drop_prefixes,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
BASE_BEST = SUBMISSIONS / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"

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


@dataclass(frozen=True)
class KeepEdit:
    condition: str
    prefixes: tuple[str, ...]


@dataclass(frozen=True)
class MultiPruneSpec:
    slug: str
    edits: tuple[KeepEdit, ...]
    message: str
    notes: str


SPECS = [
    MultiPruneSpec(
        "v296_portfolio_renal_metabolic_obstetric_prune",
        (KeepEdit(CKD, ("Q60", "Q61", "Q62")), KeepEdit(DIABETES, ("O24",)), KeepEdit(UTI, ("O23", "O86", "O03"))),
        "v296 renal/metabolic obstetric KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_cardio_pulm_noise_prune",
        (KeepEdit(CKD, ("I50",)), KeepEdit(HEART_FAILURE, ("I97",)), KeepEdit(ILD, ("J70",))),
        "v296 cardio/pulm procedural KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_thyroid_axis_prune",
        (KeepEdit(THYROIDITIS, ("E03",)), KeepEdit(HYPOTHYROIDISM, ("E04",)), KeepEdit(HYPERTHYROIDISM, ("E04", "E01", "E03", "P72"))),
        "v296 thyroid-axis KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_respiratory_noise_prune",
        (KeepEdit(PLEURISY, ("R09", "J95")), KeepEdit(BRONCHITIS, ("J43", "J68")), KeepEdit(PNEUMONIA, ("A37", "P23", "J84", "J85"))),
        "v296 respiratory-noise KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_gi_gu_skin_prune",
        (KeepEdit(HEMATEMESIS, ("R36", "K66")), KeepEdit(UTI, ("N35",)), KeepEdit(DERMATOMYCOSIS, ("B37",))),
        "v296 GI/GU/skin false-positive KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_ent_skin_endocrine_prune",
        (KeepEdit(NPC, ("D00", "C44", "D10")), KeepEdit(DERMATOMYCOSIS, ("B37",)), KeepEdit(HYPERGONADISM, ("E27",))),
        "v296 ENT/skin/endocrine KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_ckd_diabetes_full_prune",
        (KeepEdit(CKD, ("Q60", "Q61", "Q62")), KeepEdit(CKD, ("I50",)), KeepEdit(DIABETES, ("O24",)), KeepEdit(DIABETES, ("Z79", "Z86", "P70"))),
        "v296 CKD+Diabetes KEEP precision prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_uti_diabetes_obstetric_prune",
        (KeepEdit(UTI, ("O23", "O86", "O03")), KeepEdit(UTI, ("N35",)), KeepEdit(DIABETES, ("O24",))),
        "v296 UTI+Diabetes obstetric/GU KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_endocrine_small_prune",
        (KeepEdit(HYPOPARATHYROIDISM, ("E23", "E87", "P71", "E21")), KeepEdit(HYPERTHYROIDISM, ("E04", "E01", "E03", "P72")), KeepEdit(HYPOTHYROIDISM, ("E04",))),
        "v296 endocrine KEEP precision prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_neuro_cardioresp_prune",
        (KeepEdit(ICP, ("G96", "G94")), KeepEdit(PLEURISY, ("R09", "J95")), KeepEdit(HEART_FAILURE, ("I97",))),
        "v296 neuro/cardioresp KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_lower_resp_precision_prune",
        (KeepEdit(BRONCHITIS, ("J43", "J68")), KeepEdit(PNEUMONIA, ("A37", "P23", "J84", "J85")), KeepEdit(ILD, ("J70",))),
        "v296 lower-respiratory KEEP precision prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_bleed_pleura_bronch_prune",
        (KeepEdit(HEMATEMESIS, ("R36", "K66")), KeepEdit(PLEURISY, ("R09", "J95")), KeepEdit(BRONCHITIS, ("J43", "J68"))),
        "v296 bleed/pleura/bronchitis KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_ent_thyroid_prune",
        (KeepEdit(NPC, ("D00", "C44", "D10")), KeepEdit(THYROIDITIS, ("E03",)), KeepEdit(HYPOTHYROIDISM, ("E04",))),
        "v296 ENT+thyroid KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_gout_ckd_prune",
        (KeepEdit(GOUT, ("E79",)), KeepEdit(CKD, ("Q60", "Q61", "Q62")), KeepEdit(CKD, ("I50",))),
        "v296 Gout+CKD KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_obstetric_metabolic_renal_prune",
        (KeepEdit(DIABETES, ("O24",)), KeepEdit(DIABETES, ("Z79", "Z86", "P70")), KeepEdit(CKD, ("Q60", "Q61", "Q62")), KeepEdit(UTI, ("O23", "O86", "O03"))),
        "v296 obstetric/metabolic/renal KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_hf_ckd_pneumonia_prune",
        (KeepEdit(HEART_FAILURE, ("I97",)), KeepEdit(CKD, ("I50",)), KeepEdit(PNEUMONIA, ("A37", "P23", "J84", "J85"))),
        "v296 HF+CKD+Pneumonia KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_derm_uti_diabetes_prune",
        (KeepEdit(DERMATOMYCOSIS, ("B37",)), KeepEdit(UTI, ("N35",)), KeepEdit(DIABETES, ("Z79", "Z86", "P70"))),
        "v296 Derm+UTI+Diabetes KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_neuro_endocrine_prune",
        (KeepEdit(ICP, ("G96", "G94")), KeepEdit(HYPOPARATHYROIDISM, ("E23", "E87", "P71", "E21")), KeepEdit(HYPERTHYROIDISM, ("E04", "E01", "E03", "P72"))),
        "v296 neuro+endocrine KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_small_high_precision_prune",
        (KeepEdit(GOUT, ("E79",)), KeepEdit(CKD, ("I50",)), KeepEdit(HEART_FAILURE, ("I97",)), KeepEdit(UTI, ("N35",)), KeepEdit(ILD, ("J70",)), KeepEdit(HEMATEMESIS, ("R36", "K66"))),
        "v296 small high-precision KEEP prune",
        "intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
    MultiPruneSpec(
        "v296_portfolio_broad_private_prune",
        (
            KeepEdit(ICP, ("G96", "G94")),
            KeepEdit(GOUT, ("E79",)),
            KeepEdit(PLEURISY, ("R09", "J95")),
            KeepEdit(BRONCHITIS, ("J43", "J68")),
            KeepEdit(THYROIDITIS, ("E03",)),
            KeepEdit(NPC, ("D00", "C44", "D10")),
            KeepEdit(CKD, ("Q60", "Q61", "Q62", "I50")),
            KeepEdit(HYPOTHYROIDISM, ("E04",)),
            KeepEdit(HEMATEMESIS, ("R36", "K66")),
            KeepEdit(HEART_FAILURE, ("I97",)),
            KeepEdit(UTI, ("O23", "O86", "O03", "N35")),
            KeepEdit(DIABETES, ("O24", "Z79", "Z86", "P70")),
            KeepEdit(ILD, ("J70",)),
            KeepEdit(HYPOPARATHYROIDISM, ("E23", "E87", "P71", "E21")),
            KeepEdit(HYPERTHYROIDISM, ("E04", "E01", "E03", "P72")),
            KeepEdit(PNEUMONIA, ("A37", "P23", "J84", "J85")),
            KeepEdit(DERMATOMYCOSIS, ("B37",)),
        ),
        "v296 broad private KEEP prune",
        "intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty",
    ),
]


def candidate_frame(base: pd.DataFrame, spec: MultiPruneSpec) -> pd.DataFrame:
    df = base.copy()
    for edit in spec.edits:
        set_codes(df, edit.condition, "KEEP", drop_prefixes(get_codes(df, edit.condition, "KEEP"), edit.prefixes))
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_july15_multi_keep_prunes(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    if not BASE_BEST.exists():
        raise FileNotFoundError(BASE_BEST)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_BEST)
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
        df = candidate_frame(base, spec)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 15 multi KEEP prune candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-15-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=761)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july15_multi_keep_prunes(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
