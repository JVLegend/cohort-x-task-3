"""V33 — v25 th=0.91 + KEEP obscuros (codigos relacionados que estavam fora).
Ex: O24 (DM em gravidez), Z79 (uso de drogas), etc."""
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

CACHE = Path("data/icd_embeddings.npy")
TH = 0.91

# KEEP prefixos adicionais (codigos "obscuros" mas legitimos para a condicao)
KEEP_EXTRA = {
    "Diabetes": ["O24", "E08", "E09", "Z794", "Z8632"],  # gestational, DM by underlying, hist
    "Heart Failure": ["I97130", "I97131"],  # postprocedural HF
    "Pneumonia": ["P23", "P232", "P233", "P234", "P238", "P239"],  # neonatal pneumonia
    "UTI": ["O861", "O862", "O864", "P393"],  # obstetric/neonatal UTI
    "CKD": ["Q60", "Q61", "Q62"],  # congenital renal
    "Hypothyroidism": ["P721", "P720", "E000", "E001", "E002", "E009"],  # congenital, iodine def
    "Hyperthyroidism": ["P721"],  # neonatal
    "Bronchitis": ["J430", "J431", "J432", "J438", "J439"],  # emphysema (assoc)
}


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer("pritamdeka/S-PubMedBert-MS-MARCO")
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        keep_p = list(keep_p) + KEEP_EXTRA.get(cond, [])
        kws = SYN_EXP.get(cond, [cond])
        seed = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws))
        q_text = cond + " " + " ".join(kws)
        sims = (model.encode([q_text], normalize_embeddings=True) @ icd_emb.T)[0]
        seed |= set(int(i) for i in np.where(sims >= TH)[0])
        keep_idx = sorted(seed) or [0]
        rows.append((cond, icd.iloc[keep_idx]["icd_code"].tolist(), [], []))
        print(f"{cond:42s} K={len(keep_idx):4d}")
    write_submission(rows, "submissions/v33_obscure.csv")


if __name__ == "__main__":
    main()
