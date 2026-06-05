"""V52 — v33 + para cada codigo KEEP, adiciona parent codes (1-3 chars).
Hipotese: gold pode incluir codigos pai (categorias) alem dos filhos especificos.
"""
import pandas as pd
from common import load_data


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def main():
    _, icd = load_data()
    valid_codes = set(icd["icd_code"].astype(str))
    v33 = pd.read_csv("submissions/v33_obscure.csv")
    out = []
    for _, r in v33.iterrows():
        keep = set(parse(r["KEEP"]))
        expanded = set(keep)
        # Add parent prefixes that exist in dict
        for code in keep:
            for n in (3, 4, 5, 6):
                if len(code) > n:
                    parent = code[:n]
                    if parent in valid_codes:
                        expanded.add(parent)
        out.append({
            "Condition": r["Condition"],
            "KEEP": "; ".join(sorted(expanded)),
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
        print(f"{r['Condition']:42s} v33={len(keep):4d} +parents={len(expanded):4d}")
    pd.DataFrame(out).to_csv("submissions/v52_v33_plus_parents.csv", index=False)


if __name__ == "__main__":
    main()
