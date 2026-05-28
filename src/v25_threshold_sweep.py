"""V25 — Sweep BioBERT threshold para achar sweet spot exato.
Gera 4 submissions: th=0.90, 0.91, 0.92, 0.94.
Submeter em ordem amanha.
"""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
CACHE = Path("data/icd_embeddings.npy")
THRESHOLDS = [0.90, 0.91, 0.92, 0.94]


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    # Cache query embeddings (1x)
    queries = []
    keep_prefix_kw = []  # (set of indices per condition)
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_kws = SYN_EXP.get(cond, [cond])
        queries.append(cond + " " + " ".join(keep_kws))
        keep_prefix_kw.append(set(codes_matching(icd, keep_p)) |
                              set(find_by_keywords(icd, keep_kws)))
    q_embs = model.encode(queries, normalize_embeddings=True)
    sims_all = q_embs @ icd_emb.T  # (23, 97441)

    for th in THRESHOLDS:
        rows = []
        for ci, cond in enumerate(cond_df["Condition"]):
            keep_set = set(keep_prefix_kw[ci])
            keep_set |= set(int(i) for i in np.where(sims_all[ci] >= th)[0])
            keep_idx = sorted(keep_set) or [0]
            rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        path = f"submissions/v25_sweep_th{int(th*100)}.csv"
        write_submission(rows, path)


if __name__ == "__main__":
    main()
