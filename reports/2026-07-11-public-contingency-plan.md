# CohortX Plan Report — 2026-07-11-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-11-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20

## Planned Changes

| Order | File | Changed conditions | Message | Notes |
|---:|---|---|---|---|
| 1 | `submissions/v601_v296_icp_no_g96_g94.csv` | Intracranial Pressure (KEEP +0/-4) | v601: v296 ICP prune G96/G94 | remove non-core CNS disorder families from ICP KEEP |
| 2 | `submissions/v602_v296_gout_no_e79.csv` | Gout (KEEP +0/-2) | v602: v296 Gout prune E79 | remove hyperuricemia/metabolism family from Gout KEEP |
| 3 | `submissions/v603_v296_pleurisy_no_r09_j95.csv` | Pleurisy (KEEP +0/-12) | v603: v296 Pleurisy prune R09/J95 | remove symptoms/postprocedural respiratory families from Pleurisy KEEP |
| 4 | `submissions/v604_v296_bronchitis_no_j43_j68.csv` | Bronchitis (KEEP +0/-8) | v604: v296 Bronchitis prune J43/J68 | remove emphysema/inhalation families from Bronchitis KEEP |
| 5 | `submissions/v605_v296_thyroiditis_no_e03.csv` | Thyroiditis (KEEP +0/-2) | v605: v296 Thyroiditis prune E03 | remove hypothyroidism family from Thyroiditis KEEP |
| 6 | `submissions/v606_v296_npc_no_d00_c44_d10.csv` | Nasopharyngeal Carcinoma (KEEP +0/-18) | v606: v296 NPC prune D00/C44/D10 | remove carcinoma-in-situ/skin/benign mouth families from NPC KEEP |
| 7 | `submissions/v607_v296_ckd_no_q60_q61_q62.csv` | CKD (KEEP +0/-43) | v607: v296 CKD prune congenital Q families | remove congenital renal malformation families from CKD KEEP |
| 8 | `submissions/v608_v296_ckd_no_i50.csv` | CKD (KEEP +0/-3) | v608: v296 CKD prune I50 | remove heart failure family from CKD KEEP |
| 9 | `submissions/v609_v296_hypothyroid_no_e04.csv` | Hypothyroidism (KEEP +0/-6) | v609: v296 Hypothyroidism prune E04 | remove nontoxic goiter family from Hypothyroidism KEEP |
| 10 | `submissions/v610_v296_hematemesis_no_r36_k66.csv` | Hematemesis (KEEP +0/-4) | v610: v296 Hematemesis prune R36/K66 | remove urethral/peritoneal families from Hematemesis KEEP |
| 11 | `submissions/v611_v296_hf_no_i97.csv` | Heart Failure (KEEP +0/-31) | v611: v296 Heart Failure prune I97 | remove large postprocedural circulatory family from HF KEEP |
| 12 | `submissions/v612_v296_hypergonadism_no_e27.csv` | Hypergonadism (KEEP +0/-11) | v612: v296 Hypergonadism prune E27 | remove adrenal family from Hypergonadism KEEP |
| 13 | `submissions/v613_v296_uti_no_obstetric.csv` | UTI (KEEP +0/-29) | v613: v296 UTI prune obstetric families | remove pregnancy/puerperal/abortion infection families from UTI KEEP |
| 14 | `submissions/v614_v296_uti_no_n35.csv` | UTI (KEEP +0/-3) | v614: v296 UTI prune N35 | remove urethral stricture family from UTI KEEP |
| 15 | `submissions/v615_v296_diabetes_no_o24.csv` | Diabetes (KEEP +0/-57) | v615: v296 Diabetes prune O24 | remove pregnancy diabetes family from Diabetes KEEP |
| 16 | `submissions/v616_v296_diabetes_no_z_p70.csv` | Diabetes (KEEP +0/-9) | v616: v296 Diabetes prune Z/P70 | remove therapy/history/newborn metabolism extras from Diabetes KEEP |
| 17 | `submissions/v617_v296_ild_no_j70.csv` | Interstitial Lung Disease (KEEP +0/-9) | v617: v296 ILD prune J70 | remove external-agent respiratory family from ILD KEEP |
| 18 | `submissions/v618_v296_hypopara_no_e23_e87_p71_e21.csv` | Hypoparathyroidism (KEEP +0/-8) | v618: v296 Hypopara prune related endocrine/noise | remove pituitary/fluid/neonatal/opposite parathyroid families from Hypopara KEEP |
| 19 | `submissions/v619_v296_hyperthyroid_no_e04_e01_e03_p72.csv` | Hyperthyroidism (KEEP +0/-12) | v619: v296 Hyperthyroid prune non-hyperthyroid | remove goiter/iodine/hypothyroid/neonatal families from Hyperthyroidism KEEP |
| 20 | `submissions/v620_v296_pneumonia_no_a37_p23_j84_j85.csv` | Pneumonia (KEEP +0/-30) | v620: v296 Pneumonia prune noisy families | remove whooping-cough/congenital/ILD/abscess families from Pneumonia KEEP |

## Pre-Submit Checklist

- The report should show one controlled condition change for each public probe.
- Any accidental multi-condition change should be regenerated before submission.
- Run `validate-plan` immediately before `submit-plan`.

