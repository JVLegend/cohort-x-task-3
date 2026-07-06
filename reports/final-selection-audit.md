# CohortX Final Selection Audit

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Slots: 20/20
- Public score floor: 0.42453
- Best public in selection: 0.43156
- Max public drop in selection: 0.00703
- Replaceable public floor: 0.43136
- Max replaceable public drop: 0.00020
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
| public_floor | ready | replaceable_max_drop=0.00020; tolerance=0.00600; protected_slots=2 |
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
| Enlarged Mediastinum | 10 |
| CKD | 9 |
| Pneumonia | 9 |
| UTI | 8 |
| Diabetes | 8 |
| Gout | 2 |
| Pleurisy | 2 |
| Bronchitis | 2 |
| Thyroiditis | 2 |

## Slot Diagnostics

| Slot | Role | File | Public | Drop vs best | Volume | Changed columns | Changed conditions |
|---:|---|---|---:|---:|---:|---|---|
| 1 | Public anchor | `v178_FINAL.csv` | 0.42453 | 0.00703 | 0 | none | identical to anchor |
| 2 | Private hedge | `v185_private_kw.csv` | 0.42453 | 0.00703 | 447 | KEEP | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 3 | Best public/tied | `v392_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_pneumonia_assocdiff.csv` | 0.43156 | 0.00000 | 161 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Hematemesis (ASSOCIATION +65/-0); +1 more |
| 4 | Strategic ASSOC/DIFF hedge | `v391_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diabetes_assocdiff.csv` | 0.43156 | 0.00000 | 377 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Hematemesis (ASSOCIATION +65/-0); +1 more |
| 5 | Strategic ASSOC/DIFF hedge | `v389_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_uti_assocdiff.csv` | 0.43156 | 0.00000 | 208 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Hematemesis (ASSOCIATION +65/-0); +1 more |
| 6 | Strategic ASSOC/DIFF hedge | `v388_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_assocdiff.csv` | 0.43156 | 0.00000 | 229 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); +1 more |
| 7 | Strategic ASSOC/DIFF hedge | `v385_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diab_pneu_assocdiff.csv` | 0.43156 | 0.00000 | 406 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Hematemesis (ASSOCIATION +65/-0); +2 more |
| 8 | Strategic ASSOC/DIFF hedge | `v384_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_uti_assocdiff.csv` | 0.43156 | 0.00000 | 305 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); +2 more |
| 9 | Strategic ASSOC/DIFF hedge | `v382_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_no_v185keep_assocdiff.csv` | 0.43156 | 0.00000 | 132 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Hematemesis (ASSOCIATION +65/-0) |
| 10 | Strategic ASSOC/DIFF hedge | `v357_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185keep_ent_gi_derm_assocdiff.csv` | 0.43156 | 0.00000 | 579 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); +4 more |
| 11 | Strategic ASSOC/DIFF hedge | `v342_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_diab_pneu_assocdiff.csv` | 0.43156 | 0.00000 | 648 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +13 more |
| 12 | Strategic ASSOC/DIFF hedge | `v341_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_uti_assocdiff.csv` | 0.43156 | 0.00000 | 547 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +13 more |
| 13 | Strategic ASSOC/DIFF hedge | `v398_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_pneumonia_assocdiff.csv` | 0.43136 | 0.00020 | 157 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hematemesis (ASSOCIATION +65/-0); Pneumonia (KEEP +1/-28) |
| 14 | Strategic ASSOC/DIFF hedge | `v395_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_diabetes_assocdiff.csv` | 0.43136 | 0.00020 | 373 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hematemesis (ASSOCIATION +65/-0); Diabetes (KEEP +232/-13) |
| 15 | Strategic ASSOC/DIFF hedge | `v393_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_uti_assocdiff.csv` | 0.43136 | 0.00020 | 204 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hematemesis (ASSOCIATION +65/-0); UTI (KEEP +0/-76) |
| 16 | Strategic ASSOC/DIFF hedge | `v390_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_ckd_assocdiff.csv` | 0.43136 | 0.00020 | 225 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0) |
| 17 | Strategic ASSOC/DIFF hedge | `v387_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_diab_pneu_assocdiff.csv` | 0.43136 | 0.00020 | 402 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hematemesis (ASSOCIATION +65/-0); Diabetes (KEEP +232/-13); +1 more |
| 18 | Strategic ASSOC/DIFF hedge | `v386_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185_ckd_uti_assocdiff.csv` | 0.43136 | 0.00020 | 301 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0); +1 more |
| 19 | Strategic ASSOC/DIFF hedge | `v383_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_no_v185keep_assocdiff.csv` | 0.43136 | 0.00020 | 128 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Hematemesis (ASSOCIATION +65/-0) |
| 20 | Strategic ASSOC/DIFF hedge | `v381_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_v185keep_assocdiff.csv` | 0.43136 | 0.00020 | 575 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +48/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0); +3 more |

## Actions

- Treat `condition_concentration=crowded` as a warning, not a blocker: the current public leaderboard is driven by COPD, but final slots should diversify when new public-neutral private hedges appear.
- Replacement priority: swap lowest-value COPD-only controlled reserves before dropping public anchor, private hedge, best public, or ASSOC/DIFF hedges.
- Keep at least four ASSOC/DIFF hedge slots unless a later public or private signal proves those buckets harmful.
- Keep the replaceable public floor within the controlled reserve tolerance; protected anchor/hedge slots may sit below that floor by design.
