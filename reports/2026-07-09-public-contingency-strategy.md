# CohortX Plan Strategy Audit — 2026-07-09-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-09-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Best source public: NA
- Distinct source submissions: 1
- Mediastinum axis: keep=0, drop=20
- Private KEEP buckets: 1
- ASSOC/DIFF buckets: 20

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| ordering | unknown | missing source scores |
| mediastinum_toggle | thin | med=keep 0; med=drop 20 |
| private_keep_mix | thin | buckets=1; none=20 |
| assoc_mix | ready | buckets=20 |

## Axis Risk Notes

- `ordering` needs review; if submission is partial, confirm the first slots still use the strongest available source before preserving order.
- `mediastinum_toggle` is thin; post-score conclusions about thymus/nodes should be treated as weak unless a matched decision comparison exists.
- `private_keep_mix` is thin; read the plan as a fallback/hedge batch, not as a reliable decomposition of the private KEEP axis.

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
| none | 20 |

### ASSOC/DIFF

| Bucket | Slots |
|---|---:|
| assoc_epistaxis | 1 |
| assoc_gout | 1 |
| assoc_pleurisy | 1 |
| assoc_bronchitis | 1 |
| assoc_thyroiditis | 1 |
| assoc_ckd | 1 |
| assoc_hypothyroidism | 1 |
| assoc_hematemesis | 1 |
| assoc_hf | 1 |
| assoc_ild | 1 |
| assoc_hypoparathyroidism | 1 |
| assoc_hyperparathyroidism | 1 |
| assoc_hyperthyroidism | 1 |
| assoc_pneumonia | 1 |
| assoc_icp | 1 |
| assoc_adrenal | 1 |
| assoc_derm | 1 |
| assoc_npc | 1 |
| assoc_uti | 1 |
| assoc_diabetes | 1 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v521_v296_assoc_epistaxis.csv` |  |  | drop | none | assoc_epistaxis | 48 | ASSOCIATION | 1 |
| 2 | `submissions/v522_v296_assoc_gout.csv` |  |  | drop | none | assoc_gout | 17 | ASSOCIATION | 1 |
| 3 | `submissions/v523_v296_assoc_pleurisy.csv` |  |  | drop | none | assoc_pleurisy | 12 | ASSOCIATION | 1 |
| 4 | `submissions/v524_v296_assoc_bronchitis.csv` |  |  | drop | none | assoc_bronchitis | 4 | ASSOCIATION | 1 |
| 5 | `submissions/v525_v296_assoc_thyroiditis.csv` |  |  | drop | none | assoc_thyroiditis | 31 | ASSOCIATION | 1 |
| 6 | `submissions/v526_v296_assoc_ckd.csv` |  |  | drop | none | assoc_ckd | 17 | ASSOCIATION | 1 |
| 7 | `submissions/v527_v296_assoc_hypothyroidism.csv` |  |  | drop | none | assoc_hypothyroidism | 19 | ASSOCIATION | 1 |
| 8 | `submissions/v528_v296_assoc_hematemesis.csv` |  |  | drop | none | assoc_hematemesis | 65 | ASSOCIATION | 1 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
