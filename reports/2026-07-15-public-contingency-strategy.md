# CohortX Plan Strategy Audit — 2026-07-15-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-15-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Best source public: NA
- Distinct source submissions: 1
- Mediastinum axis: keep=0, drop=20
- Private KEEP buckets: 5
- ASSOC/DIFF buckets: 1

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| ordering | unknown | missing source scores |
| mediastinum_toggle | thin | med=keep 0; med=drop 20 |
| private_keep_mix | thin | buckets=5; none=0 |
| assoc_mix | thin | buckets=1 |

## Axis Coverage

### Source Submissions

| Source | Slots |
|---|---:|
| `v296` | 20 |

### Mediastinum

| Axis | Slots |
|---|---:|
| med=drop | 20 |

### Private KEEP

| Bucket | Slots |
|---|---:|
| prune_hidden | 14 |
| prune_diabetes | 3 |
| prune_bronchitis | 1 |
| prune_gout | 1 |
| prune_pneumonia | 1 |

### ASSOC/DIFF

| Bucket | Slots |
|---|---:|
| none | 20 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v761_v296_portfolio_renal_metabolic_obstetric_prune.csv` |  |  | drop | prune_hidden | none | 129 | KEEP | 3 |
| 2 | `submissions/v762_v296_portfolio_cardio_pulm_noise_prune.csv` |  |  | drop | prune_hidden | none | 43 | KEEP | 3 |
| 3 | `submissions/v763_v296_portfolio_thyroid_axis_prune.csv` |  |  | drop | prune_hidden | none | 20 | KEEP | 3 |
| 4 | `submissions/v764_v296_portfolio_respiratory_noise_prune.csv` |  |  | drop | prune_hidden | none | 50 | KEEP | 3 |
| 5 | `submissions/v765_v296_portfolio_gi_gu_skin_prune.csv` |  |  | drop | prune_hidden | none | 28 | KEEP | 3 |
| 6 | `submissions/v766_v296_portfolio_ent_skin_endocrine_prune.csv` |  |  | drop | prune_hidden | none | 50 | KEEP | 3 |
| 7 | `submissions/v767_v296_portfolio_ckd_diabetes_full_prune.csv` |  |  | drop | prune_diabetes | none | 112 | KEEP | 2 |
| 8 | `submissions/v768_v296_portfolio_uti_diabetes_obstetric_prune.csv` |  |  | drop | prune_diabetes | none | 89 | KEEP | 2 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
