"""V18 — KEEP MAXIMO ABSOLUTO: prefixos clinicos + keyword matching. ASSOC/DIFF vazios."""
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import SYN, find_by_keywords


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_kws = SYN.get(cond, [cond])
        # UNIAO de prefix + keyword
        prefix_idx = codes_matching(icd, keep_p)
        kw_idx = find_by_keywords(icd, keep_kws)
        keep_set = set(prefix_idx) | set(kw_idx)
        keep_idx = sorted(keep_set)
        if not keep_idx:
            keep_idx = [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, "submissions/v18_keep_max.csv")


if __name__ == "__main__":
    main()
