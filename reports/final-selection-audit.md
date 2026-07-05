# CohortX Final Selection Audit

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Slots: 20/20
- Public score floor: 0.42453
- Best public in selection: 0.43156
- Max public drop in selection: 0.00703
- Replaceable public floor: 0.43015
- Max replaceable public drop: 0.00141
- Max protected anchor/hedge drop: 0.00703
- ASSOC/DIFF hedge slots: 18
- Non-COPD changed slots: 19
- COPD-only changed slots: 0
- Identical/public-anchor slots: 1
- Dominant changed condition: CKD (18/20)

## Gates

| Gate | Status | Detail |
|---|---|---|
| slots | ready | selected=20/20 |
| public_floor | ready | replaceable_max_drop=0.00141; tolerance=0.00600; protected_slots=2 |
| assoc_diff_hedges | ready | slots=18; minimum=4 |
| condition_concentration | crowded | dominant=`CKD`; slots=18; warning_above=10 |
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

## Slot Diagnostics

| Slot | Role | File | Public | Drop vs best | Volume | Changed columns | Changed conditions |
|---:|---|---|---:|---:|---:|---|---|
| 1 | Public anchor | `v178_FINAL.csv` | 0.42453 | 0.00703 | 0 | none | identical to anchor |
| 2 | Private hedge | `v185_private_kw.csv` | 0.42453 | 0.00703 | 447 | KEEP | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 3 | Best public/tied | `v357_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185keep_ent_gi_derm_assocdiff.csv` | 0.43156 | 0.00000 | 579 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); +4 more |
| 4 | Strategic ASSOC/DIFF hedge | `v342_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diab_pneu_assocdiff.csv` | 0.43156 | 0.00000 | 648 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +13 more |
| 5 | Strategic ASSOC/DIFF hedge | `v341_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_uti_assocdiff.csv` | 0.43156 | 0.00000 | 547 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +13 more |
| 6 | Strategic ASSOC/DIFF hedge | `v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv` | 0.43156 | 0.00000 | 821 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +14 more |
| 7 | Strategic ASSOC/DIFF hedge | `v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv` | 0.43156 | 0.00000 | 1152 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 8 | Strategic ASSOC/DIFF hedge | `v348_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_diab_pneu_assocdiff.csv` | 0.43136 | 0.00020 | 644 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more |
| 9 | Strategic ASSOC/DIFF hedge | `v344_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_ckd_uti_assocdiff.csv` | 0.43136 | 0.00020 | 543 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more |
| 10 | Strategic ASSOC/DIFF hedge | `v359_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_bro_med_keep_v185_diab_pneu_assocdiff.csv` | 0.43035 | 0.00121 | 976 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 11 | Strategic ASSOC/DIFF hedge | `v356_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_bro_med_keep_v185_ckd_uti_assocdiff.csv` | 0.43035 | 0.00121 | 875 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 12 | Strategic ASSOC/DIFF hedge | `v355_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_hig_med_keep_v185_diab_pneu_assocdiff.csv` | 0.43035 | 0.00121 | 645 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +13 more |
| 13 | Strategic ASSOC/DIFF hedge | `v349_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_hig_med_keep_v185_ckd_uti_assocdiff.csv` | 0.43035 | 0.00121 | 544 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +13 more |
| 14 | Strategic ASSOC/DIFF hedge | `v304_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv` | 0.43035 | 0.00121 | 818 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +14 more |
| 15 | Strategic ASSOC/DIFF hedge | `v303_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv` | 0.43035 | 0.00121 | 1149 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Enlarged Mediastinum (KEEP +4/-0); +18 more |
| 16 | Strategic ASSOC/DIFF hedge | `v358_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_hig_no_med_add_v185_ckd_uti_assocdiff.csv` | 0.43015 | 0.00141 | 540 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more |
| 17 | Strategic ASSOC/DIFF hedge | `v354_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_no_v185keep_cardiorenal_assocdiff.csv` | 0.43015 | 0.00141 | 71 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (ASSOCIATION +17/-0); Heart Failure (ASSOCIATION +35/-0) |
| 18 | Strategic ASSOC/DIFF hedge | `v353_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_no_v185keep_pulmonary_assocdiff.csv` | 0.43015 | 0.00141 | 112 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Pleurisy (ASSOCIATION +12/-0); Bronchitis (ASSOCIATION +4/-0); +2 more |
| 19 | Strategic ASSOC/DIFF hedge | `v352_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185keep_endocrine_assocdiff.csv` | 0.43015 | 0.00141 | 546 | ASSOCIATION,KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Thyroiditis (ASSOCIATION +31/-0); CKD (KEEP +22/-75); +7 more |
| 20 | Strategic ASSOC/DIFF hedge | `v347_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_bro_no_med_add_v185keep_assocdiff.csv` | 0.43015 | 0.00141 | 1145 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-12); Gout (ASSOCIATION +17/-0); +17 more |

## Actions

- Treat `condition_concentration=crowded` as a warning, not a blocker: the current public leaderboard is driven by COPD, but final slots should diversify when new public-neutral private hedges appear.
- Replacement priority: swap lowest-value COPD-only controlled reserves before dropping public anchor, private hedge, best public, or ASSOC/DIFF hedges.
- Keep at least four ASSOC/DIFF hedge slots unless a later public or private signal proves those buckets harmful.
- Keep the replaceable public floor within the controlled reserve tolerance; protected anchor/hedge slots may sit below that floor by design.
