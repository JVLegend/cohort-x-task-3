# CohortX Plan Decision Matrix — 2026-07-15-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-15-public-contingency.csv`
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
| private_keep | source=v296; med=drop; assoc=none | `private_keep=prune_bronchitis` (1); `private_keep=prune_diabetes` (3); `private_keep=prune_gout` (1); `private_keep=prune_hidden` (14); `private_keep=prune_pneumonia` (1) | `prune_bronchitis`: `v772_v296_portfolio_bleed_pleura_bronch_prune.csv`; `prune_diabetes`: `v767_v296_portfolio_ckd_diabetes_full_prune.csv`, `v768_v296_portfolio_uti_diabetes_obstetric_prune.csv`, `v777_v296_portfolio_derm_uti_diabetes_prune.csv`; `prune_gout`: `v774_v296_portfolio_gout_ckd_prune.csv`; `prune_hidden`: `v761_v296_portfolio_renal_metabolic_obstetric_prune.csv`, `v762_v296_portfolio_cardio_pulm_noise_prune.csv`, `v763_v296_portfolio_thyroid_axis_prune.csv`; `prune_pneumonia`: `v776_v296_portfolio_hf_ckd_pneumonia_prune.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-15-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-15-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-15-public-contingency.csv --out reports/2026-07-15-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
