"""V29 — Sweep fino em torno do pico (0.91). Testa th=0.88, 0.89, 0.90."""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

CACHE = Path("data/icd_embeddings.npy")
MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
THS = [0.88, 0.89, 0.895]


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    seeds = []
    queries = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        kws = SYN_EXP.get(cond, [cond])
        seeds.append(set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws)))
        queries.append(cond + " " + " ".join(kws))
    sims_all = model.encode(queries, normalize_embeddings=True) @ icd_emb.T

    for th in THS:
        rows = []
        for ci, cond in enumerate(cond_df["Condition"]):
            keep_set = set(seeds[ci]) | set(int(i) for i in np.where(sims_all[ci] >= th)[0])
            keep_idx = sorted(keep_set) or [0]
            rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        write_submission(rows, f"submissions/v29_th{int(th*1000)}.csv")


if __name__ == "__main__":
    main()
