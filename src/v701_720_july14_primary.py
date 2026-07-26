"""Generate the July 14 primary plan from the v633 C37 signal.

The July 13 batch found a narrow public improvement: v543 plus C37 in Enlarged
Mediastinum. D384, C771, and A154 were negative as isolated additions, while
private KEEP variants tied. This plan keeps the v633 core and spends the daily
budget on small Mediastinum-focused additions plus a few private-hedge variants.
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
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
BASE_C37 = SUBMISSIONS / "v633_v543_med_add_c37.csv"
BASE_C37_CKD_UTI = SUBMISSIONS / "v638_v543_med_c37_v185_ckd_uti.csv"
BASE_C37_DIAB_PNEU = SUBMISSIONS / "v639_v543_med_c37_v185_diab_pneu.csv"
BASE_C37_V185 = SUBMISSIONS / "v640_v543_med_c37_v185keep.csv"


@dataclass(frozen=True)
class MediastinumSpec:
    source: Path
    slug: str
    message: str
    notes: str
    med_add: tuple[str, ...]


SPECS: tuple[MediastinumSpec, ...] = (
    MediastinumSpec(BASE_C37, "v633_med_add_e32", "v633 plus E32 thymus diseases", "C37 core plus low-volume non-neoplasm thymus family", ("E32", "E320", "E321", "E328", "E329")),
    MediastinumSpec(BASE_C37, "v633_med_add_e329", "v633 plus E329 thymus disease unspecified", "C37 core plus singleton thymus disease", ("E329",)),
    MediastinumSpec(BASE_C37, "v633_med_add_e320_e328_e329", "v633 plus E320/E328/E329 thymus disease", "C37 core plus non-abscess thymus disease cluster", ("E320", "E328", "E329")),
    MediastinumSpec(BASE_C37, "v633_med_add_e321", "v633 plus E321 thymus abscess", "C37 core plus abscess of thymus singleton", ("E321",)),
    MediastinumSpec(BASE_C37, "v633_med_add_c7a091", "v633 plus C7A091 malignant thymus carcinoid", "C37 core plus malignant carcinoid tumor of thymus", ("C7A091",)),
    MediastinumSpec(BASE_C37, "v633_med_add_d3a091", "v633 plus D3A091 benign thymus carcinoid", "C37 core plus benign carcinoid tumor of thymus", ("D3A091",)),
    MediastinumSpec(BASE_C37, "v633_med_add_thymus_carcinoids", "v633 plus thymus carcinoids", "C37 core plus malignant and benign thymus carcinoids", ("C7A091", "D3A091")),
    MediastinumSpec(BASE_C37, "v633_med_add_z8523", "v633 plus Z8523 thymus cancer history", "C37 core plus personal history of malignant neoplasm of thymus", ("Z8523",)),
    MediastinumSpec(BASE_C37, "v633_med_add_z85230_z85238", "v633 plus thymus cancer history detail", "C37 core plus detailed thymus cancer history codes", ("Z85230", "Z85238")),
    MediastinumSpec(BASE_C37, "v633_med_add_c852", "v633 plus C852 mediastinal B-cell lymphoma", "C37 core plus root mediastinal thymic large B-cell lymphoma", ("C852",)),
    MediastinumSpec(BASE_C37, "v633_med_add_c8522", "v633 plus C8522 intrathoracic B-cell lymphoma", "C37 core plus intrathoracic lymph node mediastinal lymphoma", ("C8522",)),
    MediastinumSpec(BASE_C37, "v633_med_add_c852_family", "v633 plus C852 lymphoma family", "C37 core plus full mediastinal thymic large B-cell lymphoma family", ("C852", "C8520", "C8521", "C8522", "C8523", "C8524", "C8525", "C8526", "C8527", "C8528", "C8529")),
    MediastinumSpec(BASE_C37, "v633_med_add_p252", "v633 plus P252 pneumomediastinum", "C37 core plus pneumomediastinum singleton", ("P252",)),
    MediastinumSpec(BASE_C37, "v633_med_add_n80b5", "v633 plus N80B5 mediastinal endometriosis", "C37 core plus mediastinal endometriosis singleton", ("N80B5",)),
    MediastinumSpec(BASE_C37, "v633_med_add_c39", "v633 plus C39 ill-defined intrathoracic malignancy", "C37 core plus ill-defined intrathoracic malignancy", ("C39", "C390", "C399")),
    MediastinumSpec(BASE_C37, "v633_med_add_d174", "v633 plus D174 intrathoracic lipoma", "C37 core plus benign intrathoracic lipoma singleton", ("D174",)),
    MediastinumSpec(BASE_C37_CKD_UTI, "v638_med_add_e329", "v638 plus E329 thymus disease unspecified", "public-tied CKD/UTI hedge plus singleton thymus disease", ("E329",)),
    MediastinumSpec(BASE_C37_DIAB_PNEU, "v639_med_add_e329", "v639 plus E329 thymus disease unspecified", "public-tied Diabetes/Pneumonia hedge plus singleton thymus disease", ("E329",)),
    MediastinumSpec(BASE_C37_V185, "v640_med_add_e329", "v640 plus E329 thymus disease unspecified", "public-tied full v185 hedge plus singleton thymus disease", ("E329",)),
    MediastinumSpec(BASE_C37_V185, "v640_med_add_c8522", "v640 plus C8522 intrathoracic B-cell lymphoma", "public-tied full v185 hedge plus intrathoracic mediastinal lymphoma", ("C8522",)),
)


def add_codes(existing: list[str], additions: tuple[str, ...]) -> list[str]:
    seen = set(existing)
    out = list(existing)
    for code in additions:
        if code not in seen:
            seen.add(code)
            out.append(code)
    return out


def candidate_frame(spec: MediastinumSpec) -> pd.DataFrame:
    if not spec.source.exists():
        raise FileNotFoundError(spec.source)
    df = pd.read_csv(spec.source)
    set_codes(df, MEDIASTINUM, "KEEP", add_codes(get_codes(df, MEDIASTINUM, "KEEP"), spec.med_add))
    return df


def write_july14_primary(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

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
        df = candidate_frame(spec)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 14 primary candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-14.csv")
    parser.add_argument("--start-version", type=int, default=701)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july14_primary(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
