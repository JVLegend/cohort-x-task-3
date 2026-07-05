# CohortX Plan Strategy Audit — 2026-07-07-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-07-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Best source public: NA
- Distinct source submissions: 3
- Mediastinum axis: keep=8, drop=12
- Private KEEP buckets: 1
- ASSOC/DIFF buckets: 5

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| ordering | unknown | missing source scores |
| mediastinum_toggle | ready | med=keep 8; med=drop 12 |
| private_keep_mix | thin | buckets=1; none=20 |
| assoc_mix | ready | buckets=5 |

## Axis Risk Notes

- `ordering` needs review; if submission is partial, confirm the first slots still use the strongest available source before preserving order.
- `private_keep_mix` is thin; read the plan as a fallback/hedge batch, not as a reliable decomposition of the private KEEP axis.

## Axis Coverage

### Source Submissions

| Source | Slots |
|---|---:|
| `copd_j31_j98` | 7 |
| `copd_j81_j82` | 7 |
| `copd_j93_j95` | 6 |

### Mediastinum

| Axis | Slots |
|---|---:|
| med=drop | 12 |
| med=keep | 8 |

### Private KEEP

| Bucket | Slots |
|---|---:|
| none | 20 |

### ASSOC/DIFF

| Bucket | Slots |
|---|---:|
| highconf_assoc | 6 |
| broad_assoc | 5 |
| none | 3 |
| pulmonary_assocdiff | 3 |
| cardiorenal_assocdiff | 3 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v441_copd_j31_j98_med_add_thymus_nodes.csv` |  |  | keep | none | none | 17 | KEEP | 2 |
| 2 | `submissions/v442_copd_j81_j82_med_add_thymus_nodes.csv` |  |  | keep | none | none | 8 | KEEP | 2 |
| 3 | `submissions/v443_copd_j93_j95_med_add_thymus_nodes.csv` |  |  | keep | none | none | 8 | KEEP | 2 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` |  |  | drop | none | highconf_assoc | 368 | ASSOCIATION,KEEP | 15 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` |  |  | drop | none | highconf_assoc | 359 | ASSOCIATION,KEEP | 15 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` |  |  | drop | none | highconf_assoc | 359 | ASSOCIATION,KEEP | 15 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` |  |  | drop | none | broad_assoc | 699 | ASSOCIATION,KEEP | 21 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` |  |  | drop | none | broad_assoc | 690 | ASSOCIATION,KEEP | 21 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
