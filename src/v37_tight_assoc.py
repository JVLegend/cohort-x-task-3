"""V37 — v33 KEEP + ASSOC TIGHT (so codigos canonicos exatos, 1-3 por condition).
Hipotese matematica: gold ASSOC nao-vazio em ~19/23 conditions, mas pequeno (1-3 codigos).
"""
import pandas as pd

# ASSOC canonico: codigo "irmao" mais provavel por condition (3-char root)
ASSOC_TIGHT = {
    "Epistaxis": ["R042", "R049"],  # outras hemorragias respiratorias
    "Intracranial Pressure": ["G931", "G939"],  # encefalopatia
    "Chronic Obstructive Pulmonary Disease": ["J41", "J42", "J43"],  # bronquite/enfisema
    "Enlarged Mediastinum": ["J986"],
    "Gout": ["E790"],  # hiperuricemia
    "Latent Adrenal Insufficiency": ["E2740"],
    "Dermatomycosis": ["B37"],  # candidiase
    "Pleurisy": ["J90"],  # derrame pleural
    "Bronchitis": ["J22"],
    "Thyroiditis": ["E063"],  # autoimmune
    "Nasopharyngeal Carcinoma": ["C10"],
    "CKD": ["I12", "I13"],  # HTN-CKD
    "Hypothyroidism": ["E02"],
    "Hematemesis": ["K921", "K922"],
    "Heart Failure": ["I42", "I425"],  # cardiomiopatias
    "Hypergonadism": ["E281"],
    "UTI": ["N10"],  # pielonefrite aguda
    "Diabetes": ["E162"],  # hipoglicemia farmaco
    "Interstitial Lung Disease": ["J70"],
    "Hypoparathyroidism": ["E834"],
    "Hyperparathyroidism": ["E835"],
    "Hyperthyroidism": ["E041"],
    "Pneumonia": ["J85"],
}


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def main():
    v33 = pd.read_csv("submissions/v33_obscure.csv")
    out = []
    for _, r in v33.iterrows():
        cond = r["Condition"]
        assoc = ASSOC_TIGHT.get(cond, [])
        out.append({
            "Condition": cond,
            "KEEP": r["KEEP"],
            "ASSOCIATION": "; ".join(assoc) if assoc else "Not Applicable",
            "DIFF": "Not Applicable",
        })
    pd.DataFrame(out).to_csv("submissions/v37_tight_assoc.csv", index=False)
    print("Wrote v37_tight_assoc.csv")


if __name__ == "__main__":
    main()
