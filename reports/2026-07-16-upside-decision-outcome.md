# CohortX Plan Decision Outcome — 2026-07-16-upside

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-upside.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
- Anchor public: 0.43606
- Scored plan items: 20/20
- Matched decision comparisons: 1
- Resolved comparisons: 1
- Pending comparisons: 0

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_scores | ready | scored=20/20 |
| outcome_comparisons | ready | resolved=1; pending=0; comparisons=1 |

## Axis Outcome Summary

| Axis | Public wins | Tie-breaks | Pending | Readout |
|---|---|---|---:|---|
| med | `med=unknown` 1 | none | 0 | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |

## Detailed Comparisons

| Axis | Held constant | Status | Public winner | Recommended | Scores | Volumes | Files | Rule |
|---|---|---|---|---|---|---|---|---|
| med | source=unknown; private_keep=; assoc=none | resolved | `unknown` | `unknown` | `keep` 0.43695 (7/7); `unknown` 0.43713 (13/13) | `keep` min=2; `unknown` min=2 | `keep`: `v829_v715_med_drop_j85.csv`, `v830_v715_med_drop_q34.csv`, `v831_v715_med_drop_c38.csv`; `unknown`: `v827_v715_med_drop_c78.csv`, `v828_v715_med_drop_d38.csv`, `v832_v715_med_drop_d15.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |

## Use

- Use only resolved comparisons for promotion decisions; pending rows mean Kaggle has not scored enough files yet.
- A single public winner should feed the next adaptive plan; public ties use the `Recommended` column to prefer lower-volume variants before broader private hedges.
- Keep this outcome beside `plan-scorecard` and `impact` so the next generator is guided by matched comparisons, not isolated leaderboard movement.
