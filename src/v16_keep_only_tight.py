"""V16 — So KEEP, mais ENXUTO (top canonical por condicao). ASSOC/DIFF vazios."""
from common import load_data, write_submission

# KEEP CANONICO por condicao (3-7 codigos terminais especificos)
# Baseado em conhecimento clinico — codigos billable mais provaveis no gold MIMIC-IV
KEEP_CANONICAL = {
    "Epistaxis": ["R040"],
    "Intracranial Pressure": ["G932", "G935"],
    "Chronic Obstructive Pulmonary Disease": ["J440", "J441", "J449"],
    "Enlarged Mediastinum": ["J985", "J9859"],
    "Gout": ["M109", "M1A9XX0", "M1A9XX1"],
    "Latent Adrenal Insufficiency": ["E2740", "E2749"],
    "Dermatomycosis": ["B359", "B3690"],
    "Pleurisy": ["R091"],
    "Bronchitis": ["J209", "J40", "J42"],
    "Thyroiditis": ["E069"],
    "Nasopharyngeal Carcinoma": ["C119"],
    "CKD": ["N189", "N1830", "N184", "N185", "N186"],
    "Hypothyroidism": ["E039"],
    "Hematemesis": ["K920"],
    "Heart Failure": ["I509", "I5022", "I5032", "I5042"],
    "Hypergonadism": ["E282"],
    "UTI": ["N390"],
    "Diabetes": ["E119", "E109", "E139"],
    "Interstitial Lung Disease": ["J849", "J84112", "J84111"],
    "Hypoparathyroidism": ["E2089", "E209"],
    "Hyperparathyroidism": ["E213"],
    "Hyperthyroidism": ["E0590"],
    "Pneumonia": ["J189"],
}


def main():
    cond_df, _ = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep = KEEP_CANONICAL.get(cond, [])
        rows.append((cond, keep, [], []))
    write_submission(rows, "submissions/v16_canonical.csv")


if __name__ == "__main__":
    main()
