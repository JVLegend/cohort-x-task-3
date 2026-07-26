# CohortX Plan Code Deltas - 2026-07-13

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-13.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 138
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v621_v392_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v621: v392 Epistaxis ASSOC narrowed to I10 | source v392 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_pneumonia; assoc=epistaxis_i10_narrow |
| 1 | `submissions/v621_v392_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v621: v392 Epistaxis ASSOC narrowed to I10 | source v392 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_pneumonia; assoc=epistaxis_i10_narrow |
| 1 | `submissions/v621_v392_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v621: v392 Epistaxis ASSOC narrowed to I10 | source v392 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_pneumonia; assoc=epistaxis_i10_narrow |
| 1 | `submissions/v621_v392_epi_i10_narrow.csv` | Pneumonia | KEEP | 1 | 28 | v621: v392 Epistaxis ASSOC narrowed to I10 | source v392 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_pneumonia; assoc=epistaxis_i10_narrow |
| 2 | `submissions/v622_v391_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v622: v391 Epistaxis ASSOC narrowed to I10 | source v391 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diabetes; assoc=epistaxis_i10_narrow |
| 2 | `submissions/v622_v391_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v622: v391 Epistaxis ASSOC narrowed to I10 | source v391 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diabetes; assoc=epistaxis_i10_narrow |
| 2 | `submissions/v622_v391_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v622: v391 Epistaxis ASSOC narrowed to I10 | source v391 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diabetes; assoc=epistaxis_i10_narrow |
| 2 | `submissions/v622_v391_epi_i10_narrow.csv` | Diabetes | KEEP | 232 | 13 | v622: v391 Epistaxis ASSOC narrowed to I10 | source v391 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diabetes; assoc=epistaxis_i10_narrow |
| 3 | `submissions/v623_v389_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v623: v389 Epistaxis ASSOC narrowed to I10 | source v389 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_uti; assoc=epistaxis_i10_narrow |
| 3 | `submissions/v623_v389_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v623: v389 Epistaxis ASSOC narrowed to I10 | source v389 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_uti; assoc=epistaxis_i10_narrow |
| 3 | `submissions/v623_v389_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v623: v389 Epistaxis ASSOC narrowed to I10 | source v389 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_uti; assoc=epistaxis_i10_narrow |
| 3 | `submissions/v623_v389_epi_i10_narrow.csv` | UTI | KEEP | 0 | 76 | v623: v389 Epistaxis ASSOC narrowed to I10 | source v389 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_uti; assoc=epistaxis_i10_narrow |
| 4 | `submissions/v624_v388_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v624: v388 Epistaxis ASSOC narrowed to I10 | source v388 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd; assoc=epistaxis_i10_narrow |
| 4 | `submissions/v624_v388_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v624: v388 Epistaxis ASSOC narrowed to I10 | source v388 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd; assoc=epistaxis_i10_narrow |
| 4 | `submissions/v624_v388_epi_i10_narrow.csv` | CKD | KEEP | 22 | 75 | v624: v388 Epistaxis ASSOC narrowed to I10 | source v388 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd; assoc=epistaxis_i10_narrow |
| 4 | `submissions/v624_v388_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v624: v388 Epistaxis ASSOC narrowed to I10 | source v388 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd; assoc=epistaxis_i10_narrow |
| 5 | `submissions/v625_v385_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v625: v385 Epistaxis ASSOC narrowed to I10 | source v385 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 5 | `submissions/v625_v385_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v625: v385 Epistaxis ASSOC narrowed to I10 | source v385 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 5 | `submissions/v625_v385_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v625: v385 Epistaxis ASSOC narrowed to I10 | source v385 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 5 | `submissions/v625_v385_epi_i10_narrow.csv` | Diabetes | KEEP | 232 | 13 | v625: v385 Epistaxis ASSOC narrowed to I10 | source v385 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 5 | `submissions/v625_v385_epi_i10_narrow.csv` | Pneumonia | KEEP | 1 | 28 | v625: v385 Epistaxis ASSOC narrowed to I10 | source v385 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 6 | `submissions/v626_v384_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v626: v384 Epistaxis ASSOC narrowed to I10 | source v384 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 6 | `submissions/v626_v384_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v626: v384 Epistaxis ASSOC narrowed to I10 | source v384 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 6 | `submissions/v626_v384_epi_i10_narrow.csv` | CKD | KEEP | 22 | 75 | v626: v384 Epistaxis ASSOC narrowed to I10 | source v384 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 6 | `submissions/v626_v384_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v626: v384 Epistaxis ASSOC narrowed to I10 | source v384 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 6 | `submissions/v626_v384_epi_i10_narrow.csv` | UTI | KEEP | 0 | 76 | v626: v384 Epistaxis ASSOC narrowed to I10 | source v384 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 7 | `submissions/v627_v382_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v627: v382 Epistaxis ASSOC narrowed to I10 | source v382 (0.43156, -0.00186 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10_narrow |
| 7 | `submissions/v627_v382_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v627: v382 Epistaxis ASSOC narrowed to I10 | source v382 (0.43156, -0.00186 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10_narrow |
| 7 | `submissions/v627_v382_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v627: v382 Epistaxis ASSOC narrowed to I10 | source v382 (0.43156, -0.00186 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10_narrow |
| 8 | `submissions/v628_v357_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v628: v357 Epistaxis ASSOC narrowed to I10 | source v357 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 8 | `submissions/v628_v357_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v628: v357 Epistaxis ASSOC narrowed to I10 | source v357 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 8 | `submissions/v628_v357_epi_i10_narrow.csv` | CKD | KEEP | 22 | 75 | v628: v357 Epistaxis ASSOC narrowed to I10 | source v357 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 8 | `submissions/v628_v357_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v628: v357 Epistaxis ASSOC narrowed to I10 | source v357 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 8 | `submissions/v628_v357_epi_i10_narrow.csv` | UTI | KEEP | 0 | 76 | v628: v357 Epistaxis ASSOC narrowed to I10 | source v357 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 8 | `submissions/v628_v357_epi_i10_narrow.csv` | Diabetes | KEEP | 232 | 13 | v628: v357 Epistaxis ASSOC narrowed to I10 | source v357 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 8 | `submissions/v628_v357_epi_i10_narrow.csv` | Pneumonia | KEEP | 1 | 28 | v628: v357 Epistaxis ASSOC narrowed to I10 | source v357 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Gout | ASSOCIATION | 17 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | CKD | ASSOCIATION | 17 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Diabetes | KEEP | 232 | 13 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Pneumonia | KEEP | 1 | 28 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 9 | `submissions/v629_v342_epi_i10_narrow.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v629: v342 Epistaxis ASSOC narrowed to I10 | source v342 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Gout | ASSOCIATION | 17 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | CKD | KEEP | 22 | 75 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | CKD | ASSOCIATION | 17 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | UTI | KEEP | 0 | 76 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 10 | `submissions/v630_v341_epi_i10_narrow.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v630: v341 Epistaxis ASSOC narrowed to I10 | source v341 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Gout | ASSOCIATION | 17 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | CKD | KEEP | 22 | 75 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | CKD | ASSOCIATION | 17 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | UTI | KEEP | 0 | 76 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Diabetes | KEEP | 232 | 13 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Pneumonia | KEEP | 1 | 28 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 11 | `submissions/v631_v302_epi_i10_narrow.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v631: v302 Epistaxis ASSOC narrowed to I10 | source v302 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Gout | ASSOCIATION | 17 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | CKD | KEEP | 22 | 75 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | CKD | ASSOCIATION | 17 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | UTI | KEEP | 0 | 76 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | UTI | ASSOCIATION | 20 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Diabetes | KEEP | 232 | 13 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Diabetes | ASSOCIATION | 116 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Pneumonia | KEEP | 1 | 28 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 12 | `submissions/v632_v301_epi_i10_narrow.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v632: v301 Epistaxis ASSOC narrowed to I10 | source v301 (0.43156, -0.00186 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow |
| 13 | `submissions/v633_v543_med_add_c37.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v633: v543 plus Mediastinum C37 | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 13 | `submissions/v633_v543_med_add_c37.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v633: v543 plus Mediastinum C37 | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 14 | `submissions/v634_v543_med_add_d384.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v634: v543 plus Mediastinum D384 | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 14 | `submissions/v634_v543_med_add_d384.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v634: v543 plus Mediastinum D384 | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 15 | `submissions/v635_v543_med_add_c771.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v635: v543 plus Mediastinum C771 | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 15 | `submissions/v635_v543_med_add_c771.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v635: v543 plus Mediastinum C771 | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 16 | `submissions/v636_v543_med_add_a154.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v636: v543 plus Mediastinum A154 | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 16 | `submissions/v636_v543_med_add_a154.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v636: v543 plus Mediastinum A154 | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 17 | `submissions/v637_v543_med_add_thymus_nodes.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v637: v543 plus Mediastinum thymus/nodes | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 17 | `submissions/v637_v543_med_add_thymus_nodes.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v637: v543 plus Mediastinum thymus/nodes | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=none; assoc=epistaxis_i10 |
| 18 | `submissions/v638_v543_med_c37_v185_ckd_uti.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v638: v543 plus C37 and v185 CKD/UTI KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10 |
| 18 | `submissions/v638_v543_med_c37_v185_ckd_uti.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v638: v543 plus C37 and v185 CKD/UTI KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10 |
| 18 | `submissions/v638_v543_med_c37_v185_ckd_uti.csv` | CKD | KEEP | 22 | 75 | v638: v543 plus C37 and v185 CKD/UTI KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10 |
| 18 | `submissions/v638_v543_med_c37_v185_ckd_uti.csv` | UTI | KEEP | 0 | 76 | v638: v543 plus C37 and v185 CKD/UTI KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10 |
| 19 | `submissions/v639_v543_med_c37_v185_diab_pneu.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v639: v543 plus C37 and v185 Diabetes/Pneumonia KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10 |
| 19 | `submissions/v639_v543_med_c37_v185_diab_pneu.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v639: v543 plus C37 and v185 Diabetes/Pneumonia KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10 |
| 19 | `submissions/v639_v543_med_c37_v185_diab_pneu.csv` | Diabetes | KEEP | 232 | 13 | v639: v543 plus C37 and v185 Diabetes/Pneumonia KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10 |
| 19 | `submissions/v639_v543_med_c37_v185_diab_pneu.csv` | Pneumonia | KEEP | 1 | 28 | v639: v543 plus C37 and v185 Diabetes/Pneumonia KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10 |
| 20 | `submissions/v640_v543_med_c37_v185keep.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v640: v543 plus C37 and v185 private KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10 |
| 20 | `submissions/v640_v543_med_c37_v185keep.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v640: v543 plus C37 and v185 private KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10 |
| 20 | `submissions/v640_v543_med_c37_v185keep.csv` | CKD | KEEP | 22 | 75 | v640: v543 plus C37 and v185 private KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10 |
| 20 | `submissions/v640_v543_med_c37_v185keep.csv` | UTI | KEEP | 0 | 76 | v640: v543 plus C37 and v185 private KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10 |
| 20 | `submissions/v640_v543_med_c37_v185keep.csv` | Diabetes | KEEP | 232 | 13 | v640: v543 plus C37 and v185 private KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10 |
| 20 | `submissions/v640_v543_med_c37_v185keep.csv` | Pneumonia | KEEP | 1 | 28 | v640: v543 plus C37 and v185 private KEEP | source v543 (0.43342, +0.00000 vs v543); med=keep; private_keep=v185keep; assoc=epistaxis_i10 |

## Exact Code Changes

### 1. `v621_v392_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v621: v392 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 1. `v621_v392_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v621: v392 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 1. `v621_v392_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v621: v392 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 1. `v621_v392_epi_i10_narrow.csv` - Pneumonia / KEEP

- Message: v621: v392 Epistaxis ASSOC narrowed to I10
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 2. `v622_v391_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v622: v391 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 2. `v622_v391_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v622: v391 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 2. `v622_v391_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v622: v391 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 2. `v622_v391_epi_i10_narrow.csv` - Diabetes / KEEP

- Message: v622: v391 Epistaxis ASSOC narrowed to I10
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 3. `v623_v389_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v623: v389 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 3. `v623_v389_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v623: v389 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 3. `v623_v389_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v623: v389 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 3. `v623_v389_epi_i10_narrow.csv` - UTI / KEEP

- Message: v623: v389 Epistaxis ASSOC narrowed to I10
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 4. `v624_v388_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v624: v388 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 4. `v624_v388_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v624: v388 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 4. `v624_v388_epi_i10_narrow.csv` - CKD / KEEP

- Message: v624: v388 Epistaxis ASSOC narrowed to I10
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 4. `v624_v388_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v624: v388 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 5. `v625_v385_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v625: v385 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 5. `v625_v385_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v625: v385 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 5. `v625_v385_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v625: v385 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 5. `v625_v385_epi_i10_narrow.csv` - Diabetes / KEEP

- Message: v625: v385 Epistaxis ASSOC narrowed to I10
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 5. `v625_v385_epi_i10_narrow.csv` - Pneumonia / KEEP

- Message: v625: v385 Epistaxis ASSOC narrowed to I10
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 6. `v626_v384_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v626: v384 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 6. `v626_v384_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v626: v384 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 6. `v626_v384_epi_i10_narrow.csv` - CKD / KEEP

- Message: v626: v384 Epistaxis ASSOC narrowed to I10
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 6. `v626_v384_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v626: v384 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 6. `v626_v384_epi_i10_narrow.csv` - UTI / KEEP

- Message: v626: v384 Epistaxis ASSOC narrowed to I10
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 7. `v627_v382_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v627: v382 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 7. `v627_v382_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v627: v382 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 7. `v627_v382_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v627: v382 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 8. `v628_v357_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v628: v357 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 8. `v628_v357_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v628: v357 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 8. `v628_v357_epi_i10_narrow.csv` - CKD / KEEP

- Message: v628: v357 Epistaxis ASSOC narrowed to I10
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 8. `v628_v357_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v628: v357 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 8. `v628_v357_epi_i10_narrow.csv` - UTI / KEEP

- Message: v628: v357 Epistaxis ASSOC narrowed to I10
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 8. `v628_v357_epi_i10_narrow.csv` - Diabetes / KEEP

- Message: v628: v357 Epistaxis ASSOC narrowed to I10
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 8. `v628_v357_epi_i10_narrow.csv` - Pneumonia / KEEP

- Message: v628: v357 Epistaxis ASSOC narrowed to I10
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 9. `v629_v342_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Gout / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Pleurisy / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Bronchitis / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Thyroiditis / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - CKD / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Hypothyroidism / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Heart Failure / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Diabetes / KEEP

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 9. `v629_v342_epi_i10_narrow.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Hyperthyroidism / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 9. `v629_v342_epi_i10_narrow.csv` - Pneumonia / KEEP

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 9. `v629_v342_epi_i10_narrow.csv` - Pneumonia / ASSOCIATION

- Message: v629: v342 Epistaxis ASSOC narrowed to I10
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Gout / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Pleurisy / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Bronchitis / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Thyroiditis / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - CKD / KEEP

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 10. `v630_v341_epi_i10_narrow.csv` - CKD / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Hypothyroidism / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Heart Failure / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - UTI / KEEP

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 10. `v630_v341_epi_i10_narrow.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Hyperthyroidism / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 10. `v630_v341_epi_i10_narrow.csv` - Pneumonia / ASSOCIATION

- Message: v630: v341 Epistaxis ASSOC narrowed to I10
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Gout / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Pleurisy / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Bronchitis / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Thyroiditis / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - CKD / KEEP

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 11. `v631_v302_epi_i10_narrow.csv` - CKD / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Hypothyroidism / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Heart Failure / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - UTI / KEEP

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 11. `v631_v302_epi_i10_narrow.csv` - Diabetes / KEEP

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 11. `v631_v302_epi_i10_narrow.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Hyperthyroidism / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 11. `v631_v302_epi_i10_narrow.csv` - Pneumonia / KEEP

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 11. `v631_v302_epi_i10_narrow.csv` - Pneumonia / ASSOCIATION

- Message: v631: v302 Epistaxis ASSOC narrowed to I10
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Epistaxis / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Intracranial Pressure / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Enlarged Mediastinum / KEEP

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Gout / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Dermatomycosis / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Pleurisy / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Bronchitis / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Thyroiditis / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - CKD / KEEP

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 12. `v632_v301_epi_i10_narrow.csv` - CKD / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Hypothyroidism / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Hematemesis / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Heart Failure / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - UTI / KEEP

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 12. `v632_v301_epi_i10_narrow.csv` - UTI / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Diabetes / KEEP

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 12. `v632_v301_epi_i10_narrow.csv` - Diabetes / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Hyperthyroidism / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 12. `v632_v301_epi_i10_narrow.csv` - Pneumonia / KEEP

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 12. `v632_v301_epi_i10_narrow.csv` - Pneumonia / ASSOCIATION

- Message: v632: v301 Epistaxis ASSOC narrowed to I10
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 13. `v633_v543_med_add_c37.csv` - Epistaxis / ASSOCIATION

- Message: v633: v543 plus Mediastinum C37
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 13. `v633_v543_med_add_c37.csv` - Enlarged Mediastinum / KEEP

- Message: v633: v543 plus Mediastinum C37
- Added (1): `C37` - Malignant neoplasm of thymus
- Removed (0): none

### 14. `v634_v543_med_add_d384.csv` - Epistaxis / ASSOCIATION

- Message: v634: v543 plus Mediastinum D384
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 14. `v634_v543_med_add_d384.csv` - Enlarged Mediastinum / KEEP

- Message: v634: v543 plus Mediastinum D384
- Added (1): `D384` - Neoplasm of uncertain behavior of thymus
- Removed (0): none

### 15. `v635_v543_med_add_c771.csv` - Epistaxis / ASSOCIATION

- Message: v635: v543 plus Mediastinum C771
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 15. `v635_v543_med_add_c771.csv` - Enlarged Mediastinum / KEEP

- Message: v635: v543 plus Mediastinum C771
- Added (1): `C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes
- Removed (0): none

### 16. `v636_v543_med_add_a154.csv` - Epistaxis / ASSOCIATION

- Message: v636: v543 plus Mediastinum A154
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 16. `v636_v543_med_add_a154.csv` - Enlarged Mediastinum / KEEP

- Message: v636: v543 plus Mediastinum A154
- Added (1): `A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 17. `v637_v543_med_add_thymus_nodes.csv` - Epistaxis / ASSOCIATION

- Message: v637: v543 plus Mediastinum thymus/nodes
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 17. `v637_v543_med_add_thymus_nodes.csv` - Enlarged Mediastinum / KEEP

- Message: v637: v543 plus Mediastinum thymus/nodes
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 18. `v638_v543_med_c37_v185_ckd_uti.csv` - Epistaxis / ASSOCIATION

- Message: v638: v543 plus C37 and v185 CKD/UTI KEEP
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 18. `v638_v543_med_c37_v185_ckd_uti.csv` - Enlarged Mediastinum / KEEP

- Message: v638: v543 plus C37 and v185 CKD/UTI KEEP
- Added (1): `C37` - Malignant neoplasm of thymus
- Removed (0): none

### 18. `v638_v543_med_c37_v185_ckd_uti.csv` - CKD / KEEP

- Message: v638: v543 plus C37 and v185 CKD/UTI KEEP
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 18. `v638_v543_med_c37_v185_ckd_uti.csv` - UTI / KEEP

- Message: v638: v543 plus C37 and v185 CKD/UTI KEEP
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 19. `v639_v543_med_c37_v185_diab_pneu.csv` - Epistaxis / ASSOCIATION

- Message: v639: v543 plus C37 and v185 Diabetes/Pneumonia KEEP
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 19. `v639_v543_med_c37_v185_diab_pneu.csv` - Enlarged Mediastinum / KEEP

- Message: v639: v543 plus C37 and v185 Diabetes/Pneumonia KEEP
- Added (1): `C37` - Malignant neoplasm of thymus
- Removed (0): none

### 19. `v639_v543_med_c37_v185_diab_pneu.csv` - Diabetes / KEEP

- Message: v639: v543 plus C37 and v185 Diabetes/Pneumonia KEEP
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 19. `v639_v543_med_c37_v185_diab_pneu.csv` - Pneumonia / KEEP

- Message: v639: v543 plus C37 and v185 Diabetes/Pneumonia KEEP
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 20. `v640_v543_med_c37_v185keep.csv` - Epistaxis / ASSOCIATION

- Message: v640: v543 plus C37 and v185 private KEEP
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 20. `v640_v543_med_c37_v185keep.csv` - Enlarged Mediastinum / KEEP

- Message: v640: v543 plus C37 and v185 private KEEP
- Added (1): `C37` - Malignant neoplasm of thymus
- Removed (0): none

### 20. `v640_v543_med_c37_v185keep.csv` - CKD / KEEP

- Message: v640: v543 plus C37 and v185 private KEEP
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 20. `v640_v543_med_c37_v185keep.csv` - UTI / KEEP

- Message: v640: v543 plus C37 and v185 private KEEP
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 20. `v640_v543_med_c37_v185keep.csv` - Diabetes / KEEP

- Message: v640: v543 plus C37 and v185 private KEEP
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 20. `v640_v543_med_c37_v185keep.csv` - Pneumonia / KEEP

- Message: v640: v543 plus C37 and v185 private KEEP
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more
