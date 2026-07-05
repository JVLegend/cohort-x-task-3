# CohortX Plan Decision Matrix — 2026-07-12-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-12-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Matched decision comparisons: 5

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| matched_comparisons | ready | comparisons=5 |

## Decision Comparisons

| Axis | Held constant | Variants | Files | Rule |
|---|---|---|---|---|
| private_keep | source=v296; med=drop; assoc=broad_assoc | `private_keep=prune_bronchitis` (1); `private_keep=prune_ckd` (1); `private_keep=prune_derm` (1); `private_keep=prune_diabetes` (1); `private_keep=prune_gout` (1); `private_keep=prune_hematemesis` (1); `private_keep=prune_hf` (1); `private_keep=prune_hidden` (3); `private_keep=prune_hypothyroid` (1); `private_keep=prune_ild` (1); `private_keep=prune_npc` (1); `private_keep=prune_pleurisy` (1); `private_keep=prune_pneumonia` (1); `private_keep=prune_thyroiditis` (1); `private_keep=prune_uti` (1) | `prune_bronchitis`: `v644_v296_bronchitis_no_j43_j68_assoc.csv`; `prune_ckd`: `v647_v296_ckd_no_q60_q61_q62_assoc.csv`; `prune_derm`: `v660_v296_derm_no_b37_assoc.csv`; `prune_diabetes`: `v654_v296_diabetes_no_o24_assoc.csv`; `prune_gout`: `v642_v296_gout_no_e79_assoc.csv`; `prune_hematemesis`: `v650_v296_hematemesis_no_r36_k66_assoc.csv`; `prune_hf`: `v651_v296_hf_no_i97_assoc.csv`; `prune_hidden`: `v641_v296_icp_no_g96_g94_assoc.csv`, `v657_v296_hypopara_no_e23_e87_p71_e21_assoc.csv`, `v658_v296_hyperthyroid_no_e04_e01_e03_p72_assoc.csv`; `prune_hypothyroid`: `v649_v296_hypothyroid_no_e04_assoc.csv`; `prune_ild`: `v656_v296_ild_no_j70_assoc.csv`; `prune_npc`: `v646_v296_npc_no_d00_c44_d10_assoc.csv`; `prune_pleurisy`: `v643_v296_pleurisy_no_r09_j95_assoc.csv`; `prune_pneumonia`: `v659_v296_pneumonia_no_a37_p23_j84_j85_assoc.csv`; `prune_thyroiditis`: `v645_v296_thyroiditis_no_e03_assoc.csv`; `prune_uti`: `v652_v296_uti_no_obstetric_assoc.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| private_keep | source=v296; med=drop; assoc=assoc | `private_keep=prune_ckd` (1); `private_keep=prune_diabetes` (1); `private_keep=prune_uti` (1) | `prune_ckd`: `v648_v296_ckd_no_i50_assoc.csv`; `prune_diabetes`: `v655_v296_diabetes_no_z_p70_assoc.csv`; `prune_uti`: `v653_v296_uti_no_n35_assoc.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| assoc | source=v296; med=drop; private_keep=prune_ckd | `assoc=assoc` (1); `assoc=broad_assoc` (1) | `assoc`: `v648_v296_ckd_no_i50_assoc.csv`; `broad_assoc`: `v647_v296_ckd_no_q60_q61_q62_assoc.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=v296; med=drop; private_keep=prune_uti | `assoc=assoc` (1); `assoc=broad_assoc` (1) | `assoc`: `v653_v296_uti_no_n35_assoc.csv`; `broad_assoc`: `v652_v296_uti_no_obstetric_assoc.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=v296; med=drop; private_keep=prune_diabetes | `assoc=assoc` (1); `assoc=broad_assoc` (1) | `assoc`: `v655_v296_diabetes_no_z_p70_assoc.csv`; `broad_assoc`: `v654_v296_diabetes_no_o24_assoc.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-12-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-12-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-12-public-contingency.csv --out reports/2026-07-12-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
