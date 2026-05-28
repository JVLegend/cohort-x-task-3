"""V22 — v21 KEEP + BioBERT top-N por similaridade alta (>= 0.85)."""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
CACHE = Path("data/icd_embeddings.npy")
SIM_THRESHOLD = 0.93


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_kws = SYN_EXP.get(cond, [cond])

        # prefix + keyword
        keep_set = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, keep_kws))

        # + BioBERT high-similarity (threshold absoluto)
        q_text = cond + " " + " ".join(keep_kws)
        q_emb = model.encode([q_text], normalize_embeddings=True)
        sims = (icd_emb @ q_emb[0])
        high_sim_idx = np.where(sims >= SIM_THRESHOLD)[0].tolist()
        keep_set |= set(int(i) for i in high_sim_idx)

        keep_idx = sorted(keep_set)
        if not keep_idx:
            keep_idx = [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, "submissions/v23_keep_strict.csv")


if __name__ == "__main__":
    main()
