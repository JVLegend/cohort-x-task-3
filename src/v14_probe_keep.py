"""V14 — PROBE: so KEEP preenchido (ASSOC e DIFF vazios).
Isola contribuicao do KEEP no macro F1 e diz onde estamos perdendo.
"""
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching


def term_filter(icd, idxs):
    return [i for i in idxs if len(str(icd.iloc[i]["icd_code"])) >= 5]


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_idx = term_filter(icd, codes_matching(icd, keep_p))
        if not keep_idx:
            keep_idx = codes_matching(icd, keep_p)[:3] or [0]
        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            [],  # ASSOC vazio
            [],  # DIFF vazio
        ))
    write_submission(rows, "submissions/v14_probe_keep.csv")


if __name__ == "__main__":
    main()
