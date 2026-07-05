# CohortX Plan Decision Matrix — 2026-07-09-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-09-public-contingency.csv`
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
| assoc | source=v296; med=drop; private_keep=none | `assoc=assoc_adrenal` (1); `assoc=assoc_bronchitis` (1); `assoc=assoc_ckd` (1); `assoc=assoc_derm` (1); `assoc=assoc_diabetes` (1); `assoc=assoc_epistaxis` (1); `assoc=assoc_gout` (1); `assoc=assoc_hematemesis` (1); `assoc=assoc_hf` (1); `assoc=assoc_hyperparathyroidism` (1); `assoc=assoc_hyperthyroidism` (1); `assoc=assoc_hypoparathyroidism` (1); `assoc=assoc_hypothyroidism` (1); `assoc=assoc_icp` (1); `assoc=assoc_ild` (1); `assoc=assoc_npc` (1); `assoc=assoc_pleurisy` (1); `assoc=assoc_pneumonia` (1); `assoc=assoc_thyroiditis` (1); `assoc=assoc_uti` (1) | `assoc_adrenal`: `v536_v296_assoc_adrenal.csv`; `assoc_bronchitis`: `v524_v296_assoc_bronchitis.csv`; `assoc_ckd`: `v526_v296_assoc_ckd.csv`; `assoc_derm`: `v537_v296_assoc_derm.csv`; `assoc_diabetes`: `v540_v296_assoc_diabetes.csv`; `assoc_epistaxis`: `v521_v296_assoc_epistaxis.csv`; `assoc_gout`: `v522_v296_assoc_gout.csv`; `assoc_hematemesis`: `v528_v296_assoc_hematemesis.csv`; `assoc_hf`: `v529_v296_assoc_hf.csv`; `assoc_hyperparathyroidism`: `v532_v296_assoc_hyperparathyroidism.csv`; `assoc_hyperthyroidism`: `v533_v296_assoc_hyperthyroidism.csv`; `assoc_hypoparathyroidism`: `v531_v296_assoc_hypoparathyroidism.csv`; `assoc_hypothyroidism`: `v527_v296_assoc_hypothyroidism.csv`; `assoc_icp`: `v535_v296_assoc_icp.csv`; `assoc_ild`: `v530_v296_assoc_ild.csv`; `assoc_npc`: `v538_v296_assoc_npc.csv`; `assoc_pleurisy`: `v523_v296_assoc_pleurisy.csv`; `assoc_pneumonia`: `v534_v296_assoc_pneumonia.csv`; `assoc_thyroiditis`: `v525_v296_assoc_thyroiditis.csv`; `assoc_uti`: `v539_v296_assoc_uti.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-09-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-09-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-09-public-contingency.csv --out reports/2026-07-09-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
