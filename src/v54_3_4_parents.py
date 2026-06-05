"""V54 — v33 + parents 3 e 4 chars (mais granular que v53)."""
import pandas as pd
from common import load_data


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def main(out_path, parent_lengths):
    _, icd = load_data()
    valid = set(icd["icd_code"].astype(str))
    v33 = pd.read_csv("submissions/v33_obscure.csv")
    out = []
    for _, r in v33.iterrows():
        keep = set(parse(r["KEEP"]))
        expanded = set(keep)
        for code in keep:
            for n in parent_lengths:
                if len(code) > n:
                    p = code[:n]
                    if p in valid:
                        expanded.add(p)
        out.append({
            "Condition": r["Condition"],
            "KEEP": "; ".join(sorted(expanded)),
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
    pd.DataFrame(out).to_csv(out_path, index=False)


if __name__ == "__main__":
    main("submissions/v54_34parents.csv", (3, 4))
