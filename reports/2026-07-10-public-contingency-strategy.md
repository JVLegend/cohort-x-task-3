# CohortX Plan Strategy Audit — 2026-07-10-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-10-public-contingency.csv`
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
| diff_epistaxis | 1 |
| diff_gout | 1 |
| diff_pleurisy | 1 |
| diff_bronchitis | 1 |
| diff_thyroiditis | 1 |
| diff_ckd | 1 |
| diff_hypothyroidism | 1 |
| diff_hematemesis | 1 |
| diff_hf | 1 |
| diff_ild | 1 |
| diff_hypoparathyroidism | 1 |
| diff_hyperparathyroidism | 1 |
| diff_hyperthyroidism | 1 |
| diff_pneumonia | 1 |
| diff_icp | 1 |
| diff_adrenal | 1 |
| diff_derm | 1 |
| diff_npc | 1 |
| diff_uti | 1 |
| diff_diabetes | 1 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v561_v296_diff_epistaxis.csv` |  |  | drop | none | diff_epistaxis | 2 | DIFF | 1 |
| 2 | `submissions/v562_v296_diff_gout.csv` |  |  | drop | none | diff_gout | 260 | DIFF | 1 |
| 3 | `submissions/v563_v296_diff_pleurisy.csv` |  |  | drop | none | diff_pleurisy | 17 | DIFF | 1 |
| 4 | `submissions/v564_v296_diff_bronchitis.csv` |  |  | drop | none | diff_bronchitis | 32 | DIFF | 1 |
| 5 | `submissions/v565_v296_diff_thyroiditis.csv` |  |  | drop | none | diff_thyroiditis | 6 | DIFF | 1 |
| 6 | `submissions/v566_v296_diff_ckd.csv` |  |  | drop | none | diff_ckd | 6 | DIFF | 1 |
| 7 | `submissions/v567_v296_diff_hypothyroidism.csv` |  |  | drop | none | diff_hypothyroidism | 22 | DIFF | 1 |
| 8 | `submissions/v568_v296_diff_hematemesis.csv` |  |  | drop | none | diff_hematemesis | 2 | DIFF | 1 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
