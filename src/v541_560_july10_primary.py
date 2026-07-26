"""Generate the July 10 primary adaptive plan.

The July 9 ASSOC-only screen was broadly negative, with only Epistaxis near
neutral. This batch avoids another broad role sweep. It uses the v296 public
anchor and spends most new files on small, explainable public probes:

- split the near-neutral Epistaxis ASSOC signal into smaller nodes;
- test mediastinum thymus/node additions one at a time;
- add back individual COPD families removed from v296;
- fill remaining slots with the shortest DIFF isolations from the prepared
  July 10 contingency.
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
        COPD,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        expand_nodes,
        get_codes,
        load_code_order,
        set_codes,
    )
except ModuleNotFoundError:
    from src.v281_300_assoc_diff import (
        COPD,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        expand_nodes,
        get_codes,
        load_code_order,
        set_codes,
    )


TARGET_COUNT = 20
BASE_BEST = SUBMISSIONS / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
EPISTAXIS = "Epistaxis"


@dataclass(frozen=True)
class ProbeSpec:
    slug: str
    message: str
    notes: str
    condition: str
    bucket: str
    nodes: tuple[str, ...]
    mode: str = "set"


@dataclass(frozen=True)
class ReferenceSpec:
    path: Path
    message: str
    notes: str


NEW_PROBES: tuple[ProbeSpec, ...] = (
    ProbeSpec(
        "v296_epistaxis_assoc_d68",
        "v296 Epistaxis ASSOC D68 only",
        "split near-neutral v521 Epistaxis ASSOC: coagulation defects only",
        EPISTAXIS,
        "ASSOCIATION",
        ("D68",),
    ),
    ProbeSpec(
        "v296_epistaxis_assoc_d69",
        "v296 Epistaxis ASSOC D69 only",
        "split near-neutral v521 Epistaxis ASSOC: purpura/platelet defects only",
        EPISTAXIS,
        "ASSOCIATION",
        ("D69",),
    ),
    ProbeSpec(
        "v296_epistaxis_assoc_i10",
        "v296 Epistaxis ASSOC I10 only",
        "split near-neutral v521 Epistaxis ASSOC: hypertension singleton only",
        EPISTAXIS,
        "ASSOCIATION",
        ("I10",),
    ),
    ProbeSpec(
        "v296_epistaxis_assoc_d68_d69",
        "v296 Epistaxis ASSOC D68+D69",
        "v521 minus hypertension; tests whether I10 caused the small public drop",
        EPISTAXIS,
        "ASSOCIATION",
        ("D68", "D69"),
    ),
    ProbeSpec(
        "v296_epistaxis_diff_r58",
        "v296 Epistaxis DIFF R58 only",
        "small DIFF probe: nonspecific hemorrhage only",
        EPISTAXIS,
        "DIFF",
        ("R58",),
    ),
    ProbeSpec(
        "v296_epistaxis_diff_k920",
        "v296 Epistaxis DIFF K920 only",
        "small DIFF probe: hematemesis as differential only",
        EPISTAXIS,
        "DIFF",
        ("K920",),
    ),
    ProbeSpec(
        "v296_med_add_c37",
        "v296 Mediastinum add C37",
        "split thymus/nodes addition: malignant thymus only",
        MEDIASTINUM,
        "KEEP",
        ("C37",),
        mode="add",
    ),
    ProbeSpec(
        "v296_med_add_d384",
        "v296 Mediastinum add D384",
        "split thymus/nodes addition: uncertain thymus neoplasm only",
        MEDIASTINUM,
        "KEEP",
        ("D384",),
        mode="add",
    ),
    ProbeSpec(
        "v296_med_add_c771",
        "v296 Mediastinum add C771",
        "split thymus/nodes addition: intrathoracic lymph nodes only",
        MEDIASTINUM,
        "KEEP",
        ("C771",),
        mode="add",
    ),
    ProbeSpec(
        "v296_med_add_a154",
        "v296 Mediastinum add A154",
        "split thymus/nodes addition: intrathoracic lymph node tuberculosis only",
        MEDIASTINUM,
        "KEEP",
        ("A154",),
        mode="add",
    ),
    ProbeSpec(
        "v296_copd_addback_j81",
        "v296 COPD add back J81",
        "single-family addback from v296 COPD prune: pulmonary edema",
        COPD,
        "KEEP",
        ("J81",),
        mode="add",
    ),
    ProbeSpec(
        "v296_copd_addback_j82",
        "v296 COPD add back J82",
        "single-family addback from v296 COPD prune: pulmonary eosinophilia",
        COPD,
        "KEEP",
        ("J82",),
        mode="add",
    ),
    ProbeSpec(
        "v296_copd_addback_j93",
        "v296 COPD add back J93",
        "single-family addback from v296 COPD prune: pneumothorax/air leak",
        COPD,
        "KEEP",
        ("J93",),
        mode="add",
    ),
    ProbeSpec(
        "v296_copd_addback_j95",
        "v296 COPD add back J95",
        "single-family addback from v296 COPD prune: postprocedural respiratory disorders",
        COPD,
        "KEEP",
        ("J95",),
        mode="add",
    ),
    ProbeSpec(
        "v296_copd_addback_j81_j93",
        "v296 COPD add back J81+J93",
        "paired addback of the two shorter removed COPD families",
        COPD,
        "KEEP",
        ("J81", "J93"),
        mode="add",
    ),
    ProbeSpec(
        "v296_copd_addback_j82_j95",
        "v296 COPD add back J82+J95",
        "paired addback of eosinophilia plus postprocedural respiratory disorders",
        COPD,
        "KEEP",
        ("J82", "J95"),
        mode="add",
    ),
)


REFERENCE_PROBES: tuple[ReferenceSpec, ...] = (
    ReferenceSpec(
        SUBMISSIONS / "v565_v296_diff_thyroiditis.csv",
        "v565: v296 isolate Thyroiditis DIFF only",
        "short DIFF fallback promoted into primary plan; volume=6",
    ),
    ReferenceSpec(
        SUBMISSIONS / "v566_v296_diff_ckd.csv",
        "v566: v296 isolate CKD DIFF only",
        "short DIFF fallback promoted into primary plan; volume=6",
    ),
    ReferenceSpec(
        SUBMISSIONS / "v568_v296_diff_hematemesis.csv",
        "v568: v296 isolate Hematemesis DIFF only",
        "short DIFF fallback promoted into primary plan; volume=2",
    ),
    ReferenceSpec(
        SUBMISSIONS / "v571_v296_diff_hypoparathyroidism.csv",
        "v571: v296 isolate Hypoparathyroidism DIFF only",
        "short DIFF fallback promoted into primary plan; volume=10",
    ),
    ReferenceSpec(
        SUBMISSIONS / "v572_v296_diff_hyperparathyroidism.csv",
        "v572: v296 isolate Hyperparathyroidism DIFF only",
        "short DIFF fallback promoted into primary plan; volume=5",
    ),
    ReferenceSpec(
        SUBMISSIONS / "v580_v296_diff_diabetes.csv",
        "v580: v296 isolate Diabetes DIFF only",
        "short DIFF fallback promoted into primary plan; volume=7",
    ),
)


def add_codes(existing: list[str], additions: list[str]) -> list[str]:
    seen = set(existing)
    out = list(existing)
    for code in additions:
        if code not in seen:
            seen.add(code)
            out.append(code)
    return out


def candidate_frame(base: pd.DataFrame, spec: ProbeSpec, code_order: list[str]) -> pd.DataFrame:
    df = base.copy()
    codes = expand_nodes(spec.nodes, code_order)
    if spec.mode == "add":
        codes = add_codes(get_codes(df, spec.condition, spec.bucket), codes)
    elif spec.mode != "set":
        raise ValueError(f"unknown probe mode: {spec.mode}")
    set_codes(df, spec.condition, spec.bucket, codes)
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
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


def write_july10_primary(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if not BASE_BEST.exists():
        raise FileNotFoundError(BASE_BEST)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    target_versions = set(range(start_version, start_version + TARGET_COUNT))
    base = pd.read_csv(BASE_BEST)
    code_order = load_code_order()
    used_versions = existing_versions() - target_versions
    existing_keys = {
        csv_key_from_path(path)
        for path in SUBMISSIONS.glob("*.csv")
        if local_version(path) not in target_versions
    }
    plan_keys: set[str] = set()
    rows: list[dict[str, str]] = []
    written: list[Path] = []
    version = start_version

    for spec in NEW_PROBES:
        if len(rows) >= TARGET_COUNT:
            break
        while version in used_versions:
            version += 1
        path = SUBMISSIONS / f"v{version}_{spec.slug}.csv"
        df = candidate_frame(base, spec, code_order)
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

    for ref in REFERENCE_PROBES:
        if len(rows) >= TARGET_COUNT:
            break
        if not ref.path.exists():
            raise FileNotFoundError(ref.path)
        key = csv_key_from_path(ref.path)
        if key in plan_keys:
            continue
        plan_keys.add(key)
        rows.append({
            "file": str(ref.path.relative_to(ROOT)),
            "message": ref.message[:120],
            "notes": ref.notes,
        })
        written.append(ref.path)

    if len(rows) != TARGET_COUNT:
        raise RuntimeError(f"generated {len(rows)} July 10 primary rows; expected {TARGET_COUNT}")

    if not dry_run:
        out_plan.parent.mkdir(parents=True, exist_ok=True)
        with out_plan.open("w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["file", "message", "notes"], lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    return written


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-10.csv")
    parser.add_argument("--start-version", type=int, default=541)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july10_primary(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
