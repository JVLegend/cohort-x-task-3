"""V5 — Hipotese: gold tem buckets GRANDES (toda familia ICD).
- KEEP = TODOS codigos com keyword/sinonimo da condicao no titulo (sem limite).
- ASSOC = TODOS codigos no mesmo capitulo (3 chars) que KEEP, fora do KEEP.
- DIFF = TODOS codigos com keyword diff fora dos capitulos KEEP.
"""
from common import load_data, write_submission, normalize
from v4_quickwin import SYN, DIFF_KW, find_by_keywords


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_kws = SYN.get(cond, [cond])
        diff_kws = DIFF_KW.get(cond, [])

        keep_idx = find_by_keywords(icd, keep_kws)
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_idx}

        # ASSOC: todos no mesmo capitulo, fora do KEEP
        keep_set = set(keep_idx)
        assoc_idx = icd[icd["chapter3"].isin(keep_chs) & ~icd.index.isin(keep_set)].index.tolist()

        # DIFF: keyword diff fora dos capitulos KEEP
        diff_hits = find_by_keywords(icd, diff_kws)
        diff_idx = [i for i in diff_hits
                    if icd.iloc[i]["chapter3"] not in keep_chs and i not in keep_set]

        if not keep_idx:
            keep_idx = [0]

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))

    write_submission(rows, "submissions/v5_coverage.csv")


if __name__ == "__main__":
    main()
