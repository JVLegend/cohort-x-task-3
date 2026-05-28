"""V8 — Teste de granularidade ICD.
Variantes:
  --short : SO codigos de 3 chars (raizes/categorias)
  --long  : SO codigos de 5+ chars (terminais especificos)
Base: estrategia v5 (campea ate aqui).
"""
import sys
from common import load_data, write_submission
from v4_quickwin import SYN, DIFF_KW, find_by_keywords


def main(mode: str):
    cond_df, icd = load_data()

    def keep_only(idxs):
        out = []
        for i in idxs:
            code = str(icd.iloc[i]["icd_code"])
            if mode == "short" and len(code) == 3:
                out.append(i)
            elif mode == "long" and len(code) >= 5:
                out.append(i)
        return out

    rows = []
    for cond in cond_df["Condition"]:
        keep_kws = SYN.get(cond, [cond])
        diff_kws = DIFF_KW.get(cond, [])

        keep_idx = keep_only(find_by_keywords(icd, keep_kws))
        if not keep_idx:
            # fallback: pega qualquer keyword match
            tmp = find_by_keywords(icd, keep_kws)
            keep_idx = tmp[:5] if tmp else [0]
        keep_set = set(keep_idx)
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_idx}

        assoc_idx = icd[icd["chapter3"].isin(keep_chs) & ~icd.index.isin(keep_set)].index.tolist()
        assoc_idx = keep_only(assoc_idx) or assoc_idx[:20]

        diff_hits = find_by_keywords(icd, diff_kws)
        diff_idx = keep_only([i for i in diff_hits
                              if icd.iloc[i]["chapter3"] not in keep_chs and i not in keep_set])

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))
        print(f"{cond:42s} K={len(keep_idx):3d} A={len(assoc_idx):4d} D={len(diff_idx):3d}")

    write_submission(rows, f"submissions/v8_{mode}.csv")


if __name__ == "__main__":
    main(sys.argv[1])
