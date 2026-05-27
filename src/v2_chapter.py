"""V2 — TF-IDF char + word, chapter-aware split.
KEEP = all codes whose 3-char chapter matches the top-1 retrieved chapter AND contain head keyword.
ASSOCIATION = remaining codes in the same chapter family (related conditions).
DIFF = high-similarity codes in different chapters (overlap symptoms).
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack
import numpy as np
from common import load_data, write_submission, expand_condition, normalize


def main():
    cond_df, icd = load_data()
    word_vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)
    char_vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)
    Xw = word_vec.fit_transform(icd["norm_title"])
    Xc = char_vec.fit_transform(icd["norm_title"])
    X = hstack([Xw, Xc]).tocsr()

    rows = []
    for cond in cond_df["Condition"]:
        q = normalize(expand_condition(cond))
        qv = hstack([word_vec.transform([q]), char_vec.transform([q])]).tocsr()
        sims = cosine_similarity(qv, X).ravel()
        order = np.argsort(-sims)

        # Identify top chapter(s) by votes among top-30 hits with keyword in title
        head = q.split()[-1]
        head_alt = q.split()[0] if len(q.split()) > 1 else head
        votes = {}
        for i in order[:60]:
            t = icd.iloc[i]["norm_title"]
            if head in t or head_alt in t:
                ch = icd.iloc[i]["chapter3"]
                votes[ch] = votes.get(ch, 0) + 1
        top_chapters = {c for c, _ in sorted(votes.items(), key=lambda x: -x[1])[:2]}

        keep_idx, assoc_idx, diff_idx = [], [], []
        for i in order[:1500]:
            ch = icd.iloc[i]["chapter3"]
            t = icd.iloc[i]["norm_title"]
            if ch in top_chapters:
                if (head in t or head_alt in t) and len(keep_idx) < 30:
                    keep_idx.append(i)
                elif len(assoc_idx) < 20:
                    assoc_idx.append(i)
            else:
                if sims[i] > 0.1 and len(diff_idx) < 12:
                    diff_idx.append(i)
            if len(keep_idx) >= 30 and len(assoc_idx) >= 20 and len(diff_idx) >= 12:
                break

        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))

    write_submission(rows, "submissions/v2_chapter.csv")


if __name__ == "__main__":
    main()
