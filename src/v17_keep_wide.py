"""V17 — KEEP MAXIMO (prefixos clinicos sem filtro de tamanho). ASSOC/DIFF vazios."""
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_idx = codes_matching(icd, keep_p)  # sem term_filter
        if not keep_idx:
            keep_idx = [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, "submissions/v17_keep_wide.csv")


if __name__ == "__main__":
    main()
