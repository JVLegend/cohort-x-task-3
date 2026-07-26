# CohortX Plan Strategy Audit — 2026-07-16-upside

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-upside.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
- Items: 20
- Best source public: NA
- Distinct source submissions: 1
- Mediastinum axis: keep=7, drop=0
- Private KEEP buckets: 1
- ASSOC/DIFF buckets: 1

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| ordering | unknown | missing source scores |
| mediastinum_toggle | thin | med=keep 7; med=drop 0 |
| private_keep_mix | thin | buckets=1; none=0 |
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
| `unknown` | 20 |

### Mediastinum

| Axis | Slots |
|---|---:|
| med=unknown | 13 |
| med=keep | 7 |

### Private KEEP

| Bucket | Slots |
|---|---:|
| unknown | 20 |

### ASSOC/DIFF

| Bucket | Slots |
|---|---:|
| none | 20 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v827_v715_med_drop_c78.csv` |  |  |  |  | none | 2 | KEEP | 1 |
| 2 | `submissions/v828_v715_med_drop_d38.csv` |  |  |  |  | none | 2 | KEEP | 1 |
| 3 | `submissions/v829_v715_med_drop_j85.csv` |  |  | keep |  | none | 2 | KEEP | 1 |
| 4 | `submissions/v830_v715_med_drop_q34.csv` |  |  | keep |  | none | 5 | KEEP | 1 |
| 5 | `submissions/v831_v715_med_drop_c38.csv` |  |  | keep |  | none | 7 | KEEP | 1 |
| 6 | `submissions/v832_v715_med_drop_d15.csv` |  |  |  |  | none | 6 | KEEP | 1 |
| 7 | `submissions/v833_v715_med_drop_j980_j981.csv` |  |  |  |  | none | 6 | KEEP | 1 |
| 8 | `submissions/v834_v715_med_drop_j982_j983_j984.csv` |  |  |  |  | none | 3 | KEEP | 1 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
