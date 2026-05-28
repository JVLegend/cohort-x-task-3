"""V7 — v5 (campea) + DIFF expandido por embedding (alto similar, fora chapter KEEP).

Mantem cobertura ampla de v5 para KEEP e ASSOC.
Para DIFF: combina keyword matches + top-K por similaridade BioBERT fora dos capitulos KEEP.
"""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission, normalize
from v4_quickwin import SYN, DIFF_KW, find_by_keywords

MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
CACHE = Path("data/icd_embeddings.npy")
DIFF_TOPK = 25  # top sim fora chapter


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)  # ja cacheado
    model = SentenceTransformer(MODEL_NAME)

    rows = []
    for cond in cond_df["Condition"]:
        keep_kws = SYN.get(cond, [cond])
        diff_kws = DIFF_KW.get(cond, [])

        # KEEP igual v5 (todos keyword hits)
        keep_idx = find_by_keywords(icd, keep_kws)
        if not keep_idx:
            keep_idx = [0]
        keep_set = set(keep_idx)
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_idx}

        # ASSOC igual v5 (todo chapter dos KEEP)
        assoc_idx = icd[icd["chapter3"].isin(keep_chs) & ~icd.index.isin(keep_set)].index.tolist()

        # DIFF: keyword diff matches + top sim BioBERT fora chapter KEEP
        diff_kw_idx = [i for i in find_by_keywords(icd, diff_kws)
                       if icd.iloc[i]["chapter3"] not in keep_chs and i not in keep_set]

        q_emb = model.encode([cond + " " + " ".join(keep_kws)], normalize_embeddings=True)
        emb_sim = (icd_emb @ q_emb[0])
        order = np.argsort(-emb_sim)
        diff_emb_idx = []
        for i in order:
            if i in keep_set or i in diff_kw_idx:
                continue
            if icd.iloc[i]["chapter3"] in keep_chs:
                continue
            diff_emb_idx.append(int(i))
            if len(diff_emb_idx) >= DIFF_TOPK:
                break

        diff_idx = diff_kw_idx + diff_emb_idx

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))
        print(f"{cond:42s} K={len(keep_idx):3d} A={len(assoc_idx):4d} D={len(diff_idx):3d}")

    write_submission(rows, "submissions/v7_v5plus.csv")


if __name__ == "__main__":
    main()
