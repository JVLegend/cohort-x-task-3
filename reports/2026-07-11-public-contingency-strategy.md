# CohortX Plan Strategy Audit — 2026-07-11-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-11-public-contingency.csv`
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

## Axis Risk Notes

- `ordering` needs review; if submission is partial, confirm the first slots still use the strongest available source before preserving order.
- `mediastinum_toggle` is thin; post-score conclusions about thymus/nodes should be treated as weak unless a matched decision comparison exists.
- `private_keep_mix` is thin; read the plan as a fallback/hedge batch, not as a reliable decomposition of the private KEEP axis.
- `assoc_mix` is thin; use scored comparisons for the submitted ASSOC/DIFF buckets, but avoid generalizing to untested buckets in the next adaptive plan.

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
| prune_hidden | 2 |
| prune_hypothyroid | 2 |
| prune_hf | 2 |
| prune_uti | 2 |
| prune_diabetes | 2 |
| prune_gout | 1 |
| prune_pleurisy | 1 |
| prune_bronchitis | 1 |
| prune_npc | 1 |
| prune_ckd | 1 |
| prune_hematemesis | 1 |
| prune_adrenal | 1 |
| prune_ild | 1 |
| prune_hyperthyroid | 1 |
| prune_pneumonia | 1 |

### ASSOC/DIFF

| Bucket | Slots |
|---|---:|
| none | 20 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v601_v296_icp_no_g96_g94.csv` |  |  | drop | prune_hidden | none | 4 | KEEP | 1 |
| 2 | `submissions/v602_v296_gout_no_e79.csv` |  |  | drop | prune_gout | none | 2 | KEEP | 1 |
| 3 | `submissions/v603_v296_pleurisy_no_r09_j95.csv` |  |  | drop | prune_pleurisy | none | 12 | KEEP | 1 |
| 4 | `submissions/v604_v296_bronchitis_no_j43_j68.csv` |  |  | drop | prune_bronchitis | none | 8 | KEEP | 1 |
| 5 | `submissions/v605_v296_thyroiditis_no_e03.csv` |  |  | drop | prune_hypothyroid | none | 2 | KEEP | 1 |
| 6 | `submissions/v606_v296_npc_no_d00_c44_d10.csv` |  |  | drop | prune_npc | none | 18 | KEEP | 1 |
| 7 | `submissions/v607_v296_ckd_no_q60_q61_q62.csv` |  |  | drop | prune_ckd | none | 43 | KEEP | 1 |
| 8 | `submissions/v608_v296_ckd_no_i50.csv` |  |  | drop | prune_hf | none | 3 | KEEP | 1 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
