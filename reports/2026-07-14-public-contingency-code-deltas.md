# CohortX Plan Code Deltas - 2026-07-14-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-14-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 60
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v721_v296_icp_no_g96_g94_assocdiff.csv` | Intracranial Pressure | KEEP | 0 | 4 | v721: v296 ICP prune G96/G94 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 1 | `submissions/v721_v296_icp_no_g96_g94_assocdiff.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v721: v296 ICP prune G96/G94 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 1 | `submissions/v721_v296_icp_no_g96_g94_assocdiff.csv` | Intracranial Pressure | DIFF | 97 | 0 | v721: v296 ICP prune G96/G94 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 2 | `submissions/v722_v296_gout_no_e79_assocdiff.csv` | Gout | KEEP | 0 | 2 | v722: v296 Gout prune E79 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 2 | `submissions/v722_v296_gout_no_e79_assocdiff.csv` | Gout | ASSOCIATION | 17 | 0 | v722: v296 Gout prune E79 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 2 | `submissions/v722_v296_gout_no_e79_assocdiff.csv` | Gout | DIFF | 260 | 0 | v722: v296 Gout prune E79 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 3 | `submissions/v723_v296_pleurisy_no_r09_j95_assocdiff.csv` | Pleurisy | KEEP | 0 | 12 | v723: v296 Pleurisy prune R09/J95 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 3 | `submissions/v723_v296_pleurisy_no_r09_j95_assocdiff.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v723: v296 Pleurisy prune R09/J95 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 3 | `submissions/v723_v296_pleurisy_no_r09_j95_assocdiff.csv` | Pleurisy | DIFF | 17 | 0 | v723: v296 Pleurisy prune R09/J95 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 4 | `submissions/v724_v296_bronchitis_no_j43_j68_assocdiff.csv` | Bronchitis | KEEP | 0 | 8 | v724: v296 Bronchitis prune J43/J68 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 4 | `submissions/v724_v296_bronchitis_no_j43_j68_assocdiff.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v724: v296 Bronchitis prune J43/J68 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 4 | `submissions/v724_v296_bronchitis_no_j43_j68_assocdiff.csv` | Bronchitis | DIFF | 32 | 0 | v724: v296 Bronchitis prune J43/J68 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 5 | `submissions/v725_v296_thyroiditis_no_e03_assocdiff.csv` | Thyroiditis | KEEP | 0 | 2 | v725: v296 Thyroiditis prune E03 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 5 | `submissions/v725_v296_thyroiditis_no_e03_assocdiff.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v725: v296 Thyroiditis prune E03 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 5 | `submissions/v725_v296_thyroiditis_no_e03_assocdiff.csv` | Thyroiditis | DIFF | 6 | 0 | v725: v296 Thyroiditis prune E03 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 6 | `submissions/v726_v296_npc_no_d00_c44_d10_assocdiff.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 18 | v726: v296 NPC prune D00/C44/D10 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 6 | `submissions/v726_v296_npc_no_d00_c44_d10_assocdiff.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v726: v296 NPC prune D00/C44/D10 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 6 | `submissions/v726_v296_npc_no_d00_c44_d10_assocdiff.csv` | Nasopharyngeal Carcinoma | DIFF | 17 | 0 | v726: v296 NPC prune D00/C44/D10 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 7 | `submissions/v727_v296_ckd_no_q60_q61_q62_assocdiff.csv` | CKD | KEEP | 0 | 43 | v727: v296 CKD prune congenital Q plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 7 | `submissions/v727_v296_ckd_no_q60_q61_q62_assocdiff.csv` | CKD | ASSOCIATION | 17 | 0 | v727: v296 CKD prune congenital Q plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 7 | `submissions/v727_v296_ckd_no_q60_q61_q62_assocdiff.csv` | CKD | DIFF | 6 | 0 | v727: v296 CKD prune congenital Q plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 8 | `submissions/v728_v296_ckd_no_i50_assocdiff.csv` | CKD | KEEP | 0 | 3 | v728: v296 CKD prune I50 plus ASSOC+DIFF | small CKD KEEP prune plus CKD ASSOC+DIFF |
| 8 | `submissions/v728_v296_ckd_no_i50_assocdiff.csv` | CKD | ASSOCIATION | 17 | 0 | v728: v296 CKD prune I50 plus ASSOC+DIFF | small CKD KEEP prune plus CKD ASSOC+DIFF |
| 8 | `submissions/v728_v296_ckd_no_i50_assocdiff.csv` | CKD | DIFF | 6 | 0 | v728: v296 CKD prune I50 plus ASSOC+DIFF | small CKD KEEP prune plus CKD ASSOC+DIFF |
| 9 | `submissions/v729_v296_hypothyroid_no_e04_assocdiff.csv` | Hypothyroidism | KEEP | 0 | 6 | v729: v296 Hypothyroidism prune E04 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 9 | `submissions/v729_v296_hypothyroid_no_e04_assocdiff.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v729: v296 Hypothyroidism prune E04 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 9 | `submissions/v729_v296_hypothyroid_no_e04_assocdiff.csv` | Hypothyroidism | DIFF | 22 | 0 | v729: v296 Hypothyroidism prune E04 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 10 | `submissions/v730_v296_hematemesis_no_r36_k66_assocdiff.csv` | Hematemesis | KEEP | 0 | 4 | v730: v296 Hematemesis prune R36/K66 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 10 | `submissions/v730_v296_hematemesis_no_r36_k66_assocdiff.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v730: v296 Hematemesis prune R36/K66 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 10 | `submissions/v730_v296_hematemesis_no_r36_k66_assocdiff.csv` | Hematemesis | DIFF | 2 | 0 | v730: v296 Hematemesis prune R36/K66 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 11 | `submissions/v731_v296_hf_no_i97_assocdiff.csv` | Heart Failure | KEEP | 0 | 31 | v731: v296 Heart Failure prune I97 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 11 | `submissions/v731_v296_hf_no_i97_assocdiff.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v731: v296 Heart Failure prune I97 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 11 | `submissions/v731_v296_hf_no_i97_assocdiff.csv` | Heart Failure | DIFF | 15 | 0 | v731: v296 Heart Failure prune I97 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 12 | `submissions/v732_v296_uti_no_obstetric_assocdiff.csv` | UTI | KEEP | 0 | 29 | v732: v296 UTI prune obstetric plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 12 | `submissions/v732_v296_uti_no_obstetric_assocdiff.csv` | UTI | ASSOCIATION | 20 | 0 | v732: v296 UTI prune obstetric plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 12 | `submissions/v732_v296_uti_no_obstetric_assocdiff.csv` | UTI | DIFF | 39 | 0 | v732: v296 UTI prune obstetric plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 13 | `submissions/v733_v296_uti_no_n35_assocdiff.csv` | UTI | KEEP | 0 | 3 | v733: v296 UTI prune N35 plus ASSOC+DIFF | small UTI KEEP prune plus UTI ASSOC+DIFF |
| 13 | `submissions/v733_v296_uti_no_n35_assocdiff.csv` | UTI | ASSOCIATION | 20 | 0 | v733: v296 UTI prune N35 plus ASSOC+DIFF | small UTI KEEP prune plus UTI ASSOC+DIFF |
| 13 | `submissions/v733_v296_uti_no_n35_assocdiff.csv` | UTI | DIFF | 39 | 0 | v733: v296 UTI prune N35 plus ASSOC+DIFF | small UTI KEEP prune plus UTI ASSOC+DIFF |
| 14 | `submissions/v734_v296_diabetes_no_o24_assocdiff.csv` | Diabetes | KEEP | 0 | 57 | v734: v296 Diabetes prune O24 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 14 | `submissions/v734_v296_diabetes_no_o24_assocdiff.csv` | Diabetes | ASSOCIATION | 116 | 0 | v734: v296 Diabetes prune O24 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 14 | `submissions/v734_v296_diabetes_no_o24_assocdiff.csv` | Diabetes | DIFF | 7 | 0 | v734: v296 Diabetes prune O24 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 15 | `submissions/v735_v296_diabetes_no_z_p70_assocdiff.csv` | Diabetes | KEEP | 0 | 9 | v735: v296 Diabetes prune Z/P70 plus ASSOC+DIFF | small Diabetes KEEP prune plus Diabetes ASSOC+DIFF |
| 15 | `submissions/v735_v296_diabetes_no_z_p70_assocdiff.csv` | Diabetes | ASSOCIATION | 116 | 0 | v735: v296 Diabetes prune Z/P70 plus ASSOC+DIFF | small Diabetes KEEP prune plus Diabetes ASSOC+DIFF |
| 15 | `submissions/v735_v296_diabetes_no_z_p70_assocdiff.csv` | Diabetes | DIFF | 7 | 0 | v735: v296 Diabetes prune Z/P70 plus ASSOC+DIFF | small Diabetes KEEP prune plus Diabetes ASSOC+DIFF |
| 16 | `submissions/v736_v296_ild_no_j70_assocdiff.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v736: v296 ILD prune J70 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 16 | `submissions/v736_v296_ild_no_j70_assocdiff.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v736: v296 ILD prune J70 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 16 | `submissions/v736_v296_ild_no_j70_assocdiff.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v736: v296 ILD prune J70 plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 17 | `submissions/v737_v296_hypopara_no_e23_e87_p71_e21_assocdiff.csv` | Hypoparathyroidism | KEEP | 0 | 8 | v737: v296 Hypopara prune related plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 17 | `submissions/v737_v296_hypopara_no_e23_e87_p71_e21_assocdiff.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v737: v296 Hypopara prune related plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 17 | `submissions/v737_v296_hypopara_no_e23_e87_p71_e21_assocdiff.csv` | Hypoparathyroidism | DIFF | 10 | 0 | v737: v296 Hypopara prune related plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 18 | `submissions/v738_v296_hyperthyroid_no_e04_e01_e03_p72_assocdiff.csv` | Hyperthyroidism | KEEP | 0 | 12 | v738: v296 Hyperthyroid prune non-hyper plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 18 | `submissions/v738_v296_hyperthyroid_no_e04_e01_e03_p72_assocdiff.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v738: v296 Hyperthyroid prune non-hyper plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 18 | `submissions/v738_v296_hyperthyroid_no_e04_e01_e03_p72_assocdiff.csv` | Hyperthyroidism | DIFF | 15 | 0 | v738: v296 Hyperthyroid prune non-hyper plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 19 | `submissions/v739_v296_pneumonia_no_a37_p23_j84_j85_assocdiff.csv` | Pneumonia | KEEP | 0 | 30 | v739: v296 Pneumonia prune noisy plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 19 | `submissions/v739_v296_pneumonia_no_a37_p23_j84_j85_assocdiff.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v739: v296 Pneumonia prune noisy plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 19 | `submissions/v739_v296_pneumonia_no_a37_p23_j84_j85_assocdiff.csv` | Pneumonia | DIFF | 71 | 0 | v739: v296 Pneumonia prune noisy plus ASSOC+DIFF | same-condition KEEP precision plus broad ASSOC+DIFF |
| 20 | `submissions/v740_v296_derm_no_b37_assocdiff.csv` | Dermatomycosis | KEEP | 0 | 21 | v740: v296 Dermatomycosis prune B37 plus ASSOC+DIFF | new Dermatomycosis KEEP precision plus broad ASSOC+DIFF |
| 20 | `submissions/v740_v296_derm_no_b37_assocdiff.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v740: v296 Dermatomycosis prune B37 plus ASSOC+DIFF | new Dermatomycosis KEEP precision plus broad ASSOC+DIFF |
| 20 | `submissions/v740_v296_derm_no_b37_assocdiff.csv` | Dermatomycosis | DIFF | 33 | 0 | v740: v296 Dermatomycosis prune B37 plus ASSOC+DIFF | new Dermatomycosis KEEP precision plus broad ASSOC+DIFF |

## Exact Code Changes

### 1. `v721_v296_icp_no_g96_g94_assocdiff.csv` - Intracranial Pressure / KEEP

- Message: v721: v296 ICP prune G96/G94 plus ASSOC+DIFF
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 1. `v721_v296_icp_no_g96_g94_assocdiff.csv` - Intracranial Pressure / ASSOCIATION

- Message: v721: v296 ICP prune G96/G94 plus ASSOC+DIFF
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none
### 1. `v721_v296_icp_no_g96_g94_assocdiff.csv` - Intracranial Pressure / DIFF

- Message: v721: v296 ICP prune G96/G94 plus ASSOC+DIFF
- Added (97): `G43` - Migraine<br>`G430` - Migraine without aura<br>`G4300` - Migraine without aura, not intractable<br>`G43001` - Migraine without aura, not intractable, with status migrainosus<br>`G43009` - Migraine without aura, not intractable, without status migrainosus<br>`G4301` - Migraine without aura, intractable<br>`G43011` - Migraine without aura, intractable, with status migrainosus<br>`G43019` - Migraine without aura, intractable, without status migrainosus<br>`G431` - Migraine with aura<br>`G4310` - Migraine with aura, not intractable<br>`G43101` - Migraine with aura, not intractable, with status migrainosus<br>`G43109` - Migraine with aura, not intractable, without status migrainosus<br>`G4311` - Migraine with aura, intractable<br>`G43111` - Migraine with aura, intractable, with status migrainosus<br>`G43119` - Migraine with aura, intractable, without status migrainosus<br>`G434` - Hemiplegic migraine<br>`G4340` - Hemiplegic migraine, not intractable<br>`G43401` - Hemiplegic migraine, not intractable, with status migrainosus<br>... +79 more
- Removed (0): none

### 2. `v722_v296_gout_no_e79_assocdiff.csv` - Gout / KEEP

- Message: v722: v296 Gout prune E79 plus ASSOC+DIFF
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 2. `v722_v296_gout_no_e79_assocdiff.csv` - Gout / ASSOCIATION

- Message: v722: v296 Gout prune E79 plus ASSOC+DIFF
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 2. `v722_v296_gout_no_e79_assocdiff.csv` - Gout / DIFF

- Message: v722: v296 Gout prune E79 plus ASSOC+DIFF
- Added (260): `M00` - Pyogenic arthritis<br>`M000` - Staphylococcal arthritis and polyarthritis<br>`M0000` - Staphylococcal arthritis, unspecified joint<br>`M0001` - Staphylococcal arthritis, shoulder<br>`M00011` - Staphylococcal arthritis, right shoulder<br>`M00012` - Staphylococcal arthritis, left shoulder<br>`M00019` - Staphylococcal arthritis, unspecified shoulder<br>`M0002` - Staphylococcal arthritis, elbow<br>`M00021` - Staphylococcal arthritis, right elbow<br>`M00022` - Staphylococcal arthritis, left elbow<br>`M00029` - Staphylococcal arthritis, unspecified elbow<br>`M0003` - Staphylococcal arthritis, wrist<br>`M00031` - Staphylococcal arthritis, right wrist<br>`M00032` - Staphylococcal arthritis, left wrist<br>`M00039` - Staphylococcal arthritis, unspecified wrist<br>`M0004` - Staphylococcal arthritis, hand<br>`M00041` - Staphylococcal arthritis, right hand<br>`M00042` - Staphylococcal arthritis, left hand<br>... +242 more
- Removed (0): none

### 3. `v723_v296_pleurisy_no_r09_j95_assocdiff.csv` - Pleurisy / KEEP

- Message: v723: v296 Pleurisy prune R09/J95 plus ASSOC+DIFF
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 3. `v723_v296_pleurisy_no_r09_j95_assocdiff.csv` - Pleurisy / ASSOCIATION

- Message: v723: v296 Pleurisy prune R09/J95 plus ASSOC+DIFF
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 3. `v723_v296_pleurisy_no_r09_j95_assocdiff.csv` - Pleurisy / DIFF

- Message: v723: v296 Pleurisy prune R09/J95 plus ASSOC+DIFF
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 4. `v724_v296_bronchitis_no_j43_j68_assocdiff.csv` - Bronchitis / KEEP

- Message: v724: v296 Bronchitis prune J43/J68 plus ASSOC+DIFF
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 4. `v724_v296_bronchitis_no_j43_j68_assocdiff.csv` - Bronchitis / ASSOCIATION

- Message: v724: v296 Bronchitis prune J43/J68 plus ASSOC+DIFF
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 4. `v724_v296_bronchitis_no_j43_j68_assocdiff.csv` - Bronchitis / DIFF

- Message: v724: v296 Bronchitis prune J43/J68 plus ASSOC+DIFF
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 5. `v725_v296_thyroiditis_no_e03_assocdiff.csv` - Thyroiditis / KEEP

- Message: v725: v296 Thyroiditis prune E03 plus ASSOC+DIFF
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 5. `v725_v296_thyroiditis_no_e03_assocdiff.csv` - Thyroiditis / ASSOCIATION

- Message: v725: v296 Thyroiditis prune E03 plus ASSOC+DIFF
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 5. `v725_v296_thyroiditis_no_e03_assocdiff.csv` - Thyroiditis / DIFF

- Message: v725: v296 Thyroiditis prune E03 plus ASSOC+DIFF
- Added (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified
- Removed (0): none

### 6. `v726_v296_npc_no_d00_c44_d10_assocdiff.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v726: v296 NPC prune D00/C44/D10 plus ASSOC+DIFF
- Added (0): none
- Removed (18): `C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`D00` - Carcinoma in situ of oral cavity, esophagus and stomach<br>`D000` - Carcinoma in situ of lip, oral cavity and pharynx<br>`D0000` - Carcinoma in situ of oral cavity, unspecified site<br>`D0001` - Carcinoma in situ of labial mucosa and vermilion border<br>`D0002` - Carcinoma in situ of buccal mucosa<br>`D0003` - Carcinoma in situ of gingiva and edentulous alveolar ridge<br>`D0004` - Carcinoma in situ of soft palate<br>`D0005` - Carcinoma in situ of hard palate<br>`D0006` - Carcinoma in situ of floor of mouth<br>`D0007` - Carcinoma in situ of tongue<br>`D0008` - Carcinoma in situ of pharynx<br>`D10` - Benign neoplasm of mouth and pharynx<br>`D101` - Benign neoplasm of tongue<br>`D106` - Benign neoplasm of nasopharynx<br>`D107` - Benign neoplasm of hypopharynx

### 6. `v726_v296_npc_no_d00_c44_d10_assocdiff.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v726: v296 NPC prune D00/C44/D10 plus ASSOC+DIFF
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 6. `v726_v296_npc_no_d00_c44_d10_assocdiff.csv` - Nasopharyngeal Carcinoma / DIFF

- Message: v726: v296 NPC prune D00/C44/D10 plus ASSOC+DIFF
- Added (17): `C10` - Malignant neoplasm of oropharynx<br>`C100` - Malignant neoplasm of vallecula<br>`C101` - Malignant neoplasm of anterior surface of epiglottis<br>`C102` - Malignant neoplasm of lateral wall of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C104` - Malignant neoplasm of branchial cleft<br>`C108` - Malignant neoplasm of overlapping sites of oropharynx<br>`C109` - Malignant neoplasm of oropharynx, unspecified<br>`C14` - Malignant neoplasm of other and ill-defined sites in the lip, oral cavity and pharynx<br>`C140` - Malignant neoplasm of pharynx, unspecified<br>`C142` - Malignant neoplasm of Waldeyer's ring<br>`C148` - Malignant neoplasm of overlapping sites of lip, oral cavity and pharynx<br>`J33` - Nasal polyp<br>`J330` - Polyp of nasal cavity<br>`J331` - Polypoid sinus degeneration<br>`J338` - Other polyp of sinus<br>`J339` - Nasal polyp, unspecified
- Removed (0): none

### 7. `v727_v296_ckd_no_q60_q61_q62_assocdiff.csv` - CKD / KEEP

- Message: v727: v296 CKD prune congenital Q plus ASSOC+DIFF
- Added (0): none
- Removed (43): `Q60` - Renal agenesis and other reduction defects of kidney<br>`Q600` - Renal agenesis, unilateral<br>`Q601` - Renal agenesis, bilateral<br>`Q602` - Renal agenesis, unspecified<br>`Q603` - Renal hypoplasia, unilateral<br>`Q604` - Renal hypoplasia, bilateral<br>`Q605` - Renal hypoplasia, unspecified<br>`Q606` - Potter's syndrome<br>`Q61` - Cystic kidney disease<br>`Q610` - Congenital renal cyst<br>`Q6100` - Congenital renal cyst, unspecified<br>`Q6101` - Congenital single renal cyst<br>`Q6102` - Congenital multiple renal cysts<br>`Q611` - Polycystic kidney, infantile type<br>`Q6111` - Cystic dilatation of collecting ducts<br>`Q6119` - Other polycystic kidney, infantile type<br>`Q612` - Polycystic kidney, adult type<br>`Q613` - Polycystic kidney, unspecified<br>... +25 more

### 7. `v727_v296_ckd_no_q60_q61_q62_assocdiff.csv` - CKD / ASSOCIATION

- Message: v727: v296 CKD prune congenital Q plus ASSOC+DIFF
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 7. `v727_v296_ckd_no_q60_q61_q62_assocdiff.csv` - CKD / DIFF

- Message: v727: v296 CKD prune congenital Q plus ASSOC+DIFF
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 8. `v728_v296_ckd_no_i50_assocdiff.csv` - CKD / KEEP

- Message: v728: v296 CKD prune I50 plus ASSOC+DIFF
- Added (0): none
- Removed (3): `I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure

### 8. `v728_v296_ckd_no_i50_assocdiff.csv` - CKD / ASSOCIATION

- Message: v728: v296 CKD prune I50 plus ASSOC+DIFF
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 8. `v728_v296_ckd_no_i50_assocdiff.csv` - CKD / DIFF

- Message: v728: v296 CKD prune I50 plus ASSOC+DIFF
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 9. `v729_v296_hypothyroid_no_e04_assocdiff.csv` - Hypothyroidism / KEEP

- Message: v729: v296 Hypothyroidism prune E04 plus ASSOC+DIFF
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 9. `v729_v296_hypothyroid_no_e04_assocdiff.csv` - Hypothyroidism / ASSOCIATION

- Message: v729: v296 Hypothyroidism prune E04 plus ASSOC+DIFF
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 9. `v729_v296_hypothyroid_no_e04_assocdiff.csv` - Hypothyroidism / DIFF

- Message: v729: v296 Hypothyroidism prune E04 plus ASSOC+DIFF
- Added (22): `E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>`E0521` - Thyrotoxicosis with toxic multinodular goiter with thyrotoxic crisis or storm<br>`E053` - Thyrotoxicosis from ectopic thyroid tissue<br>`E0530` - Thyrotoxicosis from ectopic thyroid tissue without thyrotoxic crisis or storm<br>`E0531` - Thyrotoxicosis from ectopic thyroid tissue with thyrotoxic crisis or storm<br>`E054` - Thyrotoxicosis factitia<br>`E0540` - Thyrotoxicosis factitia without thyrotoxic crisis or storm<br>`E0541` - Thyrotoxicosis factitia with thyrotoxic crisis or storm<br>`E058` - Other thyrotoxicosis<br>`E0580` - Other thyrotoxicosis without thyrotoxic crisis or storm<br>... +4 more
- Removed (0): none

### 10. `v730_v296_hematemesis_no_r36_k66_assocdiff.csv` - Hematemesis / KEEP

- Message: v730: v296 Hematemesis prune R36/K66 plus ASSOC+DIFF
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 10. `v730_v296_hematemesis_no_r36_k66_assocdiff.csv` - Hematemesis / ASSOCIATION

- Message: v730: v296 Hematemesis prune R36/K66 plus ASSOC+DIFF
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 10. `v730_v296_hematemesis_no_r36_k66_assocdiff.csv` - Hematemesis / DIFF

- Message: v730: v296 Hematemesis prune R36/K66 plus ASSOC+DIFF
- Added (2): `K921` - Melena<br>`R042` - Hemoptysis
- Removed (0): none

### 11. `v731_v296_hf_no_i97_assocdiff.csv` - Heart Failure / KEEP

- Message: v731: v296 Heart Failure prune I97 plus ASSOC+DIFF
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 11. `v731_v296_hf_no_i97_assocdiff.csv` - Heart Failure / ASSOCIATION

- Message: v731: v296 Heart Failure prune I97 plus ASSOC+DIFF
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 11. `v731_v296_hf_no_i97_assocdiff.csv` - Heart Failure / DIFF

- Message: v731: v296 Heart Failure prune I97 plus ASSOC+DIFF
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 12. `v732_v296_uti_no_obstetric_assocdiff.csv` - UTI / KEEP

- Message: v732: v296 UTI prune obstetric plus ASSOC+DIFF
- Added (0): none
- Removed (29): `O03` - Spontaneous abortion<br>`O0338` - Urinary tract infection following incomplete spontaneous abortion<br>`O0388` - Urinary tract infection following complete or unspecified spontaneous abortion<br>`O23` - Infections of genitourinary tract in pregnancy<br>`O233` - Infections of other parts of urinary tract in pregnancy<br>`O2330` - Infections of other parts of urinary tract in pregnancy, unspecified trimester<br>`O2332` - Infections of other parts of urinary tract in pregnancy, second trimester<br>`O234` - Unspecified infection of urinary tract in pregnancy<br>`O2340` - Unspecified infection of urinary tract in pregnancy, unspecified trimester<br>`O2341` - Unspecified infection of urinary tract in pregnancy, first trimester<br>`O2342` - Unspecified infection of urinary tract in pregnancy, second trimester<br>`O2343` - Unspecified infection of urinary tract in pregnancy, third trimester<br>`O239` - Unspecified genitourinary tract infection in pregnancy<br>`O2390` - Unspecified genitourinary tract infection in pregnancy, unspecified trimester<br>`O2391` - Unspecified genitourinary tract infection in pregnancy, first trimester<br>`O2392` - Unspecified genitourinary tract infection in pregnancy, second trimester<br>`O2393` - Unspecified genitourinary tract infection in pregnancy, third trimester<br>`O86` - Other puerperal infections<br>... +11 more

### 12. `v732_v296_uti_no_obstetric_assocdiff.csv` - UTI / ASSOCIATION

- Message: v732: v296 UTI prune obstetric plus ASSOC+DIFF
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 12. `v732_v296_uti_no_obstetric_assocdiff.csv` - UTI / DIFF

- Message: v732: v296 UTI prune obstetric plus ASSOC+DIFF
- Added (39): `N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>`N3030` - Trigonitis without hematuria<br>`N3031` - Trigonitis with hematuria<br>`N304` - Irradiation cystitis<br>`N3040` - Irradiation cystitis without hematuria<br>`N3041` - Irradiation cystitis with hematuria<br>`N308` - Other cystitis<br>`N3080` - Other cystitis without hematuria<br>... +21 more
- Removed (0): none

### 13. `v733_v296_uti_no_n35_assocdiff.csv` - UTI / KEEP

- Message: v733: v296 UTI prune N35 plus ASSOC+DIFF
- Added (0): none
- Removed (3): `N35` - Urethral stricture<br>`N35819` - Other urethral stricture, male, unspecified site<br>`N35919` - Unspecified urethral stricture, male, unspecified site

### 13. `v733_v296_uti_no_n35_assocdiff.csv` - UTI / ASSOCIATION

- Message: v733: v296 UTI prune N35 plus ASSOC+DIFF
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 13. `v733_v296_uti_no_n35_assocdiff.csv` - UTI / DIFF

- Message: v733: v296 UTI prune N35 plus ASSOC+DIFF
- Added (39): `N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>`N3030` - Trigonitis without hematuria<br>`N3031` - Trigonitis with hematuria<br>`N304` - Irradiation cystitis<br>`N3040` - Irradiation cystitis without hematuria<br>`N3041` - Irradiation cystitis with hematuria<br>`N308` - Other cystitis<br>`N3080` - Other cystitis without hematuria<br>... +21 more
- Removed (0): none

### 14. `v734_v296_diabetes_no_o24_assocdiff.csv` - Diabetes / KEEP

- Message: v734: v296 Diabetes prune O24 plus ASSOC+DIFF
- Added (0): none
- Removed (57): `O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2412` - Pre-existing type 2 diabetes mellitus, in childbirth<br>`O2413` - Pre-existing type 2 diabetes mellitus, in the puerperium<br>`O243` - Unspecified pre-existing diabetes mellitus in pregnancy, childbirth and the puerperium<br>... +39 more

### 14. `v734_v296_diabetes_no_o24_assocdiff.csv` - Diabetes / ASSOCIATION

- Message: v734: v296 Diabetes prune O24 plus ASSOC+DIFF
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 14. `v734_v296_diabetes_no_o24_assocdiff.csv` - Diabetes / DIFF

- Message: v734: v296 Diabetes prune O24 plus ASSOC+DIFF
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 15. `v735_v296_diabetes_no_z_p70_assocdiff.csv` - Diabetes / KEEP

- Message: v735: v296 Diabetes prune Z/P70 plus ASSOC+DIFF
- Added (0): none
- Removed (9): `P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`P702` - Neonatal diabetes mellitus<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 15. `v735_v296_diabetes_no_z_p70_assocdiff.csv` - Diabetes / ASSOCIATION

- Message: v735: v296 Diabetes prune Z/P70 plus ASSOC+DIFF
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 15. `v735_v296_diabetes_no_z_p70_assocdiff.csv` - Diabetes / DIFF

- Message: v735: v296 Diabetes prune Z/P70 plus ASSOC+DIFF
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 16. `v736_v296_ild_no_j70_assocdiff.csv` - Interstitial Lung Disease / KEEP

- Message: v736: v296 ILD prune J70 plus ASSOC+DIFF
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 16. `v736_v296_ild_no_j70_assocdiff.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v736: v296 ILD prune J70 plus ASSOC+DIFF
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 16. `v736_v296_ild_no_j70_assocdiff.csv` - Interstitial Lung Disease / DIFF

- Message: v736: v296 ILD prune J70 plus ASSOC+DIFF
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 17. `v737_v296_hypopara_no_e23_e87_p71_e21_assocdiff.csv` - Hypoparathyroidism / KEEP

- Message: v737: v296 Hypopara prune related plus ASSOC+DIFF
- Added (0): none
- Removed (8): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E230` - Hypopituitarism<br>`E231` - Drug-induced hypopituitarism<br>`E87` - Other disorders of fluid, electrolyte and acid-base balance<br>`E876` - Hypokalemia<br>`P71` - Transitory neonatal disorders of calcium and magnesium metabolism<br>`P714` - Transitory neonatal hypoparathyroidism

### 17. `v737_v296_hypopara_no_e23_e87_p71_e21_assocdiff.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v737: v296 Hypopara prune related plus ASSOC+DIFF
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 17. `v737_v296_hypopara_no_e23_e87_p71_e21_assocdiff.csv` - Hypoparathyroidism / DIFF

- Message: v737: v296 Hypopara prune related plus ASSOC+DIFF
- Added (10): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E210` - Primary hyperparathyroidism<br>`E211` - Secondary hyperparathyroidism, not elsewhere classified<br>`E212` - Other hyperparathyroidism<br>`E213` - Hyperparathyroidism, unspecified<br>`E214` - Other specified disorders of parathyroid gland<br>`E215` - Disorder of parathyroid gland, unspecified<br>`E55` - Vitamin D deficiency<br>`E550` - Rickets, active<br>`E559` - Vitamin D deficiency, unspecified
- Removed (0): none

### 18. `v738_v296_hyperthyroid_no_e04_e01_e03_p72_assocdiff.csv` - Hyperthyroidism / KEEP

- Message: v738: v296 Hyperthyroid prune non-hyper plus ASSOC+DIFF
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 18. `v738_v296_hyperthyroid_no_e04_e01_e03_p72_assocdiff.csv` - Hyperthyroidism / ASSOCIATION

- Message: v738: v296 Hyperthyroid prune non-hyper plus ASSOC+DIFF
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 18. `v738_v296_hyperthyroid_no_e04_e01_e03_p72_assocdiff.csv` - Hyperthyroidism / DIFF

- Message: v738: v296 Hyperthyroid prune non-hyper plus ASSOC+DIFF
- Added (15): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`F41` - Other anxiety disorders<br>`F410` - Panic disorder [episodic paroxysmal anxiety]<br>`F411` - Generalized anxiety disorder<br>`F413` - Other mixed anxiety disorders<br>`F418` - Other specified anxiety disorders<br>`F419` - Anxiety disorder, unspecified
- Removed (0): none

### 19. `v739_v296_pneumonia_no_a37_p23_j84_j85_assocdiff.csv` - Pneumonia / KEEP

- Message: v739: v296 Pneumonia prune noisy plus ASSOC+DIFF
- Added (0): none
- Removed (30): `A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`J84` - Other interstitial pulmonary diseases<br>`J8411` - Idiopathic interstitial pneumonia<br>`J84111` - Idiopathic interstitial pneumonia, not otherwise specified<br>`J84116` - Cryptogenic organizing pneumonia<br>`J84117` - Desquamative interstitial pneumonia<br>`J842` - Lymphoid interstitial pneumonia<br>`J85` - Abscess of lung and mediastinum<br>`J850` - Gangrene and necrosis of lung<br>`J851` - Abscess of lung with pneumonia<br>... +12 more

### 19. `v739_v296_pneumonia_no_a37_p23_j84_j85_assocdiff.csv` - Pneumonia / ASSOCIATION

- Message: v739: v296 Pneumonia prune noisy plus ASSOC+DIFF
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 19. `v739_v296_pneumonia_no_a37_p23_j84_j85_assocdiff.csv` - Pneumonia / DIFF

- Message: v739: v296 Pneumonia prune noisy plus ASSOC+DIFF
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 20. `v740_v296_derm_no_b37_assocdiff.csv` - Dermatomycosis / KEEP

- Message: v740: v296 Dermatomycosis prune B37 plus ASSOC+DIFF
- Added (0): none
- Removed (21): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +3 more

### 20. `v740_v296_derm_no_b37_assocdiff.csv` - Dermatomycosis / ASSOCIATION

- Message: v740: v296 Dermatomycosis prune B37 plus ASSOC+DIFF
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 20. `v740_v296_derm_no_b37_assocdiff.csv` - Dermatomycosis / DIFF

- Message: v740: v296 Dermatomycosis prune B37 plus ASSOC+DIFF
- Added (33): `L40` - Psoriasis<br>`L400` - Psoriasis vulgaris<br>`L401` - Generalized pustular psoriasis<br>`L402` - Acrodermatitis continua<br>`L403` - Pustulosis palmaris et plantaris<br>`L404` - Guttate psoriasis<br>`L405` - Arthropathic psoriasis<br>`L4050` - Arthropathic psoriasis, unspecified<br>`L4051` - Distal interphalangeal psoriatic arthropathy<br>`L4052` - Psoriatic arthritis mutilans<br>`L4053` - Psoriatic spondylitis<br>`L4054` - Psoriatic juvenile arthropathy<br>`L4059` - Other psoriatic arthropathy<br>`L408` - Other psoriasis<br>`L409` - Psoriasis, unspecified<br>`L20` - Atopic dermatitis<br>`L200` - Besnier's prurigo<br>`L208` - Other atopic dermatitis<br>... +15 more
- Removed (0): none
