"""V4 — Plano A: shrink agressivo + threshold relativo + sinonimos expandidos.

Estrategia:
- TF-IDF word+char fusion para ranking.
- Para cada condicao, expansao por sinonimos clinicos -> melhora recall do KEEP.
- Buckets enxutos: 3 KEEP / 4 ASSOC / 5 DIFF (median nos kernels lideres).
- KEEP exige keyword/sinonimo no titulo (alta precisao).
- ASSOC = mesma familia ICD (3 chars) NAO ja em KEEP.
- DIFF = top similaridade fora dos capitulos KEEP (confundiveis).
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack
import numpy as np
from common import load_data, write_submission, normalize

# Sinonimos clinicos por condicao (KEEP keywords = altissima especificidade)
SYN = {
    "Epistaxis": ["epistaxis"],
    "Intracranial Pressure": ["intracranial hypertension", "benign intracranial hypertension", "raised intracranial"],
    "Chronic Obstructive Pulmonary Disease": ["chronic obstructive pulmonary"],
    "Enlarged Mediastinum": ["mediastinum", "mediastinal mass"],
    "Gout": ["gout", "gouty"],
    "Latent Adrenal Insufficiency": ["adrenocortical insufficiency", "adrenal insufficiency", "addison"],
    "Dermatomycosis": ["dermatomycosis", "dermatophytosis", "tinea"],
    "Pleurisy": ["pleurisy"],
    "Bronchitis": ["bronchitis"],
    "Thyroiditis": ["thyroiditis"],
    "Nasopharyngeal Carcinoma": ["nasopharynx", "nasopharyngeal"],
    "CKD": ["chronic kidney disease"],
    "Hypothyroidism": ["hypothyroidism", "myxedema"],
    "Hematemesis": ["hematemesis"],
    "Heart Failure": ["heart failure"],
    "Hypergonadism": ["hyperfunction of ovary", "testicular hyperfunction", "hypergonadism"],
    "UTI": ["urinary tract infection"],
    "Diabetes": ["diabetes mellitus"],
    "Interstitial Lung Disease": ["interstitial pulmonary", "interstitial lung", "pulmonary fibrosis"],
    "Hypoparathyroidism": ["hypoparathyroidism"],
    "Hyperparathyroidism": ["hyperparathyroidism"],
    "Hyperthyroidism": ["thyrotoxicosis", "hyperthyroidism"],
    "Pneumonia": ["pneumonia"],
}

# Diferenciais clinicos (overlap sintomatico ou confundivel)
DIFF_KW = {
    "Epistaxis": ["hemoptysis", "hematemesis"],
    "Intracranial Pressure": ["headache", "papilledema", "migraine"],
    "Chronic Obstructive Pulmonary Disease": ["asthma", "bronchiectasis"],
    "Enlarged Mediastinum": ["lymphadenopathy", "thymus"],
    "Gout": ["pseudogout", "rheumatoid arthritis", "chondrocalcinosis"],
    "Latent Adrenal Insufficiency": ["hypopituitarism", "fatigue"],
    "Dermatomycosis": ["eczema", "psoriasis", "dermatitis"],
    "Pleurisy": ["pneumothorax", "pulmonary embolism"],
    "Bronchitis": ["asthma", "pneumonia"],
    "Thyroiditis": ["goiter", "hyperthyroidism"],
    "Nasopharyngeal Carcinoma": ["laryngeal", "oropharynx tumor"],
    "CKD": ["acute kidney failure", "nephritis"],
    "Hypothyroidism": ["hyperthyroidism"],
    "Hematemesis": ["melena", "hemoptysis"],
    "Heart Failure": ["myocardial infarction", "cardiomyopathy"],
    "Hypergonadism": ["hypogonadism"],
    "UTI": ["vaginitis", "prostatitis"],
    "Diabetes": ["diabetes insipidus", "hypoglycemia"],
    "Interstitial Lung Disease": ["pneumonia", "pulmonary edema"],
    "Hypoparathyroidism": ["hyperparathyroidism", "tetany"],
    "Hyperparathyroidism": ["hypoparathyroidism", "hypercalcemia"],
    "Hyperthyroidism": ["hypothyroidism", "thyroiditis"],
    "Pneumonia": ["bronchitis", "bronchiolitis"],
}

K_KEEP, K_ASSOC, K_DIFF = 3, 4, 5


def find_by_keywords(icd, keywords):
    idx = []
    seen = set()
    for kw in keywords:
        kwn = normalize(kw)
        mask = icd["norm_title"].str.contains(kwn, regex=False, na=False)
        for i in icd[mask].index.tolist():
            if i not in seen:
                seen.add(i)
                idx.append(i)
    return idx


def main():
    cond_df, icd = load_data()
    wvec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
    cvec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)
    Xw = wvec.fit_transform(icd["norm_title"])
    Xc = cvec.fit_transform(icd["norm_title"])
    X = hstack([Xw, Xc]).tocsr()

    rows = []
    for cond in cond_df["Condition"]:
        keep_kws = SYN.get(cond, [cond])
        diff_kws = DIFF_KW.get(cond, [])
        query = " ".join([cond] + keep_kws)
        qv = hstack([wvec.transform([normalize(query)]),
                     cvec.transform([normalize(query)])]).tocsr()
        sims = cosine_similarity(qv, X).ravel()
        order = np.argsort(-sims)

        # KEEP: filtra so candidatos com keyword no titulo, ordena por sim, top-K
        kw_hits = find_by_keywords(icd, keep_kws)
        kw_set = set(kw_hits)
        keep_ranked = [i for i in order if i in kw_set]
        keep_idx = keep_ranked[:K_KEEP]

        # ASSOC: codigos no mesmo capitulo (3 chars) que KEEP, fora do KEEP
        keep_chs = {icd.iloc[i]["chapter3"] for i in keep_idx}
        assoc_idx = []
        for i in order:
            if i in keep_idx:
                continue
            if icd.iloc[i]["chapter3"] in keep_chs and sims[i] > 0:
                assoc_idx.append(i)
            if len(assoc_idx) >= K_ASSOC:
                break

        # DIFF: keyword diff OU top similaridade fora dos capitulos KEEP
        diff_idx = []
        if diff_kws:
            diff_hits = set(find_by_keywords(icd, diff_kws))
            for i in order:
                if i in keep_idx or i in assoc_idx:
                    continue
                if i in diff_hits and icd.iloc[i]["chapter3"] not in keep_chs:
                    diff_idx.append(i)
                if len(diff_idx) >= K_DIFF:
                    break
        # completa com top similaridade fora dos capitulos
        if len(diff_idx) < K_DIFF:
            for i in order:
                if i in keep_idx or i in assoc_idx or i in diff_idx:
                    continue
                if icd.iloc[i]["chapter3"] not in keep_chs and sims[i] > 0.05:
                    diff_idx.append(i)
                if len(diff_idx) >= K_DIFF:
                    break

        # Fallback: garante >=1 KEEP via top-sim se keyword nao bateu
        if not keep_idx:
            keep_idx = [int(order[0])]

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))

    write_submission(rows, "submissions/v4_quickwin.csv")


if __name__ == "__main__":
    main()
