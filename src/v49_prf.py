"""V49 — Pseudo-Relevance Feedback (PRF):
- Round 1: query original -> top-5 BioBERT hits
- Round 2: expand query com titles dos top-5 -> nova similaridade
- KEEP = uniao v33 + codigos novos descobertos pelo PRF (sim >= 0.91)
"""
import numpy as np
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

CACHE = Path("data/icd_embeddings.npy")
TH = 0.91
PRF_K = 5


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer("pritamdeka/S-PubMedBert-MS-MARCO")

    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        kws = SYN_EXP.get(cond, [cond])

        # Round 1: original query
        q1 = cond + " " + " ".join(kws)
        q1_emb = model.encode([q1], normalize_embeddings=True)[0]
        sims1 = icd_emb @ q1_emb
        top5_idx = np.argsort(-sims1)[:PRF_K]
        top5_titles = [icd.iloc[i]["long_title"] for i in top5_idx]

        # Round 2: expanded query = original + top-5 titles
        q2 = q1 + " " + " ".join(top5_titles)
        q2_emb = model.encode([q2], normalize_embeddings=True)[0]
        sims2 = icd_emb @ q2_emb

        # Union: prefixos + keyword + sims1>=TH + sims2>=TH
        seed = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws))
        seed |= set(int(i) for i in np.where(sims1 >= TH)[0])
        seed |= set(int(i) for i in np.where(sims2 >= TH)[0])

        keep_idx = sorted(seed) or [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, "submissions/v49_prf.csv")


if __name__ == "__main__":
    main()
