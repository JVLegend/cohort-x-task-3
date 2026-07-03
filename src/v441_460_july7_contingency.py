"""Generate a July 7 public contingency plan.

The preferred July 7 path should be an adaptive plan from July 6 scores, so
this fallback starts at v441 and leaves v421-v440 available for that primary
path. Candidates focus on public-safe recombinations of near-best COPD anchors,
the small positive mediastinum add, and ASSOC/DIFF sources that were public
neutral or positive.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

try:
    from v281_300_assoc_diff import (
        BASE_PUBLIC,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )
except ModuleNotFoundError:
    from src.v281_300_assoc_diff import (
        BASE_PUBLIC,
        MEDIASTINUM,
        PLANS,
        PUBLIC_ASSOC_DIFF_EMPTY,
        ROOT,
        SUBMISSIONS,
        dataframe_key,
        get_codes,
        set_codes,
    )


TARGET_COUNT = 20
BASE_BEST = SUBMISSIONS / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
COPD_J31_J98 = SUBMISSIONS / "v293_copd_no_j20_j45_j31_j98.csv"
COPD_J81_J82 = SUBMISSIONS / "v294_copd_no_j20_j45_j81_j82.csv"
COPD_J93_J95 = SUBMISSIONS / "v295_copd_no_j20_j45_j93_j95.csv"
MED_POSITIVE = SUBMISSIONS / "v300_med_add_thymus_nodes.csv"
ASSOC_HIGHCONF = SUBMISSIONS / "v283_assocdiff_highconf_assoc.csv"
ASSOC_BROAD = SUBMISSIONS / "v286_assocdiff_broad_assoc.csv"
ASSOC_PULMONARY = SUBMISSIONS / "v287_assocdiff_pulmonary.csv"
ASSOC_CARDIORENAL = SUBMISSIONS / "v288_assocdiff_cardiorenal.csv"


@dataclass(frozen=True)
class ContingencySpec:
    slug: str
    message: str
    notes: str
    base_path: Path
    add_mediastinum_positive: bool = False
    assoc_source: Path | None = None


SPECS = [
    ContingencySpec("copd_j31_j98_med_add_thymus_nodes", "COPD J31/J98 prune plus mediastinum thymus/nodes", "public-only combo of v293 COPD and v300 mediastinum", COPD_J31_J98, add_mediastinum_positive=True),
    ContingencySpec("copd_j81_j82_med_add_thymus_nodes", "COPD J81/J82 prune plus mediastinum thymus/nodes", "public-only combo of v294 COPD and v300 mediastinum", COPD_J81_J82, add_mediastinum_positive=True),
    ContingencySpec("copd_j93_j95_med_add_thymus_nodes", "COPD J93/J95 prune plus mediastinum thymus/nodes", "public-only combo of v295 COPD and v300 mediastinum", COPD_J93_J95, add_mediastinum_positive=True),
    ContingencySpec("copd_j31_j98_highconf_assoc", "COPD J31/J98 plus highconf ASSOC", "near-best COPD with high-confidence ASSOC-only source v283", COPD_J31_J98, assoc_source=ASSOC_HIGHCONF),
    ContingencySpec("copd_j81_j82_highconf_assoc", "COPD J81/J82 plus highconf ASSOC", "near-best COPD with high-confidence ASSOC-only source v283", COPD_J81_J82, assoc_source=ASSOC_HIGHCONF),
    ContingencySpec("copd_j93_j95_highconf_assoc", "COPD J93/J95 plus highconf ASSOC", "near-best COPD with high-confidence ASSOC-only source v283", COPD_J93_J95, assoc_source=ASSOC_HIGHCONF),
    ContingencySpec("copd_j31_j98_broad_assoc", "COPD J31/J98 plus broad ASSOC", "near-best COPD with broad ASSOC-only source v286", COPD_J31_J98, assoc_source=ASSOC_BROAD),
    ContingencySpec("copd_j81_j82_broad_assoc", "COPD J81/J82 plus broad ASSOC", "near-best COPD with broad ASSOC-only source v286", COPD_J81_J82, assoc_source=ASSOC_BROAD),
    ContingencySpec("copd_j93_j95_broad_assoc", "COPD J93/J95 plus broad ASSOC", "near-best COPD with broad ASSOC-only source v286", COPD_J93_J95, assoc_source=ASSOC_BROAD),
    ContingencySpec("copd_j31_j98_pulmonary_assocdiff", "COPD J31/J98 plus pulmonary ASSOC/DIFF", "near-best COPD with public-tied pulmonary ASSOC/DIFF source v287", COPD_J31_J98, assoc_source=ASSOC_PULMONARY),
    ContingencySpec("copd_j81_j82_pulmonary_assocdiff", "COPD J81/J82 plus pulmonary ASSOC/DIFF", "near-best COPD with public-tied pulmonary ASSOC/DIFF source v287", COPD_J81_J82, assoc_source=ASSOC_PULMONARY),
    ContingencySpec("copd_j93_j95_pulmonary_assocdiff", "COPD J93/J95 plus pulmonary ASSOC/DIFF", "near-best COPD with public-tied pulmonary ASSOC/DIFF source v287", COPD_J93_J95, assoc_source=ASSOC_PULMONARY),
    ContingencySpec("copd_j31_j98_cardiorenal_assocdiff", "COPD J31/J98 plus cardiorenal ASSOC/DIFF", "near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288", COPD_J31_J98, assoc_source=ASSOC_CARDIORENAL),
    ContingencySpec("copd_j81_j82_cardiorenal_assocdiff", "COPD J81/J82 plus cardiorenal ASSOC/DIFF", "near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288", COPD_J81_J82, assoc_source=ASSOC_CARDIORENAL),
    ContingencySpec("copd_j93_j95_cardiorenal_assocdiff", "COPD J93/J95 plus cardiorenal ASSOC/DIFF", "near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288", COPD_J93_J95, assoc_source=ASSOC_CARDIORENAL),
    ContingencySpec("copd_j31_j98_med_highconf_assoc", "COPD J31/J98 med plus highconf ASSOC", "public-only COPD+mediastinum combo with high-confidence ASSOC", COPD_J31_J98, add_mediastinum_positive=True, assoc_source=ASSOC_HIGHCONF),
    ContingencySpec("copd_j81_j82_med_highconf_assoc", "COPD J81/J82 med plus highconf ASSOC", "public-only COPD+mediastinum combo with high-confidence ASSOC", COPD_J81_J82, add_mediastinum_positive=True, assoc_source=ASSOC_HIGHCONF),
    ContingencySpec("copd_j93_j95_med_highconf_assoc", "COPD J93/J95 med plus highconf ASSOC", "public-only COPD+mediastinum combo with high-confidence ASSOC", COPD_J93_J95, add_mediastinum_positive=True, assoc_source=ASSOC_HIGHCONF),
    ContingencySpec("copd_j31_j98_med_broad_assoc", "COPD J31/J98 med plus broad ASSOC", "public-only COPD+mediastinum combo with broad ASSOC", COPD_J31_J98, add_mediastinum_positive=True, assoc_source=ASSOC_BROAD),
    ContingencySpec("copd_j81_j82_med_broad_assoc", "COPD J81/J82 med plus broad ASSOC", "public-only COPD+mediastinum combo with broad ASSOC", COPD_J81_J82, add_mediastinum_positive=True, assoc_source=ASSOC_BROAD),
]


def copy_mediastinum_positive(df: pd.DataFrame, med_positive: pd.DataFrame) -> None:
    set_codes(df, MEDIASTINUM, "KEEP", get_codes(med_positive, MEDIASTINUM, "KEEP"))


def copy_assoc_diff(df: pd.DataFrame, source: pd.DataFrame) -> None:
    for condition in source["Condition"]:
        if condition in PUBLIC_ASSOC_DIFF_EMPTY:
            continue
        for bucket in ("ASSOCIATION", "DIFF"):
            set_codes(df, condition, bucket, get_codes(source, condition, bucket))
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])


def candidate_frame(spec: ContingencySpec, med_positive: pd.DataFrame, assoc_frames: dict[Path, pd.DataFrame]) -> pd.DataFrame:
    df = pd.read_csv(spec.base_path)
    if spec.add_mediastinum_positive:
        copy_mediastinum_positive(df, med_positive)
    if spec.assoc_source is not None:
        copy_assoc_diff(df, assoc_frames[spec.assoc_source])
    for condition in PUBLIC_ASSOC_DIFF_EMPTY:
        set_codes(df, condition, "ASSOCIATION", [])
        set_codes(df, condition, "DIFF", [])
    return df


def write_july7_contingency(start_version: int, out_plan: Path, dry_run: bool = False) -> list[Path]:
    if len(SPECS) != TARGET_COUNT:
        raise RuntimeError(f"expected {TARGET_COUNT} specs, found {len(SPECS)}")
    required_paths = {
        BASE_PUBLIC,
        BASE_BEST,
        MED_POSITIVE,
        *(spec.base_path for spec in SPECS),
        *(spec.assoc_source for spec in SPECS if spec.assoc_source is not None),
    }
    for path in required_paths:
        if not path.exists():
            raise FileNotFoundError(path)
    if not out_plan.is_absolute():
        out_plan = ROOT / out_plan

    med_positive = pd.read_csv(MED_POSITIVE)
    assoc_frames = {
        path: pd.read_csv(path)
        for path in sorted({spec.assoc_source for spec in SPECS if spec.assoc_source is not None})
    }
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
        df = candidate_frame(spec, med_positive, assoc_frames)
        key = dataframe_key(df)
        if key in existing_keys or key in seen_keys:
            raise RuntimeError(f"duplicate July 7 contingency candidate: {path.name}")
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
    parser.add_argument("--out-plan", type=Path, default=PLANS / "2026-07-07-public-contingency.csv")
    parser.add_argument("--start-version", type=int, default=441)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_plan = args.out_plan if args.out_plan.is_absolute() else ROOT / args.out_plan
    written = write_july7_contingency(args.start_version, out_plan, dry_run=args.dry_run)
    print(f"wrote_plan={out_plan.relative_to(ROOT)}" if not args.dry_run else f"dry_run_plan={out_plan.relative_to(ROOT)}")
    for path in written:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
