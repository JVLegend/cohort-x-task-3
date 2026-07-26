# CohortX Plan Decision Matrix — 2026-07-16-upside

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-upside.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
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
| med | source=unknown; private_keep=; assoc=none | `med=keep` (7); `med=unknown` (13) | `keep`: `v829_v715_med_drop_j85.csv`, `v830_v715_med_drop_q34.csv`, `v831_v715_med_drop_c38.csv`; `unknown`: `v827_v715_med_drop_c78.csv`, `v828_v715_med_drop_d38.csv`, `v832_v715_med_drop_d15.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-16-upside.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-16-upside.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-16-upside.csv --out reports/2026-07-16-upside-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
