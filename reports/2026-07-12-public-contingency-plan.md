# CohortX Plan Report — 2026-07-12-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-12-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20

## Planned Changes

| Order | File | Changed conditions | Message | Notes |
|---:|---|---|---|---|
| 1 | `submissions/v641_v296_icp_no_g96_g94_assoc.csv` | Intracranial Pressure (KEEP +0/-4, ASSOCIATION +9/-0) | v641: v296 ICP prune G96/G94 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 2 | `submissions/v642_v296_gout_no_e79_assoc.csv` | Gout (KEEP +0/-2, ASSOCIATION +17/-0) | v642: v296 Gout prune E79 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 3 | `submissions/v643_v296_pleurisy_no_r09_j95_assoc.csv` | Pleurisy (KEEP +0/-12, ASSOCIATION +12/-0) | v643: v296 Pleurisy prune R09/J95 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 4 | `submissions/v644_v296_bronchitis_no_j43_j68_assoc.csv` | Bronchitis (KEEP +0/-8, ASSOCIATION +4/-0) | v644: v296 Bronchitis prune J43/J68 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 5 | `submissions/v645_v296_thyroiditis_no_e03_assoc.csv` | Thyroiditis (KEEP +0/-2, ASSOCIATION +31/-0) | v645: v296 Thyroiditis prune E03 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 6 | `submissions/v646_v296_npc_no_d00_c44_d10_assoc.csv` | Nasopharyngeal Carcinoma (KEEP +0/-18, ASSOCIATION +30/-0) | v646: v296 NPC prune D00/C44/D10 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 7 | `submissions/v647_v296_ckd_no_q60_q61_q62_assoc.csv` | CKD (KEEP +0/-43, ASSOCIATION +17/-0) | v647: v296 CKD prune congenital Q plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 8 | `submissions/v648_v296_ckd_no_i50_assoc.csv` | CKD (KEEP +0/-3, ASSOCIATION +17/-0) | v648: v296 CKD prune I50 plus ASSOC | small CKD KEEP prune plus CKD ASSOC |
| 9 | `submissions/v649_v296_hypothyroid_no_e04_assoc.csv` | Hypothyroidism (KEEP +0/-6, ASSOCIATION +19/-0) | v649: v296 Hypothyroidism prune E04 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 10 | `submissions/v650_v296_hematemesis_no_r36_k66_assoc.csv` | Hematemesis (KEEP +0/-4, ASSOCIATION +65/-0) | v650: v296 Hematemesis prune R36/K66 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 11 | `submissions/v651_v296_hf_no_i97_assoc.csv` | Heart Failure (KEEP +0/-31, ASSOCIATION +35/-0) | v651: v296 Heart Failure prune I97 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 12 | `submissions/v652_v296_uti_no_obstetric_assoc.csv` | UTI (KEEP +0/-29, ASSOCIATION +20/-0) | v652: v296 UTI prune obstetric plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 13 | `submissions/v653_v296_uti_no_n35_assoc.csv` | UTI (KEEP +0/-3, ASSOCIATION +20/-0) | v653: v296 UTI prune N35 plus ASSOC | small UTI KEEP prune plus UTI ASSOC |
| 14 | `submissions/v654_v296_diabetes_no_o24_assoc.csv` | Diabetes (KEEP +0/-57, ASSOCIATION +116/-0) | v654: v296 Diabetes prune O24 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 15 | `submissions/v655_v296_diabetes_no_z_p70_assoc.csv` | Diabetes (KEEP +0/-9, ASSOCIATION +116/-0) | v655: v296 Diabetes prune Z/P70 plus ASSOC | small Diabetes KEEP prune plus Diabetes ASSOC |
| 16 | `submissions/v656_v296_ild_no_j70_assoc.csv` | Interstitial Lung Disease (KEEP +0/-9, ASSOCIATION +41/-0) | v656: v296 ILD prune J70 plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 17 | `submissions/v657_v296_hypopara_no_e23_e87_p71_e21_assoc.csv` | Hypoparathyroidism (KEEP +0/-8, ASSOCIATION +1/-0) | v657: v296 Hypopara prune related plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 18 | `submissions/v658_v296_hyperthyroid_no_e04_e01_e03_p72_assoc.csv` | Hyperthyroidism (KEEP +0/-12, ASSOCIATION +21/-0) | v658: v296 Hyperthyroid prune non-hyper plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 19 | `submissions/v659_v296_pneumonia_no_a37_p23_j84_j85_assoc.csv` | Pneumonia (KEEP +0/-30, ASSOCIATION +36/-0) | v659: v296 Pneumonia prune noisy plus ASSOC | same-condition KEEP precision plus broad ASSOC isolation |
| 20 | `submissions/v660_v296_derm_no_b37_assoc.csv` | Dermatomycosis (KEEP +0/-21, ASSOCIATION +137/-0) | v660: v296 Dermatomycosis prune B37 plus ASSOC | new Dermatomycosis KEEP precision plus broad ASSOC isolation |

## Pre-Submit Checklist

- The report should show one controlled condition change for each public probe.
- Any accidental multi-condition change should be regenerated before submission.
- Run `validate-plan` immediately before `submit-plan`.
