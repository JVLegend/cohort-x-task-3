"""Generate July 1 daily probe submissions.

These are intentionally small, high-information probes around v178_FINAL:
- v186-v194 zero one public/mid condition at a time.
- v195-v200 add the v184 keyword-union extras one condition at a time.
"""
from pathlib import Path

import pandas as pd


OUT = Path("submissions")
BASE = OUT / "v178_FINAL.csv"
UNION = OUT / "v184_union_kw.csv"


ZERO_PROBES = [
    (186, "zero_copd", "Chronic Obstructive Pulmonary Disease"),
    (187, "zero_hf", "Heart Failure"),
    (188, "zero_hyperthyroid", "Hyperthyroidism"),
    (189, "zero_ild", "Interstitial Lung Disease"),
    (190, "zero_derm", "Dermatomycosis"),
    (191, "zero_bronchitis", "Bronchitis"),
    (192, "zero_npc", "Nasopharyngeal Carcinoma"),
    (193, "zero_hypothyroid", "Hypothyroidism"),
    (194, "zero_mediastinum", "Enlarged Mediastinum"),
]

ADD_PROBES = [
    (195, "add_copd_kw", "Chronic Obstructive Pulmonary Disease"),
    (196, "add_hf_kw", "Heart Failure"),
    (197, "add_ild_kw", "Interstitial Lung Disease"),
    (198, "add_derm_kw", "Dermatomycosis"),
    (199, "add_mediastinum_kw", "Enlarged Mediastinum"),
    (200, "add_npc_kw", "Nasopharyngeal Carcinoma"),
]


def write(df: pd.DataFrame, version: int, slug: str) -> Path:
    path = OUT / f"v{version}_{slug}.csv"
    df.to_csv(path, index=False)
    return path


def main() -> None:
    base = pd.read_csv(BASE)
    union = pd.read_csv(UNION)

    for version, slug, condition in ZERO_PROBES:
        df = base.copy()
        mask = df["Condition"].eq(condition)
        df.loc[mask, ["KEEP", "ASSOCIATION", "DIFF"]] = "Not Applicable"
        path = write(df, version, slug)
        print(f"{path}: zeroed {condition}")

    for version, slug, condition in ADD_PROBES:
        df = base.copy()
        mask = df["Condition"].eq(condition)
        df.loc[mask, "KEEP"] = union.loc[union["Condition"].eq(condition), "KEEP"].iloc[0]
        path = write(df, version, slug)
        base_keep = base.loc[mask, "KEEP"].iloc[0]
        new_keep = df.loc[mask, "KEEP"].iloc[0]
        added = len(set(new_keep.split("; ")) - set(base_keep.split("; ")))
        print(f"{path}: added {added} keyword-union codes for {condition}")


if __name__ == "__main__":
    main()
