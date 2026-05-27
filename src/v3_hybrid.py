"""V3 — Hybrid: keyword expansion (synonyms / anatomy) + TF-IDF + ICD hierarchy.
KEEP = matches with explicit condition synonyms (high precision).
ASSOCIATION = sibling codes in the same chapter family + complications.
DIFF = differential diagnoses sharing main symptom keywords across chapters.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from common import load_data, write_submission, normalize

# Map each condition -> (keep_keywords, association_keywords, diff_keywords)
RULES = {
    "Epistaxis": (["epistaxis", "nose bleed", "nosebleed", "nasal hemorrhage", "hemorrhage from throat"],
                  ["nasal", "nose"],
                  ["hemoptysis", "hematemesis", "hemorrhage"]),
    "Intracranial Pressure": (["intracranial pressure", "intracranial hypertension", "benign intracranial hypertension"],
                              ["hydrocephalus", "cerebral edema", "intracranial"],
                              ["headache", "papilledema"]),
    "Chronic Obstructive Pulmonary Disease": (["chronic obstructive pulmonary", "copd"],
                                               ["emphysema", "chronic bronchitis", "chronic obstructive"],
                                               ["asthma", "bronchiectasis"]),
    "Enlarged Mediastinum": (["mediastinum", "mediastinal"],
                              ["mediastinal mass", "mediastinitis"],
                              ["thymus", "lymphadenopathy"]),
    "Gout": (["gout", "gouty"],
              ["uric acid", "tophus", "tophi", "hyperuricemia"],
              ["arthritis", "pseudogout", "chondrocalcinosis"]),
    "Latent Adrenal Insufficiency": (["adrenal insufficiency", "addison"],
                                      ["adrenocortical", "hypoadrenalism", "adrenal"],
                                      ["hypopituitarism", "fatigue"]),
    "Dermatomycosis": (["dermatomycosis", "dermatophytosis", "tinea"],
                        ["mycosis", "candidiasis of skin", "fungal"],
                        ["dermatitis", "eczema", "psoriasis"]),
    "Pleurisy": (["pleurisy", "pleural effusion", "pleurodynia"],
                  ["pleural", "pleuritis"],
                  ["pneumonia", "pneumothorax"]),
    "Bronchitis": (["bronchitis"],
                    ["tracheobronchitis", "bronchiolitis"],
                    ["pneumonia", "asthma", "copd"]),
    "Thyroiditis": (["thyroiditis"],
                     ["hashimoto", "thyroid"],
                     ["hyperthyroidism", "hypothyroidism", "goiter"]),
    "Nasopharyngeal Carcinoma": (["nasopharynx", "nasopharyngeal"],
                                  ["malignant neoplasm of pharynx", "oropharynx"],
                                  ["laryngeal", "tonsil"]),
    "CKD": (["chronic kidney disease", "ckd"],
             ["renal failure", "kidney", "renal insufficiency"],
             ["acute kidney", "nephritis"]),
    "Hypothyroidism": (["hypothyroidism", "myxedema"],
                        ["thyroid", "hashimoto"],
                        ["hyperthyroidism", "thyroiditis"]),
    "Hematemesis": (["hematemesis"],
                     ["gastrointestinal hemorrhage", "upper gi bleed"],
                     ["melena", "hemoptysis", "epistaxis"]),
    "Heart Failure": (["heart failure", "cardiac failure"],
                       ["cardiomyopathy", "left ventricular"],
                       ["myocardial infarction", "arrhythmia"]),
    "Hypergonadism": (["hypergonadism"],
                       ["gonadal", "ovarian hyperfunction", "testicular hyperfunction"],
                       ["hypogonadism", "hyperestrogenism"]),
    "UTI": (["urinary tract infection"],
             ["cystitis", "pyelonephritis", "urethritis"],
             ["prostatitis", "vaginitis"]),
    "Diabetes": (["diabetes mellitus", "diabetic"],
                  ["hyperglycemia", "insulin"],
                  ["diabetes insipidus", "hypoglycemia"]),
    "Interstitial Lung Disease": (["interstitial lung", "interstitial pulmonary", "pulmonary fibrosis"],
                                   ["pneumoconiosis", "alveolitis"],
                                   ["pneumonia", "copd"]),
    "Hypoparathyroidism": (["hypoparathyroidism"],
                            ["parathyroid", "hypocalcemia"],
                            ["hyperparathyroidism", "tetany"]),
    "Hyperparathyroidism": (["hyperparathyroidism"],
                             ["parathyroid", "hypercalcemia"],
                             ["hypoparathyroidism"]),
    "Hyperthyroidism": (["hyperthyroidism", "thyrotoxicosis", "graves"],
                         ["goiter", "thyroid"],
                         ["hypothyroidism", "thyroiditis"]),
    "Pneumonia": (["pneumonia"],
                   ["bronchopneumonia", "pneumonitis", "lung abscess"],
                   ["bronchitis", "pleurisy", "tuberculosis"]),
}


def hits(icd, keywords, limit):
    idx = []
    seen = set()
    for kw in keywords:
        kwn = normalize(kw)
        mask = icd["norm_title"].str.contains(kwn, regex=False, na=False)
        for i in icd[mask].index.tolist():
            if i not in seen:
                seen.add(i)
                idx.append(i)
            if len(idx) >= limit:
                return idx
    return idx


def main():
    cond_df, icd = load_data()
    vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
    X = vec.fit_transform(icd["norm_title"])

    rows = []
    for cond in cond_df["Condition"]:
        keep_kw, assoc_kw, diff_kw = RULES.get(cond, ([cond], [], []))
        keep_idx = hits(icd, keep_kw, 40)
        assoc_idx = [i for i in hits(icd, assoc_kw, 30) if i not in keep_idx][:20]

        # DIFF: keyword + must NOT be in keep chapters
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_idx}
        diff_idx = []
        for i in hits(icd, diff_kw, 50):
            if i in keep_idx or i in assoc_idx:
                continue
            if icd.iloc[i]["chapter3"] in keep_chs:
                continue
            diff_idx.append(i)
            if len(diff_idx) >= 12:
                break

        # Fallback TF-IDF if buckets empty
        if not keep_idx:
            sims = cosine_similarity(vec.transform([normalize(cond)]), X).ravel()
            keep_idx = list(np.argsort(-sims)[:10])

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))

    write_submission(rows, "submissions/v3_hybrid.csv")


if __name__ == "__main__":
    main()
