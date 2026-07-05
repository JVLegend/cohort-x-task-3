# CohortX Plan Strategy Audit — 2026-07-16-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Best source public: NA
- Distinct source submissions: 1
- Mediastinum axis: keep=0, drop=20
- Private KEEP buckets: 4
- ASSOC/DIFF buckets: 3

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| ordering | unknown | missing source scores |
| mediastinum_toggle | thin | med=keep 0; med=drop 20 |
| private_keep_mix | ready | buckets=4; none=5 |
| assoc_mix | thin | buckets=3 |

## Axis Risk Notes

- `ordering` needs review; if submission is partial, confirm the first slots still use the strongest available source before preserving order.
- `mediastinum_toggle` is thin; post-score conclusions about thymus/nodes should be treated as weak unless a matched decision comparison exists.
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
| prune_hidden | 8 |
| zero_hidden | 5 |
| none | 5 |
| zero_derm_npc_pair | 2 |

### ASSOC/DIFF

| Bucket | Slots |
|---|---:|
| highconf_assoc | 8 |
| broad_assoc | 7 |
| assoc | 5 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` |  |  | drop | zero_hidden | highconf_assoc | 881 | ASSOCIATION,KEEP | 17 |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` |  |  | drop | zero_hidden | highconf_assoc | 881 | ASSOCIATION,KEEP | 17 |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` |  |  | drop | zero_derm_npc_pair | highconf_assoc | 886 | ASSOCIATION,KEEP | 19 |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` |  |  | drop | none | highconf_assoc | 883 | ASSOCIATION,KEEP | 19 |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` |  |  | drop | prune_hidden | highconf_assoc | 873 | ASSOCIATION,KEEP | 17 |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` |  |  | drop | prune_hidden | highconf_assoc | 846 | ASSOCIATION,KEEP | 17 |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` |  |  | drop | prune_hidden | highconf_assoc | 826 | ASSOCIATION,KEEP | 17 |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` |  |  | drop | prune_hidden | highconf_assoc | 851 | ASSOCIATION,KEEP | 17 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
