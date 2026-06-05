"""V58 — v53 + adiciona codes adjacentes (mesmo 3-char root no v53)."""
import pandas as pd
from common import load_data


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def main():
    _, icd = load_data()
    valid = set(icd["icd_code"].astype(str))
    icd_set_by_root = {}
    for code in icd["icd_code"].astype(str):
        root = code[:3]
        icd_set_by_root.setdefault(root, []).append(code)

    v53 = pd.read_csv("submissions/v53_3char_parents.csv")
    out = []
    for _, r in v53.iterrows():
        keep = set(parse(r["KEEP"]))
        # adicionar TODOS os codes do dict que compartilham 3-char root
        # Mas isso pode estourar (muitos codes irrelevantes no mesmo root)
        # Restringir: so se ja temos >=3 codes daquele root no v53
        roots_count = {}
        for c in keep:
            roots_count[c[:3]] = roots_count.get(c[:3], 0) + 1
        confident_roots = {r for r, n in roots_count.items() if n >= 3}
        for root in confident_roots:
            for sibling in icd_set_by_root.get(root, []):
                keep.add(sibling)
        out.append({
            "Condition": r["Condition"],
            "KEEP": "; ".join(sorted(keep)),
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
        print(f"{r['Condition']:42s} K={len(keep):4d}")
    pd.DataFrame(out).to_csv("submissions/v58_v53_siblings.csv", index=False)


if __name__ == "__main__":
    main()
