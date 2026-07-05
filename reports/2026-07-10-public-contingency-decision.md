# CohortX Plan Decision Matrix — 2026-07-10-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-10-public-contingency.csv`
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
| assoc | source=v296; med=drop; private_keep=none | `assoc=diff_adrenal` (1); `assoc=diff_bronchitis` (1); `assoc=diff_ckd` (1); `assoc=diff_derm` (1); `assoc=diff_diabetes` (1); `assoc=diff_epistaxis` (1); `assoc=diff_gout` (1); `assoc=diff_hematemesis` (1); `assoc=diff_hf` (1); `assoc=diff_hyperparathyroidism` (1); `assoc=diff_hyperthyroidism` (1); `assoc=diff_hypoparathyroidism` (1); `assoc=diff_hypothyroidism` (1); `assoc=diff_icp` (1); `assoc=diff_ild` (1); `assoc=diff_npc` (1); `assoc=diff_pleurisy` (1); `assoc=diff_pneumonia` (1); `assoc=diff_thyroiditis` (1); `assoc=diff_uti` (1) | `diff_adrenal`: `v576_v296_diff_adrenal.csv`; `diff_bronchitis`: `v564_v296_diff_bronchitis.csv`; `diff_ckd`: `v566_v296_diff_ckd.csv`; `diff_derm`: `v577_v296_diff_derm.csv`; `diff_diabetes`: `v580_v296_diff_diabetes.csv`; `diff_epistaxis`: `v561_v296_diff_epistaxis.csv`; `diff_gout`: `v562_v296_diff_gout.csv`; `diff_hematemesis`: `v568_v296_diff_hematemesis.csv`; `diff_hf`: `v569_v296_diff_hf.csv`; `diff_hyperparathyroidism`: `v572_v296_diff_hyperparathyroidism.csv`; `diff_hyperthyroidism`: `v573_v296_diff_hyperthyroidism.csv`; `diff_hypoparathyroidism`: `v571_v296_diff_hypoparathyroidism.csv`; `diff_hypothyroidism`: `v567_v296_diff_hypothyroidism.csv`; `diff_icp`: `v575_v296_diff_icp.csv`; `diff_ild`: `v570_v296_diff_ild.csv`; `diff_npc`: `v578_v296_diff_npc.csv`; `diff_pleurisy`: `v563_v296_diff_pleurisy.csv`; `diff_pneumonia`: `v574_v296_diff_pneumonia.csv`; `diff_thyroiditis`: `v565_v296_diff_thyroiditis.csv`; `diff_uti`: `v579_v296_diff_uti.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-10-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-10-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-10-public-contingency.csv --out reports/2026-07-10-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
