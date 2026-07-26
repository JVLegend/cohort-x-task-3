# CohortX Plan Decision Outcome — 2026-07-13

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-13.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Anchor public: 0.43410
- Scored plan items: 20/20
- Matched decision comparisons: 4
- Resolved comparisons: 4
- Pending comparisons: 0

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_scores | ready | scored=20/20 |
| outcome_comparisons | ready | resolved=4; pending=0; comparisons=4 |

## Axis Outcome Summary

| Axis | Public wins | Tie-breaks | Pending | Readout |
|---|---|---|---:|---|
| private_keep | `private_keep=tie` 1 | `private_keep=none` 1 | 0 | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| source | `source=tie` 3 | `source=v385` 1; `source=v384` 1; `source=v357` 1 | 0 | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |

## Detailed Comparisons

| Axis | Held constant | Status | Public winner | Recommended | Scores | Volumes | Files | Rule |
|---|---|---|---|---|---|---|---|---|
| private_keep | source=v543; med=keep; assoc=epistaxis_i10 | resolved | `tie:none/v185_ckd_uti/v185_diab_pneu/v185keep` | `none (tie_low_volume)` | `none` 0.43410 (5/5); `v185_ckd_uti` 0.43410 (1/1); `v185_diab_pneu` 0.43410 (1/1); `v185keep` 0.43410 (1/1) | `none` min=2; `v185_ckd_uti` min=175; `v185_diab_pneu` min=276; `v185keep` min=449 | `none`: `v633_v543_med_add_c37.csv`, `v634_v543_med_add_d384.csv`, `v635_v543_med_add_c771.csv`; `v185_ckd_uti`: `v638_v543_med_c37_v185_ckd_uti.csv`; `v185_diab_pneu`: `v639_v543_med_c37_v185_diab_pneu.csv`; `v185keep`: `v640_v543_med_c37_v185keep.csv` | If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges. |
| source | med=keep; private_keep=v185_diab_pneu; assoc=epistaxis_i10_narrow | resolved | `tie:v342/v385` | `v385 (tie_low_volume)` | `v342` 0.43362 (1/1); `v385` 0.43362 (1/1) | `v342` min=586; `v385` min=344 | `v342`: `v629_v342_epi_i10_narrow.csv`; `v385`: `v625_v385_epi_i10_narrow.csv` | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |
| source | med=keep; private_keep=v185_ckd_uti; assoc=epistaxis_i10_narrow | resolved | `tie:v341/v384` | `v384 (tie_low_volume)` | `v341` 0.43362 (1/1); `v384` 0.43362 (1/1) | `v341` min=485; `v384` min=243 | `v341`: `v630_v341_epi_i10_narrow.csv`; `v384`: `v626_v384_epi_i10_narrow.csv` | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |
| source | med=keep; private_keep=v185keep; assoc=epistaxis_i10_narrow | resolved | `tie:v301/v302/v357` | `v357 (tie_low_volume)` | `v301` 0.43362 (1/1); `v302` 0.43362 (1/1); `v357` 0.43362 (1/1) | `v301` min=1090; `v302` min=759; `v357` min=517 | `v301`: `v632_v301_epi_i10_narrow.csv`; `v302`: `v631_v302_epi_i10_narrow.csv`; `v357`: `v628_v357_epi_i10_narrow.csv` | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |

## Use

- Use only resolved comparisons for promotion decisions; pending rows mean Kaggle has not scored enough files yet.
- A single public winner should feed the next adaptive plan; public ties use the `Recommended` column to prefer lower-volume variants before broader private hedges.
- Keep this outcome beside `plan-scorecard` and `impact` so the next generator is guided by matched comparisons, not isolated leaderboard movement.
