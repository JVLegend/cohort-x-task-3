# CohortX Plan Impact Readout - 2026-07-04-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-04-public-contingency.csv`
- Anchor: `submissions/v209_copd_no_acute_bronch_asthma.csv`
- Anchor public: 0.42687
- Scored items: 0/20
- Improved/tied/worse/missing: 0/0/0/20

## Decision Table

| Order | File | Status | Public | Delta | Signal | Edit | Interpretation |
|---:|---|---|---:|---:|---|---|---|
| 1 | `v321_v209_v185_keep_all.csv` | missing |  |  | missing_score | +22/-75 | wait for Kaggle score before changing strategy |
| 2 | `v322_v209_v185_keep_ckd.csv` | missing |  |  | missing_score | +22/-75 | wait for Kaggle score before changing strategy |
| 3 | `v323_v209_v185_keep_uti.csv` | missing |  |  | missing_score | removed 76 | wait for Kaggle score before changing strategy |
| 4 | `v324_v209_v185_keep_diabetes.csv` | missing |  |  | missing_score | +232/-13 | wait for Kaggle score before changing strategy |
| 5 | `v325_v209_v185_keep_pneumonia.csv` | missing |  |  | missing_score | +1/-28 | wait for Kaggle score before changing strategy |
| 6 | `v326_v209_v185_keep_ckd_uti.csv` | missing |  |  | missing_score | +22/-75 | wait for Kaggle score before changing strategy |
| 7 | `v327_v209_v185_keep_diab_pneumonia.csv` | missing |  |  | missing_score | +232/-13 | wait for Kaggle score before changing strategy |
| 8 | `v328_v209_v185_keep_highconf_both.csv` | missing |  |  | missing_score | added 48 | wait for Kaggle score before changing strategy |
| 9 | `v329_v209_v185_keep_highconf_diff.csv` | missing |  |  | missing_score | added 2 | wait for Kaggle score before changing strategy |
| 10 | `v330_v209_v185_keep_highconf_assoc.csv` | missing |  |  | missing_score | added 48 | wait for Kaggle score before changing strategy |
| 11 | `v331_v209_v185_keep_pulmonary_assocdiff.csv` | missing |  |  | missing_score | added 12 | wait for Kaggle score before changing strategy |
| 12 | `v332_v209_v185_keep_cardiorenal_assocdiff.csv` | missing |  |  | missing_score | +22/-75 | wait for Kaggle score before changing strategy |
| 13 | `v333_v209_v185_keep_endocrine_assocdiff.csv` | missing |  |  | missing_score | added 19 | wait for Kaggle score before changing strategy |
| 14 | `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | missing |  |  | missing_score | added 48 | wait for Kaggle score before changing strategy |
| 15 | `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | missing |  |  | missing_score | added 9 | wait for Kaggle score before changing strategy |
| 16 | `v336_copd_no_j20_j45_j31.csv` | missing |  |  | missing_score | removed 2 | wait for Kaggle score before changing strategy |
| 17 | `v337_copd_no_j20_j45_j98.csv` | missing |  |  | missing_score | removed 3 | wait for Kaggle score before changing strategy |
| 18 | `v338_copd_no_j20_j45_j31_j81_j82_j93_j95.csv` | missing |  |  | missing_score | removed 10 | wait for Kaggle score before changing strategy |
| 19 | `v339_med_no_q34.csv` | missing |  |  | missing_score | removed 5 | wait for Kaggle score before changing strategy |
| 20 | `v340_med_no_c78_d38_j85.csv` | missing |  |  | missing_score | removed 6 | wait for Kaggle score before changing strategy |

## Ranked Scored Probes

No completed plan scores yet. Run this again after the batch is submitted and complete.

## Use

- Improved removals are pruning candidates for public-facing combos.
- Improved additions are promotion candidates for public-facing combos.
- Tied edits are mainly private hedges unless later combo evidence says otherwise.
- Worse removals indicate codes that likely belong in the public gold slice; worse additions are public false positives.
