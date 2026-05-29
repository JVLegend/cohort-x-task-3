"""V31 — Ensemble BioBERT + mpnet. Mean dos embeddings, mesmo threshold."""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

CACHE_BIO = Path("data/icd_embeddings.npy")
CACHE_MPNET = Path("data/icd_embeddings_mpnet.npy")
BIO = "pritamdeka/S-PubMedBert-MS-MARCO"
MPNET = "sentence-transformers/all-mpnet-base-v2"
TH = 0.91


def main():
    cond_df, icd = load_data()
    titles = icd["long_title"].fillna("").tolist()

    icd_bio = np.load(CACHE_BIO)

    if CACHE_MPNET.exists():
        icd_mpnet = np.load(CACHE_MPNET)
    else:
        print("Encoding ICD with mpnet (~3min)...")
        m_mpnet = SentenceTransformer(MPNET)
        icd_mpnet = m_mpnet.encode(titles, batch_size=64, show_progress_bar=True,
                                    convert_to_numpy=True, normalize_embeddings=True)
        np.save(CACHE_MPNET, icd_mpnet)

    icd_ensemble = (icd_bio + icd_mpnet) / 2.0
    # renormalize
    norms = np.linalg.norm(icd_ensemble, axis=1, keepdims=True)
    icd_ensemble = icd_ensemble / (norms + 1e-9)

    m_bio = SentenceTransformer(BIO)
    m_mpnet = SentenceTransformer(MPNET)

    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        kws = SYN_EXP.get(cond, [cond])
        seed = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws))

        q_text = cond + " " + " ".join(kws)
        q_bio = m_bio.encode([q_text], normalize_embeddings=True)[0]
        q_mpnet = m_mpnet.encode([q_text], normalize_embeddings=True)[0]
        q_ens = (q_bio + q_mpnet) / 2.0
        q_ens /= np.linalg.norm(q_ens) + 1e-9

        sims = icd_ensemble @ q_ens
        seed |= set(int(i) for i in np.where(sims >= TH)[0])

        keep_idx = sorted(seed) or [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, "submissions/v31_ensemble.csv")


if __name__ == "__main__":
    main()
