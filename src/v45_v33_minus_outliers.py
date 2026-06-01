"""V45 — v33 com remocao de outliers: para cada condition, remove codigos
com similaridade BioBERT muito BAIXA (< 0.70). Esses sao provavelmente noise
do keyword matching (palavras coincidentes em contextos diferentes).
"""
import numpy as np
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data
from v21_keep_expanded import SYN_EXP

CACHE = Path("data/icd_embeddings.npy")
BIO = "pritamdeka/S-PubMedBert-MS-MARCO"
MIN_SIM = 0.90  # remove codigos com sim < threshold


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(BIO)
    code_to_idx = {c: i for i, c in enumerate(icd["icd_code"])}

    v33 = pd.read_csv("submissions/v33_obscure.csv")
    rows = []
    for _, r in v33.iterrows():
        cond = r["Condition"]
        keep_codes = parse(r["KEEP"])
        kws = SYN_EXP.get(cond, [cond])
        q_text = cond + " " + " ".join(kws)
        q_emb = model.encode([q_text], normalize_embeddings=True)[0]

        # filter out codes with low BioBERT similarity to query
        filtered = []
        for code in keep_codes:
            idx = code_to_idx.get(code)
            if idx is None:
                continue
            sim = float(icd_emb[idx] @ q_emb)
            if sim >= MIN_SIM:
                filtered.append(code)
        rows.append({
            "Condition": cond,
            "KEEP": "; ".join(filtered) if filtered else r["KEEP"],
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
        print(f"{cond:42s} v33={len(keep_codes):4d} -> filtered={len(filtered):4d}")

    pd.DataFrame(rows).to_csv("submissions/v46_v33_filt90.csv", index=False)


if __name__ == "__main__":
    main()
