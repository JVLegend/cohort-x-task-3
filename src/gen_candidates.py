"""Gera arquivo com top candidatos terminais por condicao para classificacao manual."""
import json
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data
from v4_quickwin import SYN, DIFF_KW, find_by_keywords

MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
CACHE = Path("data/icd_embeddings.npy")
TOP_PER_BUCKET = 50  # candidatos por bucket (chapter-in / chapter-out / keyword-diff)


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    out = {}
    for cond in cond_df["Condition"]:
        keep_kws = SYN.get(cond, [cond])
        diff_kws = DIFF_KW.get(cond, [])

        # KEEP candidates: keyword hits, terminais (5+ char), ordenados por embed sim
        q_emb = model.encode([cond + " " + " ".join(keep_kws)], normalize_embeddings=True)
        sims = (icd_emb @ q_emb[0])

        kw_hits = set(find_by_keywords(icd, keep_kws))

        # Bucket A: keyword hits (sem filtro de tamanho) ordenados por embed sim
        keep_cands = sorted(list(kw_hits), key=lambda i: -sims[i])

        # Chapters dos top keep
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_cands[:30]}

        # Bucket B: nao-keyword, mesmo chapter -> candidatos a ASSOC
        assoc_cands_idx = [i for i in np.argsort(-sims)
                           if i not in kw_hits
                           and icd.iloc[i]["chapter3"] in keep_chs]
        assoc_cands = assoc_cands_idx[:TOP_PER_BUCKET]

        # Bucket C: keyword diff + outros chapters
        diff_kw_hits = set(find_by_keywords(icd, diff_kws))
        diff_cands = sorted(
            [i for i in diff_kw_hits if icd.iloc[i]["chapter3"] not in keep_chs],
            key=lambda i: -sims[i]
        )[:TOP_PER_BUCKET]

        # Bucket D: top emb sim, fora chapter
        diff_emb_cands = []
        seen = set(keep_cands) | set(assoc_cands) | set(diff_cands)
        for i in np.argsort(-sims):
            ii = int(i)
            if ii in seen:
                continue
            if icd.iloc[ii]["chapter3"] in keep_chs:
                continue
            diff_emb_cands.append(ii)
            if len(diff_emb_cands) >= 30:
                break

        def fmt(idx_list):
            return [{
                "i": int(i),
                "code": icd.iloc[i]["icd_code"],
                "title": icd.iloc[i]["long_title"],
                "sim": float(sims[i]),
            } for i in idx_list]

        out[cond] = {
            "keep_kws": keep_kws,
            "diff_kws": diff_kws,
            "candidates_keep": fmt(keep_cands[:80]),
            "candidates_assoc": fmt(assoc_cands),
            "candidates_diff_kw": fmt(diff_cands),
            "candidates_diff_emb": fmt(diff_emb_cands),
        }
        print(f"{cond:42s} keep={len(keep_cands)} assoc={len(assoc_cands)} "
              f"diff_kw={len(diff_cands)} diff_emb={len(diff_emb_cands)}")

    with open("data/candidates.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print("Wrote data/candidates.json")


if __name__ == "__main__":
    main()
