# CohortX Plan Code Deltas - 2026-07-13-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-13-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 40
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v681_v296_icp_no_g96_g94_diff.csv` | Intracranial Pressure | KEEP | 0 | 4 | v681: v296 ICP prune G96/G94 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 1 | `submissions/v681_v296_icp_no_g96_g94_diff.csv` | Intracranial Pressure | DIFF | 97 | 0 | v681: v296 ICP prune G96/G94 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 2 | `submissions/v682_v296_gout_no_e79_diff.csv` | Gout | KEEP | 0 | 2 | v682: v296 Gout prune E79 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 2 | `submissions/v682_v296_gout_no_e79_diff.csv` | Gout | DIFF | 260 | 0 | v682: v296 Gout prune E79 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 3 | `submissions/v683_v296_pleurisy_no_r09_j95_diff.csv` | Pleurisy | KEEP | 0 | 12 | v683: v296 Pleurisy prune R09/J95 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 3 | `submissions/v683_v296_pleurisy_no_r09_j95_diff.csv` | Pleurisy | DIFF | 17 | 0 | v683: v296 Pleurisy prune R09/J95 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 4 | `submissions/v684_v296_bronchitis_no_j43_j68_diff.csv` | Bronchitis | KEEP | 0 | 8 | v684: v296 Bronchitis prune J43/J68 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 4 | `submissions/v684_v296_bronchitis_no_j43_j68_diff.csv` | Bronchitis | DIFF | 32 | 0 | v684: v296 Bronchitis prune J43/J68 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 5 | `submissions/v685_v296_thyroiditis_no_e03_diff.csv` | Thyroiditis | KEEP | 0 | 2 | v685: v296 Thyroiditis prune E03 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 5 | `submissions/v685_v296_thyroiditis_no_e03_diff.csv` | Thyroiditis | DIFF | 6 | 0 | v685: v296 Thyroiditis prune E03 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 6 | `submissions/v686_v296_npc_no_d00_c44_d10_diff.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 18 | v686: v296 NPC prune D00/C44/D10 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 6 | `submissions/v686_v296_npc_no_d00_c44_d10_diff.csv` | Nasopharyngeal Carcinoma | DIFF | 17 | 0 | v686: v296 NPC prune D00/C44/D10 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 7 | `submissions/v687_v296_ckd_no_q60_q61_q62_diff.csv` | CKD | KEEP | 0 | 43 | v687: v296 CKD prune congenital Q plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 7 | `submissions/v687_v296_ckd_no_q60_q61_q62_diff.csv` | CKD | DIFF | 6 | 0 | v687: v296 CKD prune congenital Q plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 8 | `submissions/v688_v296_ckd_no_i50_diff.csv` | CKD | KEEP | 0 | 3 | v688: v296 CKD prune I50 plus DIFF | small CKD KEEP prune plus CKD DIFF |
| 8 | `submissions/v688_v296_ckd_no_i50_diff.csv` | CKD | DIFF | 6 | 0 | v688: v296 CKD prune I50 plus DIFF | small CKD KEEP prune plus CKD DIFF |
| 9 | `submissions/v689_v296_hypothyroid_no_e04_diff.csv` | Hypothyroidism | KEEP | 0 | 6 | v689: v296 Hypothyroidism prune E04 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 9 | `submissions/v689_v296_hypothyroid_no_e04_diff.csv` | Hypothyroidism | DIFF | 22 | 0 | v689: v296 Hypothyroidism prune E04 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 10 | `submissions/v690_v296_hematemesis_no_r36_k66_diff.csv` | Hematemesis | KEEP | 0 | 4 | v690: v296 Hematemesis prune R36/K66 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 10 | `submissions/v690_v296_hematemesis_no_r36_k66_diff.csv` | Hematemesis | DIFF | 2 | 0 | v690: v296 Hematemesis prune R36/K66 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 11 | `submissions/v691_v296_hf_no_i97_diff.csv` | Heart Failure | KEEP | 0 | 31 | v691: v296 Heart Failure prune I97 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 11 | `submissions/v691_v296_hf_no_i97_diff.csv` | Heart Failure | DIFF | 15 | 0 | v691: v296 Heart Failure prune I97 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 12 | `submissions/v692_v296_uti_no_obstetric_diff.csv` | UTI | KEEP | 0 | 29 | v692: v296 UTI prune obstetric plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 12 | `submissions/v692_v296_uti_no_obstetric_diff.csv` | UTI | DIFF | 39 | 0 | v692: v296 UTI prune obstetric plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 13 | `submissions/v693_v296_uti_no_n35_diff.csv` | UTI | KEEP | 0 | 3 | v693: v296 UTI prune N35 plus DIFF | small UTI KEEP prune plus UTI DIFF |
| 13 | `submissions/v693_v296_uti_no_n35_diff.csv` | UTI | DIFF | 39 | 0 | v693: v296 UTI prune N35 plus DIFF | small UTI KEEP prune plus UTI DIFF |
| 14 | `submissions/v694_v296_diabetes_no_o24_diff.csv` | Diabetes | KEEP | 0 | 57 | v694: v296 Diabetes prune O24 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 14 | `submissions/v694_v296_diabetes_no_o24_diff.csv` | Diabetes | DIFF | 7 | 0 | v694: v296 Diabetes prune O24 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 15 | `submissions/v695_v296_diabetes_no_z_p70_diff.csv` | Diabetes | KEEP | 0 | 9 | v695: v296 Diabetes prune Z/P70 plus DIFF | small Diabetes KEEP prune plus Diabetes DIFF |
| 15 | `submissions/v695_v296_diabetes_no_z_p70_diff.csv` | Diabetes | DIFF | 7 | 0 | v695: v296 Diabetes prune Z/P70 plus DIFF | small Diabetes KEEP prune plus Diabetes DIFF |
| 16 | `submissions/v696_v296_ild_no_j70_diff.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v696: v296 ILD prune J70 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 16 | `submissions/v696_v296_ild_no_j70_diff.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v696: v296 ILD prune J70 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 17 | `submissions/v697_v296_hypopara_no_e23_e87_p71_e21_diff.csv` | Hypoparathyroidism | KEEP | 0 | 8 | v697: v296 Hypopara prune related plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 17 | `submissions/v697_v296_hypopara_no_e23_e87_p71_e21_diff.csv` | Hypoparathyroidism | DIFF | 10 | 0 | v697: v296 Hypopara prune related plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 18 | `submissions/v698_v296_hyperthyroid_no_e04_e01_e03_p72_diff.csv` | Hyperthyroidism | KEEP | 0 | 12 | v698: v296 Hyperthyroid prune non-hyper plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 18 | `submissions/v698_v296_hyperthyroid_no_e04_e01_e03_p72_diff.csv` | Hyperthyroidism | DIFF | 15 | 0 | v698: v296 Hyperthyroid prune non-hyper plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 19 | `submissions/v699_v296_pneumonia_no_a37_p23_j84_j85_diff.csv` | Pneumonia | KEEP | 0 | 30 | v699: v296 Pneumonia prune noisy plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 19 | `submissions/v699_v296_pneumonia_no_a37_p23_j84_j85_diff.csv` | Pneumonia | DIFF | 71 | 0 | v699: v296 Pneumonia prune noisy plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 20 | `submissions/v700_v296_derm_no_b37_diff.csv` | Dermatomycosis | KEEP | 0 | 21 | v700: v296 Dermatomycosis prune B37 plus DIFF | new Dermatomycosis KEEP precision plus broad DIFF isolation |
| 20 | `submissions/v700_v296_derm_no_b37_diff.csv` | Dermatomycosis | DIFF | 33 | 0 | v700: v296 Dermatomycosis prune B37 plus DIFF | new Dermatomycosis KEEP precision plus broad DIFF isolation |

## Exact Code Changes

### 1. `v681_v296_icp_no_g96_g94_diff.csv` - Intracranial Pressure / KEEP

- Message: v681: v296 ICP prune G96/G94 plus DIFF
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 1. `v681_v296_icp_no_g96_g94_diff.csv` - Intracranial Pressure / DIFF

- Message: v681: v296 ICP prune G96/G94 plus DIFF
- Added (97): `G43` - Migraine<br>`G430` - Migraine without aura<br>`G4300` - Migraine without aura, not intractable<br>`G43001` - Migraine without aura, not intractable, with status migrainosus<br>`G43009` - Migraine without aura, not intractable, without status migrainosus<br>`G4301` - Migraine without aura, intractable<br>`G43011` - Migraine without aura, intractable, with status migrainosus<br>`G43019` - Migraine without aura, intractable, without status migrainosus<br>`G431` - Migraine with aura<br>`G4310` - Migraine with aura, not intractable<br>`G43101` - Migraine with aura, not intractable, with status migrainosus<br>`G43109` - Migraine with aura, not intractable, without status migrainosus<br>`G4311` - Migraine with aura, intractable<br>`G43111` - Migraine with aura, intractable, with status migrainosus<br>`G43119` - Migraine with aura, intractable, without status migrainosus<br>`G434` - Hemiplegic migraine<br>`G4340` - Hemiplegic migraine, not intractable<br>`G43401` - Hemiplegic migraine, not intractable, with status migrainosus<br>... +79 more
- Removed (0): none
### 2. `v682_v296_gout_no_e79_diff.csv` - Gout / KEEP

- Message: v682: v296 Gout prune E79 plus DIFF
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 2. `v682_v296_gout_no_e79_diff.csv` - Gout / DIFF

- Message: v682: v296 Gout prune E79 plus DIFF
- Added (260): `M00` - Pyogenic arthritis<br>`M000` - Staphylococcal arthritis and polyarthritis<br>`M0000` - Staphylococcal arthritis, unspecified joint<br>`M0001` - Staphylococcal arthritis, shoulder<br>`M00011` - Staphylococcal arthritis, right shoulder<br>`M00012` - Staphylococcal arthritis, left shoulder<br>`M00019` - Staphylococcal arthritis, unspecified shoulder<br>`M0002` - Staphylococcal arthritis, elbow<br>`M00021` - Staphylococcal arthritis, right elbow<br>`M00022` - Staphylococcal arthritis, left elbow<br>`M00029` - Staphylococcal arthritis, unspecified elbow<br>`M0003` - Staphylococcal arthritis, wrist<br>`M00031` - Staphylococcal arthritis, right wrist<br>`M00032` - Staphylococcal arthritis, left wrist<br>`M00039` - Staphylococcal arthritis, unspecified wrist<br>`M0004` - Staphylococcal arthritis, hand<br>`M00041` - Staphylococcal arthritis, right hand<br>`M00042` - Staphylococcal arthritis, left hand<br>... +242 more
- Removed (0): none

### 3. `v683_v296_pleurisy_no_r09_j95_diff.csv` - Pleurisy / KEEP

- Message: v683: v296 Pleurisy prune R09/J95 plus DIFF
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 3. `v683_v296_pleurisy_no_r09_j95_diff.csv` - Pleurisy / DIFF

- Message: v683: v296 Pleurisy prune R09/J95 plus DIFF
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 4. `v684_v296_bronchitis_no_j43_j68_diff.csv` - Bronchitis / KEEP

- Message: v684: v296 Bronchitis prune J43/J68 plus DIFF
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 4. `v684_v296_bronchitis_no_j43_j68_diff.csv` - Bronchitis / DIFF

- Message: v684: v296 Bronchitis prune J43/J68 plus DIFF
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 5. `v685_v296_thyroiditis_no_e03_diff.csv` - Thyroiditis / KEEP

- Message: v685: v296 Thyroiditis prune E03 plus DIFF
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 5. `v685_v296_thyroiditis_no_e03_diff.csv` - Thyroiditis / DIFF

- Message: v685: v296 Thyroiditis prune E03 plus DIFF
- Added (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified
- Removed (0): none

### 6. `v686_v296_npc_no_d00_c44_d10_diff.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v686: v296 NPC prune D00/C44/D10 plus DIFF
- Added (0): none
- Removed (18): `C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`D00` - Carcinoma in situ of oral cavity, esophagus and stomach<br>`D000` - Carcinoma in situ of lip, oral cavity and pharynx<br>`D0000` - Carcinoma in situ of oral cavity, unspecified site<br>`D0001` - Carcinoma in situ of labial mucosa and vermilion border<br>`D0002` - Carcinoma in situ of buccal mucosa<br>`D0003` - Carcinoma in situ of gingiva and edentulous alveolar ridge<br>`D0004` - Carcinoma in situ of soft palate<br>`D0005` - Carcinoma in situ of hard palate<br>`D0006` - Carcinoma in situ of floor of mouth<br>`D0007` - Carcinoma in situ of tongue<br>`D0008` - Carcinoma in situ of pharynx<br>`D10` - Benign neoplasm of mouth and pharynx<br>`D101` - Benign neoplasm of tongue<br>`D106` - Benign neoplasm of nasopharynx<br>`D107` - Benign neoplasm of hypopharynx

### 6. `v686_v296_npc_no_d00_c44_d10_diff.csv` - Nasopharyngeal Carcinoma / DIFF

- Message: v686: v296 NPC prune D00/C44/D10 plus DIFF
- Added (17): `C10` - Malignant neoplasm of oropharynx<br>`C100` - Malignant neoplasm of vallecula<br>`C101` - Malignant neoplasm of anterior surface of epiglottis<br>`C102` - Malignant neoplasm of lateral wall of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C104` - Malignant neoplasm of branchial cleft<br>`C108` - Malignant neoplasm of overlapping sites of oropharynx<br>`C109` - Malignant neoplasm of oropharynx, unspecified<br>`C14` - Malignant neoplasm of other and ill-defined sites in the lip, oral cavity and pharynx<br>`C140` - Malignant neoplasm of pharynx, unspecified<br>`C142` - Malignant neoplasm of Waldeyer's ring<br>`C148` - Malignant neoplasm of overlapping sites of lip, oral cavity and pharynx<br>`J33` - Nasal polyp<br>`J330` - Polyp of nasal cavity<br>`J331` - Polypoid sinus degeneration<br>`J338` - Other polyp of sinus<br>`J339` - Nasal polyp, unspecified
- Removed (0): none

### 7. `v687_v296_ckd_no_q60_q61_q62_diff.csv` - CKD / KEEP

- Message: v687: v296 CKD prune congenital Q plus DIFF
- Added (0): none
- Removed (43): `Q60` - Renal agenesis and other reduction defects of kidney<br>`Q600` - Renal agenesis, unilateral<br>`Q601` - Renal agenesis, bilateral<br>`Q602` - Renal agenesis, unspecified<br>`Q603` - Renal hypoplasia, unilateral<br>`Q604` - Renal hypoplasia, bilateral<br>`Q605` - Renal hypoplasia, unspecified<br>`Q606` - Potter's syndrome<br>`Q61` - Cystic kidney disease<br>`Q610` - Congenital renal cyst<br>`Q6100` - Congenital renal cyst, unspecified<br>`Q6101` - Congenital single renal cyst<br>`Q6102` - Congenital multiple renal cysts<br>`Q611` - Polycystic kidney, infantile type<br>`Q6111` - Cystic dilatation of collecting ducts<br>`Q6119` - Other polycystic kidney, infantile type<br>`Q612` - Polycystic kidney, adult type<br>`Q613` - Polycystic kidney, unspecified<br>... +25 more

### 7. `v687_v296_ckd_no_q60_q61_q62_diff.csv` - CKD / DIFF

- Message: v687: v296 CKD prune congenital Q plus DIFF
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 8. `v688_v296_ckd_no_i50_diff.csv` - CKD / KEEP

- Message: v688: v296 CKD prune I50 plus DIFF
- Added (0): none
- Removed (3): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure

### 8. `v688_v296_ckd_no_i50_diff.csv` - CKD / DIFF

- Message: v688: v296 CKD prune I50 plus DIFF
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 9. `v689_v296_hypothyroid_no_e04_diff.csv` - Hypothyroidism / KEEP

- Message: v689: v296 Hypothyroidism prune E04 plus DIFF
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 9. `v689_v296_hypothyroid_no_e04_diff.csv` - Hypothyroidism / DIFF

- Message: v689: v296 Hypothyroidism prune E04 plus DIFF
- Added (22): `E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>`E0521` - Thyrotoxicosis with toxic multinodular goiter with thyrotoxic crisis or storm<br>`E053` - Thyrotoxicosis from ectopic thyroid tissue<br>`E0530` - Thyrotoxicosis from ectopic thyroid tissue without thyrotoxic crisis or storm<br>`E0531` - Thyrotoxicosis from ectopic thyroid tissue with thyrotoxic crisis or storm<br>`E054` - Thyrotoxicosis factitia<br>`E0540` - Thyrotoxicosis factitia without thyrotoxic crisis or storm<br>`E0541` - Thyrotoxicosis factitia with thyrotoxic crisis or storm<br>`E058` - Other thyrotoxicosis<br>`E0580` - Other thyrotoxicosis without thyrotoxic crisis or storm<br>... +4 more
- Removed (0): none

### 10. `v690_v296_hematemesis_no_r36_k66_diff.csv` - Hematemesis / KEEP

- Message: v690: v296 Hematemesis prune R36/K66 plus DIFF
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 10. `v690_v296_hematemesis_no_r36_k66_diff.csv` - Hematemesis / DIFF

- Message: v690: v296 Hematemesis prune R36/K66 plus DIFF
- Added (2): `K921` - Melena<br>`R042` - Hemoptysis
- Removed (0): none

### 11. `v691_v296_hf_no_i97_diff.csv` - Heart Failure / KEEP

- Message: v691: v296 Heart Failure prune I97 plus DIFF
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 11. `v691_v296_hf_no_i97_diff.csv` - Heart Failure / DIFF

- Message: v691: v296 Heart Failure prune I97 plus DIFF
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 12. `v692_v296_uti_no_obstetric_diff.csv` - UTI / KEEP

- Message: v692: v296 UTI prune obstetric plus DIFF
- Added (0): none
- Removed (29): `O03` - Spontaneous abortion<br>`O0338` - Urinary tract infection following incomplete spontaneous abortion<br>`O0388` - Urinary tract infection following complete or unspecified spontaneous abortion<br>`O23` - Infections of genitourinary tract in pregnancy<br>`O233` - Infections of other parts of urinary tract in pregnancy<br>`O2330` - Infections of other parts of urinary tract in pregnancy, unspecified trimester<br>`O2332` - Infections of other parts of urinary tract in pregnancy, second trimester<br>`O234` - Unspecified infection of urinary tract in pregnancy<br>`O2340` - Unspecified infection of urinary tract in pregnancy, unspecified trimester<br>`O2341` - Unspecified infection of urinary tract in pregnancy, first trimester<br>`O2342` - Unspecified infection of urinary tract in pregnancy, second trimester<br>`O2343` - Unspecified infection of urinary tract in pregnancy, third trimester<br>`O239` - Unspecified genitourinary tract infection in pregnancy<br>`O2390` - Unspecified genitourinary tract infection in pregnancy, unspecified trimester<br>`O2391` - Unspecified genitourinary tract infection in pregnancy, first trimester<br>`O2392` - Unspecified genitourinary tract infection in pregnancy, second trimester<br>`O2393` - Unspecified genitourinary tract infection in pregnancy, third trimester<br>`O86` - Other puerperal infections<br>... +11 more

### 12. `v692_v296_uti_no_obstetric_diff.csv` - UTI / DIFF

- Message: v692: v296 UTI prune obstetric plus DIFF
- Added (39): `N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>`N3030` - Trigonitis without hematuria<br>`N3031` - Trigonitis with hematuria<br>`N304` - Irradiation cystitis<br>`N3040` - Irradiation cystitis without hematuria<br>`N3041` - Irradiation cystitis with hematuria<br>`N308` - Other cystitis<br>`N3080` - Other cystitis without hematuria<br>... +21 more
- Removed (0): none

### 13. `v693_v296_uti_no_n35_diff.csv` - UTI / KEEP

- Message: v693: v296 UTI prune N35 plus DIFF
- Added (0): none
- Removed (3): `N35` - Urethral stricture<br>`N35819` - Other urethral stricture, male, unspecified site<br>`N35919` - Unspecified urethral stricture, male, unspecified site

### 13. `v693_v296_uti_no_n35_diff.csv` - UTI / DIFF

- Message: v693: v296 UTI prune N35 plus DIFF
- Added (39): `N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>`N3030` - Trigonitis without hematuria<br>`N3031` - Trigonitis with hematuria<br>`N304` - Irradiation cystitis<br>`N3040` - Irradiation cystitis without hematuria<br>`N3041` - Irradiation cystitis with hematuria<br>`N308` - Other cystitis<br>`N3080` - Other cystitis without hematuria<br>... +21 more
- Removed (0): none

### 14. `v694_v296_diabetes_no_o24_diff.csv` - Diabetes / KEEP

- Message: v694: v296 Diabetes prune O24 plus DIFF
- Added (0): none
- Removed (57): `O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2412` - Pre-existing type 2 diabetes mellitus, in childbirth<br>`O2413` - Pre-existing type 2 diabetes mellitus, in the puerperium<br>`O243` - Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium<br>... +39 more

### 14. `v694_v296_diabetes_no_o24_diff.csv` - Diabetes / DIFF

- Message: v694: v296 Diabetes prune O24 plus DIFF
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 15. `v695_v296_diabetes_no_z_p70_diff.csv` - Diabetes / KEEP

- Message: v695: v296 Diabetes prune Z/P70 plus DIFF
- Added (0): none
- Removed (9): `P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`P702` - Neonatal diabetes mellitus<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 15. `v695_v296_diabetes_no_z_p70_diff.csv` - Diabetes / DIFF

- Message: v695: v296 Diabetes prune Z/P70 plus DIFF
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 16. `v696_v296_ild_no_j70_diff.csv` - Interstitial Lung Disease / KEEP

- Message: v696: v296 ILD prune J70 plus DIFF
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 16. `v696_v296_ild_no_j70_diff.csv` - Interstitial Lung Disease / DIFF

- Message: v696: v296 ILD prune J70 plus DIFF
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 17. `v697_v296_hypopara_no_e23_e87_p71_e21_diff.csv` - Hypoparathyroidism / KEEP

- Message: v697: v296 Hypopara prune related plus DIFF
- Added (0): none
- Removed (8): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E230` - Hypopituitarism<br>`E231` - Drug-induced hypopituitarism<br>`E87` - Other disorders of fluid, electrolyte and acid-base balance<br>`E876` - Hypokalemia<br>`P71` - Transitory neonatal disorders of calcium and magnesium metabolism<br>`P714` - Transitory neonatal hypoparathyroidism

### 17. `v697_v296_hypopara_no_e23_e87_p71_e21_diff.csv` - Hypoparathyroidism / DIFF

- Message: v697: v296 Hypopara prune related plus DIFF
- Added (10): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E210` - Primary hyperparathyroidism<br>`E211` - Secondary hyperparathyroidism, not elsewhere classified<br>`E212` - Other hyperparathyroidism<br>`E213` - Hyperparathyroidism, unspecified<br>`E214` - Other specified disorders of parathyroid gland<br>`E215` - Disorder of parathyroid gland, unspecified<br>`E55` - Vitamin D deficiency<br>`E550` - Rickets, active<br>`E559` - Vitamin D deficiency, unspecified
- Removed (0): none

### 18. `v698_v296_hyperthyroid_no_e04_e01_e03_p72_diff.csv` - Hyperthyroidism / KEEP

- Message: v698: v296 Hyperthyroid prune non-hyper plus DIFF
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 18. `v698_v296_hyperthyroid_no_e04_e01_e03_p72_diff.csv` - Hyperthyroidism / DIFF

- Message: v698: v296 Hyperthyroid prune non-hyper plus DIFF
- Added (15): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`F41` - Other anxiety disorders<br>`F410` - Panic disorder [episodic paroxysmal anxiety]<br>`F411` - Generalized anxiety disorder<br>`F413` - Other mixed anxiety disorders<br>`F418` - Other specified anxiety disorders<br>`F419` - Anxiety disorder, unspecified
- Removed (0): none

### 19. `v699_v296_pneumonia_no_a37_p23_j84_j85_diff.csv` - Pneumonia / KEEP

- Message: v699: v296 Pneumonia prune noisy plus DIFF
- Added (0): none
- Removed (30): `A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`J84` - Other interstitial pulmonary diseases<br>`J8411` - Idiopathic interstitial pneumonia<br>`J84111` - Idiopathic interstitial pneumonia, not otherwise specified<br>`J84116` - Cryptogenic organizing pneumonia<br>`J84117` - Desquamative interstitial pneumonia<br>`J842` - Lymphoid interstitial pneumonia<br>`J85` - Abscess of lung and mediastinum<br>`J850` - Gangrene and necrosis of lung<br>`J851` - Abscess of lung with pneumonia<br>... +12 more

### 19. `v699_v296_pneumonia_no_a37_p23_j84_j85_diff.csv` - Pneumonia / DIFF

- Message: v699: v296 Pneumonia prune noisy plus DIFF
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 20. `v700_v296_derm_no_b37_diff.csv` - Dermatomycosis / KEEP

- Message: v700: v296 Dermatomycosis prune B37 plus DIFF
- Added (0): none
- Removed (21): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +3 more

### 20. `v700_v296_derm_no_b37_diff.csv` - Dermatomycosis / DIFF

- Message: v700: v296 Dermatomycosis prune B37 plus DIFF
- Added (33): `L40` - Psoriasis<br>`L400` - Psoriasis vulgaris<br>`L401` - Generalized pustular psoriasis<br>`L402` - Acrodermatitis continua<br>`L403` - Pustulosis palmaris et plantaris<br>`L404` - Guttate psoriasis<br>`L405` - Arthropathic psoriasis<br>`L4050` - Arthropathic psoriasis, unspecified<br>`L4051` - Distal interphalangeal psoriatic arthropathy<br>`L4052` - Psoriatic arthritis mutilans<br>`L4053` - Psoriatic spondylitis<br>`L4054` - Psoriatic juvenile arthropathy<br>`L4059` - Other psoriatic arthropathy<br>`L408` - Other psoriasis<br>`L409` - Psoriasis, unspecified<br>`L20` - Atopic dermatitis<br>`L200` - Besnier's prurigo<br>`L208` - Other atopic dermatitis<br>... +15 more
- Removed (0): none
