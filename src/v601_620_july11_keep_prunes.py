"""Generate a July 11 hidden KEEP-pruning contingency plan.

The preferred July 11 path should be an adaptive plan from July 10 scores, so
this fallback starts at v601 and leaves v581-v600 available for that primary
path. Candidates prune suspicious KEEP families in public-invisible conditions
on the v296 anchor. These are precision probes for private-score false positives
and deliberately avoid COPD/Mediastinum public movers.
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


@dataclass(frozen=True)
class KeepPruneSpec:
    slug: str
    condition: str
    prefixes: tuple[str, ...]
    message: str
    notes: str


SPECS = [
    KeepPruneSpec("v296_icp_no_g96_g94", ICP, ("G96", "G94"), "v296 ICP prune G96/G94", "remove non-core CNS disorder families from ICP KEEP"),
    KeepPruneSpec("v296_gout_no_e79", GOUT, ("E79",), "v296 Gout prune E79", "remove hyperuricemia/metabolism family from Gout KEEP"),
    KeepPruneSpec("v296_pleurisy_no_r09_j95", PLEURISY, ("R09", "J95"), "v296 Pleurisy prune R09/J95", "remove symptoms/postprocedural respiratory families from Pleurisy KEEP"),
    KeepPruneSpec("v296_bronchitis_no_j43_j68", BRONCHITIS, ("J43", "J68"), "v296 Bronchitis prune J43/J68", "remove emphysema/inhalation families from Bronchitis KEEP"),
    KeepPruneSpec("v296_thyroiditis_no_e03", THYROIDITIS, ("E03",), "v296 Thyroiditis prune E03", "remove hypothyroidism family from Thyroiditis KEEP"),
    KeepPruneSpec("v296_npc_no_d00_c44_d10", NPC, ("D00", "C44", "D10"), "v296 NPC prune D00/C44/D10", "remove carcinoma-in-situ/skin/benign mouth families from NPC KEEP"),
    KeepPruneSpec("v296_ckd_no_q60_q61_q62", CKD, ("Q60", "Q61", "Q62"), "v296 CKD prune congenital Q families", "remove congenital renal malformation families from CKD KEEP"),
    KeepPruneSpec("v296_ckd_no_i50", CKD, ("I50",), "v296 CKD prune I50", "remove heart failure family from CKD KEEP"),
    KeepPruneSpec("v296_hypothyroid_no_e04", HYPOTHYROIDISM, ("E04",), "v296 Hypothyroidism prune E04", "remove nontoxic goiter family from Hypothyroidism KEEP"),
    KeepPruneSpec("v296_hematemesis_no_r36_k66", HEMATEMESIS, ("R36", "K66"), "v296 Hematemesis prune R36/K66", "remove urethral/peritoneal families from Hematemesis KEEP"),
    KeepPruneSpec("v296_hf_no_i97", HEART_FAILURE, ("I97",), "v296 Heart Failure prune I97", "remove large postprocedural circulatory family from HF KEEP"),
    KeepPruneSpec("v296_hypergonadism_no_e27", HYPERGONADISM, ("E27",), "v296 Hypergonadism prune E27", "remove adrenal family from Hypergonadism KEEP"),
    KeepPruneSpec("v296_uti_no_obstetric", UTI, ("O23", "O86", "O03"), "v296 UTI prune obstetric families", "remove pregnancy/puerperal/abortion infection families from UTI KEEP"),
    KeepPruneSpec("v296_uti_no_n35", UTI, ("N35",), "v296 UTI prune N35", "remove urethral stricture family from UTI KEEP"),
    KeepPruneSpec("v296_diabetes_no_o24", DIABETES, ("O24",), "v296 Diabetes prune O24", "remove pregnancy diabetes family from Diabetes KEEP"),
    KeepPruneSpec("v296_diabetes_no_z_p70", DIABETES, ("Z79", "Z86", "P70"), "v296 Diabetes prune Z/P70", "remove therapy/history/newborn metabolism extras from Diabetes KEEP"),
    KeepPruneSpec("v296_ild_no_j70", ILD, ("J70",), "v296 ILD prune J70", "remove external-agent respiratory family from ILD KEEP"),
    KeepPruneSpec("v296_hypopara_no_e23_e87_p71_e21", HYPOPARATHYROIDISM, ("E23", "E87", "P71", "E21"), "v296 Hypopara prune related endocrine/noise", "remove pituitary/fluid/neonatal/opposite parathyroid families from Hypopara KEEP"),
    KeepPruneSpec("v296_hyperthyroid_no_e04_e01_e03_p72", HYPERTHYROIDISM, ("E04", "E01", "E03", "P72"), "v296 Hyperthyroid prune non-hyperthyroid", "remove goiter/iodine/hypothyroid/neonatal families from Hyperthyroidism KEEP"),
    KeepPruneSpec("v296_pneumonia_no_a37_p23_j84_j85", PNEUMONIA, ("A37", "P23", "J84", "J85"), "v296 Pneumonia prune noisy families", "remove whooping-cough/congenital/ILD/abscess families from Pneumonia KEEP"),
]


def candidate_frame(base: pd.DataFrame, spec: KeepPruneSpec) -> pd.DataFrame:
    df = base.copy()
    set_codes(df, spec.condition, "KEEP", drop_prefixes(get_codes(df, spec.condition, "KEEP"), spec.prefixes))
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_july11_keep_prunes(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
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
            raise RuntimeError(f"duplicate July 11 KEEP prune candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-11-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=601)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july11_keep_prunes(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
