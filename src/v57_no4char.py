"""V57 — v33 + 3-char parents, MAS remove codes 4-char (hipotese: 4-char hurts)."""
import pandas as pd
from common import load_data


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def main():
    _, icd = load_data()
    valid = set(icd["icd_code"].astype(str))
    v33 = pd.read_csv("submissions/v33_obscure.csv")
    out = []
    for _, r in v33.iterrows():
        keep = set(parse(r["KEEP"]))
        # remove 4-char codes
        keep = {c for c in keep if len(c) != 4}
        # add 3-char parents
        for code in list(keep):
            if len(code) > 3:
                p = code[:3]
                if p in valid:
                    keep.add(p)
        out.append({
            "Condition": r["Condition"],
            "KEEP": "; ".join(sorted(keep)),
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
    pd.DataFrame(out).to_csv("submissions/v57_no4char.csv", index=False)


if __name__ == "__main__":
    main()
