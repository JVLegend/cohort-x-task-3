# CohortX Final Diversity Watchlist

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Recommended final selection: 20/20
- Best public score: 0.43156
- Diversity candidate floor: 0.42556
- Crowded conditions: `CKD`, `Chronic Obstructive Pulmonary Disease`, `Enlarged Mediastinum`, `Epistaxis`, `Hematemesis`, `Pneumonia`
- Eligible concentration breakers: 44

## Gates

| Gate | Status | Detail |
|---|---|---|
| selection_concentration | crowded | crowded_conditions=6; warning_above=10 |
| diversity_alternatives | ready | candidates=44 |
| public_floor | ready | floor=0.42556; tolerance=0.00600 |

## Current Crowding

| Condition | Selected slots |
|---|---:|
| Epistaxis | 18 |
| Chronic Obstructive Pulmonary Disease | 18 |
| Enlarged Mediastinum | 17 |
| Hematemesis | 17 |
| CKD | 13 |
| Pneumonia | 13 |
| UTI | 9 |
| Diabetes | 9 |
| Gout | 9 |
| Pleurisy | 9 |
| Bronchitis | 9 |
| Thyroiditis | 9 |

## Concentration Breakers

| File | Public | Drop vs best | Crowded hits | Volume | Columns | Changed conditions |
|---|---:|---:|---:|---:|---|---|
| `v531_v296_assoc_hypoparathyroidism.csv` | 0.42995 | 0.00161 | 1 | 16 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hypoparathyroidism (ASSOCIATION +1/-0) |
| `v524_v296_assoc_bronchitis.csv` | 0.42995 | 0.00161 | 1 | 19 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Bronchitis (ASSOCIATION +4/-0) |
| `v491_v296_add_npc_kw.csv` | 0.42995 | 0.00161 | 1 | 20 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Nasopharyngeal Carcinoma (KEEP +5/-0) |
| `v488_v296_add_hf_kw.csv` | 0.42995 | 0.00161 | 1 | 21 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Heart Failure (KEEP +6/-0) |
| `v532_v296_assoc_hyperparathyroidism.csv` | 0.42995 | 0.00161 | 1 | 23 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hyperparathyroidism (ASSOCIATION +8/-0) |
| `v535_v296_assoc_icp.csv` | 0.42995 | 0.00161 | 1 | 24 | ASSOCIATION,KEEP | Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15) |
| `v489_v296_add_ild_kw.csv` | 0.42995 | 0.00161 | 1 | 24 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Interstitial Lung Disease (KEEP +9/-0) |
| `v523_v296_assoc_pleurisy.csv` | 0.42995 | 0.00161 | 1 | 27 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Pleurisy (ASSOCIATION +12/-0) |
| `v522_v296_assoc_gout.csv` | 0.42995 | 0.00161 | 1 | 32 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Gout (ASSOCIATION +17/-0) |
| `v536_v296_assoc_adrenal.csv` | 0.42995 | 0.00161 | 1 | 34 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Latent Adrenal Insufficiency (ASSOCIATION +19/-0) |
| `v527_v296_assoc_hypothyroidism.csv` | 0.42995 | 0.00161 | 1 | 34 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hypothyroidism (ASSOCIATION +19/-0) |
| `v539_v296_assoc_uti.csv` | 0.42995 | 0.00161 | 1 | 35 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); UTI (ASSOCIATION +20/-0) |

## Use

- Use this watchlist only as a swap guide; do not drop public anchor, private hedge, best-public slots, or strong ASSOC/DIFF hedges just to reduce concentration.
- Prefer the lowest `Crowded hits` candidates, especially zero-hit candidates when they appear after the next scored batch.
- Keep every replacement within the controlled public reserve floor unless later private evidence justifies a larger public drop.
