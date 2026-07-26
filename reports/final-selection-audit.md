# CohortX Final Selection Audit

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Slots: 20/20
- Public score floor: 0.42453
- Best public in selection: 0.43713
- Max public drop in selection: 0.01260
- Replaceable public floor: 0.43476
- Max replaceable public drop: 0.00237
- Max protected anchor/hedge drop: 0.01260
- ASSOC/DIFF hedge slots: 18
- Non-COPD changed slots: 19
- COPD-only changed slots: 0
- Identical/public-anchor slots: 1
- Dominant changed condition: Epistaxis (18/20)

## Gates

| Gate | Status | Detail |
|---|---|---|
| slots | ready | selected=20/20 |
| public_floor | ready | replaceable_max_drop=0.00237; tolerance=0.00600; protected_slots=2 |
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
| Enlarged Mediastinum | 18 |
| CKD | 4 |
| UTI | 4 |
| Diabetes | 4 |
| Pneumonia | 4 |

## Slot Diagnostics

| Slot | Role | File | Public | Drop vs best | Volume | Changed columns | Changed conditions |
|---:|---|---|---:|---:|---:|---|---|
| 1 | Public anchor | `v178_FINAL.csv` | 0.42453 | 0.01260 | 0 | none | identical to anchor |
| 2 | Private hedge | `v185_private_kw.csv` | 0.42453 | 0.01260 | 447 | KEEP | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 3 | Best public/tied | `v832_v715_med_drop_d15.csv` | 0.43713 | 0.00000 | 26 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-6) |
| 4 | Strategic ASSOC/DIFF hedge | `v830_v715_med_drop_q34.csv` | 0.43695 | 0.00018 | 25 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-5) |
| 5 | Strategic ASSOC/DIFF hedge | `v838_v715_med_drop_q34_nonmediastinal.csv` | 0.43658 | 0.00055 | 23 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-3) |
| 6 | Strategic ASSOC/DIFF hedge | `v828_v715_med_drop_d38.csv` | 0.43641 | 0.00072 | 22 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-2) |
| 7 | Strategic ASSOC/DIFF hedge | `v827_v715_med_drop_c78.csv` | 0.43641 | 0.00072 | 22 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-2) |
| 8 | Strategic ASSOC/DIFF hedge | `v750_v633_med_add_c39_med_keep_v185_pneumonia_assocdiff.csv` | 0.43606 | 0.00107 | 49 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Pneumonia (KEEP +1/-28) |
| 9 | Strategic ASSOC/DIFF hedge | `v749_v633_med_add_c39_med_keep_v185_diabetes_assocdiff.csv` | 0.43606 | 0.00107 | 265 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Diabetes (KEEP +232/-13) |
| 10 | Strategic ASSOC/DIFF hedge | `v747_v633_med_add_c39_med_keep_v185_uti_assocdiff.csv` | 0.43606 | 0.00107 | 96 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); UTI (KEEP +0/-76) |
| 11 | Strategic ASSOC/DIFF hedge | `v745_v633_med_add_c39_med_keep_v185_ckd_assocdiff.csv` | 0.43606 | 0.00107 | 117 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75) |
| 12 | Strategic ASSOC/DIFF hedge | `v743_v633_med_add_c39_med_keep_v185_diab_pneu_assocdiff.csv` | 0.43606 | 0.00107 | 294 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Diabetes (KEEP +232/-13); +1 more |
| 13 | Strategic ASSOC/DIFF hedge | `v742_v633_med_add_c39_med_keep_v185_ckd_uti_assocdiff.csv` | 0.43606 | 0.00107 | 193 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); +1 more |
| 14 | Strategic ASSOC/DIFF hedge | `v741_v633_med_add_c39_med_keep_v185keep_assoc_only.csv` | 0.43606 | 0.00107 | 467 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); +3 more |
| 15 | Strategic ASSOC/DIFF hedge | `v715_v633_med_add_c39.csv` | 0.43606 | 0.00107 | 20 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0) |
| 16 | Strategic ASSOC/DIFF hedge | `v826_v633_med_add_c390_c399.csv` | 0.43541 | 0.00172 | 19 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +3/-0) |
| 17 | Strategic ASSOC/DIFF hedge | `v825_v633_med_add_c39_c399.csv` | 0.43541 | 0.00172 | 19 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +3/-0) |
| 18 | Strategic ASSOC/DIFF hedge | `v824_v633_med_add_c39_c390.csv` | 0.43541 | 0.00172 | 19 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +3/-0) |
| 19 | Strategic ASSOC/DIFF hedge | `v829_v715_med_drop_j85.csv` | 0.43476 | 0.00237 | 22 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-2) |
| 20 | Strategic ASSOC/DIFF hedge | `v823_v633_med_add_c399.csv` | 0.43476 | 0.00237 | 18 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +2/-0) |

## Actions

- Treat `condition_concentration=crowded` as a warning, not a blocker: the current public leaderboard is driven by COPD, but final slots should diversify when new public-neutral private hedges appear.
- Replacement priority: swap lowest-value COPD-only controlled reserves before dropping public anchor, private hedge, best public, or ASSOC/DIFF hedges.
- Keep at least four ASSOC/DIFF hedge slots unless a later public or private signal proves those buckets harmful.
- Keep the replaceable public floor within the controlled reserve tolerance; protected anchor/hedge slots may sit below that floor by design.
