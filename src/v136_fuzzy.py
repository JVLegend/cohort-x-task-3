"""V136 — v93 + rapidfuzz hybrid: adiciona codes com fuzzy match alto a query.
Insight do NBME comp: string matching + BERT combinados batem cada um sozinho.
"""
import pandas as pd
from rapidfuzz import fuzz
from common import load_data
from v21_keep_expanded import SYN_EXP


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def normalize_title(t):
    """Expande abreviacoes comuns ICD."""
    t = str(t).lower()
    repl = [
        (" w/", " with "),
        (" w/o ", " without "),
        (" nos", " not otherwise specified"),
        (" unspec.", " unspecified"),
        (" unsp ", " unspecified "),
        (" due to ", " "),
        ("(", " "),
        (")", " "),
        ("-", " "),
    ]
    for a, b in repl:
        t = t.replace(a, b)
    return " ".join(t.split())


def main():
    cond_df, icd = load_data()
    v93 = pd.read_csv("submissions/v93_t4.csv")
    code_to_title = dict(zip(icd["icd_code"].astype(str),
                              icd["long_title"].fillna("").astype(str)))

    rows = []
    for _, r in v93.iterrows():
        cond = r["Condition"]
        keep = set(parse(r["KEEP"]))
        # query expandida com sinonimos
        kws = SYN_EXP.get(cond, [cond])
        query = normalize_title(cond + " " + " ".join(kws))

        # adiciona codes com fuzzy partial_ratio >= 85
        added = 0
        for code in icd["icd_code"].astype(str):
            if code in keep:
                continue
            title = normalize_title(code_to_title.get(code, ""))
            if not title:
                continue
            # token_set_ratio capta titulos com palavras-chave embaralhadas
            score = fuzz.token_set_ratio(query, title)
            if score >= 85:
                keep.add(code)
                added += 1
                if added >= 30:  # cap fuzzy additions per condition
                    break
        rows.append({
            "Condition": cond,
            "KEEP": "; ".join(sorted(keep)),
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
        print(f"{cond:42s} +{added:3d} fuzzy -> total {len(keep)}")

    pd.DataFrame(rows).to_csv("submissions/v136_fuzzy.csv", index=False)


if __name__ == "__main__":
    main()
