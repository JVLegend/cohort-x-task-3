# CohortX Plan Decision Outcome — 2026-07-15

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-15.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
- Anchor public: 0.43606
- Scored plan items: 20/20
- Matched decision comparisons: 2
- Resolved comparisons: 2
- Pending comparisons: 0

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_scores | ready | scored=20/20 |
| outcome_comparisons | ready | resolved=2; pending=0; comparisons=2 |

## Axis Outcome Summary

| Axis | Public wins | Tie-breaks | Pending | Readout |
|---|---|---|---:|---|
| assoc | `assoc=tie` 1 | `assoc=none` 1 | 0 | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| private_keep | `private_keep=tie` 1 | `private_keep=none` 1 | 0 | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |

## Detailed Comparisons

| Axis | Held constant | Status | Public winner | Recommended | Scores | Volumes | Files | Rule |
|---|---|---|---|---|---|---|---|---|
| private_keep | source=unknown; med=keep; assoc=pulmonary_assocdiff | resolved | `tie:none/unknown` | `none (tie_low_volume)` | `none` 0.43259 (1/1); `unknown` 0.43259 (6/6) | `none` min=1; `unknown` min=77 | `none`: `v746_v633_med_add_c39_med_keep_no_v185keep_pulmonary_assocdiff.csv`; `unknown`: `v744_v633_med_add_c39_med_keep_v185keep_pulmonary_assocdiff.csv`, `v748_v633_med_add_c39_med_keep_v185_ckd_uti_pulmonary_assocdiff.csv`, `v751_v633_med_add_c39_med_keep_v185_diab_pneu_pulmonary_assocdiff.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| assoc | source=unknown; med=keep; private_keep= | resolved | `tie:assocdiff/none` | `none (tie_low_volume)` | `assocdiff` 0.43606 (6/6); `none` 0.43606 (7/7); `pulmonary_assocdiff` 0.43259 (6/6) | `assocdiff` min=29; `none` min=1; `pulmonary_assocdiff` min=77 | `assocdiff`: `v742_v633_med_add_c39_med_keep_v185_ckd_uti_assocdiff.csv`, `v743_v633_med_add_c39_med_keep_v185_diab_pneu_assocdiff.csv`, `v745_v633_med_add_c39_med_keep_v185_ckd_assocdiff.csv`; `none`: `v741_v633_med_add_c39_med_keep_v185keep_assoc_only.csv`, `v821_v633_med_add_c39_root.csv`, `v822_v633_med_add_c390.csv`; `pulmonary_assocdiff`: `v744_v633_med_add_c39_med_keep_v185keep_pulmonary_assocdiff.csv`, `v748_v633_med_add_c39_med_keep_v185_ckd_uti_pulmonary_assocdiff.csv`, `v751_v633_med_add_c39_med_keep_v185_diab_pneu_pulmonary_assocdiff.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |

## Use

- Use only resolved comparisons for promotion decisions; pending rows mean Kaggle has not scored enough files yet.
- A single public winner should feed the next adaptive plan; public ties use the `Recommended` column to prefer lower-volume variants before broader private hedges.
- Keep this outcome beside `plan-scorecard` and `impact` so the next generator is guided by matched comparisons, not isolated leaderboard movement.
