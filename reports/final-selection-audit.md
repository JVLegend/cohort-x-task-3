# CohortX Final Selection Audit

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Slots: 20/20
- Public score floor: 0.42453
- Best public in selection: 0.42995
- Max public drop in selection: 0.00542
- ASSOC/DIFF hedge slots: 4
- Non-COPD changed slots: 8
- COPD-only changed slots: 11
- Identical/public-anchor slots: 1
- Dominant changed condition: Chronic Obstructive Pulmonary Disease (17/20)

## Gates

| Gate | Status | Detail |
|---|---|---|
| slots | ready | selected=20/20 |
| public_floor | ready | max_drop=0.00542 tolerance=0.00600 |
| assoc_diff_hedges | ready | slots=4; minimum=4 |
| condition_concentration | crowded | dominant=`Chronic Obstructive Pulmonary Disease`; slots=17; warning_above=10 |
| non_copd_hedges | ready | slots=8; minimum=5 |

## Role Mix

| Role | Slots |
|---|---:|
| Controlled public reserve | 8 |
| Near-best public hedge | 5 |
| Strategic ASSOC/DIFF hedge | 4 |
| Public anchor | 1 |
| Private hedge | 1 |
| Best public/tied | 1 |

## Changed Columns

| Column | Slots |
|---|---:|
| KEEP | 19 |
| ASSOCIATION | 4 |
| DIFF | 2 |

## Changed Condition Concentration

| Condition | Slots |
|---|---:|
| Chronic Obstructive Pulmonary Disease | 17 |
| CKD | 4 |
| Pneumonia | 4 |
| Diabetes | 3 |
| Pleurisy | 3 |
| Bronchitis | 3 |
| Heart Failure | 3 |
| Interstitial Lung Disease | 3 |
| UTI | 2 |
| Epistaxis | 2 |
| Gout | 2 |
| Thyroiditis | 2 |

## Slot Diagnostics

| Slot | Role | File | Public | Drop vs best | Volume | Changed columns | Changed conditions |
|---:|---|---|---:|---:|---:|---|---|
| 1 | Public anchor | `v178_FINAL.csv` | 0.42453 | 0.00542 | 0 | none | identical to anchor |
| 2 | Private hedge | `v185_private_kw.csv` | 0.42453 | 0.00542 | 447 | KEEP | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 3 | Best public/tied | `v296_copd_no_j20_j45_j81_j82_j93_j95.csv` | 0.42995 | 0.00000 | 15 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15) |
| 4 | Strategic ASSOC/DIFF hedge | `v286_assocdiff_broad_assoc.csv` | 0.42828 | 0.00167 | 693 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Gout (ASSOCIATION +17/-0); +17 more |
| 5 | Strategic ASSOC/DIFF hedge | `v283_assocdiff_highconf_assoc.csv` | 0.42828 | 0.00167 | 362 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +11 more |
| 6 | Strategic ASSOC/DIFF hedge | `v288_assocdiff_cardiorenal.csv` | 0.42687 | 0.00308 | 203 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7); CKD (ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); Diabetes (ASSOCIATION +116/-0, DIFF +7/-0) |
| 7 | Strategic ASSOC/DIFF hedge | `v287_assocdiff_pulmonary.csv` | 0.42687 | 0.00308 | 255 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); Interstitial Lung Disease (ASSOCIATION +41/-0, DIFF +35/-0); +1 more |
| 8 | Near-best public hedge | `v293_copd_no_j20_j45_j31_j98.csv` | 0.42874 | 0.00121 | 12 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-12) |
| 9 | Near-best public hedge | `v295_copd_no_j20_j45_j93_j95.csv` | 0.42835 | 0.00160 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11) |
| 10 | Near-best public hedge | `v294_copd_no_j20_j45_j81_j82.csv` | 0.42835 | 0.00160 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11) |
| 11 | Near-best public hedge | `v300_med_add_thymus_nodes.csv` | 0.42707 | 0.00288 | 11 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Enlarged Mediastinum (KEEP +4/-0) |
| 12 | Near-best public hedge | `v209_copd_no_acute_bronch_asthma.csv` | 0.42687 | 0.00308 | 7 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7) |
| 13 | Controlled public reserve | `v205_copd_no_j93_j95.csv` | 0.42583 | 0.00412 | 4 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) |
| 14 | Controlled public reserve | `v204_copd_no_j81_j82.csv` | 0.42583 | 0.00412 | 4 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) |
| 15 | Controlled public reserve | `v203_copd_no_j45.csv` | 0.42583 | 0.00412 | 4 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) |
| 16 | Controlled public reserve | `v207_copd_no_j98.csv` | 0.42550 | 0.00445 | 3 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-3) |
| 17 | Controlled public reserve | `v201_copd_no_j20.csv` | 0.42550 | 0.00445 | 3 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-3) |
| 18 | Controlled public reserve | `v299_med_add_c852.csv` | 0.42528 | 0.00467 | 18 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-7); Enlarged Mediastinum (KEEP +11/-0) |
| 19 | Controlled public reserve | `v202_copd_no_j31.csv` | 0.42517 | 0.00478 | 2 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-2) |
| 20 | Controlled public reserve | `v200_add_npc_kw.csv` | 0.42453 | 0.00542 | 5 | KEEP | Nasopharyngeal Carcinoma (KEEP +5/-0) |

## Actions

- Treat `condition_concentration=crowded` as a warning, not a blocker: the current public leaderboard is driven by COPD, but final slots should diversify when new public-neutral private hedges appear.
- Replacement priority: swap lowest-value COPD-only controlled reserves before dropping public anchor, private hedge, best public, or ASSOC/DIFF hedges.
- Keep at least four ASSOC/DIFF hedge slots unless a later public or private signal proves those buckets harmful.
- Keep the public floor within the controlled reserve tolerance unless the new candidate adds a deliberately stronger private/hidden hypothesis.
