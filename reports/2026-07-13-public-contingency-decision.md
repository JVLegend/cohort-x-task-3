# CohortX Plan Decision Matrix — 2026-07-13-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-13-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Matched decision comparisons: 1

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| matched_comparisons | ready | comparisons=1 |

## Decision Comparisons

| Axis | Held constant | Variants | Files | Rule |
|---|---|---|---|---|
| private_keep | source=v296; med=drop; assoc=diff | `private_keep=prune_bronchitis` (1); `private_keep=prune_ckd` (2); `private_keep=prune_derm` (1); `private_keep=prune_diabetes` (2); `private_keep=prune_gout` (1); `private_keep=prune_hematemesis` (1); `private_keep=prune_hf` (1); `private_keep=prune_hidden` (3); `private_keep=prune_hypothyroid` (1); `private_keep=prune_ild` (1); `private_keep=prune_npc` (1); `private_keep=prune_pleurisy` (1); `private_keep=prune_pneumonia` (1); `private_keep=prune_thyroiditis` (1); `private_keep=prune_uti` (2) | `prune_bronchitis`: `v684_v296_bronchitis_no_j43_j68_diff.csv`; `prune_ckd`: `v687_v296_ckd_no_q60_q61_q62_diff.csv`, `v688_v296_ckd_no_i50_diff.csv`; `prune_derm`: `v700_v296_derm_no_b37_diff.csv`; `prune_diabetes`: `v694_v296_diabetes_no_o24_diff.csv`, `v695_v296_diabetes_no_z_p70_diff.csv`; `prune_gout`: `v682_v296_gout_no_e79_diff.csv`; `prune_hematemesis`: `v690_v296_hematemesis_no_r36_k66_diff.csv`; `prune_hf`: `v691_v296_hf_no_i97_diff.csv`; `prune_hidden`: `v681_v296_icp_no_g96_g94_diff.csv`, `v697_v296_hypopara_no_e23_e87_p71_e21_diff.csv`, `v698_v296_hyperthyroid_no_e04_e01_e03_p72_diff.csv`; `prune_hypothyroid`: `v689_v296_hypothyroid_no_e04_diff.csv`; `prune_ild`: `v696_v296_ild_no_j70_diff.csv`; `prune_npc`: `v686_v296_npc_no_d00_c44_d10_diff.csv`; `prune_pleurisy`: `v683_v296_pleurisy_no_r09_j95_diff.csv`; `prune_pneumonia`: `v699_v296_pneumonia_no_a37_p23_j84_j85_diff.csv`; `prune_thyroiditis`: `v685_v296_thyroiditis_no_e03_diff.csv`; `prune_uti`: `v692_v296_uti_no_obstetric_diff.csv`, `v693_v296_uti_no_n35_diff.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-13-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-13-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-13-public-contingency.csv --out reports/2026-07-13-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
