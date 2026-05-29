"""V30 — Multi-query embedding: para cada condition, encoda 3-5 variantes da query
e usa o MAXIMO da similaridade. Captura formas alternativas que single-query perde.
"""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

CACHE = Path("data/icd_embeddings.npy")
MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
TH = 0.91

# Multi-formulacoes da query medica
MULTI_Q = {
    "Diabetes": ["diabetes mellitus", "type 1 diabetes", "type 2 diabetes",
                 "diabetic", "diabetes with complication"],
    "CKD": ["chronic kidney disease", "chronic renal failure",
            "chronic kidney failure", "end stage renal"],
    "Heart Failure": ["heart failure", "congestive heart failure",
                      "systolic heart failure", "diastolic heart failure"],
    "Pneumonia": ["pneumonia", "bacterial pneumonia", "viral pneumonia",
                  "aspiration pneumonia", "bronchopneumonia"],
    "Hypothyroidism": ["hypothyroidism", "primary hypothyroidism", "myxedema",
                       "iatrogenic hypothyroidism"],
    "Hyperthyroidism": ["hyperthyroidism", "thyrotoxicosis", "graves disease",
                        "toxic goiter"],
    "UTI": ["urinary tract infection", "cystitis", "pyelonephritis"],
    "Chronic Obstructive Pulmonary Disease": ["chronic obstructive pulmonary disease",
                                               "copd exacerbation", "emphysema",
                                               "chronic bronchitis"],
}


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        kws = SYN_EXP.get(cond, [cond])
        seed = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws))

        # Multi-query encoding
        queries = MULTI_Q.get(cond, [cond + " " + " ".join(kws)])
        q_embs = model.encode(queries, normalize_embeddings=True)
        # Max sim across queries
        max_sims = (q_embs @ icd_emb.T).max(axis=0)
        seed |= set(int(i) for i in np.where(max_sims >= TH)[0])

        keep_idx = sorted(seed) or [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, "submissions/v30_multi_query.csv")


if __name__ == "__main__":
    main()
