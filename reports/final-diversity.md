# CohortX Final Diversity Watchlist

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Recommended final selection: 20/20
- Best public score: 0.43156
- Diversity candidate floor: 0.42556
- Crowded conditions: `Bronchitis`, `CKD`, `Chronic Obstructive Pulmonary Disease`, `Diabetes`, `Enlarged Mediastinum`, `Heart Failure`, `Interstitial Lung Disease`, `Pleurisy`, `Pneumonia`, `UTI`
- Eligible concentration breakers: 12

## Gates

| Gate | Status | Detail |
|---|---|---|
| selection_concentration | crowded | crowded_conditions=10; warning_above=10 |
| diversity_alternatives | ready | candidates=12 |
| public_floor | ready | floor=0.42556; tolerance=0.00600 |

## Current Crowding

| Condition | Selected slots |
|---|---:|
| CKD | 18 |
| UTI | 18 |
| Diabetes | 18 |
| Pneumonia | 18 |
| Chronic Obstructive Pulmonary Disease | 18 |
| Enlarged Mediastinum | 17 |
| Pleurisy | 12 |
| Bronchitis | 12 |
| Heart Failure | 12 |
| Interstitial Lung Disease | 12 |
| Epistaxis | 8 |
| Gout | 8 |

## Concentration Breakers

| File | Public | Drop vs best | Crowded hits | Volume | Columns | Changed conditions |
|---|---:|---:|---:|---:|---|---|
| `v293_copd_no_j20_j45_j31_j98.csv` | 0.42874 | 0.00282 | 1 | 12 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-12) |
| `v295_copd_no_j20_j45_j93_j95.csv` | 0.42835 | 0.00321 | 1 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11) |
| `v294_copd_no_j20_j45_j81_j82.csv` | 0.42835 | 0.00321 | 1 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11) |
| `v209_copd_no_acute_bronch_asthma.csv` | 0.42687 | 0.00469 | 1 | 7 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7) |
| `v300_med_add_thymus_nodes.csv` | 0.42707 | 0.00449 | 2 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Enlarged Mediastinum (KEEP +4/-0) |
| `v288_assocdiff_cardiorenal.csv` | 0.42687 | 0.00469 | 4 | 203 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7); CKD (ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); Diabetes (ASSOCIATION +116/-0, DIFF +7/-0) |
| `v287_assocdiff_pulmonary.csv` | 0.42687 | 0.00469 | 5 | 255 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); Interstitial Lung Disease (ASSOCIATION +41/-0, DIFF +35/-0); +1 more |
| `v318_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_v185keep.csv` | 0.42894 | 0.00262 | 6 | 463 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| `v320_copd_no_j20_j45_j81_j82_med_add_thymus_nodes_v185keep.csv` | 0.42855 | 0.00301 | 6 | 462 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| `v319_copd_no_j20_j45_j93_j95_med_add_thymus_nodes_v185keep.csv` | 0.42855 | 0.00301 | 6 | 462 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| `v283_assocdiff_highconf_assoc.csv` | 0.42828 | 0.00328 | 7 | 362 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +11 more |
| `v286_assocdiff_broad_assoc.csv` | 0.42828 | 0.00328 | 9 | 693 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Gout (ASSOCIATION +17/-0); +17 more |

## Use

- Use this watchlist only as a swap guide; do not drop public anchor, private hedge, best-public slots, or strong ASSOC/DIFF hedges just to reduce concentration.
- Prefer the lowest `Crowded hits` candidates, especially zero-hit candidates when they appear after the next scored batch.
- Keep every replacement within the controlled public reserve floor unless later private evidence justifies a larger public drop.
