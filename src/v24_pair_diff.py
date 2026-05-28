"""V24 — v23 KEEP + DIFF minimo somente em pares clinicos obvios (hipo/hiper)."""
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

# Pares clinicos diferenciais (codigos do "oposto")
DIFF_PAIRS = {
    "Hyperthyroidism": ["E03"],
    "Hypothyroidism": ["E05"],
    "Hyperparathyroidism": ["E20"],
    "Hypoparathyroidism": ["E21"],
}


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_kws = SYN_EXP.get(cond, [cond])
        keep_set = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, keep_kws))
        q_text = cond + " " + " ".join(keep_kws)
        q_emb = model.encode([q_text], normalize_embeddings=True)
        sims = (icd_emb @ q_emb[0])
        keep_set |= set(int(i) for i in np.where(sims >= SIM_THRESHOLD)[0].tolist())
        keep_idx = sorted(keep_set)
        if not keep_idx:
            keep_idx = [0]

        diff_idx = []
        if cond in DIFF_PAIRS:
            diff_idx = [i for i in codes_matching(icd, DIFF_PAIRS[cond])
                        if i not in keep_set]

        rows.append((cond,
                     icd.iloc[keep_idx]["icd_code"].tolist(),
                     [],
                     icd.iloc[diff_idx]["icd_code"].tolist() if diff_idx else []))
    write_submission(rows, "submissions/v24_pair_diff.csv")


if __name__ == "__main__":
    main()
