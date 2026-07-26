# CohortX Plan Decision Outcome — 2026-07-11-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-11-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Anchor public: 0.43342
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
| private_keep | `private_keep=prune_hidden` 1 | none | 0 | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Detailed Comparisons

| Axis | Held constant | Status | Public winner | Recommended | Scores | Volumes | Files | Rule |
|---|---|---|---|---|---|---|---|---|
| private_keep | source=v296; med=drop; assoc=none | resolved | `prune_hidden` | `prune_hidden` | `prune_adrenal` 0.42995 (1/1); `prune_bronchitis` 0.42995 (1/1); `prune_ckd` 0.42995 (1/1); `prune_diabetes` 0.42995 (2/2); `prune_gout` 0.42964 (1/1); `prune_hematemesis` 0.42995 (1/1); `prune_hf` 0.42995 (2/2); `prune_hidden` 0.43045 (2/2); `prune_hyperthyroid` 0.42995 (1/1); `prune_hypothyroid` 0.42995 (2/2); `prune_ild` 0.42995 (1/1); `prune_npc` 0.42995 (1/1); `prune_pleurisy` 0.42995 (1/1); `prune_pneumonia` 0.42995 (1/1); `prune_uti` 0.42995 (2/2) | `prune_adrenal` min=11; `prune_bronchitis` min=8; `prune_ckd` min=43; `prune_diabetes` min=9; `prune_gout` min=2; `prune_hematemesis` min=4; `prune_hf` min=3; `prune_hidden` min=4; `prune_hyperthyroid` min=12; `prune_hypothyroid` min=2; `prune_ild` min=9; `prune_npc` min=18; `prune_pleurisy` min=12; `prune_pneumonia` min=30; `prune_uti` min=3 | `prune_adrenal`: `v612_v296_hypergonadism_no_e27.csv`; `prune_bronchitis`: `v604_v296_bronchitis_no_j43_j68.csv`; `prune_ckd`: `v607_v296_ckd_no_q60_q61_q62.csv`; `prune_diabetes`: `v615_v296_diabetes_no_o24.csv`, `v616_v296_diabetes_no_z_p70.csv`; `prune_gout`: `v602_v296_gout_no_e79.csv`; `prune_hematemesis`: `v610_v296_hematemesis_no_r36_k66.csv`; `prune_hf`: `v608_v296_ckd_no_i50.csv`, `v611_v296_hf_no_i97.csv`; `prune_hidden`: `v601_v296_icp_no_g96_g94.csv`, `v618_v296_hypopara_no_e23_e87_p71_e21.csv`; `prune_hyperthyroid`: `v619_v296_hyperthyroid_no_e04_e01_e03_p72.csv`; `prune_hypothyroid`: `v605_v296_thyroiditis_no_e03.csv`, `v609_v296_hypothyroid_no_e04.csv`; `prune_ild`: `v617_v296_ild_no_j70.csv`; `prune_npc`: `v606_v296_npc_no_d00_c44_d10.csv`; `prune_pleurisy`: `v603_v296_pleurisy_no_r09_j95.csv`; `prune_pneumonia`: `v620_v296_pneumonia_no_a37_p23_j84_j85.csv`; `prune_uti`: `v613_v296_uti_no_obstetric.csv`, `v614_v296_uti_no_n35.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Use

- Use only resolved comparisons for promotion decisions; pending rows mean Kaggle has not scored enough files yet.
- A single public winner should feed the next adaptive plan; public ties use the `Recommended` column to prefer lower-volume variants before broader private hedges.
- Keep this outcome beside `plan-scorecard` and `impact` so the next generator is guided by matched comparisons, not isolated leaderboard movement.
