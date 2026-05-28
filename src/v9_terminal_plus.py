"""V9 — v8_long (terminais) + DIFF reforcado BioBERT.
- KEEP: keyword match, so codigos com len(code) >= 5.
- ASSOC: mesmo chapter dos KEEP, terminais.
- DIFF: keyword diff + top-K BioBERT fora chapter, terminais.
"""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v4_quickwin import SYN, DIFF_KW, find_by_keywords

MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
CACHE = Path("data/icd_embeddings.npy")
DIFF_TOPK = 30


def is_terminal(code: str) -> bool:
    return len(str(code)) >= 5


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    rows = []
    for cond in cond_df["Condition"]:
        keep_kws = SYN.get(cond, [cond])
        diff_kws = DIFF_KW.get(cond, [])

        kw_hits = find_by_keywords(icd, keep_kws)
        keep_idx = [i for i in kw_hits if is_terminal(icd.iloc[i]["icd_code"])]
        if not keep_idx:
            keep_idx = kw_hits[:5] if kw_hits else [0]
        keep_set = set(keep_idx)
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_idx}

        assoc_all = icd[icd["chapter3"].isin(keep_chs) & ~icd.index.isin(keep_set)]
        assoc_idx = [i for i in assoc_all.index if is_terminal(icd.iloc[i]["icd_code"])]

        # DIFF: keyword diff terminais
        diff_idx = [i for i in find_by_keywords(icd, diff_kws)
                    if is_terminal(icd.iloc[i]["icd_code"])
                    and icd.iloc[i]["chapter3"] not in keep_chs
                    and i not in keep_set]
        # Augment com BioBERT top-K terminais fora chapter
        q_emb = model.encode([cond + " " + " ".join(keep_kws)], normalize_embeddings=True)
        sims = (icd_emb @ q_emb[0])
        order = np.argsort(-sims)
        diff_set = set(diff_idx)
        added = 0
        for i in order:
            ii = int(i)
            if ii in keep_set or ii in diff_set:
                continue
            if icd.iloc[ii]["chapter3"] in keep_chs:
                continue
            if not is_terminal(icd.iloc[ii]["icd_code"]):
                continue
            diff_idx.append(ii)
            diff_set.add(ii)
            added += 1
            if added >= DIFF_TOPK:
                break

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))
        print(f"{cond:42s} K={len(keep_idx):3d} A={len(assoc_idx):4d} D={len(diff_idx):3d}")

    write_submission(rows, "submissions/v9_terminal_plus.csv")


if __name__ == "__main__":
    main()
