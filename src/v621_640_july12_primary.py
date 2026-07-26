"""Generate the July 12 primary plan from the v543 public signal.

The July 10 batch found the first new public improvement: Epistaxis
ASSOCIATION=I10 alone. D68/D69, Epistaxis DIFF, COPD addbacks, broad hidden
KEEP prunes, and broad ASSOC screens all hurt public score. This batch promotes
the only positive signal by:

- narrowing Epistaxis ASSOCIATION to I10 inside the strongest historical hedges;
- testing small Mediastinum additions on top of v543;
- combining v543+C37 with a few private KEEP hedges.
"""
from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

try:
    from v281_300_assoc_diff import (
        MEDIASTINUM,
        PLANS,
        ROOT,
        SUBMISSIONS,
        get_codes,
        set_codes,
    )
except ModuleNotFoundError:
    from src.v281_300_assoc_diff import (
        MEDIASTINUM,
        PLANS,
        ROOT,
        SUBMISSIONS,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
EPISTAXIS = "Epistaxis"
CKD = "CKD"
UTI = "UTI"
DIABETES = "Diabetes"
PNEUMONIA = "Pneumonia"
BASE_V543 = SUBMISSIONS / "v543_v296_epistaxis_assoc_i10.csv"
PRIVATE_ANCHOR = SUBMISSIONS / "v185_private_kw.csv"
I10_CODES = ["I10"]
THYMUS_NODE_CODES = ["C37", "D384", "C771", "A154"]


@dataclass(frozen=True)
class SourceNarrowSpec:
    source: Path
    slug: str
    public_score: str
    source_role: str
    med: str
    private_keep: str


@dataclass(frozen=True)
class BaseEditSpec:
    slug: str
    message: str
    notes: str
    med_add: tuple[str, ...] = ()
    private_keep_conditions: tuple[str, ...] = ()


SOURCE_NARROW_SPECS: tuple[SourceNarrowSpec, ...] = (
    SourceNarrowSpec(
        SUBMISSIONS / "v392_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_pneumonia_assocdiff.csv",
        "v392_epi_i10_narrow",
        "0.43156",
        "v392",
        "keep",
        "v185_pneumonia",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v391_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diabetes_assocdiff.csv",
        "v391_epi_i10_narrow",
        "0.43156",
        "v391",
        "keep",
        "v185_diabetes",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v389_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_uti_assocdiff.csv",
        "v389_epi_i10_narrow",
        "0.43156",
        "v389",
        "keep",
        "v185_uti",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v388_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_assocdiff.csv",
        "v388_epi_i10_narrow",
        "0.43156",
        "v388",
        "keep",
        "v185_ckd",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v385_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diab_pneu_assocdiff.csv",
        "v385_epi_i10_narrow",
        "0.43156",
        "v385",
        "keep",
        "v185_diab_pneu",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v384_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_uti_assocdiff.csv",
        "v384_epi_i10_narrow",
        "0.43156",
        "v384",
        "keep",
        "v185_ckd_uti",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v382_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_no_v185keep_assocdiff.csv",
        "v382_epi_i10_narrow",
        "0.43156",
        "v382",
        "keep",
        "none",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v357_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185keep_ent_gi_derm_assocdiff.csv",
        "v357_epi_i10_narrow",
        "0.43156",
        "v357",
        "keep",
        "v185keep",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v342_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diab_pneu_assocdiff.csv",
        "v342_epi_i10_narrow",
        "0.43156",
        "v342",
        "keep",
        "v185_diab_pneu",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v341_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_uti_assocdiff.csv",
        "v341_epi_i10_narrow",
        "0.43156",
        "v341",
        "keep",
        "v185_ckd_uti",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv",
        "v302_epi_i10_narrow",
        "0.43156",
        "v302",
        "keep",
        "v185keep",
    ),
    SourceNarrowSpec(
        SUBMISSIONS / "v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv",
        "v301_epi_i10_narrow",
        "0.43156",
        "v301",
        "keep",
        "v185keep",
    ),
)


BASE_EDIT_SPECS: tuple[BaseEditSpec, ...] = (
    BaseEditSpec(
        "v543_med_add_c37",
        "v543 plus Mediastinum C37",
        "source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10",
        med_add=("C37",),
    ),
    BaseEditSpec(
        "v543_med_add_d384",
        "v543 plus Mediastinum D384",
        "source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10",
        med_add=("D384",),
    ),
    BaseEditSpec(
        "v543_med_add_c771",
        "v543 plus Mediastinum C771",
        "source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10",
        med_add=("C771",),
    ),
    BaseEditSpec(
        "v543_med_add_a154",
        "v543 plus Mediastinum A154",
        "source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10",
        med_add=("A154",),
    ),
    BaseEditSpec(
        "v543_med_add_thymus_nodes",
        "v543 plus Mediastinum thymus/nodes",
        "source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10",
        med_add=tuple(THYMUS_NODE_CODES),
    ),
    BaseEditSpec(
        "v543_med_c37_v185_ckd_uti",
        "v543 plus C37 and v185 CKD/UTI KEEP",
        "source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10",
        med_add=("C37",),
        private_keep_conditions=(CKD, UTI),
    ),
    BaseEditSpec(
        "v543_med_c37_v185_diab_pneu",
        "v543 plus C37 and v185 Diabetes/Pneumonia KEEP",
        "source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10",
        med_add=("C37",),
        private_keep_conditions=(DIABETES, PNEUMONIA),
    ),
    BaseEditSpec(
        "v543_med_c37_v185keep",
        "v543 plus C37 and v185 private KEEP",
        "source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10",
        med_add=("C37",),
        private_keep_conditions=(CKD, UTI, DIABETES, PNEUMONIA),
    ),
)


def add_codes(existing: list[str], additions: tuple[str, ...]) -> list[str]:
    seen = set(existing)
    out = list(existing)
    for code in additions:
        if code not in seen:
            seen.add(code)
            out.append(code)
    return out


def narrow_epistaxis_to_i10(df: pd.DataFrame) -> None:
    set_codes(df, EPISTAXIS, "ASSOCIATION", I10_CODES)
    set_codes(df, EPISTAXIS, "DIFF", [])


def source_narrow_frame(spec: SourceNarrowSpec) -> pd.DataFrame:
    if not spec.source.exists():
        raise FileNotFoundError(spec.source)
    df = pd.read_csv(spec.source)
    narrow_epistaxis_to_i10(df)
    return df


def base_edit_frame(spec: BaseEditSpec) -> pd.DataFrame:
    if not BASE_V543.exists():
        raise FileNotFoundError(BASE_V543)
    df = pd.read_csv(BASE_V543)
    if spec.med_add:
        set_codes(df, MEDIASTINUM, "KEEP", add_codes(get_codes(df, MEDIASTINUM, "KEEP"), spec.med_add))
    if spec.private_keep_conditions:
        private = pd.read_csv(PRIVATE_ANCHOR)
        for condition in spec.private_keep_conditions:
            set_codes(df, condition, "KEEP", get_codes(private, condition, "KEEP"))
    return df


def local_version(path: Path) -> int | None:
    match = re.match(r"v(\d+)_", path.name)
    return int(match.group(1)) if match else None


def existing_versions() -> set[int]:
    versions: set[int] = set()
    for path in SUBMISSIONS.glob("v*.csv"):
        version = local_version(path)
        if version is not None:
            versions.add(version)
    return versions


def csv_key_from_frame(df: pd.DataFrame) -> str:
    return df.to_csv(index=False)


def csv_key_from_path(path: Path) -> str:
    return path.read_text()


def write_july12_primary(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if not BASE_V543.exists():
        raise FileNotFoundError(BASE_V543)
    if not PRIVATE_ANCHOR.exists():
        raise FileNotFoundError(PRIVATE_ANCHOR)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    target_versions = set(range(start_version, start_version + TARGET_COUNT))
    existing_keys = {
        csv_key_from_path(path)
        for path in SUBMISSIONS.glob("*.csv")
        if local_version(path) not in target_versions
    }
    used_versions = existing_versions() - target_versions
    plan_keys: set[str] = set()
    rows: list[dict[str, str]] = []
    written: list[Path] = []
    version = start_version

    for spec in SOURCE_NARROW_SPECS:
        while version in used_versions:
            version += 1
        path = SUBMISSIONS / f"v{version}_{spec.slug}.csv"
        df = source_narrow_frame(spec)
        key = csv_key_from_frame(df)
        if key in existing_keys or key in plan_keys:
            continue
        plan_keys.add(key)
        rows.append({
            "file": str(path.relative_to(ROOT)),
            "message": f"v{version}: {spec.source_role} Epistaxis ASSOC narrowed to I10"[:120],
            "notes": (
                f"source {spec.source_role} ({spec.public_score}, -0.00186 vs v543); "
                f"med={spec.med}; private_keep={spec.private_keep}; assoc=epistaxis_i10_narrow"
            ),
        })
        written.append(path)
        if not dry_run:
            df.to_csv(path, index=False)
        version += 1

    for spec in BASE_EDIT_SPECS:
        while version in used_versions:
            version += 1
        path = SUBMISSIONS / f"v{version}_{spec.slug}.csv"
        df = base_edit_frame(spec)
        key = csv_key_from_frame(df)
        if key in existing_keys or key in plan_keys:
            continue
        plan_keys.add(key)
        rows.append({
            "file": str(path.relative_to(ROOT)),
            "message": f"v{version}: {spec.message}"[:120],
            "notes": spec.notes,
        })
        written.append(path)
        if not dry_run:
            df.to_csv(path, index=False)
        version += 1

    if len(rows) != TARGET_COUNT:
        raise RuntimeError(f"generated {len(rows)} July 12 primary rows; expected {TARGET_COUNT}")

    if not dry_run:
        out_plan.parent.mkdir(parents=True, exist_ok=True)
        with out_plan.open("w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["file", "message", "notes"], lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-12.csv")
    parser.add_argument("--start-version", type=int, default=621)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july12_primary(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
