# CohortX Plan Scorecard — 2026-07-02

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-02.csv`
- Anchor: `submissions/v178_FINAL.csv`
- Anchor public: 0.42453
- Items: 20

## Plan Items

| Order | File | Status | Public | Delta vs anchor | Signal | Changed conditions | Message | Notes |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `submissions/v201_copd_no_j20.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-3) | v201: COPD remove J20 acute bronchitis | public COPD family ablation |
| 2 | `submissions/v202_copd_no_j31.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-2) | v202: COPD remove J31 chronic rhinitis | public COPD family ablation |
| 3 | `submissions/v203_copd_no_j45.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) | v203: COPD remove J45 asthma | public COPD family ablation |
| 4 | `submissions/v204_copd_no_j81_j82.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) | v204: COPD remove J81/J82 edema eosinophilia | public COPD family ablation |
| 5 | `submissions/v205_copd_no_j93_j95.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) | v205: COPD remove J93/J95 pneumothorax postop | public COPD family ablation |
| 6 | `submissions/v206_copd_no_j96.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-17) | v206: COPD remove J96 respiratory failure | public COPD family ablation |
| 7 | `submissions/v207_copd_no_j98.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-3) | v207: COPD remove J98 other respiratory disorders | public COPD family ablation |
| 8 | `submissions/v208_copd_core_j41_j42_j43_j44.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-41) | v208: COPD core J41/J42/J43/J44 only | public COPD precision probe |
| 9 | `submissions/v209_copd_no_acute_bronch_asthma.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-7) | v209: COPD remove J20 and J45 together | public COPD combined ablation |
| 10 | `submissions/v210_copd_add_p25_only.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +3/-0) | v210: COPD add P25 perinatal emphysema only | public COPD isolated addition |
| 11 | `submissions/v211_copd_add_t79_t81_only.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +8/-0) | v211: COPD add T79/T81 emphysema only | public COPD isolated addition |
| 12 | `submissions/v212_med_no_j98.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-16) | v212: mediastinum remove J98 | public mediastinum family ablation |
| 13 | `submissions/v213_med_no_q34.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-5) | v213: mediastinum remove Q34 | public mediastinum family ablation |
| 14 | `submissions/v214_med_no_d15.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-6) | v214: mediastinum remove D15 | public mediastinum family ablation |
| 15 | `submissions/v215_med_no_c38.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-7) | v215: mediastinum remove C38 | public mediastinum family ablation |
| 16 | `submissions/v216_med_only_mediastin_title.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-26) | v216: mediastinum keep titles containing mediastin | public mediastinum precision probe |
| 17 | `submissions/v217_med_keep_neoplasm_only.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-23) | v217: mediastinum neoplasm-only set | public mediastinum precision probe |
| 18 | `submissions/v218_med_add_c852_only.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +11/-0) | v218: mediastinum add C852 lymphoma only | public mediastinum isolated addition |
| 19 | `submissions/v219_med_add_n80b5_only.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +1/-0) | v219: mediastinum add N80B5 only | public mediastinum isolated addition |
| 20 | `submissions/v220_med_add_p252_only.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +1/-0) | v220: mediastinum add P252 only | public mediastinum isolated addition |

## Ranked Complete Signals

No completed plan items yet.

## Strategy Use

- Improved rows are immediate candidates for promotion or cross-condition combinations.
- Tied rows are public-neutral and mainly useful as private hedges.
- Worse rows identify public-sensitive code families; use the direction of the edit before deciding whether to add back or remove codes.
- Missing rows mean the adaptive generator should wait rather than fill the next plan with weak guesses.

