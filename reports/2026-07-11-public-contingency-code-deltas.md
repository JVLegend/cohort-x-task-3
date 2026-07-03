# CohortX Plan Code Deltas - 2026-07-11-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-11-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 20
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v601_v296_icp_no_g96_g94.csv` | Intracranial Pressure | KEEP | 0 | 4 | v601: v296 ICP prune G96/G94 | remove non-core CNS disorder families from ICP KEEP |
| 2 | `submissions/v602_v296_gout_no_e79.csv` | Gout | KEEP | 0 | 2 | v602: v296 Gout prune E79 | remove hyperuricemia/metabolism family from Gout KEEP |
| 3 | `submissions/v603_v296_pleurisy_no_r09_j95.csv` | Pleurisy | KEEP | 0 | 12 | v603: v296 Pleurisy prune R09/J95 | remove symptoms/postprocedural respiratory families from Pleurisy KEEP |
| 4 | `submissions/v604_v296_bronchitis_no_j43_j68.csv` | Bronchitis | KEEP | 0 | 8 | v604: v296 Bronchitis prune J43/J68 | remove emphysema/inhalation families from Bronchitis KEEP |
| 5 | `submissions/v605_v296_thyroiditis_no_e03.csv` | Thyroiditis | KEEP | 0 | 2 | v605: v296 Thyroiditis prune E03 | remove hypothyroidism family from Thyroiditis KEEP |
| 6 | `submissions/v606_v296_npc_no_d00_c44_d10.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 18 | v606: v296 NPC prune D00/C44/D10 | remove carcinoma-in-situ/skin/benign mouth families from NPC KEEP |
| 7 | `submissions/v607_v296_ckd_no_q60_q61_q62.csv` | CKD | KEEP | 0 | 43 | v607: v296 CKD prune congenital Q families | remove congenital renal malformation families from CKD KEEP |
| 8 | `submissions/v608_v296_ckd_no_i50.csv` | CKD | KEEP | 0 | 3 | v608: v296 CKD prune I50 | remove heart failure family from CKD KEEP |
| 9 | `submissions/v609_v296_hypothyroid_no_e04.csv` | Hypothyroidism | KEEP | 0 | 6 | v609: v296 Hypothyroidism prune E04 | remove nontoxic goiter family from Hypothyroidism KEEP |
| 10 | `submissions/v610_v296_hematemesis_no_r36_k66.csv` | Hematemesis | KEEP | 0 | 4 | v610: v296 Hematemesis prune R36/K66 | remove urethral/peritoneal families from Hematemesis KEEP |
| 11 | `submissions/v611_v296_hf_no_i97.csv` | Heart Failure | KEEP | 0 | 31 | v611: v296 Heart Failure prune I97 | remove large postprocedural circulatory family from HF KEEP |
| 12 | `submissions/v612_v296_hypergonadism_no_e27.csv` | Hypergonadism | KEEP | 0 | 11 | v612: v296 Hypergonadism prune E27 | remove adrenal family from Hypergonadism KEEP |
| 13 | `submissions/v613_v296_uti_no_obstetric.csv` | UTI | KEEP | 0 | 29 | v613: v296 UTI prune obstetric families | remove pregnancy/puerperal/abortion infection families from UTI KEEP |
| 14 | `submissions/v614_v296_uti_no_n35.csv` | UTI | KEEP | 0 | 3 | v614: v296 UTI prune N35 | remove urethral stricture family from UTI KEEP |
| 15 | `submissions/v615_v296_diabetes_no_o24.csv` | Diabetes | KEEP | 0 | 57 | v615: v296 Diabetes prune O24 | remove pregnancy diabetes family from Diabetes KEEP |
| 16 | `submissions/v616_v296_diabetes_no_z_p70.csv` | Diabetes | KEEP | 0 | 9 | v616: v296 Diabetes prune Z/P70 | remove therapy/history/newborn metabolism extras from Diabetes KEEP |
| 17 | `submissions/v617_v296_ild_no_j70.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v617: v296 ILD prune J70 | remove external-agent respiratory family from ILD KEEP |
| 18 | `submissions/v618_v296_hypopara_no_e23_e87_p71_e21.csv` | Hypoparathyroidism | KEEP | 0 | 8 | v618: v296 Hypopara prune related endocrine/noise | remove pituitary/fluid/neonatal/opposite parathyroid families from Hypopara KEEP |
| 19 | `submissions/v619_v296_hyperthyroid_no_e04_e01_e03_p72.csv` | Hyperthyroidism | KEEP | 0 | 12 | v619: v296 Hyperthyroid prune non-hyperthyroid | remove goiter/iodine/hypothyroid/neonatal families from Hyperthyroidism KEEP |
| 20 | `submissions/v620_v296_pneumonia_no_a37_p23_j84_j85.csv` | Pneumonia | KEEP | 0 | 30 | v620: v296 Pneumonia prune noisy families | remove whooping-cough/congenital/ILD/abscess families from Pneumonia KEEP |

## Exact Code Changes

### 1. `v601_v296_icp_no_g96_g94.csv` - Intracranial Pressure / KEEP

- Message: v601: v296 ICP prune G96/G94
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 2. `v602_v296_gout_no_e79.csv` - Gout / KEEP

- Message: v602: v296 Gout prune E79
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 3. `v603_v296_pleurisy_no_r09_j95.csv` - Pleurisy / KEEP

- Message: v603: v296 Pleurisy prune R09/J95
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 4. `v604_v296_bronchitis_no_j43_j68.csv` - Bronchitis / KEEP

- Message: v604: v296 Bronchitis prune J43/J68
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 5. `v605_v296_thyroiditis_no_e03.csv` - Thyroiditis / KEEP

- Message: v605: v296 Thyroiditis prune E03
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 6. `v606_v296_npc_no_d00_c44_d10.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v606: v296 NPC prune D00/C44/D10
- Added (0): none
- Removed (18): `C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`D00` - Carcinoma in situ of oral cavity, esophagus and stomach<br>`D000` - Carcinoma in situ of lip, oral cavity and pharynx<br>`D0000` - Carcinoma in situ of oral cavity, unspecified site<br>`D0001` - Carcinoma in situ of labial mucosa and vermilion border<br>`D0002` - Carcinoma in situ of buccal mucosa<br>`D0003` - Carcinoma in situ of gingiva and edentulous alveolar ridge<br>`D0004` - Carcinoma in situ of soft palate<br>`D0005` - Carcinoma in situ of hard palate<br>`D0006` - Carcinoma in situ of floor of mouth<br>`D0007` - Carcinoma in situ of tongue<br>`D0008` - Carcinoma in situ of pharynx<br>`D10` - Benign neoplasm of mouth and pharynx<br>`D101` - Benign neoplasm of tongue<br>`D106` - Benign neoplasm of nasopharynx<br>`D107` - Benign neoplasm of hypopharynx

### 7. `v607_v296_ckd_no_q60_q61_q62.csv` - CKD / KEEP

- Message: v607: v296 CKD prune congenital Q families
- Added (0): none
- Removed (43): `Q60` - Renal agenesis and other reduction defects of kidney<br>`Q600` - Renal agenesis, unilateral<br>`Q601` - Renal agenesis, bilateral<br>`Q602` - Renal agenesis, unspecified<br>`Q603` - Renal hypoplasia, unilateral<br>`Q604` - Renal hypoplasia, bilateral<br>`Q605` - Renal hypoplasia, unspecified<br>`Q606` - Potter's syndrome<br>`Q61` - Cystic kidney disease<br>`Q610` - Congenital renal cyst<br>`Q6100` - Congenital renal cyst, unspecified<br>`Q6101` - Congenital single renal cyst<br>`Q6102` - Congenital multiple renal cysts<br>`Q611` - Polycystic kidney, infantile type<br>`Q6111` - Cystic dilatation of collecting ducts<br>`Q6119` - Other polycystic kidney, infantile type<br>`Q612` - Polycystic kidney, adult type<br>`Q613` - Polycystic kidney, unspecified<br>... +25 more

### 8. `v608_v296_ckd_no_i50.csv` - CKD / KEEP

- Message: v608: v296 CKD prune I50
- Added (0): none
- Removed (3): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure

### 9. `v609_v296_hypothyroid_no_e04.csv` - Hypothyroidism / KEEP

- Message: v609: v296 Hypothyroidism prune E04
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 10. `v610_v296_hematemesis_no_r36_k66.csv` - Hematemesis / KEEP

- Message: v610: v296 Hematemesis prune R36/K66
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 11. `v611_v296_hf_no_i97.csv` - Heart Failure / KEEP

- Message: v611: v296 Heart Failure prune I97
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 12. `v612_v296_hypergonadism_no_e27.csv` - Hypergonadism / KEEP

- Message: v612: v296 Hypergonadism prune E27
- Added (0): none
- Removed (11): `E27` - Other disorders of adrenal gland<br>`E270` - Other adrenocortical overactivity<br>`E271` - Primary adrenocortical insufficiency<br>`E272` - Addisonian crisis<br>`E273` - Drug-induced adrenocortical insufficiency<br>`E274` - Other and unspecified adrenocortical insufficiency<br>`E2740` - Unspecified adrenocortical insufficiency<br>`E2749` - Other adrenocortical insufficiency<br>`E275` - Adrenomedullary hyperfunction<br>`E278` - Other specified disorders of adrenal gland<br>`E279` - Disorder of adrenal gland, unspecified

### 13. `v613_v296_uti_no_obstetric.csv` - UTI / KEEP

- Message: v613: v296 UTI prune obstetric families
- Added (0): none
- Removed (29): `O03` - Spontaneous abortion<br>`O0338` - Urinary tract infection following incomplete spontaneous abortion<br>`O0388` - Urinary tract infection following complete or unspecified spontaneous abortion<br>`O23` - Infections of genitourinary tract in pregnancy<br>`O233` - Infections of other parts of urinary tract in pregnancy<br>`O2330` - Infections of other parts of urinary tract in pregnancy, unspecified trimester<br>`O2332` - Infections of other parts of urinary tract in pregnancy, second trimester<br>`O234` - Unspecified infection of urinary tract in pregnancy<br>`O2340` - Unspecified infection of urinary tract in pregnancy, unspecified trimester<br>`O2341` - Unspecified infection of urinary tract in pregnancy, first trimester<br>`O2342` - Unspecified infection of urinary tract in pregnancy, second trimester<br>`O2343` - Unspecified infection of urinary tract in pregnancy, third trimester<br>`O239` - Unspecified genitourinary tract infection in pregnancy<br>`O2390` - Unspecified genitourinary tract infection in pregnancy, unspecified trimester<br>`O2391` - Unspecified genitourinary tract infection in pregnancy, first trimester<br>`O2392` - Unspecified genitourinary tract infection in pregnancy, second trimester<br>`O2393` - Unspecified genitourinary tract infection in pregnancy, third trimester<br>`O86` - Other puerperal infections<br>... +11 more

### 14. `v614_v296_uti_no_n35.csv` - UTI / KEEP

- Message: v614: v296 UTI prune N35
- Added (0): none
- Removed (3): `N35` - Urethral stricture<br>`N35819` - Other urethral stricture, male, unspecified site<br>`N35919` - Unspecified urethral stricture, male, unspecified site

### 15. `v615_v296_diabetes_no_o24.csv` - Diabetes / KEEP

- Message: v615: v296 Diabetes prune O24
- Added (0): none
- Removed (57): `O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2412` - Pre-existing type 2 diabetes mellitus, in childbirth<br>`O2413` - Pre-existing type 2 diabetes mellitus, in the puerperium<br>`O243` - Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium<br>... +39 more

### 16. `v616_v296_diabetes_no_z_p70.csv` - Diabetes / KEEP

- Message: v616: v296 Diabetes prune Z/P70
- Added (0): none
- Removed (9): `P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`P702` - Neonatal diabetes mellitus<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 17. `v617_v296_ild_no_j70.csv` - Interstitial Lung Disease / KEEP

- Message: v617: v296 ILD prune J70
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 18. `v618_v296_hypopara_no_e23_e87_p71_e21.csv` - Hypoparathyroidism / KEEP

- Message: v618: v296 Hypopara prune related endocrine/noise
- Added (0): none
- Removed (8): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E230` - Hypopituitarism<br>`E231` - Drug-induced hypopituitarism<br>`E87` - Other disorders of fluid, electrolyte and acid-base balance<br>`E876` - Hypokalemia<br>`P71` - Transitory neonatal disorders of calcium and magnesium metabolism<br>`P714` - Transitory neonatal hypoparathyroidism

### 19. `v619_v296_hyperthyroid_no_e04_e01_e03_p72.csv` - Hyperthyroidism / KEEP

- Message: v619: v296 Hyperthyroid prune non-hyperthyroid
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 20. `v620_v296_pneumonia_no_a37_p23_j84_j85.csv` - Pneumonia / KEEP

- Message: v620: v296 Pneumonia prune noisy families
- Added (0): none
- Removed (30): `A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`J84` - Other interstitial pulmonary diseases<br>`J8411` - Idiopathic interstitial pneumonia<br>`J84111` - Idiopathic interstitial pneumonia, not otherwise specified<br>`J84116` - Cryptogenic organizing pneumonia<br>`J84117` - Desquamative interstitial pneumonia<br>`J842` - Lymphoid interstitial pneumonia<br>`J85` - Abscess of lung and mediastinum<br>`J850` - Gangrene and necrosis of lung<br>`J851` - Abscess of lung with pneumonia<br>... +12 more

