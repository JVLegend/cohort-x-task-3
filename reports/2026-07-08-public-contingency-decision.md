# CohortX Plan Decision Matrix — 2026-07-08-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-08-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Matched decision comparisons: 7

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| matched_comparisons | ready | comparisons=7 |

## Decision Comparisons

| Axis | Held constant | Variants | Files | Rule |
|---|---|---|---|---|
| med | source=v296; private_keep=zero_hf; assoc=none | `med=drop` (1); `med=keep` (1) | `drop`: `v481_v296_zero_hf.csv`; `keep`: `v496_v296_med_zero_hf.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=v296; private_keep=zero_endocrine_pair; assoc=none | `med=drop` (1); `med=keep` (1) | `drop`: `v492_v296_zero_endocrine_pair.csv`; `keep`: `v497_v296_med_zero_endocrine_pair.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=v296; private_keep=zero_pulmonary_pair; assoc=none | `med=drop` (1); `med=keep` (1) | `drop`: `v493_v296_zero_pulmonary_pair.csv`; `keep`: `v498_v296_med_zero_pulmonary_pair.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=v296; private_keep=zero_derm_npc_pair; assoc=none | `med=drop` (1); `med=keep` (1) | `drop`: `v494_v296_zero_derm_npc_pair.csv`; `keep`: `v499_v296_med_zero_derm_npc_pair.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=v296; private_keep=add_hidden_kw_group; assoc=none | `med=drop` (1); `med=keep` (1) | `drop`: `v495_v296_add_hidden_kw_group.csv`; `keep`: `v500_v296_med_add_hidden_kw_group.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| private_keep | source=v296; med=drop; assoc=none | `private_keep=add_derm` (1); `private_keep=add_hf` (1); `private_keep=add_hidden_kw_group` (1); `private_keep=add_ild` (1); `private_keep=add_npc` (1); `private_keep=zero_bronchitis` (1); `private_keep=zero_derm` (1); `private_keep=zero_derm_npc_pair` (1); `private_keep=zero_endocrine_pair` (1); `private_keep=zero_hf` (1); `private_keep=zero_hyperthyroid` (1); `private_keep=zero_hypothyroid` (1); `private_keep=zero_ild` (1); `private_keep=zero_npc` (1); `private_keep=zero_pulmonary_pair` (1) | `add_derm`: `v490_v296_add_derm_kw.csv`; `add_hf`: `v488_v296_add_hf_kw.csv`; `add_hidden_kw_group`: `v495_v296_add_hidden_kw_group.csv`; `add_ild`: `v489_v296_add_ild_kw.csv`; `add_npc`: `v491_v296_add_npc_kw.csv`; `zero_bronchitis`: `v485_v296_zero_bronchitis.csv`; `zero_derm`: `v484_v296_zero_derm.csv`; `zero_derm_npc_pair`: `v494_v296_zero_derm_npc_pair.csv`; `zero_endocrine_pair`: `v492_v296_zero_endocrine_pair.csv`; `zero_hf`: `v481_v296_zero_hf.csv`; `zero_hyperthyroid`: `v482_v296_zero_hyperthyroid.csv`; `zero_hypothyroid`: `v487_v296_zero_hypothyroid.csv`; `zero_ild`: `v483_v296_zero_ild.csv`; `zero_npc`: `v486_v296_zero_npc.csv`; `zero_pulmonary_pair`: `v493_v296_zero_pulmonary_pair.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| private_keep | source=v296; med=keep; assoc=none | `private_keep=add_hidden_kw_group` (1); `private_keep=zero_derm_npc_pair` (1); `private_keep=zero_endocrine_pair` (1); `private_keep=zero_hf` (1); `private_keep=zero_pulmonary_pair` (1) | `add_hidden_kw_group`: `v500_v296_med_add_hidden_kw_group.csv`; `zero_derm_npc_pair`: `v499_v296_med_zero_derm_npc_pair.csv`; `zero_endocrine_pair`: `v497_v296_med_zero_endocrine_pair.csv`; `zero_hf`: `v496_v296_med_zero_hf.csv`; `zero_pulmonary_pair`: `v498_v296_med_zero_pulmonary_pair.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-08-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-08-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-08-public-contingency.csv --out reports/2026-07-08-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
