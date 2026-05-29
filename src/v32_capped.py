"""V32 — v25 th=0.91 com CAP por condition (top-K por similaridade BioBERT)."""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP
import sys

CACHE = Path("data/icd_embeddings.npy")
TH = 0.91


def main(cap):
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer("pritamdeka/S-PubMedBert-MS-MARCO")
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        kws = SYN_EXP.get(cond, [cond])
        seed = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws))
        q_text = cond + " " + " ".join(kws)
        sims = (model.encode([q_text], normalize_embeddings=True) @ icd_emb.T)[0]
        seed |= set(int(i) for i in np.where(sims >= TH)[0])
        # CAP: top-cap por sim
        if len(seed) > cap:
            seed_sorted = sorted(seed, key=lambda i: -sims[i])
            seed = set(seed_sorted[:cap])
        keep_idx = sorted(seed) or [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, f"submissions/v32_cap{cap}.csv")


if __name__ == "__main__":
    main(int(sys.argv[1]))
