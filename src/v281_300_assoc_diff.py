"""Generate the first ASSOC/DIFF-focused batch after the 2026-07-01 strategy revision.

The plan preserves the current public anchor (`v209`, COPD J20/J45 pruned) and
adds selective ASSOCIATION/DIFF nodes only for public-invisible conditions.
COPD and Enlarged Mediastinum keep ASSOC/DIFF empty by design.
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
ICD = ROOT / "data" / "icd_dict.csv"
BASE_PUBLIC = SUBMISSIONS / "v209_copd_no_acute_bronch_asthma.csv"
BASE_PRIVATE = SUBMISSIONS / "v185_private_kw.csv"
TARGET_COUNT = 20

COPD = "Chronic Obstructive Pulmonary Disease"
MEDIASTINUM = "Enlarged Mediastinum"
PUBLIC_ASSOC_DIFF_EMPTY = {COPD, MEDIASTINUM}


NodeSpec = dict[str, dict[str, tuple[str, ...]]]


ASSOC_DIFF_HIGH_CONF: NodeSpec = {
    "Epistaxis": {
        "ASSOCIATION": ("D68", "D69", "I10"),
        "DIFF": ("R58", "K920"),
    },
    "Gout": {
        "ASSOCIATION": ("E79", "N18"),
        "DIFF": ("M00", "M11"),
    },
    "Pleurisy": {
        "ASSOCIATION": ("J90", "J91", "A15"),
        "DIFF": ("J18", "I26"),
    },
    "Bronchitis": {
        "ASSOCIATION": ("J44",),
        "DIFF": ("J18", "J45"),
    },
    "Thyroiditis": {
        "ASSOCIATION": ("E03", "E05"),
        "DIFF": ("E04",),
    },
    "CKD": {
        "ASSOCIATION": ("I12", "I13", "E112", "D63"),
        "DIFF": ("N17",),
    },
    "Hypothyroidism": {
        "ASSOCIATION": ("E06", "E01", "E04"),
        "DIFF": ("E05",),
    },
    "Hematemesis": {
        "ASSOCIATION": ("K25", "K26", "K27", "I85", "K29"),
        "DIFF": ("K921", "R042"),
    },
    "Heart Failure": {
        "ASSOCIATION": ("I42", "I48", "N18"),
        "DIFF": ("J44", "I26"),
    },
    "Interstitial Lung Disease": {
        "ASSOCIATION": ("M35", "D86"),
        "DIFF": ("J18", "I50"),
    },
    "Hypoparathyroidism": {
        "ASSOCIATION": ("E8351",),
        "DIFF": ("E21", "E55"),
    },
    "Hyperparathyroidism": {
        "ASSOCIATION": ("E8352", "N25"),
        "DIFF": ("E20",),
    },
    "Hyperthyroidism": {
        "ASSOCIATION": ("E06", "I48"),
        "DIFF": ("E03", "F41"),
    },
    "Pneumonia": {
        "ASSOCIATION": ("A41", "J90", "J96"),
        "DIFF": ("J20", "J40", "A15", "C34", "I50"),
    },
}


ASSOC_DIFF_BROAD: NodeSpec = {
    **ASSOC_DIFF_HIGH_CONF,
    "Intracranial Pressure": {
        "ASSOCIATION": ("G91", "H4711"),
        "DIFF": ("G43", "R51", "C71", "D33"),
    },
    "Latent Adrenal Insufficiency": {
        "ASSOCIATION": ("E31", "E03"),
        "DIFF": ("E86", "R53"),
    },
    "Dermatomycosis": {
        "ASSOCIATION": ("B37", "E11"),
        "DIFF": ("L40", "L20", "L30"),
    },
    "Nasopharyngeal Carcinoma": {
        "ASSOCIATION": ("B27", "C77"),
        "DIFF": ("C10", "C14", "J33"),
    },
    "UTI": {
        "ASSOCIATION": ("N10", "N12", "A41"),
        "DIFF": ("N30", "N34", "N76"),
    },
    "Diabetes": {
        "ASSOCIATION": ("E112", "E113", "E114", "E115", "E116", "E66"),
        "DIFF": ("R73",),
    },
}


CONDITION_GROUPS = {
    "pulmonary": ("Pleurisy", "Bronchitis", "Interstitial Lung Disease", "Pneumonia"),
    "cardiorenal": ("CKD", "Heart Failure", "Diabetes"),
    "endocrine": (
        "Latent Adrenal Insufficiency",
        "Thyroiditis",
        "Hypothyroidism",
        "Hypoparathyroidism",
        "Hyperparathyroidism",
        "Hyperthyroidism",
        "Diabetes",
    ),
    "ent_gi_derm": ("Epistaxis", "Dermatomycosis", "Hematemesis", "Nasopharyngeal Carcinoma"),
    "neuro_rheum": ("Intracranial Pressure", "Gout"),
}


@dataclass(frozen=True)
class BatchSpec:
    slug: str
    message: str
    notes: str
    assoc_diff: NodeSpec | None = None
    buckets: tuple[str, ...] = ("ASSOCIATION", "DIFF")
    conditions: tuple[str, ...] | None = None
    base_private_keep: bool = False
    keep_remove: dict[str, tuple[str, ...]] | None = None
    keep_add: dict[str, tuple[str, ...]] | None = None


SPECS = [
    BatchSpec("assocdiff_highconf_both", "assoc/diff high-confidence both", "ASSOC+DIFF on high-confidence hidden conditions", ASSOC_DIFF_HIGH_CONF),
    BatchSpec("assocdiff_highconf_diff", "assoc/diff high-confidence DIFF only", "isolates DIFF signal on high-confidence hidden conditions", ASSOC_DIFF_HIGH_CONF, buckets=("DIFF",)),
    BatchSpec("assocdiff_highconf_assoc", "assoc/diff high-confidence ASSOC only", "isolates ASSOC signal on high-confidence hidden conditions", ASSOC_DIFF_HIGH_CONF, buckets=("ASSOCIATION",)),
    BatchSpec("assocdiff_broad_both", "assoc/diff broad both", "adds broader curated hidden-condition map", ASSOC_DIFF_BROAD),
    BatchSpec("assocdiff_broad_diff", "assoc/diff broad DIFF only", "broad DIFF-only private hedge", ASSOC_DIFF_BROAD, buckets=("DIFF",)),
    BatchSpec("assocdiff_broad_assoc", "assoc/diff broad ASSOC only", "broad ASSOC-only private hedge", ASSOC_DIFF_BROAD, buckets=("ASSOCIATION",)),
    BatchSpec("assocdiff_pulmonary", "assoc/diff pulmonary hidden set", "pulmonary private conditions only", ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["pulmonary"]),
    BatchSpec("assocdiff_cardiorenal", "assoc/diff cardio-renal hidden set", "CKD/HF/Diabetes private-condition map", ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["cardiorenal"]),
    BatchSpec("assocdiff_endocrine", "assoc/diff endocrine hidden set", "thyroid/parathyroid/adrenal/diabetes private-condition map", ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["endocrine"]),
    BatchSpec("assocdiff_ent_gi_derm", "assoc/diff ENT GI derm hidden set", "Epistaxis/Derm/GI/NPC private-condition map", ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["ent_gi_derm"]),
    BatchSpec("assocdiff_neuro_rheum", "assoc/diff neuro rheum hidden set", "Intracranial pressure plus gout map", ASSOC_DIFF_BROAD, conditions=CONDITION_GROUPS["neuro_rheum"]),
    BatchSpec("v209_private_keep_assocdiff", "v209 plus v185 private KEEP and assoc/diff", "combines best public COPD prune, v185 private KEEP hedge, and broad ASSOC/DIFF", ASSOC_DIFF_BROAD, base_private_keep=True),
    BatchSpec("copd_no_j20_j45_j31_j98", "COPD remove J20/J45/J31/J98", "public combo: v209 plus J31/J98 removals", keep_remove={COPD: ("J31", "J98")}),
    BatchSpec("copd_no_j20_j45_j81_j82", "COPD remove J20/J45/J81/J82", "public combo: v209 plus pulmonary edema/eosinophilia removals", keep_remove={COPD: ("J81", "J82")}),
    BatchSpec("copd_no_j20_j45_j93_j95", "COPD remove J20/J45/J93/J95", "public combo: v209 plus pneumothorax/postprocedural removals", keep_remove={COPD: ("J93", "J95")}),
    BatchSpec("copd_no_j20_j45_j81_j82_j93_j95", "COPD remove J20/J45/J81/J82/J93/J95", "public combo: combine strongest non-J96 COPD removals", keep_remove={COPD: ("J81", "J82", "J93", "J95")}),
    BatchSpec("med_no_j98", "mediastinum remove J98", "unsubmitted mediastinum public ablation", keep_remove={MEDIASTINUM: ("J98",)}),
    BatchSpec("med_no_d15_c38", "mediastinum remove D15/C38", "mediastinum neoplasm-family ablation combo", keep_remove={MEDIASTINUM: ("D15", "C38")}),
    BatchSpec("med_add_c852", "mediastinum add C852 lymphoma", "unsubmitted mediastinal B-cell lymphoma addition", keep_add={MEDIASTINUM: ("C852", "C8520", "C8521", "C8522", "C8523", "C8524", "C8525", "C8526", "C8527", "C8528", "C8529")}),
    BatchSpec("med_add_thymus_nodes", "mediastinum add thymus/nodes", "small thymus and intrathoracic-node addition", keep_add={MEDIASTINUM: ("C37", "D384", "C771", "A154")}),
]


def parse_codes(value: str) -> list[str]:
    if pd.isna(value) or value == "Not Applicable":
        return []
    return [code.strip() for code in str(value).split(";") if code.strip()]


def fmt(codes: list[str]) -> str:
    return "; ".join(codes) if codes else "Not Applicable"


def dataframe_key(df: pd.DataFrame) -> str:
    return df.to_csv(index=False)


def load_code_order() -> list[str]:
    icd = pd.read_csv(ICD)
    return icd["icd_code"].astype(str).str.strip().tolist()


def expand_nodes(nodes: tuple[str, ...], code_order: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for node in nodes:
        matches = [code for code in code_order if code.startswith(node)]
        if not matches:
            raise ValueError(f"ICD node has no descendants in dictionary: {node}")
        for code in matches:
            if code not in seen:
                seen.add(code)
                out.append(code)
    return out


def get_codes(df: pd.DataFrame, condition: str, column: str = "KEEP") -> list[str]:
    rows = df.loc[df["Condition"].eq(condition), column]
    if rows.empty:
        raise ValueError(f"condition not found: {condition}")
    return parse_codes(rows.iloc[0])


def set_codes(df: pd.DataFrame, condition: str, column: str, codes: list[str]) -> None:
    if not df["Condition"].eq(condition).any():
        raise ValueError(f"condition not found: {condition}")
    df.loc[df["Condition"].eq(condition), column] = fmt(codes)


def add_codes(codes: list[str], additions: tuple[str, ...]) -> list[str]:
    seen = set(codes)
    out = list(codes)
    for code in additions:
        if code not in seen:
            seen.add(code)
            out.append(code)
    return out


def drop_prefixes(codes: list[str], prefixes: tuple[str, ...]) -> list[str]:
    return [code for code in codes if not code.startswith(prefixes)]


def copy_private_keep(base: pd.DataFrame) -> pd.DataFrame:
    private = pd.read_csv(BASE_PRIVATE)
    out = base.copy()
    for condition in private["Condition"]:
        if condition in PUBLIC_ASSOC_DIFF_EMPTY:
            continue
        set_codes(out, condition, "KEEP", get_codes(private, condition, "KEEP"))
    return out


def apply_assoc_diff(df: pd.DataFrame, spec: BatchSpec, code_order: list[str]) -> None:
    if spec.assoc_diff is None:
        return
    allowed = set(spec.conditions) if spec.conditions else set(spec.assoc_diff)
    for condition, buckets in spec.assoc_diff.items():
        if condition not in allowed or condition in PUBLIC_ASSOC_DIFF_EMPTY:
            continue
        for bucket in spec.buckets:
            nodes = buckets.get(bucket, ())
            set_codes(df, condition, bucket, expand_nodes(nodes, code_order))


def apply_keep_edits(df: pd.DataFrame, spec: BatchSpec) -> None:
    for condition, prefixes in (spec.keep_remove or {}).items():
        set_codes(df, condition, "KEEP", drop_prefixes(get_codes(df, condition), prefixes))
    for condition, additions in (spec.keep_add or {}).items():
        set_codes(df, condition, "KEEP", add_codes(get_codes(df, condition), additions))


def candidate_frame(base: pd.DataFrame, spec: BatchSpec, code_order: list[str]) -> pd.DataFrame:
    df = copy_private_keep(base) if spec.base_private_keep else base.copy()
    apply_assoc_diff(df, spec, code_order)
    apply_keep_edits(df, spec)
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_assoc_diff_batch(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    if not BASE_PUBLIC.exists():
        raise FileNotFoundError(BASE_PUBLIC)
    if not BASE_PRIVATE.exists():
        raise FileNotFoundError(BASE_PRIVATE)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_PUBLIC)
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
            raise RuntimeError(f"duplicate assoc/diff candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-03.csv")
    parser.add_argument("--start-version", type=int, default=281)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_assoc_diff_batch(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
