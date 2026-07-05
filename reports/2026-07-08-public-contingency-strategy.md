# CohortX Plan Strategy Audit — 2026-07-08-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-08-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Best source public: NA
- Distinct source submissions: 1
- Mediastinum axis: keep=5, drop=15
- Private KEEP buckets: 15
- ASSOC/DIFF buckets: 1

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| ordering | unknown | missing source scores |
| mediastinum_toggle | ready | med=keep 5; med=drop 15 |
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
| med=drop | 15 |
| med=keep | 5 |

### Private KEEP

| Bucket | Slots |
|---|---:|
| zero_hf | 2 |
| zero_endocrine_pair | 2 |
| zero_pulmonary_pair | 2 |
| zero_derm_npc_pair | 2 |
| add_hidden_kw_group | 2 |
| zero_hyperthyroid | 1 |
| zero_ild | 1 |
| zero_derm | 1 |
| zero_bronchitis | 1 |
| zero_npc | 1 |
| zero_hypothyroid | 1 |
| add_hf | 1 |
| add_ild | 1 |
| add_derm | 1 |
| add_npc | 1 |

### ASSOC/DIFF

| Bucket | Slots |
|---|---:|
| none | 20 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v481_v296_zero_hf.csv` |  |  | drop | zero_hf | none | 72 | KEEP | 1 |
| 2 | `submissions/v482_v296_zero_hyperthyroid.csv` |  |  | drop | zero_hyperthyroid | none | 49 | KEEP | 1 |
| 3 | `submissions/v483_v296_zero_ild.csv` |  |  | drop | zero_ild | none | 42 | KEEP | 1 |
| 4 | `submissions/v484_v296_zero_derm.csv` |  |  | drop | zero_derm | none | 38 | KEEP | 1 |
| 5 | `submissions/v485_v296_zero_bronchitis.csv` |  |  | drop | zero_bronchitis | none | 33 | KEEP | 1 |
| 6 | `submissions/v486_v296_zero_npc.csv` |  |  | drop | zero_npc | none | 42 | KEEP | 1 |
| 7 | `submissions/v487_v296_zero_hypothyroid.csv` |  |  | drop | zero_hypothyroid | none | 26 | KEEP | 1 |
| 8 | `submissions/v488_v296_add_hf_kw.csv` |  |  | drop | add_hf | none | 6 | KEEP | 1 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
