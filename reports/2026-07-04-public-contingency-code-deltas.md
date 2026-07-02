# CohortX Plan Code Deltas - 2026-07-04-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-04-public-contingency.csv`
- Anchor: `submissions/v209_copd_no_acute_bronch_asthma.csv`
- Changed rows: 145
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v321_v209_v185_keep_all.csv` | CKD | KEEP | 22 | 75 | v321: v209 plus v185 private KEEP | best public COPD prune plus v185 hidden KEEP hedge |
| 1 | `submissions/v321_v209_v185_keep_all.csv` | UTI | KEEP | 0 | 76 | v321: v209 plus v185 private KEEP | best public COPD prune plus v185 hidden KEEP hedge |
| 1 | `submissions/v321_v209_v185_keep_all.csv` | Diabetes | KEEP | 232 | 13 | v321: v209 plus v185 private KEEP | best public COPD prune plus v185 hidden KEEP hedge |
| 1 | `submissions/v321_v209_v185_keep_all.csv` | Pneumonia | KEEP | 1 | 28 | v321: v209 plus v185 private KEEP | best public COPD prune plus v185 hidden KEEP hedge |
| 2 | `submissions/v322_v209_v185_keep_ckd.csv` | CKD | KEEP | 22 | 75 | v322: v209 plus v185 CKD KEEP | isolates v185 CKD private KEEP on v209 |
| 3 | `submissions/v323_v209_v185_keep_uti.csv` | UTI | KEEP | 0 | 76 | v323: v209 plus v185 UTI KEEP | isolates v185 UTI private KEEP on v209 |
| 4 | `submissions/v324_v209_v185_keep_diabetes.csv` | Diabetes | KEEP | 232 | 13 | v324: v209 plus v185 Diabetes KEEP | isolates v185 Diabetes private KEEP on v209 |
| 5 | `submissions/v325_v209_v185_keep_pneumonia.csv` | Pneumonia | KEEP | 1 | 28 | v325: v209 plus v185 Pneumonia KEEP | isolates v185 Pneumonia private KEEP on v209 |
| 6 | `submissions/v326_v209_v185_keep_ckd_uti.csv` | CKD | KEEP | 22 | 75 | v326: v209 plus v185 CKD/UTI KEEP | paired renal/urinary private KEEP hedge |
| 6 | `submissions/v326_v209_v185_keep_ckd_uti.csv` | UTI | KEEP | 0 | 76 | v326: v209 plus v185 CKD/UTI KEEP | paired renal/urinary private KEEP hedge |
| 7 | `submissions/v327_v209_v185_keep_diab_pneumonia.csv` | Diabetes | KEEP | 232 | 13 | v327: v209 plus v185 Diabetes/Pneumonia KEEP | paired high-volume private KEEP hedge |
| 7 | `submissions/v327_v209_v185_keep_diab_pneumonia.csv` | Pneumonia | KEEP | 1 | 28 | v327: v209 plus v185 Diabetes/Pneumonia KEEP | paired high-volume private KEEP hedge |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Epistaxis | DIFF | 2 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Gout | ASSOCIATION | 17 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Gout | DIFF | 260 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Pleurisy | DIFF | 17 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Bronchitis | DIFF | 32 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Thyroiditis | DIFF | 6 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | CKD | KEEP | 22 | 75 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | CKD | ASSOCIATION | 17 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | CKD | DIFF | 6 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hypothyroidism | DIFF | 22 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hematemesis | DIFF | 2 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Heart Failure | DIFF | 15 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | UTI | KEEP | 0 | 76 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Diabetes | KEEP | 232 | 13 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hypoparathyroidism | DIFF | 10 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hyperparathyroidism | DIFF | 5 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Hyperthyroidism | DIFF | 15 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Pneumonia | KEEP | 1 | 28 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Pneumonia | DIFF | 71 | 0 | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Epistaxis | DIFF | 2 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Gout | DIFF | 260 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Pleurisy | DIFF | 17 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Bronchitis | DIFF | 32 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Thyroiditis | DIFF | 6 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | CKD | KEEP | 22 | 75 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | CKD | DIFF | 6 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Hypothyroidism | DIFF | 22 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Hematemesis | DIFF | 2 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Heart Failure | DIFF | 15 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | UTI | KEEP | 0 | 76 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Diabetes | KEEP | 232 | 13 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Hypoparathyroidism | DIFF | 10 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Hyperparathyroidism | DIFF | 5 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Hyperthyroidism | DIFF | 15 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Pneumonia | KEEP | 1 | 28 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Pneumonia | DIFF | 71 | 0 | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | UTI | KEEP | 0 | 76 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Diabetes | KEEP | 232 | 13 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Pleurisy | DIFF | 17 | 0 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Bronchitis | DIFF | 32 | 0 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | CKD | KEEP | 22 | 75 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | UTI | KEEP | 0 | 76 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Diabetes | KEEP | 232 | 13 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Pneumonia | KEEP | 1 | 28 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Pneumonia | DIFF | 71 | 0 | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | CKD | KEEP | 22 | 75 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | CKD | ASSOCIATION | 17 | 0 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | CKD | DIFF | 6 | 0 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | Heart Failure | DIFF | 15 | 0 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | UTI | KEEP | 0 | 76 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | Diabetes | KEEP | 232 | 13 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | Diabetes | ASSOCIATION | 116 | 0 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | Diabetes | DIFF | 7 | 0 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | Pneumonia | KEEP | 1 | 28 | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Latent Adrenal Insufficiency | DIFF | 12 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Thyroiditis | DIFF | 6 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | CKD | KEEP | 22 | 75 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Hypothyroidism | DIFF | 22 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | UTI | KEEP | 0 | 76 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Diabetes | KEEP | 232 | 13 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Diabetes | ASSOCIATION | 116 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Diabetes | DIFF | 7 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Hypoparathyroidism | DIFF | 10 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Hyperparathyroidism | DIFF | 5 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Hyperthyroidism | DIFF | 15 | 0 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Pneumonia | KEEP | 1 | 28 | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Epistaxis | DIFF | 2 | 0 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Dermatomycosis | DIFF | 33 | 0 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Nasopharyngeal Carcinoma | DIFF | 17 | 0 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | CKD | KEEP | 22 | 75 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Hematemesis | DIFF | 2 | 0 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | UTI | KEEP | 0 | 76 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Diabetes | KEEP | 232 | 13 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Pneumonia | KEEP | 1 | 28 | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | Intracranial Pressure | DIFF | 97 | 0 | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | Gout | ASSOCIATION | 17 | 0 | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | Gout | DIFF | 260 | 0 | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | CKD | KEEP | 22 | 75 | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | UTI | KEEP | 0 | 76 | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | Diabetes | KEEP | 232 | 13 | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | Pneumonia | KEEP | 1 | 28 | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 16 | `submissions/v336_copd_no_j20_j45_j31.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 2 | v336: COPD remove J20/J45/J31 | v209 plus J31 removal, isolating one extra positive public signal |
| 17 | `submissions/v337_copd_no_j20_j45_j98.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 3 | v337: COPD remove J20/J45/J98 | v209 plus J98 removal, isolating one extra positive public signal |
| 18 | `submissions/v338_copd_no_j20_j45_j31_j81_j82_j93_j95.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 10 | v338: COPD remove J20/J45/J31/J81/J82/J93/J95 | v209 plus strongest non-J96 COPD removals, excluding J98 |
| 19 | `submissions/v339_med_no_q34.csv` | Enlarged Mediastinum | KEEP | 0 | 5 | v339: mediastinum remove Q34 | unsubmitted mediastinum family ablation on v209 |
| 20 | `submissions/v340_med_no_c78_d38_j85.csv` | Enlarged Mediastinum | KEEP | 0 | 6 | v340: mediastinum remove C78/D38/J85 | small mediastinum false-positive ablation bundle on v209 |

## Exact Code Changes

### 1. `v321_v209_v185_keep_all.csv` - CKD / KEEP

- Message: v321: v209 plus v185 private KEEP
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 1. `v321_v209_v185_keep_all.csv` - UTI / KEEP

- Message: v321: v209 plus v185 private KEEP
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 1. `v321_v209_v185_keep_all.csv` - Diabetes / KEEP

- Message: v321: v209 plus v185 private KEEP
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 1. `v321_v209_v185_keep_all.csv` - Pneumonia / KEEP

- Message: v321: v209 plus v185 private KEEP
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 2. `v322_v209_v185_keep_ckd.csv` - CKD / KEEP

- Message: v322: v209 plus v185 CKD KEEP
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 3. `v323_v209_v185_keep_uti.csv` - UTI / KEEP

- Message: v323: v209 plus v185 UTI KEEP
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 4. `v324_v209_v185_keep_diabetes.csv` - Diabetes / KEEP

- Message: v324: v209 plus v185 Diabetes KEEP
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 5. `v325_v209_v185_keep_pneumonia.csv` - Pneumonia / KEEP

- Message: v325: v209 plus v185 Pneumonia KEEP
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 6. `v326_v209_v185_keep_ckd_uti.csv` - CKD / KEEP

- Message: v326: v209 plus v185 CKD/UTI KEEP
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 6. `v326_v209_v185_keep_ckd_uti.csv` - UTI / KEEP

- Message: v326: v209 plus v185 CKD/UTI KEEP
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 7. `v327_v209_v185_keep_diab_pneumonia.csv` - Diabetes / KEEP

- Message: v327: v209 plus v185 Diabetes/Pneumonia KEEP
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 7. `v327_v209_v185_keep_diab_pneumonia.csv` - Pneumonia / KEEP

- Message: v327: v209 plus v185 Diabetes/Pneumonia KEEP
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 8. `v328_v209_v185_keep_highconf_both.csv` - Epistaxis / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Epistaxis / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (2): `R58` - Hemorrhage, not elsewhere classified<br>`K920` - Hematemesis
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Gout / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Gout / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (260): `M00` - Pyogenic arthritis<br>`M000` - Staphylococcal arthritis and polyarthritis<br>`M0000` - Staphylococcal arthritis, unspecified joint<br>`M0001` - Staphylococcal arthritis, shoulder<br>`M00011` - Staphylococcal arthritis, right shoulder<br>`M00012` - Staphylococcal arthritis, left shoulder<br>`M00019` - Staphylococcal arthritis, unspecified shoulder<br>`M0002` - Staphylococcal arthritis, elbow<br>`M00021` - Staphylococcal arthritis, right elbow<br>`M00022` - Staphylococcal arthritis, left elbow<br>`M00029` - Staphylococcal arthritis, unspecified elbow<br>`M0003` - Staphylococcal arthritis, wrist<br>`M00031` - Staphylococcal arthritis, right wrist<br>`M00032` - Staphylococcal arthritis, left wrist<br>`M00039` - Staphylococcal arthritis, unspecified wrist<br>`M0004` - Staphylococcal arthritis, hand<br>`M00041` - Staphylococcal arthritis, right hand<br>`M00042` - Staphylococcal arthritis, left hand<br>... +242 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Pleurisy / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Pleurisy / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Bronchitis / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Bronchitis / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Thyroiditis / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Thyroiditis / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - CKD / KEEP

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 8. `v328_v209_v185_keep_highconf_both.csv` - CKD / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - CKD / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hypothyroidism / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hypothyroidism / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (22): `E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>`E0521` - Thyrotoxicosis with toxic multinodular goiter with thyrotoxic crisis or storm<br>`E053` - Thyrotoxicosis from ectopic thyroid tissue<br>`E0530` - Thyrotoxicosis from ectopic thyroid tissue without thyrotoxic crisis or storm<br>`E0531` - Thyrotoxicosis from ectopic thyroid tissue with thyrotoxic crisis or storm<br>`E054` - Thyrotoxicosis factitia<br>`E0540` - Thyrotoxicosis factitia without thyrotoxic crisis or storm<br>`E0541` - Thyrotoxicosis factitia with thyrotoxic crisis or storm<br>`E058` - Other thyrotoxicosis<br>`E0580` - Other thyrotoxicosis without thyrotoxic crisis or storm<br>... +4 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hematemesis / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hematemesis / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (2): `K921` - Melena<br>`R042` - Hemoptysis
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Heart Failure / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Heart Failure / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - UTI / KEEP

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 8. `v328_v209_v185_keep_highconf_both.csv` - Diabetes / KEEP

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 8. `v328_v209_v185_keep_highconf_both.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Interstitial Lung Disease / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hypoparathyroidism / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (10): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E210` - Primary hyperparathyroidism<br>`E211` - Secondary hyperparathyroidism, not elsewhere classified<br>`E212` - Other hyperparathyroidism<br>`E213` - Hyperparathyroidism, unspecified<br>`E214` - Other specified disorders of parathyroid gland<br>`E215` - Disorder of parathyroid gland, unspecified<br>`E55` - Vitamin D deficiency<br>`E550` - Rickets, active<br>`E559` - Vitamin D deficiency, unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hyperparathyroidism / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (5): `E20` - Hypoparathyroidism<br>`E200` - Idiopathic hypoparathyroidism<br>`E201` - Pseudohypoparathyroidism<br>`E208` - Other hypoparathyroidism<br>`E209` - Hypoparathyroidism, unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hyperthyroidism / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Hyperthyroidism / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (15): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`F41` - Other anxiety disorders<br>`F410` - Panic disorder [episodic paroxysmal anxiety]<br>`F411` - Generalized anxiety disorder<br>`F413` - Other mixed anxiety disorders<br>`F418` - Other specified anxiety disorders<br>`F419` - Anxiety disorder, unspecified
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Pneumonia / KEEP

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 8. `v328_v209_v185_keep_highconf_both.csv` - Pneumonia / ASSOCIATION

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 8. `v328_v209_v185_keep_highconf_both.csv` - Pneumonia / DIFF

- Message: v328: v209 v185 KEEP plus highconf assoc/diff
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Epistaxis / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (2): `R58` - Hemorrhage, not elsewhere classified<br>`K920` - Hematemesis
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Gout / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (260): `M00` - Pyogenic arthritis<br>`M000` - Staphylococcal arthritis and polyarthritis<br>`M0000` - Staphylococcal arthritis, unspecified joint<br>`M0001` - Staphylococcal arthritis, shoulder<br>`M00011` - Staphylococcal arthritis, right shoulder<br>`M00012` - Staphylococcal arthritis, left shoulder<br>`M00019` - Staphylococcal arthritis, unspecified shoulder<br>`M0002` - Staphylococcal arthritis, elbow<br>`M00021` - Staphylococcal arthritis, right elbow<br>`M00022` - Staphylococcal arthritis, left elbow<br>`M00029` - Staphylococcal arthritis, unspecified elbow<br>`M0003` - Staphylococcal arthritis, wrist<br>`M00031` - Staphylococcal arthritis, right wrist<br>`M00032` - Staphylococcal arthritis, left wrist<br>`M00039` - Staphylococcal arthritis, unspecified wrist<br>`M0004` - Staphylococcal arthritis, hand<br>`M00041` - Staphylococcal arthritis, right hand<br>`M00042` - Staphylococcal arthritis, left hand<br>... +242 more
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Pleurisy / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Bronchitis / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Thyroiditis / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - CKD / KEEP

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 9. `v329_v209_v185_keep_highconf_diff.csv` - CKD / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Hypothyroidism / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (22): `E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>`E0521` - Thyrotoxicosis with toxic multinodular goiter with thyrotoxic crisis or storm<br>`E053` - Thyrotoxicosis from ectopic thyroid tissue<br>`E0530` - Thyrotoxicosis from ectopic thyroid tissue without thyrotoxic crisis or storm<br>`E0531` - Thyrotoxicosis from ectopic thyroid tissue with thyrotoxic crisis or storm<br>`E054` - Thyrotoxicosis factitia<br>`E0540` - Thyrotoxicosis factitia without thyrotoxic crisis or storm<br>`E0541` - Thyrotoxicosis factitia with thyrotoxic crisis or storm<br>`E058` - Other thyrotoxicosis<br>`E0580` - Other thyrotoxicosis without thyrotoxic crisis or storm<br>... +4 more
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Hematemesis / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (2): `K921` - Melena<br>`R042` - Hemoptysis
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Heart Failure / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - UTI / KEEP

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Diabetes / KEEP

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Interstitial Lung Disease / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Hypoparathyroidism / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (10): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E210` - Primary hyperparathyroidism<br>`E211` - Secondary hyperparathyroidism, not elsewhere classified<br>`E212` - Other hyperparathyroidism<br>`E213` - Hyperparathyroidism, unspecified<br>`E214` - Other specified disorders of parathyroid gland<br>`E215` - Disorder of parathyroid gland, unspecified<br>`E55` - Vitamin D deficiency<br>`E550` - Rickets, active<br>`E559` - Vitamin D deficiency, unspecified
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Hyperparathyroidism / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (5): `E20` - Hypoparathyroidism<br>`E200` - Idiopathic hypoparathyroidism<br>`E201` - Pseudohypoparathyroidism<br>`E208` - Other hypoparathyroidism<br>`E209` - Hypoparathyroidism, unspecified
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Hyperthyroidism / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (15): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`F41` - Other anxiety disorders<br>`F410` - Panic disorder [episodic paroxysmal anxiety]<br>`F411` - Generalized anxiety disorder<br>`F413` - Other mixed anxiety disorders<br>`F418` - Other specified anxiety disorders<br>`F419` - Anxiety disorder, unspecified
- Removed (0): none

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Pneumonia / KEEP

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 9. `v329_v209_v185_keep_highconf_diff.csv` - Pneumonia / DIFF

- Message: v329: v209 v185 KEEP plus highconf DIFF
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - CKD / KEEP

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - UTI / KEEP

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Diabetes / KEEP

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 10. `v330_v209_v185_keep_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v330: v209 v185 KEEP plus highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Pleurisy / ASSOCIATION

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Pleurisy / DIFF

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Bronchitis / ASSOCIATION

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Bronchitis / DIFF

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - CKD / KEEP

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - UTI / KEEP

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Diabetes / KEEP

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Interstitial Lung Disease / DIFF

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Pneumonia / KEEP

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Pneumonia / ASSOCIATION

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 11. `v331_v209_v185_keep_pulmonary_assocdiff.csv` - Pneumonia / DIFF

- Message: v331: v209 v185 KEEP plus pulmonary assoc/diff
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - CKD / KEEP

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - CKD / ASSOCIATION

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - CKD / DIFF

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - Heart Failure / ASSOCIATION

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - Heart Failure / DIFF

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - UTI / KEEP

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - Diabetes / KEEP

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - Diabetes / ASSOCIATION

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - Diabetes / DIFF

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 12. `v332_v209_v185_keep_cardiorenal_assocdiff.csv` - Pneumonia / KEEP

- Message: v332: v209 v185 KEEP plus cardiorenal assoc/diff
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Latent Adrenal Insufficiency / DIFF

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (12): `E86` - Volume depletion<br>`E860` - Dehydration<br>`E861` - Hypovolemia<br>`E869` - Volume depletion, unspecified<br>`R53` - Malaise and fatigue<br>`R530` - Neoplastic (malignant) related fatigue<br>`R531` - Weakness<br>`R532` - Functional quadriplegia<br>`R538` - Other malaise and fatigue<br>`R5381` - Other malaise<br>`R5382` - Chronic fatigue, unspecified<br>`R5383` - Other fatigue
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Thyroiditis / ASSOCIATION

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Thyroiditis / DIFF

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - CKD / KEEP

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Hypothyroidism / ASSOCIATION

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Hypothyroidism / DIFF

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (22): `E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>`E0521` - Thyrotoxicosis with toxic multinodular goiter with thyrotoxic crisis or storm<br>`E053` - Thyrotoxicosis from ectopic thyroid tissue<br>`E0530` - Thyrotoxicosis from ectopic thyroid tissue without thyrotoxic crisis or storm<br>`E0531` - Thyrotoxicosis from ectopic thyroid tissue with thyrotoxic crisis or storm<br>`E054` - Thyrotoxicosis factitia<br>`E0540` - Thyrotoxicosis factitia without thyrotoxic crisis or storm<br>`E0541` - Thyrotoxicosis factitia with thyrotoxic crisis or storm<br>`E058` - Other thyrotoxicosis<br>`E0580` - Other thyrotoxicosis without thyrotoxic crisis or storm<br>... +4 more
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - UTI / KEEP

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Diabetes / KEEP

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Diabetes / ASSOCIATION

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Diabetes / DIFF

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Hypoparathyroidism / DIFF

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (10): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E210` - Primary hyperparathyroidism<br>`E211` - Secondary hyperparathyroidism, not elsewhere classified<br>`E212` - Other hyperparathyroidism<br>`E213` - Hyperparathyroidism, unspecified<br>`E214` - Other specified disorders of parathyroid gland<br>`E215` - Disorder of parathyroid gland, unspecified<br>`E55` - Vitamin D deficiency<br>`E550` - Rickets, active<br>`E559` - Vitamin D deficiency, unspecified
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Hyperparathyroidism / DIFF

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (5): `E20` - Hypoparathyroidism<br>`E200` - Idiopathic hypoparathyroidism<br>`E201` - Pseudohypoparathyroidism<br>`E208` - Other hypoparathyroidism<br>`E209` - Hypoparathyroidism, unspecified
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Hyperthyroidism / ASSOCIATION

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Hyperthyroidism / DIFF

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (15): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`F41` - Other anxiety disorders<br>`F410` - Panic disorder [episodic paroxysmal anxiety]<br>`F411` - Generalized anxiety disorder<br>`F413` - Other mixed anxiety disorders<br>`F418` - Other specified anxiety disorders<br>`F419` - Anxiety disorder, unspecified
- Removed (0): none

### 13. `v333_v209_v185_keep_endocrine_assocdiff.csv` - Pneumonia / KEEP

- Message: v333: v209 v185 KEEP plus endocrine assoc/diff
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Epistaxis / ASSOCIATION

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Epistaxis / DIFF

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (2): `R58` - Hemorrhage, not elsewhere classified<br>`K920` - Hematemesis
- Removed (0): none

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Dermatomycosis / ASSOCIATION

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Dermatomycosis / DIFF

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (33): `L40` - Psoriasis<br>`L400` - Psoriasis vulgaris<br>`L401` - Generalized pustular psoriasis<br>`L402` - Acrodermatitis continua<br>`L403` - Pustulosis palmaris et plantaris<br>`L404` - Guttate psoriasis<br>`L405` - Arthropathic psoriasis<br>`L4050` - Arthropathic psoriasis, unspecified<br>`L4051` - Distal interphalangeal psoriatic arthropathy<br>`L4052` - Psoriatic arthritis mutilans<br>`L4053` - Psoriatic spondylitis<br>`L4054` - Psoriatic juvenile arthropathy<br>`L4059` - Other psoriatic arthropathy<br>`L408` - Other psoriasis<br>`L409` - Psoriasis, unspecified<br>`L20` - Atopic dermatitis<br>`L200` - Besnier's prurigo<br>`L208` - Other atopic dermatitis<br>... +15 more
- Removed (0): none

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Nasopharyngeal Carcinoma / DIFF

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (17): `C10` - Malignant neoplasm of oropharynx<br>`C100` - Malignant neoplasm of vallecula<br>`C101` - Malignant neoplasm of anterior surface of epiglottis<br>`C102` - Malignant neoplasm of lateral wall of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C104` - Malignant neoplasm of branchial cleft<br>`C108` - Malignant neoplasm of overlapping sites of oropharynx<br>`C109` - Malignant neoplasm of oropharynx, unspecified<br>`C14` - Malignant neoplasm of other and ill-defined sites in the lip, oral cavity and pharynx<br>`C140` - Malignant neoplasm of pharynx, unspecified<br>`C142` - Malignant neoplasm of Waldeyer's ring<br>`C148` - Malignant neoplasm of overlapping sites of lip, oral cavity and pharynx<br>`J33` - Nasal polyp<br>`J330` - Polyp of nasal cavity<br>`J331` - Polypoid sinus degeneration<br>`J338` - Other polyp of sinus<br>`J339` - Nasal polyp, unspecified
- Removed (0): none

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - CKD / KEEP

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Hematemesis / ASSOCIATION

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Hematemesis / DIFF

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (2): `K921` - Melena<br>`R042` - Hemoptysis
- Removed (0): none

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - UTI / KEEP

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Diabetes / KEEP

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 14. `v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` - Pneumonia / KEEP

- Message: v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 15. `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` - Intracranial Pressure / ASSOCIATION

- Message: v335: v209 v185 KEEP plus neuro/rheum assoc/diff
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 15. `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` - Intracranial Pressure / DIFF

- Message: v335: v209 v185 KEEP plus neuro/rheum assoc/diff
- Added (97): `G43` - Migraine<br>`G430` - Migraine without aura<br>`G4300` - Migraine without aura, not intractable<br>`G43001` - Migraine without aura, not intractable, with status migrainosus<br>`G43009` - Migraine without aura, not intractable, without status migrainosus<br>`G4301` - Migraine without aura, intractable<br>`G43011` - Migraine without aura, intractable, with status migrainosus<br>`G43019` - Migraine without aura, intractable, without status migrainosus<br>`G431` - Migraine with aura<br>`G4310` - Migraine with aura, not intractable<br>`G43101` - Migraine with aura, not intractable, with status migrainosus<br>`G43109` - Migraine with aura, not intractable, without status migrainosus<br>`G4311` - Migraine with aura, intractable<br>`G43111` - Migraine with aura, intractable, with status migrainosus<br>`G43119` - Migraine with aura, intractable, without status migrainosus<br>`G434` - Hemiplegic migraine<br>`G4340` - Hemiplegic migraine, not intractable<br>`G43401` - Hemiplegic migraine, not intractable, with status migrainosus<br>... +79 more
- Removed (0): none

### 15. `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` - Gout / ASSOCIATION

- Message: v335: v209 v185 KEEP plus neuro/rheum assoc/diff
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 15. `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` - Gout / DIFF

- Message: v335: v209 v185 KEEP plus neuro/rheum assoc/diff
- Added (260): `M00` - Pyogenic arthritis<br>`M000` - Staphylococcal arthritis and polyarthritis<br>`M0000` - Staphylococcal arthritis, unspecified joint<br>`M0001` - Staphylococcal arthritis, shoulder<br>`M00011` - Staphylococcal arthritis, right shoulder<br>`M00012` - Staphylococcal arthritis, left shoulder<br>`M00019` - Staphylococcal arthritis, unspecified shoulder<br>`M0002` - Staphylococcal arthritis, elbow<br>`M00021` - Staphylococcal arthritis, right elbow<br>`M00022` - Staphylococcal arthritis, left elbow<br>`M00029` - Staphylococcal arthritis, unspecified elbow<br>`M0003` - Staphylococcal arthritis, wrist<br>`M00031` - Staphylococcal arthritis, right wrist<br>`M00032` - Staphylococcal arthritis, left wrist<br>`M00039` - Staphylococcal arthritis, unspecified wrist<br>`M0004` - Staphylococcal arthritis, hand<br>`M00041` - Staphylococcal arthritis, right hand<br>`M00042` - Staphylococcal arthritis, left hand<br>... +242 more
- Removed (0): none

### 15. `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` - CKD / KEEP

- Message: v335: v209 v185 KEEP plus neuro/rheum assoc/diff
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 15. `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` - UTI / KEEP

- Message: v335: v209 v185 KEEP plus neuro/rheum assoc/diff
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 15. `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` - Diabetes / KEEP

- Message: v335: v209 v185 KEEP plus neuro/rheum assoc/diff
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 15. `v335_v209_v185_keep_neuro_rheum_assocdiff.csv` - Pneumonia / KEEP

- Message: v335: v209 v185 KEEP plus neuro/rheum assoc/diff
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 16. `v336_copd_no_j20_j45_j31.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v336: COPD remove J20/J45/J31
- Added (0): none
- Removed (2): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis

### 17. `v337_copd_no_j20_j45_j98.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v337: COPD remove J20/J45/J98
- Added (0): none
- Removed (3): `J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 18. `v338_copd_no_j20_j45_j31_j81_j82_j93_j95.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v338: COPD remove J20/J45/J31/J81/J82/J93/J95
- Added (0): none
- Removed (10): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure

### 19. `v339_med_no_q34.csv` - Enlarged Mediastinum / KEEP

- Message: v339: mediastinum remove Q34
- Added (0): none
- Removed (5): `Q34` - Other congenital malformations of respiratory system<br>`Q340` - Anomaly of pleura<br>`Q341` - Congenital cyst of mediastinum<br>`Q348` - Other specified congenital malformations of respiratory system<br>`Q349` - Congenital malformation of respiratory system, unspecified

### 20. `v340_med_no_c78_d38_j85.csv` - Enlarged Mediastinum / KEEP

- Message: v340: mediastinum remove C78/D38/J85
- Added (0): none
- Removed (6): `C78` - Secondary malignant neoplasm of respiratory and digestive organs<br>`C781` - Secondary malignant neoplasm of mediastinum<br>`D38` - Neoplasm of uncertain behavior of middle ear and respiratory and intrathoracic organs<br>`D383` - Neoplasm of uncertain behavior of mediastinum<br>`J85` - Abscess of lung and mediastinum<br>`J853` - Abscess of mediastinum
