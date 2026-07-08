# CohortX Plan Decision Outcome — 2026-07-08-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-08-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Anchor public: 0.43156
- Scored plan items: 20/20
- Matched decision comparisons: 7
- Resolved comparisons: 7
- Pending comparisons: 0

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_scores | ready | scored=20/20 |
| outcome_comparisons | ready | resolved=7; pending=0; comparisons=7 |

## Axis Outcome Summary

| Axis | Public wins | Tie-breaks | Pending | Readout |
|---|---|---|---:|---|
| med | `med=keep` 5 | none | 0 | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| private_keep | `private_keep=tie` 2 | `private_keep=add_npc` 1; `private_keep=zero_hf` 1 | 0 | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Detailed Comparisons

| Axis | Held constant | Status | Public winner | Recommended | Scores | Volumes | Files | Rule |
|---|---|---|---|---|---|---|---|---|
| med | source=v296; private_keep=zero_hf; assoc=none | resolved | `keep` | `keep` | `drop` 0.42995 (1/1); `keep` 0.43015 (1/1) | `drop` min=72; `keep` min=76 | `drop`: `v481_v296_zero_hf.csv`; `keep`: `v496_v296_med_zero_hf.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=v296; private_keep=zero_endocrine_pair; assoc=none | resolved | `keep` | `keep` | `drop` 0.42995 (1/1); `keep` 0.43015 (1/1) | `drop` min=75; `keep` min=79 | `drop`: `v492_v296_zero_endocrine_pair.csv`; `keep`: `v497_v296_med_zero_endocrine_pair.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=v296; private_keep=zero_pulmonary_pair; assoc=none | resolved | `keep` | `keep` | `drop` 0.42995 (1/1); `keep` 0.43015 (1/1) | `drop` min=75; `keep` min=79 | `drop`: `v493_v296_zero_pulmonary_pair.csv`; `keep`: `v498_v296_med_zero_pulmonary_pair.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=v296; private_keep=zero_derm_npc_pair; assoc=none | resolved | `keep` | `keep` | `drop` 0.42995 (1/1); `keep` 0.43015 (1/1) | `drop` min=80; `keep` min=84 | `drop`: `v494_v296_zero_derm_npc_pair.csv`; `keep`: `v499_v296_med_zero_derm_npc_pair.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=v296; private_keep=add_hidden_kw_group; assoc=none | resolved | `keep` | `keep` | `drop` 0.42995 (1/1); `keep` 0.43015 (1/1) | `drop` min=77; `keep` min=81 | `drop`: `v495_v296_add_hidden_kw_group.csv`; `keep`: `v500_v296_med_add_hidden_kw_group.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| private_keep | source=v296; med=drop; assoc=none | resolved | `tie:add_derm/add_hf/add_hidden_kw_group/add_ild/add_npc/zero_bronchitis/zero_derm/zero_derm_npc_pair/zero_endocrine_pair/zero_hf/zero_hyperthyroid/zero_hypothyroid/zero_ild/zero_npc/zero_pulmonary_pair` | `add_npc (tie_low_volume)` | `add_derm` 0.42995 (1/1); `add_hf` 0.42995 (1/1); `add_hidden_kw_group` 0.42995 (1/1); `add_ild` 0.42995 (1/1); `add_npc` 0.42995 (1/1); `zero_bronchitis` 0.42995 (1/1); `zero_derm` 0.42995 (1/1); `zero_derm_npc_pair` 0.42995 (1/1); `zero_endocrine_pair` 0.42995 (1/1); `zero_hf` 0.42995 (1/1); `zero_hyperthyroid` 0.42995 (1/1); `zero_hypothyroid` 0.42995 (1/1); `zero_ild` 0.42995 (1/1); `zero_npc` 0.42995 (1/1); `zero_pulmonary_pair` 0.42995 (1/1) | `add_derm` min=57; `add_hf` min=6; `add_hidden_kw_group` min=77; `add_ild` min=9; `add_npc` min=5; `zero_bronchitis` min=33; `zero_derm` min=38; `zero_derm_npc_pair` min=80; `zero_endocrine_pair` min=75; `zero_hf` min=72; `zero_hyperthyroid` min=49; `zero_hypothyroid` min=26; `zero_ild` min=42; `zero_npc` min=42; `zero_pulmonary_pair` min=75 | `add_derm`: `v490_v296_add_derm_kw.csv`; `add_hf`: `v488_v296_add_hf_kw.csv`; `add_hidden_kw_group`: `v495_v296_add_hidden_kw_group.csv`; `add_ild`: `v489_v296_add_ild_kw.csv`; `add_npc`: `v491_v296_add_npc_kw.csv`; `zero_bronchitis`: `v485_v296_zero_bronchitis.csv`; `zero_derm`: `v484_v296_zero_derm.csv`; `zero_derm_npc_pair`: `v494_v296_zero_derm_npc_pair.csv`; `zero_endocrine_pair`: `v492_v296_zero_endocrine_pair.csv`; `zero_hf`: `v481_v296_zero_hf.csv`; `zero_hyperthyroid`: `v482_v296_zero_hyperthyroid.csv`; `zero_hypothyroid`: `v487_v296_zero_hypothyroid.csv`; `zero_ild`: `v483_v296_zero_ild.csv`; `zero_npc`: `v486_v296_zero_npc.csv`; `zero_pulmonary_pair`: `v493_v296_zero_pulmonary_pair.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| private_keep | source=v296; med=keep; assoc=none | resolved | `tie:add_hidden_kw_group/zero_derm_npc_pair/zero_endocrine_pair/zero_hf/zero_pulmonary_pair` | `zero_hf (tie_low_volume)` | `add_hidden_kw_group` 0.43015 (1/1); `zero_derm_npc_pair` 0.43015 (1/1); `zero_endocrine_pair` 0.43015 (1/1); `zero_hf` 0.43015 (1/1); `zero_pulmonary_pair` 0.43015 (1/1) | `add_hidden_kw_group` min=81; `zero_derm_npc_pair` min=84; `zero_endocrine_pair` min=79; `zero_hf` min=76; `zero_pulmonary_pair` min=79 | `add_hidden_kw_group`: `v500_v296_med_add_hidden_kw_group.csv`; `zero_derm_npc_pair`: `v499_v296_med_zero_derm_npc_pair.csv`; `zero_endocrine_pair`: `v497_v296_med_zero_endocrine_pair.csv`; `zero_hf`: `v496_v296_med_zero_hf.csv`; `zero_pulmonary_pair`: `v498_v296_med_zero_pulmonary_pair.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Use

- Use only resolved comparisons for promotion decisions; pending rows mean Kaggle has not scored enough files yet.
- A single public winner should feed the next adaptive plan; public ties use the `Recommended` column to prefer lower-volume variants before broader private hedges.
- Keep this outcome beside `plan-scorecard` and `impact` so the next generator is guided by matched comparisons, not isolated leaderboard movement.
