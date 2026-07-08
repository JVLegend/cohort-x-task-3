# CohortX Final Diversity Watchlist

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Recommended final selection: 20/20
- Best public score: 0.43156
- Diversity candidate floor: 0.42556
- Crowded conditions: `Bronchitis`, `CKD`, `Chronic Obstructive Pulmonary Disease`, `Epistaxis`, `Gout`, `Heart Failure`, `Hematemesis`, `Hyperparathyroidism`, `Hyperthyroidism`, `Hypoparathyroidism`, `Hypothyroidism`, `Interstitial Lung Disease`, `Pleurisy`, `Pneumonia`, `Thyroiditis`
- Eligible concentration breakers: 32

## Gates

| Gate | Status | Detail |
|---|---|---|
| selection_concentration | crowded | crowded_conditions=15; warning_above=10 |
| diversity_alternatives | ready | candidates=32 |
| public_floor | ready | floor=0.42556; tolerance=0.00600 |

## Current Crowding

| Condition | Selected slots |
|---|---:|
| Epistaxis | 18 |
| Chronic Obstructive Pulmonary Disease | 18 |
| Hematemesis | 18 |
| Pneumonia | 16 |
| CKD | 14 |
| Gout | 13 |
| Pleurisy | 13 |
| Bronchitis | 13 |
| Thyroiditis | 13 |
| Hypothyroidism | 13 |
| Heart Failure | 13 |
| Interstitial Lung Disease | 13 |

## Concentration Breakers

| File | Public | Drop vs best | Crowded hits | Volume | Columns | Changed conditions |
|---|---:|---:|---:|---:|---|---|
| `v499_v296_med_zero_derm_npc_pair.csv` | 0.43015 | 0.00141 | 1 | 99 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Dermatomycosis (KEEP +0/-38); Nasopharyngeal Carcinoma (KEEP +0/-42) |
| `v491_v296_add_npc_kw.csv` | 0.42995 | 0.00161 | 1 | 20 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Nasopharyngeal Carcinoma (KEEP +5/-0) |
| `v484_v296_zero_derm.csv` | 0.42995 | 0.00161 | 1 | 53 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Dermatomycosis (KEEP +0/-38) |
| `v486_v296_zero_npc.csv` | 0.42995 | 0.00161 | 1 | 57 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Nasopharyngeal Carcinoma (KEEP +0/-42) |
| `v490_v296_add_derm_kw.csv` | 0.42995 | 0.00161 | 1 | 72 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Dermatomycosis (KEEP +57/-0) |
| `v494_v296_zero_derm_npc_pair.csv` | 0.42995 | 0.00161 | 1 | 95 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Dermatomycosis (KEEP +0/-38); Nasopharyngeal Carcinoma (KEEP +0/-42) |
| `v441_copd_j31_j98_med_add_thymus_nodes.csv` | 0.42894 | 0.00262 | 1 | 16 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0) |
| `v443_copd_j93_j95_med_add_thymus_nodes.csv` | 0.42855 | 0.00301 | 1 | 15 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0) |
| `v442_copd_j81_j82_med_add_thymus_nodes.csv` | 0.42855 | 0.00301 | 1 | 15 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0) |
| `v496_v296_med_zero_hf.csv` | 0.43015 | 0.00141 | 2 | 91 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Heart Failure (KEEP +0/-72) |
| `v488_v296_add_hf_kw.csv` | 0.42995 | 0.00161 | 2 | 21 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Heart Failure (KEEP +6/-0) |
| `v489_v296_add_ild_kw.csv` | 0.42995 | 0.00161 | 2 | 24 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Interstitial Lung Disease (KEEP +9/-0) |

## Use

- Use this watchlist only as a swap guide; do not drop public anchor, private hedge, best-public slots, or strong ASSOC/DIFF hedges just to reduce concentration.
- Prefer the lowest `Crowded hits` candidates, especially zero-hit candidates when they appear after the next scored batch.
- Keep every replacement within the controlled public reserve floor unless later private evidence justifies a larger public drop.
