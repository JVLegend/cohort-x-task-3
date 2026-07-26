"""Generate the July 16 primary plan from the v715 C39 plateau.

The July 15 batch confirmed that the full C39/C390/C399 family is needed, that
pulmonary ASSOC/DIFF variants are harmful, and that CKD/UTI/Diabetes/Pneumonia
private KEEP overlays are public-neutral. This plan keeps v715 as the public
anchor, fills the remaining private KEEP subset matrix, and then tests small
Mediastinum overlays on top of the C39 core.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

try:
    from v281_300_assoc_diff import (
        BASE_PRIVATE,
        MEDIASTINUM,
        PLANS,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )
except ModuleNotFoundError:
    from src.v281_300_assoc_diff import (
        BASE_PRIVATE,
        MEDIASTINUM,
        PLANS,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
BASE_C39 = SUBMISSIONS / "v715_v633_med_add_c39.csv"

CKD = "CKD"
UTI = "UTI"
DIABETES = "Diabetes"
PNEUMONIA = "Pneumonia"


@dataclass(frozen=True)
class PrivateKeepSpec:
    slug: str
    message: str
    notes: str
    conditions: tuple[str, ...]


@dataclass(frozen=True)
class MediastinumSpec:
    slug: str
    message: str
    notes: str
    additions: tuple[str, ...]


PRIVATE_KEEP_SPECS: tuple[PrivateKeepSpec, ...] = (
    PrivateKeepSpec("v715_v185_ckd_diabetes", "v715 plus CKD+Diabetes private KEEP", "fill untested public-neutral v185 subset: CKD and Diabetes", (CKD, DIABETES)),
    PrivateKeepSpec("v715_v185_ckd_pneumonia", "v715 plus CKD+Pneumonia private KEEP", "fill untested public-neutral v185 subset: CKD and Pneumonia", (CKD, PNEUMONIA)),
    PrivateKeepSpec("v715_v185_uti_diabetes", "v715 plus UTI+Diabetes private KEEP", "fill untested public-neutral v185 subset: UTI and Diabetes", (UTI, DIABETES)),
    PrivateKeepSpec("v715_v185_uti_pneumonia", "v715 plus UTI+Pneumonia private KEEP", "fill untested public-neutral v185 subset: UTI and Pneumonia", (UTI, PNEUMONIA)),
    PrivateKeepSpec("v715_v185_ckd_uti_diabetes", "v715 plus CKD+UTI+Diabetes private KEEP", "fill untested public-neutral v185 subset: CKD, UTI, Diabetes", (CKD, UTI, DIABETES)),
    PrivateKeepSpec("v715_v185_ckd_uti_pneumonia", "v715 plus CKD+UTI+Pneumonia private KEEP", "fill untested public-neutral v185 subset: CKD, UTI, Pneumonia", (CKD, UTI, PNEUMONIA)),
    PrivateKeepSpec("v715_v185_ckd_diabetes_pneumonia", "v715 plus CKD+Diabetes+Pneumonia private KEEP", "fill untested public-neutral v185 subset: CKD, Diabetes, Pneumonia", (CKD, DIABETES, PNEUMONIA)),
    PrivateKeepSpec("v715_v185_uti_diabetes_pneumonia", "v715 plus UTI+Diabetes+Pneumonia private KEEP", "fill untested public-neutral v185 subset: UTI, Diabetes, Pneumonia", (UTI, DIABETES, PNEUMONIA)),
)


MEDIASTINUM_SPECS: tuple[MediastinumSpec, ...] = (
    MediastinumSpec("v715_med_add_e329", "v715 plus E329 thymus disease unspecified", "C39 core plus singleton thymus disease addback", ("E329",)),
    MediastinumSpec("v715_med_add_e321", "v715 plus E321 thymus abscess", "C39 core plus singleton thymus abscess addback", ("E321",)),
    MediastinumSpec("v715_med_add_c7a091", "v715 plus C7A091 malignant thymus carcinoid", "C39 core plus malignant carcinoid tumor of thymus", ("C7A091",)),
    MediastinumSpec("v715_med_add_d3a091", "v715 plus D3A091 benign thymus carcinoid", "C39 core plus benign carcinoid tumor of thymus", ("D3A091",)),
    MediastinumSpec("v715_med_add_z8523", "v715 plus Z8523 thymus cancer history", "C39 core plus personal history of malignant neoplasm of thymus", ("Z8523",)),
    MediastinumSpec("v715_med_add_c852", "v715 plus C852 mediastinal B-cell lymphoma", "C39 core plus root mediastinal thymic large B-cell lymphoma", ("C852",)),
    MediastinumSpec("v715_med_add_c8522", "v715 plus C8522 intrathoracic B-cell lymphoma", "C39 core plus intrathoracic lymph node mediastinal lymphoma", ("C8522",)),
    MediastinumSpec("v715_med_add_p252", "v715 plus P252 pneumomediastinum", "C39 core plus pneumomediastinum singleton", ("P252",)),
    MediastinumSpec("v715_med_add_n80b5", "v715 plus N80B5 mediastinal endometriosis", "C39 core plus mediastinal endometriosis singleton", ("N80B5",)),
    MediastinumSpec("v715_med_add_d174", "v715 plus D174 intrathoracic lipoma", "C39 core plus benign intrathoracic lipoma singleton", ("D174",)),
    MediastinumSpec("v715_med_add_thymus_carcinoids", "v715 plus thymus carcinoids", "C39 core plus malignant and benign thymus carcinoids", ("C7A091", "D3A091")),
    MediastinumSpec("v715_med_add_c852_family", "v715 plus C852 lymphoma family", "C39 core plus full mediastinal thymic large B-cell lymphoma family", ("C852", "C8520", "C8521", "C8522", "C8523", "C8524", "C8525", "C8526", "C8527", "C8528", "C8529")),
)


def add_codes(existing: list[str], additions: tuple[str, ...]) -> list[str]:
    seen = set(existing)
    out = list(existing)
    for code in additions:
        if code not in seen:
            seen.add(code)
            out.append(code)
    return out


def private_keep_frame(base: pd.DataFrame, private: pd.DataFrame, spec: PrivateKeepSpec) -> pd.DataFrame:
    df = base.copy()
    for condition in spec.conditions:
        set_codes(df, condition, "KEEP", get_codes(private, condition, "KEEP"))
    return df


def mediastinum_frame(base: pd.DataFrame, spec: MediastinumSpec) -> pd.DataFrame:
    df = base.copy()
    set_codes(df, MEDIASTINUM, "KEEP", add_codes(get_codes(df, MEDIASTINUM, "KEEP"), spec.additions))
    return df


def write_july16_primary(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(PRIVATE_KEEP_SPECS) + len(MEDIASTINUM_SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(PRIVATE_KEEP_SPECS) + len(MEDIASTINUM_SPECS)}")
    if not BASE_C39.exists():
        raise FileNotFoundError(BASE_C39)
    if not BASE_PRIVATE.exists():
        raise FileNotFoundError(BASE_PRIVATE)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_C39)
    private = pd.read_csv(BASE_PRIVATE)
    all_specs = (*PRIVATE_KEEP_SPECS, *MEDIASTINUM_SPECS)
    target_paths = [SUBMISSIONS / f"v{start_version + idx}_{spec.slug}.csv" for idx, spec in enumerate(all_specs)]
    target_set = set(target_paths)
    existing_keys = {
        dataframe_key(pd.read_csv(path))
        for path in SUBMISSIONS.glob("*.csv")
        if path not in target_set
    }

    rows: list[dict[str, str]] = []
    written: list[Path] = []
    seen_keys: set[str] = set()
    for idx, spec in enumerate(all_specs):
        version = start_version + idx
        path = SUBMISSIONS / f"v{version}_{spec.slug}.csv"
        if isinstance(spec, PrivateKeepSpec):
            df = private_keep_frame(base, private, spec)
        else:
            df = mediastinum_frame(base, spec)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 16 primary candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-16.csv")
    parser.add_argument("--start-version", type=int, default=781)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july16_primary(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
