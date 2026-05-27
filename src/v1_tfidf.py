"""V1 — TF-IDF baseline.
KEEP = top similar titles that literally contain the condition keyword.
ASSOCIATION = next strongest matches.
DIFF = same ICD chapter family but different 3-char code (likely-confusables).
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from common import load_data, write_submission, expand_condition, normalize


def main():
    cond_df, icd = load_data()
    vec = TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True)
    X = vec.fit_transform(icd["norm_title"])

    rows = []
    for cond in cond_df["Condition"]:
        q = normalize(expand_condition(cond))
        qv = vec.transform([q])
        sims = cosine_similarity(qv, X).ravel()
        order = np.argsort(-sims)

        # KEEP: titles literally containing the head keyword
        head = q.split()[-1]
        keep_idx, assoc_idx, diff_idx = [], [], []
        for i in order[:200]:
            if sims[i] <= 0:
                break
            title = icd.iloc[i]["norm_title"]
            if head in title and len(keep_idx) < 25:
                keep_idx.append(i)
            elif len(assoc_idx) < 15:
                assoc_idx.append(i)
            if len(keep_idx) >= 25 and len(assoc_idx) >= 15:
                break

        # DIFF: same chapter prefix as KEEP but not in KEEP — confusables
        if keep_idx:
            chapters = {icd.iloc[i]["chapter3"] for i in keep_idx}
            for i in order[:500]:
                if i in keep_idx or i in assoc_idx:
                    continue
                if icd.iloc[i]["chapter3"] in chapters:
                    diff_idx.append(i)
                if len(diff_idx) >= 10:
                    break

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))

    write_submission(rows, "submissions/v1_tfidf.csv")


if __name__ == "__main__":
    main()
