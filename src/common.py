"""Shared helpers for CohortX Task 3 submissions."""
import re
import pandas as pd

ABBREV = {
    "COPD": "chronic obstructive pulmonary disease",
    "CKD": "chronic kidney disease",
    "UTI": "urinary tract infection",
    "ILD": "interstitial lung disease",
    "ICP": "intracranial pressure",
    "HF": "heart failure",
    "NPC": "nasopharyngeal carcinoma",
}


def expand_condition(name: str) -> str:
    key = name.strip().upper()
    if key in ABBREV:
        return f"{name} {ABBREV[key]}"
    return name


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", str(text).lower())


def load_data(data_dir: str = "data"):
    cond = pd.read_csv(f"{data_dir}/task_3.csv")
    icd = pd.read_csv(f"{data_dir}/icd_dict.csv")
    icd["long_title"] = icd["long_title"].fillna("")
    icd["norm_title"] = icd["long_title"].map(normalize)
    icd["chapter3"] = icd["icd_code"].str[:3]
    return cond, icd


def write_submission(rows, path: str):
    """rows: list of (condition, keep_list, assoc_list, diff_list)."""
    out = []
    for cond, keep, assoc, diff in rows:
        out.append({
            "Condition": cond,
            "KEEP": "; ".join(keep) if keep else "Not Applicable",
            "ASSOCIATION": "; ".join(assoc) if assoc else "Not Applicable",
            "DIFF": "; ".join(diff) if diff else "Not Applicable",
        })
    pd.DataFrame(out).to_csv(path, index=False)
    print(f"Wrote {path} ({len(out)} rows)")
