"""V11 — Prefixos clinicos (v10) FILTRADOS para terminais 5+ char (insight v8_long)."""
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, assoc_p, diff_p = RULES.get(cond, ([cond.lower()], [], []))

        def term_filter(idxs):
            return [i for i in idxs if len(str(icd.iloc[i]["icd_code"])) >= 5]

        keep_idx = term_filter(codes_matching(icd, keep_p))
        if not keep_idx:
            keep_idx = codes_matching(icd, keep_p)[:3]
        keep_set = set(keep_idx)
        assoc_idx = [i for i in term_filter(codes_matching(icd, assoc_p)) if i not in keep_set]
        assoc_set = set(assoc_idx)
        diff_idx = [i for i in term_filter(codes_matching(icd, diff_p))
                    if i not in keep_set and i not in assoc_set]
        if not keep_idx:
            keep_idx = [0]
        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))
        print(f"{cond:42s} K={len(keep_idx):3d} A={len(assoc_idx):4d} D={len(diff_idx):3d}")

    write_submission(rows, "submissions/v11_combo.csv")


if __name__ == "__main__":
    main()
