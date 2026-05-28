"""V13 — UNIAO de prefixos clinicos (v11) + keyword matching (v8_long).
Hipotese: cobertura combinada captura codigos que sozinhos cada metodo perde.
Mantem filtro terminal 5+ char.
"""
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import SYN, DIFF_KW, find_by_keywords


def term_filter(icd, idxs):
    return [i for i in idxs if len(str(icd.iloc[i]["icd_code"])) >= 5]


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, assoc_p, diff_p = RULES.get(cond, ([cond.lower()], [], []))
        keep_kws = SYN.get(cond, [cond])
        diff_kws = DIFF_KW.get(cond, [])

        # KEEP: uniao prefixos + keyword matches, terminais
        keep_prefix = term_filter(icd, codes_matching(icd, keep_p))
        keep_kw = term_filter(icd, find_by_keywords(icd, keep_kws))
        keep_set = set(keep_prefix) | set(keep_kw)
        keep_idx = sorted(keep_set)
        if not keep_idx:
            keep_idx = codes_matching(icd, keep_p)[:3] or [0]
        keep_set = set(keep_idx)
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_idx}

        # ASSOC: prefixos ASSOC + todos terminais do mesmo chapter dos KEEP
        assoc_prefix = term_filter(icd, codes_matching(icd, assoc_p))
        assoc_chapter = term_filter(icd,
            icd[icd["chapter3"].isin(keep_chs) & ~icd.index.isin(keep_set)].index.tolist())
        assoc_set = (set(assoc_prefix) | set(assoc_chapter)) - keep_set
        assoc_idx = sorted(assoc_set)

        # DIFF: uniao prefixos DIFF + keyword DIFF (fora chapter KEEP), terminais
        diff_prefix = [i for i in term_filter(icd, codes_matching(icd, diff_p))
                       if i not in keep_set and i not in assoc_set]
        diff_kw_idx = [i for i in term_filter(icd, find_by_keywords(icd, diff_kws))
                       if icd.iloc[i]["chapter3"] not in keep_chs
                       and i not in keep_set and i not in assoc_set]
        diff_set = set(diff_prefix) | set(diff_kw_idx)
        diff_idx = sorted(diff_set)

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))
        print(f"{cond:42s} K={len(keep_idx):4d} A={len(assoc_idx):4d} D={len(diff_idx):3d}")

    write_submission(rows, "submissions/v13_union.csv")


if __name__ == "__main__":
    main()
