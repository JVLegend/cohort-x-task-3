"""Generate a public-mover contingency plan for 2026-07-03.

This plan is deliberately separate from the adaptive v221-v240 path. Use it
only if the v201-v220 scores do not yield a safe nonnegative adaptive combo and
we still want a public-signal batch before falling back to private hedges.
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
BASE_PUBLIC = SUBMISSIONS / "v178_FINAL.csv"
TARGET_COUNT = 20

COPD = "Chronic Obstructive Pulmonary Disease"
MEDIASTINUM = "Enlarged Mediastinum"


@dataclass(frozen=True)
class PublicSpec:
    slug: str
    condition: str
    message: str
    notes: str
    add: tuple[str, ...] = ()
    remove_prefixes: tuple[str, ...] = ()


SPECS = [
    PublicSpec("copd_no_j40", COPD, "contingency: COPD remove J40", "core COPD ablation: unspecified bronchitis", remove_prefixes=("J40",)),
    PublicSpec("copd_no_j41", COPD, "contingency: COPD remove J41", "core COPD ablation: simple/mucopurulent chronic bronchitis", remove_prefixes=("J41",)),
    PublicSpec("copd_no_j42", COPD, "contingency: COPD remove J42", "core COPD ablation: unspecified chronic bronchitis", remove_prefixes=("J42",)),
    PublicSpec("copd_no_j43", COPD, "contingency: COPD remove J43", "core COPD ablation: emphysema", remove_prefixes=("J43",)),
    PublicSpec("copd_no_j44", COPD, "contingency: COPD remove J44", "core COPD ablation: explicit COPD codes", remove_prefixes=("J44",)),
    PublicSpec("copd_no_j47", COPD, "contingency: COPD remove J47", "core COPD ablation: bronchiectasis", remove_prefixes=("J47",)),
    PublicSpec("copd_no_j40_j47", COPD, "contingency: COPD remove J40/J47", "combined non-COPD-ish bronchitis/bronchiectasis ablation", remove_prefixes=("J40", "J47")),
    PublicSpec("copd_add_j479", COPD, "contingency: COPD add J479", "isolated bronchiectasis uncomplicated addition", add=("J479",)),
    PublicSpec("copd_add_q334", COPD, "contingency: COPD add Q334", "isolated congenital bronchiectasis addition", add=("Q334",)),
    PublicSpec("copd_add_j479_q334", COPD, "contingency: COPD add J479/Q334", "small bronchiectasis completion addition", add=("J479", "Q334")),
    PublicSpec("med_no_c78", MEDIASTINUM, "contingency: mediastinum remove C78", "mediastinum ablation: secondary neoplasm of mediastinum", remove_prefixes=("C78",)),
    PublicSpec("med_no_d38", MEDIASTINUM, "contingency: mediastinum remove D38", "mediastinum ablation: uncertain behavior neoplasm", remove_prefixes=("D38",)),
    PublicSpec("med_no_j85", MEDIASTINUM, "contingency: mediastinum remove J85", "mediastinum ablation: abscess of mediastinum", remove_prefixes=("J85",)),
    PublicSpec("med_add_thymus_neoplasm", MEDIASTINUM, "contingency: mediastinum add thymus neoplasm", "targeted thymus/thymic neoplasm addition", add=("C37", "C7A091", "D3A091", "D384")),
    PublicSpec("med_add_e32_thymus", MEDIASTINUM, "contingency: mediastinum add E32 thymus", "targeted non-neoplasm thymus disease addition", add=("E32", "E320", "E321", "E328", "E329")),
    PublicSpec("med_add_c771_nodes", MEDIASTINUM, "contingency: mediastinum add C771", "isolated intrathoracic lymph-node metastasis addition", add=("C771",)),
    PublicSpec("med_add_c39_intrathoracic", MEDIASTINUM, "contingency: mediastinum add C39", "isolated ill-defined intrathoracic malignancy addition", add=("C39",)),
    PublicSpec("med_add_a154_tb_nodes", MEDIASTINUM, "contingency: mediastinum add A154", "isolated intrathoracic lymph-node tuberculosis addition", add=("A154",)),
    PublicSpec("med_add_d174_lipoma", MEDIASTINUM, "contingency: mediastinum add D174", "isolated benign intrathoracic lipoma addition", add=("D174",)),
    PublicSpec(
        "med_add_lymphoma_nodes",
        MEDIASTINUM,
        "contingency: mediastinum add lymphoma nodes",
        "intrathoracic lymph-node lymphoma addition, separate from C852 mediastinal B-cell probe",
        add=(
            "C8102", "C8112", "C8122", "C8132", "C8142", "C8172", "C8192",
            "C8202", "C8212", "C8222", "C8232", "C8242", "C8252", "C8262",
            "C8282", "C8292", "C8302", "C8312", "C8332", "C8352", "C8372",
            "C8382", "C8392", "C8402", "C8412", "C8442", "C8462", "C8472",
            "C8492", "C84A2", "C84Z2", "C8512", "C8582", "C8592",
        ),
    ),
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


def add_codes(codes: list[str], additions: tuple[str, ...]) -> list[str]:
    seen = set(codes)
    out = list(codes)
    for code in additions:
        if code not in seen:
            out.append(code)
            seen.add(code)
    return out


def drop_prefixes(codes: list[str], prefixes: tuple[str, ...]) -> list[str]:
    return [code for code in codes if not code.startswith(prefixes)]


def dataframe_key(df: pd.DataFrame) -> str:
    return df.to_csv(index=False)


def candidate_frame(base: pd.DataFrame, spec: PublicSpec) -> pd.DataFrame:
    df = base.copy()
    codes = get_codes(df, spec.condition)
    if spec.remove_prefixes:
        codes = drop_prefixes(codes, spec.remove_prefixes)
    if spec.add:
        codes = add_codes(codes, spec.add)
    set_codes(df, spec.condition, codes)
    return df


def write_public_contingency(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    if not BASE_PUBLIC.exists():
        raise FileNotFoundError(BASE_PUBLIC)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_PUBLIC)
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
            raise RuntimeError(f"duplicate public contingency candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-03-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=261)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_public_contingency(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
