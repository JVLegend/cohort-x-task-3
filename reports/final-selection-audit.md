# CohortX Final Selection Audit

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Slots: 20/20
- Public score floor: 0.42453
- Best public in selection: 0.43156
- Max public drop in selection: 0.00703
- ASSOC/DIFF hedge slots: 16
- Non-COPD changed slots: 18
- COPD-only changed slots: 1
- Identical/public-anchor slots: 1
- Dominant changed condition: CKD (18/20)

## Gates

| Gate | Status | Detail |
|---|---|---|
| slots | ready | selected=20/20 |
| public_floor | wide_drop | max_drop=0.00703 tolerance=0.00600 |
| assoc_diff_hedges | ready | slots=16; minimum=4 |
| condition_concentration | crowded | dominant=`CKD`; slots=18; warning_above=10 |
| non_copd_hedges | ready | slots=18; minimum=5 |

## Role Mix

| Role | Slots |
|---|---:|
| Strategic ASSOC/DIFF hedge | 15 |
| Near-best public hedge | 2 |
| Public anchor | 1 |
| Private hedge | 1 |
| Best public/tied | 1 |

## Changed Columns

| Column | Slots |
|---|---:|
| KEEP | 19 |
| ASSOCIATION | 16 |
| DIFF | 8 |

## Changed Condition Concentration

| Condition | Slots |
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

## Slot Diagnostics

| Slot | Role | File | Public | Drop vs best | Volume | Changed columns | Changed conditions |
|---:|---|---|---:|---:|---:|---|---|
| 1 | Public anchor | `v178_FINAL.csv` | 0.42453 | 0.00703 | 0 | none | identical to anchor |
| 2 | Private hedge | `v185_private_kw.csv` | 0.42453 | 0.00703 | 447 | KEEP | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 3 | Best public/tied | `v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv` | 0.43156 | 0.00000 | 821 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +14 more |
| 4 | Strategic ASSOC/DIFF hedge | `v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv` | 0.43156 | 0.00000 | 1152 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 5 | Strategic ASSOC/DIFF hedge | `v304_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv` | 0.43035 | 0.00121 | 818 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +14 more |
| 6 | Strategic ASSOC/DIFF hedge | `v303_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv` | 0.43035 | 0.00121 | 1149 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 7 | Strategic ASSOC/DIFF hedge | `v306_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_pulmonary_v185keep.csv` | 0.43015 | 0.00141 | 714 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); +5 more |
| 8 | Strategic ASSOC/DIFF hedge | `v305_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_cardiorenal_v185keep.csv` | 0.43015 | 0.00141 | 662 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75, ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); +3 more |
| 9 | Strategic ASSOC/DIFF hedge | `v310_copd_no_j20_j45_j81_j82_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv` | 0.42996 | 0.00160 | 817 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +14 more |
| 10 | Strategic ASSOC/DIFF hedge | `v309_copd_no_j20_j45_j81_j82_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv` | 0.42996 | 0.00160 | 1148 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 11 | Strategic ASSOC/DIFF hedge | `v308_copd_no_j20_j45_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv` | 0.42996 | 0.00160 | 817 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +14 more |
| 12 | Strategic ASSOC/DIFF hedge | `v307_copd_no_j20_j45_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv` | 0.42996 | 0.00160 | 1148 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 13 | Strategic ASSOC/DIFF hedge | `v312_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_pulmonary_v185keep.csv` | 0.42894 | 0.00262 | 711 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); +5 more |
| 14 | Strategic ASSOC/DIFF hedge | `v311_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_cardiorenal_v185keep.csv` | 0.42894 | 0.00262 | 659 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75, ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); +3 more |
| 15 | Strategic ASSOC/DIFF hedge | `v316_copd_no_j20_j45_j81_j82_med_add_thymus_nodes_assocdiff_pulmonary_v185keep.csv` | 0.42855 | 0.00301 | 710 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); +5 more |
| 16 | Strategic ASSOC/DIFF hedge | `v315_copd_no_j20_j45_j81_j82_med_add_thymus_nodes_assocdiff_cardiorenal_v185keep.csv` | 0.42855 | 0.00301 | 658 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75, ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); +3 more |
| 17 | Strategic ASSOC/DIFF hedge | `v314_copd_no_j20_j45_j93_j95_med_add_thymus_nodes_assocdiff_pulmonary_v185keep.csv` | 0.42855 | 0.00301 | 710 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); +5 more |
| 18 | Strategic ASSOC/DIFF hedge | `v313_copd_no_j20_j45_j93_j95_med_add_thymus_nodes_assocdiff_cardiorenal_v185keep.csv` | 0.42855 | 0.00301 | 658 | ASSOCIATION,DIFF,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75, ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); +3 more |
| 19 | Near-best public hedge | `v317_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_v185keep.csv` | 0.43015 | 0.00141 | 466 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| 20 | Near-best public hedge | `v296_copd_no_j20_j45_j81_j82_j93_j95.csv` | 0.42995 | 0.00161 | 15 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15) |

## Actions

- Treat `condition_concentration=crowded` as a warning, not a blocker: the current public leaderboard is driven by COPD, but final slots should diversify when new public-neutral private hedges appear.
- Replacement priority: swap lowest-value COPD-only controlled reserves before dropping public anchor, private hedge, best public, or ASSOC/DIFF hedges.
- Keep at least four ASSOC/DIFF hedge slots unless a later public or private signal proves those buckets harmful.
- Keep the public floor within the controlled reserve tolerance unless the new candidate adds a deliberately stronger private/hidden hypothesis.
