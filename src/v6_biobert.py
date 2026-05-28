"""V6 — Plano B: BioBERT + TF-IDF + BM25 fusion (receita dos kernels lideres).

- Bi-encoder: pritamdeka/S-PubMedBert-MS-MARCO (PubMed, otimo p/ ICD).
- Fusao: 0.75*embed + 0.15*tfidf + 0.10*bm25 (todos min-max).
- KEEP = top sim com keyword no titulo (cobertura alta como v5 funcionou).
- ASSOC = mesmo chapter ICD dos KEEP, alta sim, sem KEEP.
- DIFF = top sim em outros chapters + keyword diff.
"""
import numpy as np
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize as l2
from scipy.sparse import hstack
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission, normalize
from v4_quickwin import SYN, DIFF_KW, find_by_keywords

MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
CACHE = Path("data/icd_embeddings.npy")

# Tamanhos calibrados em cima da v5 (cobertura ajuda mas demais e ruim)
K_KEEP_MAX = 60
K_ASSOC_MAX = 80
K_DIFF_MAX = 40
SIM_FLOOR_KEEP = 0.35
SIM_FLOOR_ASSOC = 0.25
SIM_FLOOR_DIFF = 0.30


def minmax(x):
    lo, hi = x.min(), x.max()
    return (x - lo) / (hi - lo + 1e-9)


def main():
    cond_df, icd = load_data()
    titles = icd["long_title"].fillna("").tolist()

    print("Loading BioBERT...")
    model = SentenceTransformer(MODEL_NAME)
    if CACHE.exists():
        print("Loading cached embeddings")
        icd_emb = np.load(CACHE)
    else:
        print(f"Encoding {len(titles)} titles (this takes a few min)...")
        icd_emb = model.encode(titles, batch_size=64, show_progress_bar=True,
                                convert_to_numpy=True, normalize_embeddings=True)
        np.save(CACHE, icd_emb)
    print("ICD emb shape:", icd_emb.shape)

    # TF-IDF
    wvec = TfidfVectorizer(ngram_range=(1, 3), sublinear_tf=True, min_df=1)
    Xw = wvec.fit_transform(icd["norm_title"])
    # BM25
    tokenized = [t.split() for t in icd["norm_title"]]
    bm25 = BM25Okapi(tokenized)

    rows = []
    for cond in cond_df["Condition"]:
        keep_kws = SYN.get(cond, [cond])
        diff_kws = DIFF_KW.get(cond, [])
        query_text = cond + " " + " ".join(keep_kws)
        qn = normalize(query_text)

        # Embedding sim
        q_emb = model.encode([query_text], normalize_embeddings=True)
        emb_sim = (icd_emb @ q_emb[0])
        # TF-IDF sim
        qv = wvec.transform([qn])
        tfidf_sim = cosine_similarity(qv, Xw).ravel()
        # BM25
        bm25_sim = np.array(bm25.get_scores(qn.split()))

        score = 0.75 * minmax(emb_sim) + 0.15 * minmax(tfidf_sim) + 0.10 * minmax(bm25_sim)
        order = np.argsort(-score)

        # KEEP: keyword hits ordenados por score, ate K_KEEP_MAX (sem floor — mantem cobertura tipo v5)
        kw_hits = set(find_by_keywords(icd, keep_kws))
        keep_idx = [i for i in order if i in kw_hits][:K_KEEP_MAX]
        if not keep_idx:
            keep_idx = [int(order[0])]
        keep_set = set(keep_idx)
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_idx}

        # ASSOC: mesmo chapter dos KEEP, ordenado por score, com floor
        assoc_idx = []
        for i in order:
            if i in keep_set:
                continue
            if icd.iloc[i]["chapter3"] in keep_chs and score[i] >= SIM_FLOOR_ASSOC:
                assoc_idx.append(i)
            if len(assoc_idx) >= K_ASSOC_MAX:
                break

        # DIFF: keyword diff + fora chapter KEEP, ou top score fora chapter KEEP
        diff_hits = set(find_by_keywords(icd, diff_kws))
        diff_idx = []
        for i in order:
            if i in keep_set or i in assoc_idx:
                continue
            ch = icd.iloc[i]["chapter3"]
            if ch in keep_chs:
                continue
            if i in diff_hits or score[i] >= SIM_FLOOR_DIFF:
                diff_idx.append(i)
            if len(diff_idx) >= K_DIFF_MAX:
                break

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))
        print(f"{cond:42s} K={len(keep_idx):3d} A={len(assoc_idx):3d} D={len(diff_idx):3d}")

    write_submission(rows, "submissions/v6_biobert.csv")


if __name__ == "__main__":
    main()
