"""Generate next daily probes for the confirmed public movers.

Targets from 2026-07-01 probes:
- COPD affects the public score.
- Enlarged Mediastinum affects the public score.

The variants below make one interpretable family-level change at a time.
"""
from pathlib import Path

import pandas as pd


OUT = Path("submissions")
BASE = OUT / "v178_FINAL.csv"
ICD = Path("data/icd_dict.csv")

COPD = "Chronic Obstructive Pulmonary Disease"
MEDIASTINUM = "Enlarged Mediastinum"


def parse_codes(value: str) -> list[str]:
    if pd.isna(value) or value == "Not Applicable":
        return []
    return [code.strip() for code in str(value).split(";") if code.strip()]


def fmt(codes: list[str]) -> str:
    return "; ".join(codes) if codes else "Not Applicable"


def get_codes(df: pd.DataFrame, condition: str) -> list[str]:
    return parse_codes(df.loc[df["Condition"].eq(condition), "KEEP"].iloc[0])


def set_codes(df: pd.DataFrame, condition: str, codes: list[str]) -> None:
    df.loc[df["Condition"].eq(condition), "KEEP"] = fmt(codes)


def drop_prefixes(codes: list[str], prefixes: tuple[str, ...]) -> list[str]:
    return [code for code in codes if not code.startswith(prefixes)]


def add_codes(codes: list[str], additions: list[str]) -> list[str]:
    seen = set(codes)
    out = list(codes)
    for code in additions:
        if code not in seen:
            out.append(code)
            seen.add(code)
    return out


def title_contains(icd: pd.DataFrame, codes: list[str], term: str) -> list[str]:
    titles = icd.set_index("icd_code")["long_title"].fillna("").to_dict()
    return [code for code in codes if term.lower() in titles.get(code, "").lower()]


def write(df: pd.DataFrame, version: int, slug: str) -> None:
    path = OUT / f"v{version}_{slug}.csv"
    df.to_csv(path, index=False)
    print(path)


def main() -> None:
    base = pd.read_csv(BASE)
    icd = pd.read_csv(ICD)
    copd_codes = get_codes(base, COPD)
    med_codes = get_codes(base, MEDIASTINUM)

    variants = [
        (201, "copd_no_j20", COPD, drop_prefixes(copd_codes, ("J20",))),
        (202, "copd_no_j31", COPD, drop_prefixes(copd_codes, ("J31",))),
        (203, "copd_no_j45", COPD, drop_prefixes(copd_codes, ("J45",))),
        (204, "copd_no_j81_j82", COPD, drop_prefixes(copd_codes, ("J81", "J82"))),
        (205, "copd_no_j93_j95", COPD, drop_prefixes(copd_codes, ("J93", "J95"))),
        (206, "copd_no_j96", COPD, drop_prefixes(copd_codes, ("J96",))),
        (207, "copd_no_j98", COPD, drop_prefixes(copd_codes, ("J98",))),
        (208, "copd_core_j41_j42_j43_j44", COPD, [c for c in copd_codes if c.startswith(("J41", "J42", "J43", "J44"))]),
        (209, "copd_no_acute_bronch_asthma", COPD, drop_prefixes(copd_codes, ("J20", "J45"))),
        (210, "copd_add_p25_only", COPD, add_codes(copd_codes, ["P25", "P250", "P258"])),
        (211, "copd_add_t79_t81_only", COPD, add_codes(copd_codes, ["T797", "T797XXA", "T797XXD", "T797XXS", "T8182", "T8182XA", "T8182XD", "T8182XS"])),
        (212, "med_no_j98", MEDIASTINUM, drop_prefixes(med_codes, ("J98",))),
        (213, "med_no_q34", MEDIASTINUM, drop_prefixes(med_codes, ("Q34",))),
        (214, "med_no_d15", MEDIASTINUM, drop_prefixes(med_codes, ("D15",))),
        (215, "med_no_c38", MEDIASTINUM, drop_prefixes(med_codes, ("C38",))),
        (216, "med_only_mediastin_title", MEDIASTINUM, title_contains(icd, med_codes, "mediastin")),
        (217, "med_keep_neoplasm_only", MEDIASTINUM, [c for c in med_codes if c.startswith(("C38", "C78", "D15", "D38"))]),
        (218, "med_add_c852_only", MEDIASTINUM, add_codes(med_codes, ["C852", "C8520", "C8521", "C8522", "C8523", "C8524", "C8525", "C8526", "C8527", "C8528", "C8529"])),
        (219, "med_add_n80b5_only", MEDIASTINUM, add_codes(med_codes, ["N80B5"])),
        (220, "med_add_p252_only", MEDIASTINUM, add_codes(med_codes, ["P252"])),
    ]

    for version, slug, condition, codes in variants:
        df = base.copy()
        set_codes(df, condition, codes)
        write(df, version, slug)


if __name__ == "__main__":
    main()
