# CohortX Final Selection Audit

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Slots: 20/20
- Public score floor: 0.42453
- Best public in selection: 0.43156
- Max public drop in selection: 0.00703
- Replaceable public floor: 0.42976
- Max replaceable public drop: 0.00180
- Max protected anchor/hedge drop: 0.00703
- ASSOC/DIFF hedge slots: 18
- Non-COPD changed slots: 19
- COPD-only changed slots: 0
- Identical/public-anchor slots: 1
- Dominant changed condition: Epistaxis (18/20)

## Gates

| Gate | Status | Detail |
|---|---|---|
| slots | ready | selected=20/20 |
| public_floor | ready | replaceable_max_drop=0.00180; tolerance=0.00600; protected_slots=2 |
| assoc_diff_hedges | ready | slots=18; minimum=4 |
| condition_concentration | crowded | dominant=`Epistaxis`; slots=18; warning_above=10 |
| non_copd_hedges | ready | slots=19; minimum=5 |

## Role Mix

| Role | Slots |
|---|---:|
| Strategic ASSOC/DIFF hedge | 17 |
| Public anchor | 1 |
| Private hedge | 1 |
| Best public/tied | 1 |

## Changed Columns

| Column | Slots |
|---|---:|
| KEEP | 19 |
| ASSOCIATION | 18 |
| DIFF | 0 |

## Changed Condition Concentration

| Condition | Slots |
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

## Slot Diagnostics

| Slot | Role | File | Public | Drop vs best | Volume | Changed columns | Changed conditions |
|---:|---|---|---:|---:|---:|---|---|
| 1 | Public anchor | `v178_FINAL.csv` | 0.42453 | 0.00703 | 0 | none | identical to anchor |
| 2 | Private hedge | `v185_private_kw.csv` | 0.42453 | 0.00703 | 447 | KEEP | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 3 | Best public/tied | `v392_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_pneumonia_assocdiff.csv` | 0.43156 | 0.00000 | 161 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Hematemesis (ASSOCIATION +65/-0); +1 more |
| 4 | Strategic ASSOC/DIFF hedge | `v391_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diabetes_assocdiff.csv` | 0.43156 | 0.00000 | 377 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Hematemesis (ASSOCIATION +65/-0); +1 more |
| 5 | Strategic ASSOC/DIFF hedge | `v398_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_pneumonia_assocdiff.csv` | 0.43136 | 0.00020 | 157 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hematemesis (ASSOCIATION +65/-0); Pneumonia (KEEP +1/-28) |
| 6 | Strategic ASSOC/DIFF hedge | `v395_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_diabetes_assocdiff.csv` | 0.43136 | 0.00020 | 373 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hematemesis (ASSOCIATION +65/-0); Diabetes (KEEP +232/-13) |
| 7 | Strategic ASSOC/DIFF hedge | `v393_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_uti_assocdiff.csv` | 0.43136 | 0.00020 | 204 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hematemesis (ASSOCIATION +65/-0); UTI (KEEP +0/-76) |
| 8 | Strategic ASSOC/DIFF hedge | `v459_copd_j31_j98_med_broad_assoc.csv` | 0.43035 | 0.00121 | 702 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 9 | Strategic ASSOC/DIFF hedge | `v456_copd_j31_j98_med_highconf_assoc.csv` | 0.43035 | 0.00121 | 371 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +12 more |
| 10 | Strategic ASSOC/DIFF hedge | `v447_copd_j31_j98_broad_assoc.csv` | 0.43015 | 0.00141 | 698 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Gout (ASSOCIATION +17/-0); +17 more |
| 11 | Strategic ASSOC/DIFF hedge | `v444_copd_j31_j98_highconf_assoc.csv` | 0.43015 | 0.00141 | 367 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +11 more |
| 12 | Strategic ASSOC/DIFF hedge | `v400_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_bro_no_med_add_v185_diab_pneu_assocdiff.csv` | 0.43015 | 0.00141 | 972 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Gout (ASSOCIATION +17/-0); +17 more |
| 13 | Strategic ASSOC/DIFF hedge | `v397_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_bro_no_med_add_v185_ckd_uti_assocdiff.csv` | 0.43015 | 0.00141 | 871 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Gout (ASSOCIATION +17/-0); +17 more |
| 14 | Strategic ASSOC/DIFF hedge | `v460_copd_j81_j82_med_broad_assoc.csv` | 0.42996 | 0.00160 | 701 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 15 | Strategic ASSOC/DIFF hedge | `v458_copd_j93_j95_med_highconf_assoc.csv` | 0.42996 | 0.00160 | 370 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +12 more |
| 16 | Strategic ASSOC/DIFF hedge | `v457_copd_j81_j82_med_highconf_assoc.csv` | 0.42996 | 0.00160 | 370 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +12 more |
| 17 | Strategic ASSOC/DIFF hedge | `v449_copd_j93_j95_broad_assoc.csv` | 0.42976 | 0.00180 | 697 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Gout (ASSOCIATION +17/-0); +17 more |
| 18 | Strategic ASSOC/DIFF hedge | `v448_copd_j81_j82_broad_assoc.csv` | 0.42976 | 0.00180 | 697 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Gout (ASSOCIATION +17/-0); +17 more |
| 19 | Strategic ASSOC/DIFF hedge | `v446_copd_j93_j95_highconf_assoc.csv` | 0.42976 | 0.00180 | 366 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +11 more |
| 20 | Strategic ASSOC/DIFF hedge | `v445_copd_j81_j82_highconf_assoc.csv` | 0.42976 | 0.00180 | 366 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-11); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +11 more |

## Actions

- Treat `condition_concentration=crowded` as a warning, not a blocker: the current public leaderboard is driven by COPD, but final slots should diversify when new public-neutral private hedges appear.
- Replacement priority: swap lowest-value COPD-only controlled reserves before dropping public anchor, private hedge, best public, or ASSOC/DIFF hedges.
- Keep at least four ASSOC/DIFF hedge slots unless a later public or private signal proves those buckets harmful.
- Keep the replaceable public floor within the controlled reserve tolerance; protected anchor/hedge slots may sit below that floor by design.
