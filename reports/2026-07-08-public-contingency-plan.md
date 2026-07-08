# CohortX Plan Report — 2026-07-08-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-08-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20

## Planned Changes

| Order | File | Changed conditions | Message | Notes |
|---:|---|---|---|---|
| 1 | `submissions/v481_v296_zero_hf.csv` | Heart Failure (KEEP +0/-72) | v481: v296 zero Heart Failure KEEP | public-neutral zero probe v187 on v296 anchor |
| 2 | `submissions/v482_v296_zero_hyperthyroid.csv` | Hyperthyroidism (KEEP +0/-49) | v482: v296 zero Hyperthyroidism KEEP | public-neutral zero probe v188 on v296 anchor |
| 3 | `submissions/v483_v296_zero_ild.csv` | Interstitial Lung Disease (KEEP +0/-42) | v483: v296 zero ILD KEEP | public-neutral zero probe v189 on v296 anchor |
| 4 | `submissions/v484_v296_zero_derm.csv` | Dermatomycosis (KEEP +0/-38) | v484: v296 zero Dermatomycosis KEEP | public-neutral zero probe v190 on v296 anchor |
| 5 | `submissions/v485_v296_zero_bronchitis.csv` | Bronchitis (KEEP +0/-33) | v485: v296 zero Bronchitis KEEP | public-neutral zero probe v191 on v296 anchor |
| 6 | `submissions/v486_v296_zero_npc.csv` | Nasopharyngeal Carcinoma (KEEP +0/-42) | v486: v296 zero NPC KEEP | public-neutral zero probe v192 on v296 anchor |
| 7 | `submissions/v487_v296_zero_hypothyroid.csv` | Hypothyroidism (KEEP +0/-26) | v487: v296 zero Hypothyroidism KEEP | public-neutral zero probe v193 on v296 anchor |
| 8 | `submissions/v488_v296_add_hf_kw.csv` | Heart Failure (KEEP +6/-0) | v488: v296 add Heart Failure keyword KEEP | public-neutral keyword add v196 on v296 anchor |
| 9 | `submissions/v489_v296_add_ild_kw.csv` | Interstitial Lung Disease (KEEP +9/-0) | v489: v296 add ILD keyword KEEP | public-neutral keyword add v197 on v296 anchor |
| 10 | `submissions/v490_v296_add_derm_kw.csv` | Dermatomycosis (KEEP +57/-0) | v490: v296 add Dermatomycosis keyword KEEP | public-neutral keyword add v198 on v296 anchor |
| 11 | `submissions/v491_v296_add_npc_kw.csv` | Nasopharyngeal Carcinoma (KEEP +5/-0) | v491: v296 add NPC keyword KEEP | public-neutral keyword add v200 on v296 anchor |
| 12 | `submissions/v492_v296_zero_endocrine_pair.csv` | Hypothyroidism (KEEP +0/-26); Hyperthyroidism (KEEP +0/-49) | v492: v296 zero thyroid pair KEEP | paired public-neutral thyroid ablation |
| 13 | `submissions/v493_v296_zero_pulmonary_pair.csv` | Bronchitis (KEEP +0/-33); Interstitial Lung Disease (KEEP +0/-42) | v493: v296 zero ILD/Bronchitis KEEP | paired public-neutral pulmonary hidden KEEP ablation |
| 14 | `submissions/v494_v296_zero_derm_npc_pair.csv` | Dermatomycosis (KEEP +0/-38); Nasopharyngeal Carcinoma (KEEP +0/-42) | v494: v296 zero Derm/NPC KEEP | paired public-neutral derm/NPC ablation |
| 15 | `submissions/v495_v296_add_hidden_kw_group.csv` | Dermatomycosis (KEEP +57/-0); Nasopharyngeal Carcinoma (KEEP +5/-0); Heart Failure (KEEP +6/-0); Interstitial Lung Disease (KEEP +9/-0) | v495: v296 add hidden keyword group | combined public-neutral keyword additions from v196/v197/v198/v200 |
| 16 | `submissions/v496_v296_med_zero_hf.csv` | Enlarged Mediastinum (KEEP +4/-0); Heart Failure (KEEP +0/-72) | v496: v296 mediastinum plus zero HF | med positive plus public-neutral HF ablation |
| 17 | `submissions/v497_v296_med_zero_endocrine_pair.csv` | Enlarged Mediastinum (KEEP +4/-0); Hypothyroidism (KEEP +0/-26); Hyperthyroidism (KEEP +0/-49) | v497: v296 mediastinum plus zero thyroid pair | med positive plus public-neutral thyroid ablation |
| 18 | `submissions/v498_v296_med_zero_pulmonary_pair.csv` | Enlarged Mediastinum (KEEP +4/-0); Bronchitis (KEEP +0/-33); Interstitial Lung Disease (KEEP +0/-42) | v498: v296 mediastinum plus zero ILD/Bronchitis | med positive plus public-neutral pulmonary ablation |
| 19 | `submissions/v499_v296_med_zero_derm_npc_pair.csv` | Enlarged Mediastinum (KEEP +4/-0); Dermatomycosis (KEEP +0/-38); Nasopharyngeal Carcinoma (KEEP +0/-42) | v499: v296 mediastinum plus zero Derm/NPC | med positive plus public-neutral derm/NPC ablation |
| 20 | `submissions/v500_v296_med_add_hidden_kw_group.csv` | Enlarged Mediastinum (KEEP +4/-0); Dermatomycosis (KEEP +57/-0); Nasopharyngeal Carcinoma (KEEP +5/-0); Heart Failure (KEEP +6/-0); +1 more | v500: v296 mediastinum plus hidden keyword group | med positive plus combined public-neutral keyword additions |

## Pre-Submit Checklist

- The report should show one controlled condition change for each public probe.
- Any accidental multi-condition change should be regenerated before submission.
- Run `validate-plan` immediately before `submit-plan`.
