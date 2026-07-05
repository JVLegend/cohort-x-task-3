# CohortX Plan Strategy Audit — 2026-07-13-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-13-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Best source public: NA
- Distinct source submissions: 1
- Mediastinum axis: keep=0, drop=20
- Private KEEP buckets: 15
- ASSOC/DIFF buckets: 1

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| ordering | unknown | missing source scores |
| mediastinum_toggle | thin | med=keep 0; med=drop 20 |
| private_keep_mix | thin | buckets=15; none=0 |
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
| prune_hidden | 3 |
| prune_ckd | 2 |
| prune_uti | 2 |
| prune_diabetes | 2 |
| prune_gout | 1 |
| prune_pleurisy | 1 |
| prune_bronchitis | 1 |
| prune_thyroiditis | 1 |
| prune_npc | 1 |
| prune_hypothyroid | 1 |
| prune_hematemesis | 1 |
| prune_hf | 1 |
| prune_ild | 1 |
| prune_pneumonia | 1 |
| prune_derm | 1 |

### ASSOC/DIFF

| Bucket | Slots |
|---|---:|
| diff | 20 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v681_v296_icp_no_g96_g94_diff.csv` |  |  | drop | prune_hidden | diff | 101 | DIFF,KEEP | 1 |
| 2 | `submissions/v682_v296_gout_no_e79_diff.csv` |  |  | drop | prune_gout | diff | 262 | DIFF,KEEP | 1 |
| 3 | `submissions/v683_v296_pleurisy_no_r09_j95_diff.csv` |  |  | drop | prune_pleurisy | diff | 29 | DIFF,KEEP | 1 |
| 4 | `submissions/v684_v296_bronchitis_no_j43_j68_diff.csv` |  |  | drop | prune_bronchitis | diff | 40 | DIFF,KEEP | 1 |
| 5 | `submissions/v685_v296_thyroiditis_no_e03_diff.csv` |  |  | drop | prune_thyroiditis | diff | 8 | DIFF,KEEP | 1 |
| 6 | `submissions/v686_v296_npc_no_d00_c44_d10_diff.csv` |  |  | drop | prune_npc | diff | 35 | DIFF,KEEP | 1 |
| 7 | `submissions/v687_v296_ckd_no_q60_q61_q62_diff.csv` |  |  | drop | prune_ckd | diff | 49 | DIFF,KEEP | 1 |
| 8 | `submissions/v688_v296_ckd_no_i50_diff.csv` |  |  | drop | prune_ckd | diff | 9 | DIFF,KEEP | 1 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
