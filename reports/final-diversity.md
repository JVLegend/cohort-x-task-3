# CohortX Final Diversity Watchlist

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Recommended final selection: 20/20
- Best public score: 0.43156
- Diversity candidate floor: 0.42556
- Crowded conditions: `Bronchitis`, `CKD`, `Chronic Obstructive Pulmonary Disease`, `Diabetes`, `Enlarged Mediastinum`, `Epistaxis`, `Gout`, `Heart Failure`, `Hematemesis`, `Hyperparathyroidism`, `Hyperthyroidism`, `Hypoparathyroidism`, `Hypothyroidism`, `Interstitial Lung Disease`, `Pleurisy`, `Pneumonia`, `Thyroiditis`, `UTI`
- Eligible concentration breakers: 27

## Gates

| Gate | Status | Detail |
|---|---|---|
| selection_concentration | crowded | crowded_conditions=18; warning_above=10 |
| diversity_alternatives | ready | candidates=27 |
| public_floor | ready | floor=0.42556; tolerance=0.00600 |

## Current Crowding

| Condition | Selected slots |
|---|---:|
| CKD | 18 |
| Pneumonia | 18 |
| Chronic Obstructive Pulmonary Disease | 18 |
| Epistaxis | 15 |
| Hematemesis | 15 |
| Pleurisy | 15 |
| Bronchitis | 15 |
| Thyroiditis | 15 |
| Hypothyroidism | 15 |
| Heart Failure | 15 |
| Interstitial Lung Disease | 15 |
| Hypoparathyroidism | 15 |

## Concentration Breakers

| File | Public | Drop vs best | Crowded hits | Volume | Columns | Changed conditions |
|---|---:|---:|---:|---:|---|---|
| `v296_copd_no_j20_j45_j81_j82_j93_j95.csv` | 0.42995 | 0.00161 | 1 | 15 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15) |
| `v293_copd_no_j20_j45_j31_j98.csv` | 0.42874 | 0.00282 | 1 | 12 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-12) |
| `v295_copd_no_j20_j45_j93_j95.csv` | 0.42835 | 0.00321 | 1 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11) |
| `v294_copd_no_j20_j45_j81_j82.csv` | 0.42835 | 0.00321 | 1 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11) |
| `v300_med_add_thymus_nodes.csv` | 0.42707 | 0.00449 | 2 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Enlarged Mediastinum (KEEP +4/-0) |
| `v317_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_v185keep.csv` | 0.43015 | 0.00141 | 6 | 466 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| `v351_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185keep_cardiorenal_assocdiff.csv` | 0.42995 | 0.00161 | 6 | 514 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); CKD (KEEP +22/-75, ASSOCIATION +17/-0); Heart Failure (ASSOCIATION +35/-0); UTI (KEEP +0/-76); +2 more |
| `v318_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_v185keep.csv` | 0.42894 | 0.00262 | 6 | 463 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| `v320_copd_no_j20_j45_j81_j82_med_add_thymus_nodes_v185keep.csv` | 0.42855 | 0.00301 | 6 | 462 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| `v319_copd_no_j20_j45_j93_j95_med_add_thymus_nodes_v185keep.csv` | 0.42855 | 0.00301 | 6 | 462 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| `v346_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185keep_cardiorenal_assocdiff.csv` | 0.43015 | 0.00141 | 7 | 518 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75, ASSOCIATION +17/-0); Heart Failure (ASSOCIATION +35/-0); +3 more |
| `v305_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_cardiorenal_v185keep.csv` | 0.43015 | 0.00141 | 7 | 662 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75, ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); +3 more |

## Use

- Use this watchlist only as a swap guide; do not drop public anchor, private hedge, best-public slots, or strong ASSOC/DIFF hedges just to reduce concentration.
- Prefer the lowest `Crowded hits` candidates, especially zero-hit candidates when they appear after the next scored batch.
- Keep every replacement within the controlled public reserve floor unless later private evidence justifies a larger public drop.
