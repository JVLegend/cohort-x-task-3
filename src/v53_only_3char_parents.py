"""V53 — v33 + so parents de 3-char (categoria raiz)."""
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
        expanded = set(keep)
        for code in keep:
            if len(code) > 3:
                root = code[:3]
                if root in valid:
                    expanded.add(root)
        out.append({
            "Condition": r["Condition"],
            "KEEP": "; ".join(sorted(expanded)),
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
    pd.DataFrame(out).to_csv("submissions/v53_3char_parents.csv", index=False)


if __name__ == "__main__":
    main()
