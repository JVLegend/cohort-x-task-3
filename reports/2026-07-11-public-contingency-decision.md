# CohortX Plan Decision Matrix — 2026-07-11-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-11-public-contingency.csv`
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
| private_keep | source=v296; med=drop; assoc=none | `private_keep=prune_adrenal` (1); `private_keep=prune_bronchitis` (1); `private_keep=prune_ckd` (1); `private_keep=prune_diabetes` (2); `private_keep=prune_gout` (1); `private_keep=prune_hematemesis` (1); `private_keep=prune_hf` (2); `private_keep=prune_hidden` (2); `private_keep=prune_hyperthyroid` (1); `private_keep=prune_hypothyroid` (2); `private_keep=prune_ild` (1); `private_keep=prune_npc` (1); `private_keep=prune_pleurisy` (1); `private_keep=prune_pneumonia` (1); `private_keep=prune_uti` (2) | `prune_adrenal`: `v612_v296_hypergonadism_no_e27.csv`; `prune_bronchitis`: `v604_v296_bronchitis_no_j43_j68.csv`; `prune_ckd`: `v607_v296_ckd_no_q60_q61_q62.csv`; `prune_diabetes`: `v615_v296_diabetes_no_o24.csv`, `v616_v296_diabetes_no_z_p70.csv`; `prune_gout`: `v602_v296_gout_no_e79.csv`; `prune_hematemesis`: `v610_v296_hematemesis_no_r36_k66.csv`; `prune_hf`: `v608_v296_ckd_no_i50.csv`, `v611_v296_hf_no_i97.csv`; `prune_hidden`: `v601_v296_icp_no_g96_g94.csv`, `v618_v296_hypopara_no_e23_e87_p71_e21.csv`; `prune_hyperthyroid`: `v619_v296_hyperthyroid_no_e04_e01_e03_p72.csv`; `prune_hypothyroid`: `v605_v296_thyroiditis_no_e03.csv`, `v609_v296_hypothyroid_no_e04.csv`; `prune_ild`: `v617_v296_ild_no_j70.csv`; `prune_npc`: `v606_v296_npc_no_d00_c44_d10.csv`; `prune_pleurisy`: `v603_v296_pleurisy_no_r09_j95.csv`; `prune_pneumonia`: `v620_v296_pneumonia_no_a37_p23_j84_j85.csv`; `prune_uti`: `v613_v296_uti_no_obstetric.csv`, `v614_v296_uti_no_n35.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-11-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-11-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-11-public-contingency.csv --out reports/2026-07-11-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
