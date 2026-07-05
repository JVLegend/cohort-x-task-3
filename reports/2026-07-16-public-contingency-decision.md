# CohortX Plan Decision Matrix — 2026-07-16-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-public-contingency.csv`
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
| private_keep | source=v296; med=drop; assoc=highconf_assoc | `private_keep=none` (1); `private_keep=prune_hidden` (4); `private_keep=zero_derm_npc_pair` (1); `private_keep=zero_hidden` (2) | `none`: `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv`; `prune_hidden`: `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv`, `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv`, `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv`; `zero_derm_npc_pair`: `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv`; `zero_hidden`: `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv`, `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| private_keep | source=v296; med=drop; assoc=broad_assoc | `private_keep=none` (1); `private_keep=prune_hidden` (3); `private_keep=zero_derm_npc_pair` (1); `private_keep=zero_hidden` (2) | `none`: `v812_v296_final_v185_add_hidden_broad_assoc.csv`; `prune_hidden`: `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv`, `v814_v296_final_v185_prune_small_precision_broad_assoc.csv`, `v815_v296_final_v185_broad_private_prune_broad_assoc.csv`; `zero_derm_npc_pair`: `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv`; `zero_hidden`: `v809_v296_final_v185_zero_thyroid_broad_assoc.csv`, `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| private_keep | source=v296; med=drop; assoc=assoc | `private_keep=none` (3); `private_keep=prune_hidden` (1); `private_keep=zero_hidden` (1) | `none`: `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv`, `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv`, `v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv`; `prune_hidden`: `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv`; `zero_hidden`: `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| assoc | source=v296; med=drop; private_keep=zero_hidden | `assoc=assoc` (1); `assoc=broad_assoc` (2); `assoc=highconf_assoc` (2) | `assoc`: `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv`; `broad_assoc`: `v809_v296_final_v185_zero_thyroid_broad_assoc.csv`, `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv`; `highconf_assoc`: `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv`, `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=v296; med=drop; private_keep=zero_derm_npc_pair | `assoc=broad_assoc` (1); `assoc=highconf_assoc` (1) | `broad_assoc`: `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv`; `highconf_assoc`: `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=v296; med=drop; private_keep=none | `assoc=assoc` (3); `assoc=broad_assoc` (1); `assoc=highconf_assoc` (1) | `assoc`: `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv`, `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv`, `v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv`; `broad_assoc`: `v812_v296_final_v185_add_hidden_broad_assoc.csv`; `highconf_assoc`: `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=v296; med=drop; private_keep=prune_hidden | `assoc=assoc` (1); `assoc=broad_assoc` (3); `assoc=highconf_assoc` (4) | `assoc`: `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv`; `broad_assoc`: `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv`, `v814_v296_final_v185_prune_small_precision_broad_assoc.csv`, `v815_v296_final_v185_broad_private_prune_broad_assoc.csv`; `highconf_assoc`: `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv`, `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv`, `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-16-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-16-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-16-public-contingency.csv --out reports/2026-07-16-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
