"""Generate a higher-upside July 16 plan.

The conservative July 16 primary mostly spends slots on public-neutral private
KEEP hedges. This alternative uses the final window for public movement: precise
Mediastinum KEEP ablations on top of v715, plus C39 overlays on older top-scoring
composites. It is riskier, but it has a better chance to break the 0.43606 tie.
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
        drop_prefixes,
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
        drop_prefixes,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
BASE_C39 = SUBMISSIONS / "v715_v633_med_add_c39.csv"
C39_FAMILY = ("C37", "C39", "C390", "C399")


@dataclass(frozen=True)
class AblationSpec:
    slug: str
    message: str
    notes: str
    prefixes: tuple[str, ...]


@dataclass(frozen=True)
class OverlaySpec:
    source: Path
    slug: str
    message: str
    notes: str


ABLATIONS: tuple[AblationSpec, ...] = (
    AblationSpec("v715_med_drop_c78", "v715 drop C78 mediastinal secondary neoplasm", "fine public-upside ablation: remove C78/C781 while preserving C37+C39", ("C78",)),
    AblationSpec("v715_med_drop_d38", "v715 drop D38 uncertain mediastinal neoplasm", "fine public-upside ablation: remove D38/D383 while preserving C37+C39", ("D38",)),
    AblationSpec("v715_med_drop_j85", "v715 drop J85 abscess mediastinum", "fine public-upside ablation: remove J85/J853 while preserving C37+C39", ("J85",)),
    AblationSpec("v715_med_drop_q34", "v715 drop Q34 congenital mediastinum family", "fine public-upside ablation: remove Q34 family while preserving C37+C39", ("Q34",)),
    AblationSpec("v715_med_drop_c38", "v715 drop C38 heart/mediastinum/pleura malignancy", "single-family ablation split from earlier D15+C38 negative combo", ("C38",)),
    AblationSpec("v715_med_drop_d15", "v715 drop D15 benign intrathoracic family", "single-family ablation split from earlier D15+C38 negative combo", ("D15",)),
    AblationSpec("v715_med_drop_j980_j981", "v715 drop J980/J981 bronchus-collapse branch", "J98 was important when removed as a block; test smaller likely-noisy branch", ("J980", "J981")),
    AblationSpec("v715_med_drop_j982_j983_j984", "v715 drop J982/J983/J984 emphysema-respiratory branch", "J98 was important as a block; test smaller emphysema/other-respiratory branch", ("J982", "J983", "J984")),
    AblationSpec("v715_med_drop_j985", "v715 drop J985 mediastinum NEC branch", "direct mediastinum disease branch ablation inside the broad J98 family", ("J985",)),
    AblationSpec("v715_med_drop_j986_j988_j989", "v715 drop J986/J988/J989 other respiratory tail", "J98 tail ablation while keeping J985 mediastinum-specific codes", ("J986", "J988", "J989")),
    AblationSpec("v715_med_drop_c380_c384_c388", "v715 drop non-mediastinum C38 children", "keep C381/C382/C383 mediastinum children; remove heart/pleura/overlap children", ("C380", "C384", "C388")),
    AblationSpec("v715_med_drop_q34_nonmediastinal", "v715 drop non-mediastinum Q34 children", "keep Q341 congenital mediastinum cyst; remove broader Q34 respiratory malformations", ("Q340", "Q348", "Q349")),
)


OVERLAYS: tuple[OverlaySpec, ...] = (
    OverlaySpec(SUBMISSIONS / "v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv", "v301_add_c39_family", "v301 plus full C39 family", "C39 overlay on old broad-assoc top composite"),
    OverlaySpec(SUBMISSIONS / "v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv", "v302_add_c39_family", "v302 plus full C39 family", "C39 overlay on old highconf-assoc top composite"),
    OverlaySpec(SUBMISSIONS / "v341_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_uti_assocdiff.csv", "v341_add_c39_family", "v341 plus full C39 family", "C39 overlay on old CKD/UTI top composite"),
    OverlaySpec(SUBMISSIONS / "v342_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diab_pneu_assocdiff.csv", "v342_add_c39_family", "v342 plus full C39 family", "C39 overlay on old Diabetes/Pneumonia top composite"),
    OverlaySpec(SUBMISSIONS / "v357_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185keep_ent_gi_derm_assocdiff.csv", "v357_add_c39_family", "v357 plus full C39 family", "C39 overlay on old ENT/GI/Derm assoc top composite"),
    OverlaySpec(SUBMISSIONS / "v382_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_no_v185keep_assocdiff.csv", "v382_add_c39_family", "v382 plus full C39 family", "C39 overlay on no-v185keep top composite"),
    OverlaySpec(SUBMISSIONS / "v384_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_uti_assocdiff.csv", "v384_add_c39_family", "v384 plus full C39 family", "C39 overlay on July 6 CKD/UTI top composite"),
    OverlaySpec(SUBMISSIONS / "v385_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diab_pneu_assocdiff.csv", "v385_add_c39_family", "v385 plus full C39 family", "C39 overlay on July 6 Diabetes/Pneumonia top composite"),
)


def add_codes(existing: list[str], additions: tuple[str, ...]) -> list[str]:
    seen = set(existing)
    out = list(existing)
    for code in additions:
        if code not in seen:
            seen.add(code)
            out.append(code)
    return out


def ablation_frame(base: pd.DataFrame, spec: AblationSpec) -> pd.DataFrame:
    df = base.copy()
    set_codes(df, MEDIASTINUM, "KEEP", drop_prefixes(get_codes(df, MEDIASTINUM, "KEEP"), spec.prefixes))
    return df


def overlay_frame(spec: OverlaySpec) -> pd.DataFrame:
    if not spec.source.exists():
        raise FileNotFoundError(spec.source)
    df = pd.read_csv(spec.source)
    set_codes(df, MEDIASTINUM, "KEEP", add_codes(get_codes(df, MEDIASTINUM, "KEEP"), C39_FAMILY))
    return df


def write_july16_upside(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(ABLATIONS) + len(OVERLAYS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(ABLATIONS) + len(OVERLAYS)}")
    if not BASE_C39.exists():
        raise FileNotFoundError(BASE_C39)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    base = pd.read_csv(BASE_C39)
    all_specs = (*ABLATIONS, *OVERLAYS)
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
        df = ablation_frame(base, spec) if isinstance(spec, AblationSpec) else overlay_frame(spec)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 16 upside candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-16-upside.csv")
    parser.add_argument("--start-version", type=int, default=827)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july16_upside(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
