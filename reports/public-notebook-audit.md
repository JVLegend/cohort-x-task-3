# Public Notebook Audit

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Downloaded public notebooks audited: 4
- Scope: local notebooks in `external_notebooks/` linked to CohortX Task 3.
- Decision: do not copy these baselines directly; use them only as weak retrieval ideas.

## Notebook Signals

| Ref | Title | Lines | Retrieval | Models | Label strategy | Risk/read |
|---|---|---:|---|---|---|---|
| `haradibots/identify-relevant-icd-10-cm-codes-ba3f6c` | Identify Relevant ICD-10-CM Codes ba3f6c | 117 | embedding cosine<br>TF-IDF | pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb | fixed top-k split: KEEP first 3, ASSOC next 5, DIFF next 7 | fills ASSOC/DIFF; risky because local probes show empty ASSOC/DIFF is often rewarded |
| `jek1wantaufik/identify-relevant-icd-10-cm-codes` | Identify Relevant ICD-10-CM Codes | 59 | embedding cosine | all-MiniLM-L6-v2 | dynamic z-style split over top candidates | fills ASSOC/DIFF; risky because local probes show empty ASSOC/DIFF is often rewarded; generic MiniLM/mpnet signal is weaker than current medical-curated anchor |
| `jek1wantaufik/resolving-medical-conditions` | Resolving Medical Conditions | 280 | embedding cosine<br>TF-IDF<br>BM25<br>score ensemble<br>abbreviation expansion | pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb | relative-threshold split over top candidates | fills ASSOC/DIFF; risky because local probes show empty ASSOC/DIFF is often rewarded; BM25/TF-IDF can inspire retrieval candidates, but not direct label filling |
| `jek1wantaufik/resolving-to-icd-10-cm-codes` | Resolving to ICD-10-CM Codes | 307 | embedding cosine<br>TF-IDF<br>BM25<br>score ensemble<br>abbreviation expansion<br>embedding ensemble | pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb<br>sentence-transformers/all-mpnet-base-v2 | relative-threshold split over top candidates | fills ASSOC/DIFF; risky because local probes show empty ASSOC/DIFF is often rewarded; BM25/TF-IDF can inspire retrieval candidates, but not direct label filling |

## Constants

| Ref | Constants | Imports |
|---|---|---|
| `haradibots/identify-relevant-icd-10-cm-codes-ba3f6c` | none | import pandas as pd<br>import numpy as np<br>import re<br>from sklearn.feature_extraction.text import TfidfVectorizer<br>from sklearn.metrics.pairwise import cosine_similarity<br>from sklearn.preprocessing import normalize<br>from sentence_transformers import SentenceTransformer |
| `jek1wantaufik/identify-relevant-icd-10-cm-codes` | none | import pandas as pd<br>import numpy as np<br>from sentence_transformers import SentenceTransformer<br>from sklearn.metrics.pairwise import cosine_similarity |
| `jek1wantaufik/resolving-medical-conditions` | TOP_K = 8<br>ALPHA = 0.72<br>BETA = 0.18<br>GAMMA = 0.10<br>KEEP_THRESHOLD = 0.91<br>ASSOCIATION_THRESHOLD = 0.73 | import sys<br>import subprocess<br>import pandas as pd<br>import numpy as np<br>import re<br>import torch<br>from sentence_transformers import SentenceTransformer<br>from sklearn.feature_extraction.text import TfidfVectorizer<br>from sklearn.metrics.pairwise import cosine_similarity<br>from rank_bm25 import BM25Okapi |
| `jek1wantaufik/resolving-to-icd-10-cm-codes` | TOP_K = 6<br>ALPHA = 0.80<br>BETA = 0.12<br>GAMMA = 0.08<br>KEEP_THRESHOLD = 0.93<br>ASSOCIATION_THRESHOLD = 0.78 | import sys<br>import subprocess<br>import pandas as pd<br>import numpy as np<br>import re<br>import torch<br>from sentence_transformers import SentenceTransformer<br>from sklearn.feature_extraction.text import TfidfVectorizer<br>from sklearn.metrics.pairwise import cosine_similarity<br>from rank_bm25 import BM25Okapi |

## Strategic Takeaways

- All downloaded public notebooks are retrieval baselines, not evidence of a stronger labeling policy.
- Every notebook fills ASSOCIATION/DIFF either by fixed slices or score thresholds; local Kaggle probes indicate that is usually harmful.
- Useful reusable ideas are limited to abbreviation expansion, BM25/TF-IDF candidate generation, and model ensembling for candidate discovery.
- The active plan should remain controlled public probes on COPD and Enlarged Mediastinum, followed by adaptive combinations only after scores are complete.

