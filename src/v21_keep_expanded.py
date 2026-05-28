"""V21 — v18 + sinonimos clinicos expandidos para maximizar recall KEEP."""
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords

# Sinonimos clinicos expandidos (substitui SYN de v4)
SYN_EXP = {
    "Epistaxis": ["epistaxis", "nose bleed", "nosebleed", "nasal hemorrhage"],
    "Intracranial Pressure": ["intracranial hypertension", "intracranial pressure",
                              "benign intracranial", "raised intracranial", "cerebral edema"],
    "Chronic Obstructive Pulmonary Disease": ["chronic obstructive pulmonary",
                                               "emphysema", "chronic bronchitis"],
    "Enlarged Mediastinum": ["mediastinum", "mediastinal mass", "mediastinitis"],
    "Gout": ["gout", "gouty", "tophus", "tophi"],
    "Latent Adrenal Insufficiency": ["adrenocortical insufficiency", "adrenal insufficiency",
                                     "addison", "hypoadrenalism", "hypoaldosteronism"],
    "Dermatomycosis": ["dermatomycosis", "dermatophytosis", "tinea", "ringworm",
                       "mycosis of skin", "fungal skin"],
    "Pleurisy": ["pleurisy", "pleural effusion", "pleurodynia", "pleuritis"],
    "Bronchitis": ["bronchitis", "tracheobronchitis"],
    "Thyroiditis": ["thyroiditis", "hashimoto", "de quervain"],
    "Nasopharyngeal Carcinoma": ["nasopharynx", "nasopharyngeal"],
    "CKD": ["chronic kidney disease", "chronic renal failure", "chronic renal insufficiency"],
    "Hypothyroidism": ["hypothyroidism", "myxedema", "hypothyroid"],
    "Hematemesis": ["hematemesis", "vomiting blood", "vomiting of blood"],
    "Heart Failure": ["heart failure", "cardiac failure", "congestive heart"],
    "Hypergonadism": ["hyperfunction of ovary", "testicular hyperfunction", "hypergonadism"],
    "UTI": ["urinary tract infection", "site not specified urinary"],
    "Diabetes": ["diabetes mellitus", "diabetic"],
    "Interstitial Lung Disease": ["interstitial pulmonary", "interstitial lung",
                                   "pulmonary fibrosis", "interstitial pneumon"],
    "Hypoparathyroidism": ["hypoparathyroidism", "hypoparathyroid"],
    "Hyperparathyroidism": ["hyperparathyroidism", "hyperparathyroid"],
    "Hyperthyroidism": ["thyrotoxicosis", "hyperthyroidism", "graves"],
    "Pneumonia": ["pneumonia", "bronchopneumonia"],
}


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_kws = SYN_EXP.get(cond, [cond])
        keep_set = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, keep_kws))
        keep_idx = sorted(keep_set)
        if not keep_idx:
            keep_idx = [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, "submissions/v21_keep_expanded.csv")


if __name__ == "__main__":
    main()
