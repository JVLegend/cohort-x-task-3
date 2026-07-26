"""Generate the July 15 primary plan from the v715 C39 signal.

The July 14 batch found a strong public improvement: v633 plus the C39 family
(`C39`, `C390`, `C399`) reached 0.43606. Auto-next already materialized 15
C39/private-hedge candidates, but stopped short of a 20-item plan. This plan
reuses 14 of those candidates and adds six C39-family decompositions.
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
BASE_C39 = SUBMISSIONS / "v715_v633_med_add_c39.csv"


@dataclass(frozen=True)
class ReferenceSpec:
    path: Path
    message: str
    notes: str


@dataclass(frozen=True)
class GeneratedSpec:
    slug: str
    message: str
    notes: str
    med_add: tuple[str, ...]


REFERENCES: tuple[ReferenceSpec, ...] = (
    ReferenceSpec(SUBMISSIONS / "v741_v633_med_add_c39_med_keep_v185keep_assoc_only.csv", "v741: v633+C39 plus v185keep assoc-only", "auto-next C39 hedge: full v185 private KEEP, assoc-only"),
    ReferenceSpec(SUBMISSIONS / "v742_v633_med_add_c39_med_keep_v185_ckd_uti_assocdiff.csv", "v742: v633+C39 plus CKD/UTI assocdiff", "auto-next C39 hedge: CKD/UTI private KEEP plus assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v743_v633_med_add_c39_med_keep_v185_diab_pneu_assocdiff.csv", "v743: v633+C39 plus Diabetes/Pneumonia assocdiff", "auto-next C39 hedge: Diabetes/Pneumonia private KEEP plus assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v744_v633_med_add_c39_med_keep_v185keep_pulmonary_assocdiff.csv", "v744: v633+C39 plus v185keep pulmonary assocdiff", "auto-next C39 hedge: full v185 private KEEP plus pulmonary assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v745_v633_med_add_c39_med_keep_v185_ckd_assocdiff.csv", "v745: v633+C39 plus CKD assocdiff", "auto-next C39 hedge: CKD private KEEP plus assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v746_v633_med_add_c39_med_keep_no_v185keep_pulmonary_assocdiff.csv", "v746: v633+C39 plus no-v185 pulmonary assocdiff", "auto-next C39 hedge: no private KEEP plus pulmonary assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v747_v633_med_add_c39_med_keep_v185_uti_assocdiff.csv", "v747: v633+C39 plus UTI assocdiff", "auto-next C39 hedge: UTI private KEEP plus assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v748_v633_med_add_c39_med_keep_v185_ckd_uti_pulmonary_assocdiff.csv", "v748: v633+C39 plus CKD/UTI pulmonary assocdiff", "auto-next C39 hedge: CKD/UTI private KEEP plus pulmonary assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v749_v633_med_add_c39_med_keep_v185_diabetes_assocdiff.csv", "v749: v633+C39 plus Diabetes assocdiff", "auto-next C39 hedge: Diabetes private KEEP plus assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v750_v633_med_add_c39_med_keep_v185_pneumonia_assocdiff.csv", "v750: v633+C39 plus Pneumonia assocdiff", "auto-next C39 hedge: Pneumonia private KEEP plus assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v751_v633_med_add_c39_med_keep_v185_diab_pneu_pulmonary_assocdiff.csv", "v751: v633+C39 plus Diabetes/Pneumonia pulmonary assocdiff", "auto-next C39 hedge: Diabetes/Pneumonia private KEEP plus pulmonary assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v752_v633_med_add_c39_med_keep_v185_ckd_pulmonary_assocdiff.csv", "v752: v633+C39 plus CKD pulmonary assocdiff", "auto-next C39 hedge: CKD private KEEP plus pulmonary assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v753_v633_med_add_c39_med_keep_v185_uti_pulmonary_assocdiff.csv", "v753: v633+C39 plus UTI pulmonary assocdiff", "auto-next C39 hedge: UTI private KEEP plus pulmonary assocdiff"),
    ReferenceSpec(SUBMISSIONS / "v754_v633_med_add_c39_med_keep_v185_diabetes_pulmonary_assocdiff.csv", "v754: v633+C39 plus Diabetes pulmonary assocdiff", "auto-next C39 hedge: Diabetes private KEEP plus pulmonary assocdiff"),
)


GENERATED: tuple[GeneratedSpec, ...] = (
    GeneratedSpec("v633_med_add_c39_root", "v633 plus C39 root only", "decompose v715: root C39 only", ("C39",)),
    GeneratedSpec("v633_med_add_c390", "v633 plus C390 only", "decompose v715: upper respiratory tract unspecified", ("C390",)),
    GeneratedSpec("v633_med_add_c399", "v633 plus C399 only", "decompose v715: lower respiratory tract unspecified", ("C399",)),
    GeneratedSpec("v633_med_add_c39_c390", "v633 plus C39+C390", "decompose v715: root plus upper respiratory tract", ("C39", "C390")),
    GeneratedSpec("v633_med_add_c39_c399", "v633 plus C39+C399", "decompose v715: root plus lower respiratory tract", ("C39", "C399")),
    GeneratedSpec("v633_med_add_c390_c399", "v633 plus C390+C399", "decompose v715: children without root", ("C390", "C399")),
)


def add_codes(existing: list[str], additions: tuple[str, ...]) -> list[str]:
    seen = set(existing)
    out = list(existing)
    for code in additions:
        if code not in seen:
            seen.add(code)
            out.append(code)
    return out


def generated_frame(spec: GeneratedSpec) -> pd.DataFrame:
    if not BASE_C37.exists():
        raise FileNotFoundError(BASE_C37)
    df = pd.read_csv(BASE_C37)
    set_codes(df, MEDIASTINUM, "KEEP", add_codes(get_codes(df, MEDIASTINUM, "KEEP"), spec.med_add))
    return df


def write_july15_primary(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(REFERENCES) + len(GENERATED) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(REFERENCES) + len(GENERATED)}")
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    target_paths = [spec.path for spec in REFERENCES]
    target_paths.extend(SUBMISSIONS / f"v{start_version + idx}_{spec.slug}.csv" for idx, spec in enumerate(GENERATED))
    target_set = set(target_paths)
    existing_keys = {
        dataframe_key(pd.read_csv(path))
        for path in SUBMISSIONS.glob("*.csv")
        if path not in target_set
    }

    rows: list[dict[str, str]] = []
    written: list[Path] = []
    seen_keys: set[str] = set()
    for spec in REFERENCES:
        if not spec.path.exists():
            raise FileNotFoundError(spec.path)
        key = dataframe_key(pd.read_csv(spec.path))
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 15 reference candidate: {spec.path.name}")
        seen_keys.add(key)
        rows.append({
            "file": str(spec.path.relative_to(ROOT)),
            "message": spec.message[:120],
            "notes": spec.notes,
        })
        written.append(spec.path)

    for idx, spec in enumerate(GENERATED):
        version = start_version + idx
        path = SUBMISSIONS / f"v{version}_{spec.slug}.csv"
        df = generated_frame(spec)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 15 primary candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-15.csv")
    parser.add_argument("--start-version", type=int, default=821)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july15_primary(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
