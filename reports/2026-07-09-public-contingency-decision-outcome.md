# CohortX Plan Decision Outcome — 2026-07-09-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-09-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Anchor public: 0.43156
- Scored plan items: 20/20
- Matched decision comparisons: 1
- Resolved comparisons: 1
- Pending comparisons: 0

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_scores | ready | scored=20/20 |
| outcome_comparisons | ready | resolved=1; pending=0; comparisons=1 |

## Axis Outcome Summary

| Axis | Public wins | Tie-breaks | Pending | Readout |
|---|---|---|---:|---|
| assoc | `assoc=assoc_epistaxis` 1 | none | 0 | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |

## Detailed Comparisons

| Axis | Held constant | Status | Public winner | Recommended | Scores | Volumes | Files | Rule |
|---|---|---|---|---|---|---|---|---|
| assoc | source=v296; med=drop; private_keep=none | resolved | `assoc_epistaxis` | `assoc_epistaxis` | `assoc_adrenal` 0.42995 (1/1); `assoc_bronchitis` 0.42995 (1/1); `assoc_ckd` 0.42995 (1/1); `assoc_derm` 0.42995 (1/1); `assoc_diabetes` 0.42995 (1/1); `assoc_epistaxis` 0.43136 (1/1); `assoc_gout` 0.42995 (1/1); `assoc_hematemesis` 0.42995 (1/1); `assoc_hf` 0.42995 (1/1); `assoc_hyperparathyroidism` 0.42995 (1/1); `assoc_hyperthyroidism` 0.42995 (1/1); `assoc_hypoparathyroidism` 0.42995 (1/1); `assoc_hypothyroidism` 0.42995 (1/1); `assoc_icp` 0.42995 (1/1); `assoc_ild` 0.42995 (1/1); `assoc_npc` 0.42995 (1/1); `assoc_pleurisy` 0.42995 (1/1); `assoc_pneumonia` 0.42995 (1/1); `assoc_thyroiditis` 0.42995 (1/1); `assoc_uti` 0.42995 (1/1) | `assoc_adrenal` min=19; `assoc_bronchitis` min=4; `assoc_ckd` min=17; `assoc_derm` min=137; `assoc_diabetes` min=116; `assoc_epistaxis` min=48; `assoc_gout` min=17; `assoc_hematemesis` min=65; `assoc_hf` min=35; `assoc_hyperparathyroidism` min=8; `assoc_hyperthyroidism` min=21; `assoc_hypoparathyroidism` min=1; `assoc_hypothyroidism` min=19; `assoc_icp` min=9; `assoc_ild` min=41; `assoc_npc` min=30; `assoc_pleurisy` min=12; `assoc_pneumonia` min=36; `assoc_thyroiditis` min=31; `assoc_uti` min=20 | `assoc_adrenal`: `v536_v296_assoc_adrenal.csv`; `assoc_bronchitis`: `v524_v296_assoc_bronchitis.csv`; `assoc_ckd`: `v526_v296_assoc_ckd.csv`; `assoc_derm`: `v537_v296_assoc_derm.csv`; `assoc_diabetes`: `v540_v296_assoc_diabetes.csv`; `assoc_epistaxis`: `v521_v296_assoc_epistaxis.csv`; `assoc_gout`: `v522_v296_assoc_gout.csv`; `assoc_hematemesis`: `v528_v296_assoc_hematemesis.csv`; `assoc_hf`: `v529_v296_assoc_hf.csv`; `assoc_hyperparathyroidism`: `v532_v296_assoc_hyperparathyroidism.csv`; `assoc_hyperthyroidism`: `v533_v296_assoc_hyperthyroidism.csv`; `assoc_hypoparathyroidism`: `v531_v296_assoc_hypoparathyroidism.csv`; `assoc_hypothyroidism`: `v527_v296_assoc_hypothyroidism.csv`; `assoc_icp`: `v535_v296_assoc_icp.csv`; `assoc_ild`: `v530_v296_assoc_ild.csv`; `assoc_npc`: `v538_v296_assoc_npc.csv`; `assoc_pleurisy`: `v523_v296_assoc_pleurisy.csv`; `assoc_pneumonia`: `v534_v296_assoc_pneumonia.csv`; `assoc_thyroiditis`: `v525_v296_assoc_thyroiditis.csv`; `assoc_uti`: `v539_v296_assoc_uti.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |

## Use

- Use only resolved comparisons for promotion decisions; pending rows mean Kaggle has not scored enough files yet.
- A single public winner should feed the next adaptive plan; public ties use the `Recommended` column to prefer lower-volume variants before broader private hedges.
- Keep this outcome beside `plan-scorecard` and `impact` so the next generator is guided by matched comparisons, not isolated leaderboard movement.
