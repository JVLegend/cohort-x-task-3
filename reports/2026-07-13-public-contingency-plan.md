# CohortX Plan Report — 2026-07-13-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-13-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20

## Planned Changes

| Order | File | Changed conditions | Message | Notes |
|---:|---|---|---|---|
| 1 | `submissions/v681_v296_icp_no_g96_g94_diff.csv` | Intracranial Pressure (KEEP +0/-4, DIFF +97/-0) | v681: v296 ICP prune G96/G94 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 2 | `submissions/v682_v296_gout_no_e79_diff.csv` | Gout (KEEP +0/-2, DIFF +260/-0) | v682: v296 Gout prune E79 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 3 | `submissions/v683_v296_pleurisy_no_r09_j95_diff.csv` | Pleurisy (KEEP +0/-12, DIFF +17/-0) | v683: v296 Pleurisy prune R09/J95 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 4 | `submissions/v684_v296_bronchitis_no_j43_j68_diff.csv` | Bronchitis (KEEP +0/-8, DIFF +32/-0) | v684: v296 Bronchitis prune J43/J68 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 5 | `submissions/v685_v296_thyroiditis_no_e03_diff.csv` | Thyroiditis (KEEP +0/-2, DIFF +6/-0) | v685: v296 Thyroiditis prune E03 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 6 | `submissions/v686_v296_npc_no_d00_c44_d10_diff.csv` | Nasopharyngeal Carcinoma (KEEP +0/-18, DIFF +17/-0) | v686: v296 NPC prune D00/C44/D10 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 7 | `submissions/v687_v296_ckd_no_q60_q61_q62_diff.csv` | CKD (KEEP +0/-43, DIFF +6/-0) | v687: v296 CKD prune congenital Q plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 8 | `submissions/v688_v296_ckd_no_i50_diff.csv` | CKD (KEEP +0/-3, DIFF +6/-0) | v688: v296 CKD prune I50 plus DIFF | small CKD KEEP prune plus CKD DIFF |
| 9 | `submissions/v689_v296_hypothyroid_no_e04_diff.csv` | Hypothyroidism (KEEP +0/-6, DIFF +22/-0) | v689: v296 Hypothyroidism prune E04 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 10 | `submissions/v690_v296_hematemesis_no_r36_k66_diff.csv` | Hematemesis (KEEP +0/-4, DIFF +2/-0) | v690: v296 Hematemesis prune R36/K66 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 11 | `submissions/v691_v296_hf_no_i97_diff.csv` | Heart Failure (KEEP +0/-31, DIFF +15/-0) | v691: v296 Heart Failure prune I97 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 12 | `submissions/v692_v296_uti_no_obstetric_diff.csv` | UTI (KEEP +0/-29, DIFF +39/-0) | v692: v296 UTI prune obstetric plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 13 | `submissions/v693_v296_uti_no_n35_diff.csv` | UTI (KEEP +0/-3, DIFF +39/-0) | v693: v296 UTI prune N35 plus DIFF | small UTI KEEP prune plus UTI DIFF |
| 14 | `submissions/v694_v296_diabetes_no_o24_diff.csv` | Diabetes (KEEP +0/-57, DIFF +7/-0) | v694: v296 Diabetes prune O24 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 15 | `submissions/v695_v296_diabetes_no_z_p70_diff.csv` | Diabetes (KEEP +0/-9, DIFF +7/-0) | v695: v296 Diabetes prune Z/P70 plus DIFF | small Diabetes KEEP prune plus Diabetes DIFF |
| 16 | `submissions/v696_v296_ild_no_j70_diff.csv` | Interstitial Lung Disease (KEEP +0/-9, DIFF +35/-0) | v696: v296 ILD prune J70 plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 17 | `submissions/v697_v296_hypopara_no_e23_e87_p71_e21_diff.csv` | Hypoparathyroidism (KEEP +0/-8, DIFF +10/-0) | v697: v296 Hypopara prune related plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 18 | `submissions/v698_v296_hyperthyroid_no_e04_e01_e03_p72_diff.csv` | Hyperthyroidism (KEEP +0/-12, DIFF +15/-0) | v698: v296 Hyperthyroid prune non-hyper plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 19 | `submissions/v699_v296_pneumonia_no_a37_p23_j84_j85_diff.csv` | Pneumonia (KEEP +0/-30, DIFF +71/-0) | v699: v296 Pneumonia prune noisy plus DIFF | same-condition KEEP precision plus broad DIFF isolation |
| 20 | `submissions/v700_v296_derm_no_b37_diff.csv` | Dermatomycosis (KEEP +0/-21, DIFF +33/-0) | v700: v296 Dermatomycosis prune B37 plus DIFF | new Dermatomycosis KEEP precision plus broad DIFF isolation |

## Pre-Submit Checklist

- The report should show one controlled condition change for each public probe.
- Any accidental multi-condition change should be regenerated before submission.
- Run `validate-plan` immediately before `submit-plan`.
