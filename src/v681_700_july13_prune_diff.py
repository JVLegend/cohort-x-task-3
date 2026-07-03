"""Generate a July 13 KEEP-prune plus DIFF contingency plan.

The preferred July 13 path should be an adaptive plan from July 12 scores, so
this fallback starts at v681 and leaves v661-v680 available for that primary
path. Candidates combine one hidden-condition KEEP precision prune with that
same condition's DIFF-only map. This is a higher-risk complement to the July 12
ASSOC version because broad DIFF hurt public score, so it stays a fallback.
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
UTI = "UTI"
DIABETES = "Diabetes"
ILD = "Interstitial Lung Disease"
HYPOPARATHYROIDISM = "Hypoparathyroidism"
HYPERTHYROIDISM = "Hyperthyroidism"
PNEUMONIA = "Pneumonia"
DERMATOMYCOSIS = "Dermatomycosis"


@dataclass(frozen=True)
class PruneDiffSpec:
    slug: str
    condition: str
    prefixes: tuple[str, ...]
    message: str
    notes: str


SPECS = [
    PruneDiffSpec("v296_icp_no_g96_g94_diff", ICP, ("G96", "G94"), "v296 ICP prune G96/G94 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_gout_no_e79_diff", GOUT, ("E79",), "v296 Gout prune E79 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_pleurisy_no_r09_j95_diff", PLEURISY, ("R09", "J95"), "v296 Pleurisy prune R09/J95 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_bronchitis_no_j43_j68_diff", BRONCHITIS, ("J43", "J68"), "v296 Bronchitis prune J43/J68 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_thyroiditis_no_e03_diff", THYROIDITIS, ("E03",), "v296 Thyroiditis prune E03 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_npc_no_d00_c44_d10_diff", NPC, ("D00", "C44", "D10"), "v296 NPC prune D00/C44/D10 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_ckd_no_q60_q61_q62_diff", CKD, ("Q60", "Q61", "Q62"), "v296 CKD prune congenital Q plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_ckd_no_i50_diff", CKD, ("I50",), "v296 CKD prune I50 plus DIFF", "small CKD KEEP prune plus CKD DIFF"),
    PruneDiffSpec("v296_hypothyroid_no_e04_diff", HYPOTHYROIDISM, ("E04",), "v296 Hypothyroidism prune E04 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_hematemesis_no_r36_k66_diff", HEMATEMESIS, ("R36", "K66"), "v296 Hematemesis prune R36/K66 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_hf_no_i97_diff", HEART_FAILURE, ("I97",), "v296 Heart Failure prune I97 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_uti_no_obstetric_diff", UTI, ("O23", "O86", "O03"), "v296 UTI prune obstetric plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_uti_no_n35_diff", UTI, ("N35",), "v296 UTI prune N35 plus DIFF", "small UTI KEEP prune plus UTI DIFF"),
    PruneDiffSpec("v296_diabetes_no_o24_diff", DIABETES, ("O24",), "v296 Diabetes prune O24 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_diabetes_no_z_p70_diff", DIABETES, ("Z79", "Z86", "P70"), "v296 Diabetes prune Z/P70 plus DIFF", "small Diabetes KEEP prune plus Diabetes DIFF"),
    PruneDiffSpec("v296_ild_no_j70_diff", ILD, ("J70",), "v296 ILD prune J70 plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_hypopara_no_e23_e87_p71_e21_diff", HYPOPARATHYROIDISM, ("E23", "E87", "P71", "E21"), "v296 Hypopara prune related plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_hyperthyroid_no_e04_e01_e03_p72_diff", HYPERTHYROIDISM, ("E04", "E01", "E03", "P72"), "v296 Hyperthyroid prune non-hyper plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_pneumonia_no_a37_p23_j84_j85_diff", PNEUMONIA, ("A37", "P23", "J84", "J85"), "v296 Pneumonia prune noisy plus DIFF", "same-condition KEEP precision plus broad DIFF isolation"),
    PruneDiffSpec("v296_derm_no_b37_diff", DERMATOMYCOSIS, ("B37",), "v296 Dermatomycosis prune B37 plus DIFF", "new Dermatomycosis KEEP precision plus broad DIFF isolation"),
]


def candidate_frame(base: pd.DataFrame, spec: PruneDiffSpec, code_order: list[str]) -> pd.DataFrame:
    df = base.copy()
    set_codes(df, spec.condition, "KEEP", drop_prefixes(get_codes(df, spec.condition, "KEEP"), spec.prefixes))
    diff_nodes = ASSOC_DIFF_BROAD[spec.condition]["DIFF"]
    set_codes(df, spec.condition, "ASSOCIATION", [])
    set_codes(df, spec.condition, "DIFF", expand_nodes(diff_nodes, code_order))
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_july13_prune_diff(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    if not BASE_BEST.exists():
        raise FileNotFoundError(BASE_BEST)
    missing = [spec.condition for spec in SPECS if spec.condition not in ASSOC_DIFF_BROAD]
    if missing:
        raise KeyError(f"missing DIFF specs: {missing}")
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
            raise RuntimeError(f"duplicate July 13 KEEP prune+DIFF candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-13-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=681)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july13_prune_diff(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
