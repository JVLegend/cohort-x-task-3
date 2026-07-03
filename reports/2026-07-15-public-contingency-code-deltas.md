# CohortX Plan Code Deltas - 2026-07-15-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-15-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 74
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v761_v296_portfolio_renal_metabolic_obstetric_prune.csv` | CKD | KEEP | 0 | 43 | v761: v296 renal/metabolic obstetric KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 1 | `submissions/v761_v296_portfolio_renal_metabolic_obstetric_prune.csv` | UTI | KEEP | 0 | 29 | v761: v296 renal/metabolic obstetric KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 1 | `submissions/v761_v296_portfolio_renal_metabolic_obstetric_prune.csv` | Diabetes | KEEP | 0 | 57 | v761: v296 renal/metabolic obstetric KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 2 | `submissions/v762_v296_portfolio_cardio_pulm_noise_prune.csv` | CKD | KEEP | 0 | 3 | v762: v296 cardio/pulm procedural KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 2 | `submissions/v762_v296_portfolio_cardio_pulm_noise_prune.csv` | Heart Failure | KEEP | 0 | 31 | v762: v296 cardio/pulm procedural KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 2 | `submissions/v762_v296_portfolio_cardio_pulm_noise_prune.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v762: v296 cardio/pulm procedural KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 3 | `submissions/v763_v296_portfolio_thyroid_axis_prune.csv` | Thyroiditis | KEEP | 0 | 2 | v763: v296 thyroid-axis KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 3 | `submissions/v763_v296_portfolio_thyroid_axis_prune.csv` | Hypothyroidism | KEEP | 0 | 6 | v763: v296 thyroid-axis KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 3 | `submissions/v763_v296_portfolio_thyroid_axis_prune.csv` | Hyperthyroidism | KEEP | 0 | 12 | v763: v296 thyroid-axis KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 4 | `submissions/v764_v296_portfolio_respiratory_noise_prune.csv` | Pleurisy | KEEP | 0 | 12 | v764: v296 respiratory-noise KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 4 | `submissions/v764_v296_portfolio_respiratory_noise_prune.csv` | Bronchitis | KEEP | 0 | 8 | v764: v296 respiratory-noise KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 4 | `submissions/v764_v296_portfolio_respiratory_noise_prune.csv` | Pneumonia | KEEP | 0 | 30 | v764: v296 respiratory-noise KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 5 | `submissions/v765_v296_portfolio_gi_gu_skin_prune.csv` | Dermatomycosis | KEEP | 0 | 21 | v765: v296 GI/GU/skin false-positive KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 5 | `submissions/v765_v296_portfolio_gi_gu_skin_prune.csv` | Hematemesis | KEEP | 0 | 4 | v765: v296 GI/GU/skin false-positive KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 5 | `submissions/v765_v296_portfolio_gi_gu_skin_prune.csv` | UTI | KEEP | 0 | 3 | v765: v296 GI/GU/skin false-positive KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 6 | `submissions/v766_v296_portfolio_ent_skin_endocrine_prune.csv` | Dermatomycosis | KEEP | 0 | 21 | v766: v296 ENT/skin/endocrine KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 6 | `submissions/v766_v296_portfolio_ent_skin_endocrine_prune.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 18 | v766: v296 ENT/skin/endocrine KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 6 | `submissions/v766_v296_portfolio_ent_skin_endocrine_prune.csv` | Hypergonadism | KEEP | 0 | 11 | v766: v296 ENT/skin/endocrine KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 7 | `submissions/v767_v296_portfolio_ckd_diabetes_full_prune.csv` | CKD | KEEP | 0 | 46 | v767: v296 CKD+Diabetes KEEP precision prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 7 | `submissions/v767_v296_portfolio_ckd_diabetes_full_prune.csv` | Diabetes | KEEP | 0 | 66 | v767: v296 CKD+Diabetes KEEP precision prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 8 | `submissions/v768_v296_portfolio_uti_diabetes_obstetric_prune.csv` | UTI | KEEP | 0 | 32 | v768: v296 UTI+Diabetes obstetric/GU KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 8 | `submissions/v768_v296_portfolio_uti_diabetes_obstetric_prune.csv` | Diabetes | KEEP | 0 | 57 | v768: v296 UTI+Diabetes obstetric/GU KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 9 | `submissions/v769_v296_portfolio_endocrine_small_prune.csv` | Hypothyroidism | KEEP | 0 | 6 | v769: v296 endocrine KEEP precision prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 9 | `submissions/v769_v296_portfolio_endocrine_small_prune.csv` | Hypoparathyroidism | KEEP | 0 | 8 | v769: v296 endocrine KEEP precision prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 9 | `submissions/v769_v296_portfolio_endocrine_small_prune.csv` | Hyperthyroidism | KEEP | 0 | 12 | v769: v296 endocrine KEEP precision prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 10 | `submissions/v770_v296_portfolio_neuro_cardioresp_prune.csv` | Intracranial Pressure | KEEP | 0 | 4 | v770: v296 neuro/cardioresp KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 10 | `submissions/v770_v296_portfolio_neuro_cardioresp_prune.csv` | Pleurisy | KEEP | 0 | 12 | v770: v296 neuro/cardioresp KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 10 | `submissions/v770_v296_portfolio_neuro_cardioresp_prune.csv` | Heart Failure | KEEP | 0 | 31 | v770: v296 neuro/cardioresp KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 11 | `submissions/v771_v296_portfolio_lower_resp_precision_prune.csv` | Bronchitis | KEEP | 0 | 8 | v771: v296 lower-respiratory KEEP precision prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 11 | `submissions/v771_v296_portfolio_lower_resp_precision_prune.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v771: v296 lower-respiratory KEEP precision prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 11 | `submissions/v771_v296_portfolio_lower_resp_precision_prune.csv` | Pneumonia | KEEP | 0 | 30 | v771: v296 lower-respiratory KEEP precision prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 12 | `submissions/v772_v296_portfolio_bleed_pleura_bronch_prune.csv` | Pleurisy | KEEP | 0 | 12 | v772: v296 bleed/pleura/bronchitis KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 12 | `submissions/v772_v296_portfolio_bleed_pleura_bronch_prune.csv` | Bronchitis | KEEP | 0 | 8 | v772: v296 bleed/pleura/bronchitis KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 12 | `submissions/v772_v296_portfolio_bleed_pleura_bronch_prune.csv` | Hematemesis | KEEP | 0 | 4 | v772: v296 bleed/pleura/bronchitis KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 13 | `submissions/v773_v296_portfolio_ent_thyroid_prune.csv` | Thyroiditis | KEEP | 0 | 2 | v773: v296 ENT+thyroid KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 13 | `submissions/v773_v296_portfolio_ent_thyroid_prune.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 18 | v773: v296 ENT+thyroid KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 13 | `submissions/v773_v296_portfolio_ent_thyroid_prune.csv` | Hypothyroidism | KEEP | 0 | 6 | v773: v296 ENT+thyroid KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 14 | `submissions/v774_v296_portfolio_gout_ckd_prune.csv` | Gout | KEEP | 0 | 2 | v774: v296 Gout+CKD KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 14 | `submissions/v774_v296_portfolio_gout_ckd_prune.csv` | CKD | KEEP | 0 | 46 | v774: v296 Gout+CKD KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 15 | `submissions/v775_v296_portfolio_obstetric_metabolic_renal_prune.csv` | CKD | KEEP | 0 | 43 | v775: v296 obstetric/metabolic/renal KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 15 | `submissions/v775_v296_portfolio_obstetric_metabolic_renal_prune.csv` | UTI | KEEP | 0 | 29 | v775: v296 obstetric/metabolic/renal KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 15 | `submissions/v775_v296_portfolio_obstetric_metabolic_renal_prune.csv` | Diabetes | KEEP | 0 | 66 | v775: v296 obstetric/metabolic/renal KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 16 | `submissions/v776_v296_portfolio_hf_ckd_pneumonia_prune.csv` | CKD | KEEP | 0 | 3 | v776: v296 HF+CKD+Pneumonia KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 16 | `submissions/v776_v296_portfolio_hf_ckd_pneumonia_prune.csv` | Heart Failure | KEEP | 0 | 31 | v776: v296 HF+CKD+Pneumonia KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 16 | `submissions/v776_v296_portfolio_hf_ckd_pneumonia_prune.csv` | Pneumonia | KEEP | 0 | 30 | v776: v296 HF+CKD+Pneumonia KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 17 | `submissions/v777_v296_portfolio_derm_uti_diabetes_prune.csv` | Dermatomycosis | KEEP | 0 | 21 | v777: v296 Derm+UTI+Diabetes KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 17 | `submissions/v777_v296_portfolio_derm_uti_diabetes_prune.csv` | UTI | KEEP | 0 | 3 | v777: v296 Derm+UTI+Diabetes KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 17 | `submissions/v777_v296_portfolio_derm_uti_diabetes_prune.csv` | Diabetes | KEEP | 0 | 9 | v777: v296 Derm+UTI+Diabetes KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 18 | `submissions/v778_v296_portfolio_neuro_endocrine_prune.csv` | Intracranial Pressure | KEEP | 0 | 4 | v778: v296 neuro+endocrine KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 18 | `submissions/v778_v296_portfolio_neuro_endocrine_prune.csv` | Hypoparathyroidism | KEEP | 0 | 8 | v778: v296 neuro+endocrine KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 18 | `submissions/v778_v296_portfolio_neuro_endocrine_prune.csv` | Hyperthyroidism | KEEP | 0 | 12 | v778: v296 neuro+endocrine KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 19 | `submissions/v779_v296_portfolio_small_high_precision_prune.csv` | Gout | KEEP | 0 | 2 | v779: v296 small high-precision KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 19 | `submissions/v779_v296_portfolio_small_high_precision_prune.csv` | CKD | KEEP | 0 | 3 | v779: v296 small high-precision KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 19 | `submissions/v779_v296_portfolio_small_high_precision_prune.csv` | Hematemesis | KEEP | 0 | 4 | v779: v296 small high-precision KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 19 | `submissions/v779_v296_portfolio_small_high_precision_prune.csv` | Heart Failure | KEEP | 0 | 31 | v779: v296 small high-precision KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 19 | `submissions/v779_v296_portfolio_small_high_precision_prune.csv` | UTI | KEEP | 0 | 3 | v779: v296 small high-precision KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 19 | `submissions/v779_v296_portfolio_small_high_precision_prune.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v779: v296 small high-precision KEEP prune | intentional multi-condition private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Intracranial Pressure | KEEP | 0 | 4 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Gout | KEEP | 0 | 2 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Dermatomycosis | KEEP | 0 | 21 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Pleurisy | KEEP | 0 | 12 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Bronchitis | KEEP | 0 | 8 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Thyroiditis | KEEP | 0 | 2 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 18 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | CKD | KEEP | 0 | 46 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Hypothyroidism | KEEP | 0 | 6 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Hematemesis | KEEP | 0 | 4 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Heart Failure | KEEP | 0 | 31 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | UTI | KEEP | 0 | 32 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Diabetes | KEEP | 0 | 66 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Hypoparathyroidism | KEEP | 0 | 8 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Hyperthyroidism | KEEP | 0 | 12 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |
| 20 | `submissions/v780_v296_portfolio_broad_private_prune.csv` | Pneumonia | KEEP | 0 | 30 | v780: v296 broad private KEEP prune | intentional broad private KEEP-prune portfolio; ASSOC/DIFF kept empty |

## Exact Code Changes

### 1. `v761_v296_portfolio_renal_metabolic_obstetric_prune.csv` - CKD / KEEP

- Message: v761: v296 renal/metabolic obstetric KEEP prune
- Added (0): none
- Removed (43): `Q60` - Renal agenesis and other reduction defects of kidney<br>`Q600` - Renal agenesis, unilateral<br>`Q601` - Renal agenesis, bilateral<br>`Q602` - Renal agenesis, unspecified<br>`Q603` - Renal hypoplasia, unilateral<br>`Q604` - Renal hypoplasia, bilateral<br>`Q605` - Renal hypoplasia, unspecified<br>`Q606` - Potter's syndrome<br>`Q61` - Cystic kidney disease<br>`Q610` - Congenital renal cyst<br>`Q6100` - Congenital renal cyst, unspecified<br>`Q6101` - Congenital single renal cyst<br>`Q6102` - Congenital multiple renal cysts<br>`Q611` - Polycystic kidney, infantile type<br>`Q6111` - Cystic dilatation of collecting ducts<br>`Q6119` - Other polycystic kidney, infantile type<br>`Q612` - Polycystic kidney, adult type<br>`Q613` - Polycystic kidney, unspecified<br>... +25 more

### 1. `v761_v296_portfolio_renal_metabolic_obstetric_prune.csv` - UTI / KEEP

- Message: v761: v296 renal/metabolic obstetric KEEP prune
- Added (0): none
- Removed (29): `O03` - Spontaneous abortion<br>`O0338` - Urinary tract infection following incomplete spontaneous abortion<br>`O0388` - Urinary tract infection following complete or unspecified spontaneous abortion<br>`O23` - Infections of genitourinary tract in pregnancy<br>`O233` - Infections of other parts of urinary tract in pregnancy<br>`O2330` - Infections of other parts of urinary tract in pregnancy, unspecified trimester<br>`O2332` - Infections of other parts of urinary tract in pregnancy, second trimester<br>`O234` - Unspecified infection of urinary tract in pregnancy<br>`O2340` - Unspecified infection of urinary tract in pregnancy, unspecified trimester<br>`O2341` - Unspecified infection of urinary tract in pregnancy, first trimester<br>`O2342` - Unspecified infection of urinary tract in pregnancy, second trimester<br>`O2343` - Unspecified infection of urinary tract in pregnancy, third trimester<br>`O239` - Unspecified genitourinary tract infection in pregnancy<br>`O2390` - Unspecified genitourinary tract infection in pregnancy, unspecified trimester<br>`O2391` - Unspecified genitourinary tract infection in pregnancy, first trimester<br>`O2392` - Unspecified genitourinary tract infection in pregnancy, second trimester<br>`O2393` - Unspecified genitourinary tract infection in pregnancy, third trimester<br>`O86` - Other puerperal infections<br>... +11 more

### 1. `v761_v296_portfolio_renal_metabolic_obstetric_prune.csv` - Diabetes / KEEP

- Message: v761: v296 renal/metabolic obstetric KEEP prune
- Added (0): none
- Removed (57): `O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2412` - Pre-existing type 2 diabetes mellitus, in childbirth<br>`O2413` - Pre-existing type 2 diabetes mellitus, in the puerperium<br>`O243` - Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium<br>... +39 more

### 2. `v762_v296_portfolio_cardio_pulm_noise_prune.csv` - CKD / KEEP

- Message: v762: v296 cardio/pulm procedural KEEP prune
- Added (0): none
- Removed (3): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure

### 2. `v762_v296_portfolio_cardio_pulm_noise_prune.csv` - Heart Failure / KEEP

- Message: v762: v296 cardio/pulm procedural KEEP prune
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 2. `v762_v296_portfolio_cardio_pulm_noise_prune.csv` - Interstitial Lung Disease / KEEP

- Message: v762: v296 cardio/pulm procedural KEEP prune
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 3. `v763_v296_portfolio_thyroid_axis_prune.csv` - Thyroiditis / KEEP

- Message: v763: v296 thyroid-axis KEEP prune
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 3. `v763_v296_portfolio_thyroid_axis_prune.csv` - Hypothyroidism / KEEP

- Message: v763: v296 thyroid-axis KEEP prune
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 3. `v763_v296_portfolio_thyroid_axis_prune.csv` - Hyperthyroidism / KEEP

- Message: v763: v296 thyroid-axis KEEP prune
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 4. `v764_v296_portfolio_respiratory_noise_prune.csv` - Pleurisy / KEEP

- Message: v764: v296 respiratory-noise KEEP prune
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 4. `v764_v296_portfolio_respiratory_noise_prune.csv` - Bronchitis / KEEP

- Message: v764: v296 respiratory-noise KEEP prune
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 4. `v764_v296_portfolio_respiratory_noise_prune.csv` - Pneumonia / KEEP

- Message: v764: v296 respiratory-noise KEEP prune
- Added (0): none
- Removed (30): `A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`J84` - Other interstitial pulmonary diseases<br>`J8411` - Idiopathic interstitial pneumonia<br>`J84111` - Idiopathic interstitial pneumonia, not otherwise specified<br>`J84116` - Cryptogenic organizing pneumonia<br>`J84117` - Desquamative interstitial pneumonia<br>`J842` - Lymphoid interstitial pneumonia<br>`J85` - Abscess of lung and mediastinum<br>`J850` - Gangrene and necrosis of lung<br>`J851` - Abscess of lung with pneumonia<br>... +12 more
### 5. `v765_v296_portfolio_gi_gu_skin_prune.csv` - Dermatomycosis / KEEP

- Message: v765: v296 GI/GU/skin false-positive KEEP prune
- Added (0): none
- Removed (21): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +3 more

### 5. `v765_v296_portfolio_gi_gu_skin_prune.csv` - Hematemesis / KEEP

- Message: v765: v296 GI/GU/skin false-positive KEEP prune
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 5. `v765_v296_portfolio_gi_gu_skin_prune.csv` - UTI / KEEP

- Message: v765: v296 GI/GU/skin false-positive KEEP prune
- Added (0): none
- Removed (3): `N35` - Urethral stricture<br>`N35819` - Other urethral stricture, male, unspecified site<br>`N35919` - Unspecified urethral stricture, male, unspecified site

### 6. `v766_v296_portfolio_ent_skin_endocrine_prune.csv` - Dermatomycosis / KEEP

- Message: v766: v296 ENT/skin/endocrine KEEP prune
- Added (0): none
- Removed (21): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +3 more

### 6. `v766_v296_portfolio_ent_skin_endocrine_prune.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v766: v296 ENT/skin/endocrine KEEP prune
- Added (0): none
- Removed (18): `C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`D00` - Carcinoma in situ of oral cavity, esophagus and stomach<br>`D000` - Carcinoma in situ of lip, oral cavity and pharynx<br>`D0000` - Carcinoma in situ of oral cavity, unspecified site<br>`D0001` - Carcinoma in situ of labial mucosa and vermilion border<br>`D0002` - Carcinoma in situ of buccal mucosa<br>`D0003` - Carcinoma in situ of gingiva and edentulous alveolar ridge<br>`D0004` - Carcinoma in situ of soft palate<br>`D0005` - Carcinoma in situ of hard palate<br>`D0006` - Carcinoma in situ of floor of mouth<br>`D0007` - Carcinoma in situ of tongue<br>`D0008` - Carcinoma in situ of pharynx<br>`D10` - Benign neoplasm of mouth and pharynx<br>`D101` - Benign neoplasm of tongue<br>`D106` - Benign neoplasm of nasopharynx<br>`D107` - Benign neoplasm of hypopharynx

### 6. `v766_v296_portfolio_ent_skin_endocrine_prune.csv` - Hypergonadism / KEEP

- Message: v766: v296 ENT/skin/endocrine KEEP prune
- Added (0): none
- Removed (11): `E27` - Other disorders of adrenal gland<br>`E270` - Other adrenocortical overactivity<br>`E271` - Primary adrenocortical insufficiency<br>`E272` - Addisonian crisis<br>`E273` - Drug-induced adrenocortical insufficiency<br>`E274` - Other and unspecified adrenocortical insufficiency<br>`E2740` - Unspecified adrenocortical insufficiency<br>`E2749` - Other adrenocortical insufficiency<br>`E275` - Adrenomedullary hyperfunction<br>`E278` - Other specified disorders of adrenal gland<br>`E279` - Disorder of adrenal gland, unspecified

### 7. `v767_v296_portfolio_ckd_diabetes_full_prune.csv` - CKD / KEEP

- Message: v767: v296 CKD+Diabetes KEEP precision prune
- Added (0): none
- Removed (46): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`Q60` - Renal agenesis and other reduction defects of kidney<br>`Q600` - Renal agenesis, unilateral<br>`Q601` - Renal agenesis, bilateral<br>`Q602` - Renal agenesis, unspecified<br>`Q603` - Renal hypoplasia, unilateral<br>`Q604` - Renal hypoplasia, bilateral<br>`Q605` - Renal hypoplasia, unspecified<br>`Q606` - Potter's syndrome<br>`Q61` - Cystic kidney disease<br>`Q610` - Congenital renal cyst<br>`Q6100` - Congenital renal cyst, unspecified<br>`Q6101` - Congenital single renal cyst<br>`Q6102` - Congenital multiple renal cysts<br>`Q611` - Polycystic kidney, infantile type<br>`Q6111` - Cystic dilatation of collecting ducts<br>... +28 more

### 7. `v767_v296_portfolio_ckd_diabetes_full_prune.csv` - Diabetes / KEEP

- Message: v767: v296 CKD+Diabetes KEEP precision prune
- Added (0): none
- Removed (66): `O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2412` - Pre-existing type 2 diabetes mellitus, in childbirth<br>`O2413` - Pre-existing type 2 diabetes mellitus, in the puerperium<br>`O243` - Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium<br>... +48 more

### 8. `v768_v296_portfolio_uti_diabetes_obstetric_prune.csv` - UTI / KEEP

- Message: v768: v296 UTI+Diabetes obstetric/GU KEEP prune
- Added (0): none
- Removed (32): `N35` - Urethral stricture<br>`N35819` - Other urethral stricture, male, unspecified site<br>`N35919` - Unspecified urethral stricture, male, unspecified site<br>`O03` - Spontaneous abortion<br>`O0338` - Urinary tract infection following incomplete spontaneous abortion<br>`O0388` - Urinary tract infection following complete or unspecified spontaneous abortion<br>`O23` - Infections of genitourinary tract in pregnancy<br>`O233` - Infections of other parts of urinary tract in pregnancy<br>`O2330` - Infections of other parts of urinary tract in pregnancy, unspecified trimester<br>`O2332` - Infections of other parts of urinary tract in pregnancy, second trimester<br>`O234` - Unspecified infection of urinary tract in pregnancy<br>`O2340` - Unspecified infection of urinary tract in pregnancy, unspecified trimester<br>`O2341` - Unspecified infection of urinary tract in pregnancy, first trimester<br>`O2342` - Unspecified infection of urinary tract in pregnancy, second trimester<br>`O2343` - Unspecified infection of urinary tract in pregnancy, third trimester<br>`O239` - Unspecified genitourinary tract infection in pregnancy<br>`O2390` - Unspecified genitourinary tract infection in pregnancy, unspecified trimester<br>`O2391` - Unspecified genitourinary tract infection in pregnancy, first trimester<br>... +14 more

### 8. `v768_v296_portfolio_uti_diabetes_obstetric_prune.csv` - Diabetes / KEEP

- Message: v768: v296 UTI+Diabetes obstetric/GU KEEP prune
- Added (0): none
- Removed (57): `O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2412` - Pre-existing type 2 diabetes mellitus, in childbirth<br>`O2413` - Pre-existing type 2 diabetes mellitus, in the puerperium<br>`O243` - Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium<br>... +39 more

### 9. `v769_v296_portfolio_endocrine_small_prune.csv` - Hypothyroidism / KEEP

- Message: v769: v296 endocrine KEEP precision prune
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 9. `v769_v296_portfolio_endocrine_small_prune.csv` - Hypoparathyroidism / KEEP

- Message: v769: v296 endocrine KEEP precision prune
- Added (0): none
- Removed (8): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E230` - Hypopituitarism<br>`E231` - Drug-induced hypopituitarism<br>`E87` - Other disorders of fluid, electrolyte and acid-base balance<br>`E876` - Hypokalemia<br>`P71` - Transitory neonatal disorders of calcium and magnesium metabolism<br>`P714` - Transitory neonatal hypoparathyroidism

### 9. `v769_v296_portfolio_endocrine_small_prune.csv` - Hyperthyroidism / KEEP

- Message: v769: v296 endocrine KEEP precision prune
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 10. `v770_v296_portfolio_neuro_cardioresp_prune.csv` - Intracranial Pressure / KEEP

- Message: v770: v296 neuro/cardioresp KEEP prune
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 10. `v770_v296_portfolio_neuro_cardioresp_prune.csv` - Pleurisy / KEEP

- Message: v770: v296 neuro/cardioresp KEEP prune
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 10. `v770_v296_portfolio_neuro_cardioresp_prune.csv` - Heart Failure / KEEP

- Message: v770: v296 neuro/cardioresp KEEP prune
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 11. `v771_v296_portfolio_lower_resp_precision_prune.csv` - Bronchitis / KEEP

- Message: v771: v296 lower-respiratory KEEP precision prune
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 11. `v771_v296_portfolio_lower_resp_precision_prune.csv` - Interstitial Lung Disease / KEEP

- Message: v771: v296 lower-respiratory KEEP precision prune
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 11. `v771_v296_portfolio_lower_resp_precision_prune.csv` - Pneumonia / KEEP

- Message: v771: v296 lower-respiratory KEEP precision prune
- Added (0): none
- Removed (30): `A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`J84` - Other interstitial pulmonary diseases<br>`J8411` - Idiopathic interstitial pneumonia<br>`J84111` - Idiopathic interstitial pneumonia, not otherwise specified<br>`J84116` - Cryptogenic organizing pneumonia<br>`J84117` - Desquamative interstitial pneumonia<br>`J842` - Lymphoid interstitial pneumonia<br>`J85` - Abscess of lung and mediastinum<br>`J850` - Gangrene and necrosis of lung<br>`J851` - Abscess of lung with pneumonia<br>... +12 more

### 12. `v772_v296_portfolio_bleed_pleura_bronch_prune.csv` - Pleurisy / KEEP

- Message: v772: v296 bleed/pleura/bronchitis KEEP prune
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 12. `v772_v296_portfolio_bleed_pleura_bronch_prune.csv` - Bronchitis / KEEP

- Message: v772: v296 bleed/pleura/bronchitis KEEP prune
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 12. `v772_v296_portfolio_bleed_pleura_bronch_prune.csv` - Hematemesis / KEEP

- Message: v772: v296 bleed/pleura/bronchitis KEEP prune
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 13. `v773_v296_portfolio_ent_thyroid_prune.csv` - Thyroiditis / KEEP

- Message: v773: v296 ENT+thyroid KEEP prune
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 13. `v773_v296_portfolio_ent_thyroid_prune.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v773: v296 ENT+thyroid KEEP prune
- Added (0): none
- Removed (18): `C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`D00` - Carcinoma in situ of oral cavity, esophagus and stomach<br>`D000` - Carcinoma in situ of lip, oral cavity and pharynx<br>`D0000` - Carcinoma in situ of oral cavity, unspecified site<br>`D0001` - Carcinoma in situ of labial mucosa and vermilion border<br>`D0002` - Carcinoma in situ of buccal mucosa<br>`D0003` - Carcinoma in situ of gingiva and edentulous alveolar ridge<br>`D0004` - Carcinoma in situ of soft palate<br>`D0005` - Carcinoma in situ of hard palate<br>`D0006` - Carcinoma in situ of floor of mouth<br>`D0007` - Carcinoma in situ of tongue<br>`D0008` - Carcinoma in situ of pharynx<br>`D10` - Benign neoplasm of mouth and pharynx<br>`D101` - Benign neoplasm of tongue<br>`D106` - Benign neoplasm of nasopharynx<br>`D107` - Benign neoplasm of hypopharynx

### 13. `v773_v296_portfolio_ent_thyroid_prune.csv` - Hypothyroidism / KEEP

- Message: v773: v296 ENT+thyroid KEEP prune
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 14. `v774_v296_portfolio_gout_ckd_prune.csv` - Gout / KEEP

- Message: v774: v296 Gout+CKD KEEP prune
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 14. `v774_v296_portfolio_gout_ckd_prune.csv` - CKD / KEEP

- Message: v774: v296 Gout+CKD KEEP prune
- Added (0): none
- Removed (46): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`Q60` - Renal agenesis and other reduction defects of kidney<br>`Q600` - Renal agenesis, unilateral<br>`Q601` - Renal agenesis, bilateral<br>`Q602` - Renal agenesis, unspecified<br>`Q603` - Renal hypoplasia, unilateral<br>`Q604` - Renal hypoplasia, bilateral<br>`Q605` - Renal hypoplasia, unspecified<br>`Q606` - Potter's syndrome<br>`Q61` - Cystic kidney disease<br>`Q610` - Congenital renal cyst<br>`Q6100` - Congenital renal cyst, unspecified<br>`Q6101` - Congenital single renal cyst<br>`Q6102` - Congenital multiple renal cysts<br>`Q611` - Polycystic kidney, infantile type<br>`Q6111` - Cystic dilatation of collecting ducts<br>... +28 more

### 15. `v775_v296_portfolio_obstetric_metabolic_renal_prune.csv` - CKD / KEEP

- Message: v775: v296 obstetric/metabolic/renal KEEP prune
- Added (0): none
- Removed (43): `Q60` - Renal agenesis and other reduction defects of kidney<br>`Q600` - Renal agenesis, unilateral<br>`Q601` - Renal agenesis, bilateral<br>`Q602` - Renal agenesis, unspecified<br>`Q603` - Renal hypoplasia, unilateral<br>`Q604` - Renal hypoplasia, bilateral<br>`Q605` - Renal hypoplasia, unspecified<br>`Q606` - Potter's syndrome<br>`Q61` - Cystic kidney disease<br>`Q610` - Congenital renal cyst<br>`Q6100` - Congenital renal cyst, unspecified<br>`Q6101` - Congenital single renal cyst<br>`Q6102` - Congenital multiple renal cysts<br>`Q611` - Polycystic kidney, infantile type<br>`Q6111` - Cystic dilatation of collecting ducts<br>`Q6119` - Other polycystic kidney, infantile type<br>`Q612` - Polycystic kidney, adult type<br>`Q613` - Polycystic kidney, unspecified<br>... +25 more

### 15. `v775_v296_portfolio_obstetric_metabolic_renal_prune.csv` - UTI / KEEP

- Message: v775: v296 obstetric/metabolic/renal KEEP prune
- Added (0): none
- Removed (29): `O03` - Spontaneous abortion<br>`O0338` - Urinary tract infection following incomplete spontaneous abortion<br>`O0388` - Urinary tract infection following complete or unspecified spontaneous abortion<br>`O23` - Infections of genitourinary tract in pregnancy<br>`O233` - Infections of other parts of urinary tract in pregnancy<br>`O2330` - Infections of other parts of urinary tract in pregnancy, unspecified trimester<br>`O2332` - Infections of other parts of urinary tract in pregnancy, second trimester<br>`O234` - Unspecified infection of urinary tract in pregnancy<br>`O2340` - Unspecified infection of urinary tract in pregnancy, unspecified trimester<br>`O2341` - Unspecified infection of urinary tract in pregnancy, first trimester<br>`O2342` - Unspecified infection of urinary tract in pregnancy, second trimester<br>`O2343` - Unspecified infection of urinary tract in pregnancy, third trimester<br>`O239` - Unspecified genitourinary tract infection in pregnancy<br>`O2390` - Unspecified genitourinary tract infection in pregnancy, unspecified trimester<br>`O2391` - Unspecified genitourinary tract infection in pregnancy, first trimester<br>`O2392` - Unspecified genitourinary tract infection in pregnancy, second trimester<br>`O2393` - Unspecified genitourinary tract infection in pregnancy, third trimester<br>`O86` - Other puerperal infections<br>... +11 more

### 15. `v775_v296_portfolio_obstetric_metabolic_renal_prune.csv` - Diabetes / KEEP

- Message: v775: v296 obstetric/metabolic/renal KEEP prune
- Added (0): none
- Removed (66): `O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2412` - Pre-existing type 2 diabetes mellitus, in childbirth<br>`O2413` - Pre-existing type 2 diabetes mellitus, in the puerperium<br>`O243` - Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium<br>... +48 more

### 16. `v776_v296_portfolio_hf_ckd_pneumonia_prune.csv` - CKD / KEEP

- Message: v776: v296 HF+CKD+Pneumonia KEEP prune
- Added (0): none
- Removed (3): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure

### 16. `v776_v296_portfolio_hf_ckd_pneumonia_prune.csv` - Heart Failure / KEEP

- Message: v776: v296 HF+CKD+Pneumonia KEEP prune
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 16. `v776_v296_portfolio_hf_ckd_pneumonia_prune.csv` - Pneumonia / KEEP

- Message: v776: v296 HF+CKD+Pneumonia KEEP prune
- Added (0): none
- Removed (30): `A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`J84` - Other interstitial pulmonary diseases<br>`J8411` - Idiopathic interstitial pneumonia<br>`J84111` - Idiopathic interstitial pneumonia, not otherwise specified<br>`J84116` - Cryptogenic organizing pneumonia<br>`J84117` - Desquamative interstitial pneumonia<br>`J842` - Lymphoid interstitial pneumonia<br>`J85` - Abscess of lung and mediastinum<br>`J850` - Gangrene and necrosis of lung<br>`J851` - Abscess of lung with pneumonia<br>... +12 more

### 17. `v777_v296_portfolio_derm_uti_diabetes_prune.csv` - Dermatomycosis / KEEP

- Message: v777: v296 Derm+UTI+Diabetes KEEP prune
- Added (0): none
- Removed (21): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +3 more

### 17. `v777_v296_portfolio_derm_uti_diabetes_prune.csv` - UTI / KEEP

- Message: v777: v296 Derm+UTI+Diabetes KEEP prune
- Added (0): none
- Removed (3): `N35` - Urethral stricture<br>`N35819` - Other urethral stricture, male, unspecified site<br>`N35919` - Unspecified urethral stricture, male, unspecified site

### 17. `v777_v296_portfolio_derm_uti_diabetes_prune.csv` - Diabetes / KEEP

- Message: v777: v296 Derm+UTI+Diabetes KEEP prune
- Added (0): none
- Removed (9): `P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`P702` - Neonatal diabetes mellitus<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 18. `v778_v296_portfolio_neuro_endocrine_prune.csv` - Intracranial Pressure / KEEP

- Message: v778: v296 neuro+endocrine KEEP prune
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 18. `v778_v296_portfolio_neuro_endocrine_prune.csv` - Hypoparathyroidism / KEEP

- Message: v778: v296 neuro+endocrine KEEP prune
- Added (0): none
- Removed (8): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E230` - Hypopituitarism<br>`E231` - Drug-induced hypopituitarism<br>`E87` - Other disorders of fluid, electrolyte and acid-base balance<br>`E876` - Hypokalemia<br>`P71` - Transitory neonatal disorders of calcium and magnesium metabolism<br>`P714` - Transitory neonatal hypoparathyroidism

### 18. `v778_v296_portfolio_neuro_endocrine_prune.csv` - Hyperthyroidism / KEEP

- Message: v778: v296 neuro+endocrine KEEP prune
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 19. `v779_v296_portfolio_small_high_precision_prune.csv` - Gout / KEEP

- Message: v779: v296 small high-precision KEEP prune
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 19. `v779_v296_portfolio_small_high_precision_prune.csv` - CKD / KEEP

- Message: v779: v296 small high-precision KEEP prune
- Added (0): none
- Removed (3): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure

### 19. `v779_v296_portfolio_small_high_precision_prune.csv` - Hematemesis / KEEP

- Message: v779: v296 small high-precision KEEP prune
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 19. `v779_v296_portfolio_small_high_precision_prune.csv` - Heart Failure / KEEP

- Message: v779: v296 small high-precision KEEP prune
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 19. `v779_v296_portfolio_small_high_precision_prune.csv` - UTI / KEEP

- Message: v779: v296 small high-precision KEEP prune
- Added (0): none
- Removed (3): `N35` - Urethral stricture<br>`N35819` - Other urethral stricture, male, unspecified site<br>`N35919` - Unspecified urethral stricture, male, unspecified site

### 19. `v779_v296_portfolio_small_high_precision_prune.csv` - Interstitial Lung Disease / KEEP

- Message: v779: v296 small high-precision KEEP prune
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Intracranial Pressure / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Gout / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Dermatomycosis / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (21): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +3 more

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Pleurisy / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Bronchitis / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Thyroiditis / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (18): `C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`D00` - Carcinoma in situ of oral cavity, esophagus and stomach<br>`D000` - Carcinoma in situ of lip, oral cavity and pharynx<br>`D0000` - Carcinoma in situ of oral cavity, unspecified site<br>`D0001` - Carcinoma in situ of labial mucosa and vermilion border<br>`D0002` - Carcinoma in situ of buccal mucosa<br>`D0003` - Carcinoma in situ of gingiva and edentulous alveolar ridge<br>`D0004` - Carcinoma in situ of soft palate<br>`D0005` - Carcinoma in situ of hard palate<br>`D0006` - Carcinoma in situ of floor of mouth<br>`D0007` - Carcinoma in situ of tongue<br>`D0008` - Carcinoma in situ of pharynx<br>`D10` - Benign neoplasm of mouth and pharynx<br>`D101` - Benign neoplasm of tongue<br>`D106` - Benign neoplasm of nasopharynx<br>`D107` - Benign neoplasm of hypopharynx

### 20. `v780_v296_portfolio_broad_private_prune.csv` - CKD / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (46): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`Q60` - Renal agenesis and other reduction defects of kidney<br>`Q600` - Renal agenesis, unilateral<br>`Q601` - Renal agenesis, bilateral<br>`Q602` - Renal agenesis, unspecified<br>`Q603` - Renal hypoplasia, unilateral<br>`Q604` - Renal hypoplasia, bilateral<br>`Q605` - Renal hypoplasia, unspecified<br>`Q606` - Potter's syndrome<br>`Q61` - Cystic kidney disease<br>`Q610` - Congenital renal cyst<br>`Q6100` - Congenital renal cyst, unspecified<br>`Q6101` - Congenital single renal cyst<br>`Q6102` - Congenital multiple renal cysts<br>`Q611` - Polycystic kidney, infantile type<br>`Q6111` - Cystic dilatation of collecting ducts<br>... +28 more

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Hypothyroidism / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Hematemesis / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Heart Failure / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 20. `v780_v296_portfolio_broad_private_prune.csv` - UTI / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (32): `N35` - Urethral stricture<br>`N35819` - Other urethral stricture, male, unspecified site<br>`N35919` - Unspecified urethral stricture, male, unspecified site<br>`O03` - Spontaneous abortion<br>`O0338` - Urinary tract infection following incomplete spontaneous abortion<br>`O0388` - Urinary tract infection following complete or unspecified spontaneous abortion<br>`O23` - Infections of genitourinary tract in pregnancy<br>`O233` - Infections of other parts of urinary tract in pregnancy<br>`O2330` - Infections of other parts of urinary tract in pregnancy, unspecified trimester<br>`O2332` - Infections of other parts of urinary tract in pregnancy, second trimester<br>`O234` - Unspecified infection of urinary tract in pregnancy<br>`O2340` - Unspecified infection of urinary tract in pregnancy, unspecified trimester<br>`O2341` - Unspecified infection of urinary tract in pregnancy, first trimester<br>`O2342` - Unspecified infection of urinary tract in pregnancy, second trimester<br>`O2343` - Unspecified infection of urinary tract in pregnancy, third trimester<br>`O239` - Unspecified genitourinary tract infection in pregnancy<br>`O2390` - Unspecified genitourinary tract infection in pregnancy, unspecified trimester<br>`O2391` - Unspecified genitourinary tract infection in pregnancy, first trimester<br>... +14 more

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Diabetes / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (66): `O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2412` - Pre-existing type 2 diabetes mellitus, in childbirth<br>`O2413` - Pre-existing type 2 diabetes mellitus, in the puerperium<br>`O243` - Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium<br>... +48 more

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Interstitial Lung Disease / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Hypoparathyroidism / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (8): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E230` - Hypopituitarism<br>`E231` - Drug-induced hypopituitarism<br>`E87` - Other disorders of fluid, electrolyte and acid-base balance<br>`E876` - Hypokalemia<br>`P71` - Transitory neonatal disorders of calcium and magnesium metabolism<br>`P714` - Transitory neonatal hypoparathyroidism

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Hyperthyroidism / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 20. `v780_v296_portfolio_broad_private_prune.csv` - Pneumonia / KEEP

- Message: v780: v296 broad private KEEP prune
- Added (0): none
- Removed (30): `A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`J84` - Other interstitial pulmonary diseases<br>`J8411` - Idiopathic interstitial pneumonia<br>`J84111` - Idiopathic interstitial pneumonia, not otherwise specified<br>`J84116` - Cryptogenic organizing pneumonia<br>`J84117` - Desquamative interstitial pneumonia<br>`J842` - Lymphoid interstitial pneumonia<br>`J85` - Abscess of lung and mediastinum<br>`J850` - Gangrene and necrosis of lung<br>`J851` - Abscess of lung with pneumonia<br>... +12 more
