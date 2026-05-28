"""V20 — v18 (KEEP max) + ASSOC seletivo APENAS em conditions de alta confianca de ter ASSOC no gold."""
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import SYN, find_by_keywords

# Conditions onde gold ASSOC provavelmente NAO e vazio
# (doencas cronicas com complicacoes/comorbidades padrao)
ASSOC_OVERRIDES = {
    "Chronic Obstructive Pulmonary Disease": ["J41", "J42", "J43", "J47"],
    "CKD": ["I12", "I13", "Z992", "Z9115", "N083"],
    "Diabetes": ["E08", "E09", "Z794", "R73"],
    "Heart Failure": ["I40", "I41", "I42", "I43", "I255"],
    "Pneumonia": ["J20", "J21", "J22", "J690", "J85"],
    "Hypothyroidism": ["E02", "E890"],
    "Hyperthyroidism": ["E04", "E06"],
}


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_kws = SYN.get(cond, [cond])
        keep_set = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, keep_kws))
        keep_idx = sorted(keep_set)
        if not keep_idx:
            keep_idx = [0]

        assoc_p = ASSOC_OVERRIDES.get(cond)
        if assoc_p:
            assoc_set = set(codes_matching(icd, assoc_p)) - keep_set
            assoc_idx = sorted(assoc_set)
        else:
            assoc_idx = []

        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(),
                    icd.iloc[assoc_idx]["icd_code"].tolist() if assoc_idx else [],
                    []))
        print(f"{cond:42s} K={len(keep_idx):4d} A={len(assoc_idx):3d}")
    write_submission(rows, "submissions/v20_selective_assoc.csv")


if __name__ == "__main__":
    main()
