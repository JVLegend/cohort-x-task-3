# CohortX Final Diversity Watchlist

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Recommended final selection: 20/20
- Best public score: 0.43713
- Diversity candidate floor: 0.43113
- Crowded conditions: `Chronic Obstructive Pulmonary Disease`, `Enlarged Mediastinum`, `Epistaxis`
- Eligible concentration breakers: 44

## Gates

| Gate | Status | Detail |
|---|---|---|
| selection_concentration | crowded | crowded_conditions=3; warning_above=10 |
| diversity_alternatives | ready | candidates=44 |
| public_floor | ready | floor=0.43113; tolerance=0.00600 |

## Current Crowding

| Condition | Selected slots |
|---|---:|
| Epistaxis | 18 |
| Chronic Obstructive Pulmonary Disease | 18 |
| Enlarged Mediastinum | 18 |
| CKD | 4 |
| UTI | 4 |
| Diabetes | 4 |
| Pneumonia | 4 |

## Concentration Breakers

| File | Public | Drop vs best | Crowded hits | Volume | Columns | Changed conditions |
|---|---:|---:|---:|---:|---|---|
| `v746_v633_med_add_c39_med_keep_no_v185keep_pulmonary_assocdiff.csv` | 0.43259 | 0.00454 | 2 | 19 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0) |
| `v753_v633_med_add_c39_med_keep_v185_uti_pulmonary_assocdiff.csv` | 0.43259 | 0.00454 | 2 | 95 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); UTI (KEEP +0/-76) |
| `v752_v633_med_add_c39_med_keep_v185_ckd_pulmonary_assocdiff.csv` | 0.43259 | 0.00454 | 2 | 116 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75) |
| `v748_v633_med_add_c39_med_keep_v185_ckd_uti_pulmonary_assocdiff.csv` | 0.43259 | 0.00454 | 2 | 192 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76) |
| `v754_v633_med_add_c39_med_keep_v185_diabetes_pulmonary_assocdiff.csv` | 0.43259 | 0.00454 | 2 | 264 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Diabetes (KEEP +232/-13) |
| `v751_v633_med_add_c39_med_keep_v185_diab_pneu_pulmonary_assocdiff.csv` | 0.43259 | 0.00454 | 2 | 293 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| `v744_v633_med_add_c39_med_keep_v185keep_pulmonary_assocdiff.csv` | 0.43259 | 0.00454 | 2 | 466 | KEEP | Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more |
| `v822_v633_med_add_c390.csv` | 0.43476 | 0.00237 | 3 | 18 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +2/-0) |
| `v821_v633_med_add_c39_root.csv` | 0.43476 | 0.00237 | 3 | 18 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +2/-0) |
| `v837_v715_med_drop_c380_c384_c388.csv` | 0.43410 | 0.00303 | 3 | 23 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-3) |
| `v836_v715_med_drop_j986_j988_j989.csv` | 0.43410 | 0.00303 | 3 | 23 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-3) |
| `v835_v715_med_drop_j985.csv` | 0.43410 | 0.00303 | 3 | 23 | ASSOCIATION,KEEP | Epistaxis (ASSOCIATION +1/-0); Chronic Obstructive Pulmonary Disease (KEEP +0/-15); Enlarged Mediastinum (KEEP +4/-3) |

## Use

- Use this watchlist only as a swap guide; do not drop public anchor, private hedge, best-public slots, or strong ASSOC/DIFF hedges just to reduce concentration.
- Prefer the lowest `Crowded hits` candidates, especially zero-hit candidates when they appear after the next scored batch.
- Keep every replacement within the controlled public reserve floor unless later private evidence justifies a larger public drop.
