"""V137 — v93 com filtro de chapters clinicamente corretos por condition.
Insight: ICP tem 68 S06 codes (trauma) incorretos no v93 por colisao keyword "intracranial".
"""
import pandas as pd
from common import load_data


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


# Chapters permitidos por condition (1 char = chapter ICD-10)
ALLOWED_CHAPTERS = {
    "Epistaxis": {"R"},  # symptoms (R040)
    "Intracranial Pressure": {"G", "H"},  # G932 etc, H47 papiledema
    "Chronic Obstructive Pulmonary Disease": {"J"},
    "Enlarged Mediastinum": {"D", "J", "Q", "C"},  # neoplasms, resp, congenital, malignant
    "Gout": {"M", "E"},  # musculoskeletal + uric acid
    "Latent Adrenal Insufficiency": {"E"},
    "Dermatomycosis": {"B", "L"},  # infections + skin
    "Pleurisy": {"J", "R"},
    "Bronchitis": {"J"},
    "Thyroiditis": {"E"},
    "Nasopharyngeal Carcinoma": {"C", "D"},
    "CKD": {"N", "I", "Z", "Q"},  # renal, HTN-CKD, history, congenital
    "Hypothyroidism": {"E", "P"},  # E + congenital P72.x
    "Hematemesis": {"K", "R"},
    "Heart Failure": {"I"},
    "Hypergonadism": {"E"},
    "UTI": {"N", "O", "P"},  # urinary, obstetric, neonatal
    "Diabetes": {"E", "O", "Z", "P"},  # endo, gestational, history, neonatal
    "Interstitial Lung Disease": {"J"},
    "Hypoparathyroidism": {"E", "P"},
    "Hyperparathyroidism": {"E"},
    "Hyperthyroidism": {"E", "P"},
    "Pneumonia": {"J", "A", "B", "P"},  # resp + specific infectious + neonatal
}


def main():
    cond_df, icd = load_data()
    v93 = pd.read_csv("submissions/v93_t4.csv")
    rows = []
    for _, r in v93.iterrows():
        cond = r["Condition"]
        keep = parse(r["KEEP"])
        allowed = ALLOWED_CHAPTERS.get(cond, set())
        if not allowed:
            filtered = keep
        else:
            filtered = [c for c in keep if c[0] in allowed]
        if not filtered:
            filtered = keep[:5]
        rows.append({
            "Condition": cond,
            "KEEP": "; ".join(filtered),
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
        removed = len(keep) - len(filtered)
        print(f"{cond:42s} v93={len(keep):4d} -> filtered={len(filtered):4d} (removed {removed})")
    pd.DataFrame(rows).to_csv("submissions/v137_chapter_filter.csv", index=False)


if __name__ == "__main__":
    main()
