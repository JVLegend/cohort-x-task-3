# CohortX Plan Strategy Audit — 2026-07-14-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-14-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Best source public: NA
- Distinct source submissions: 1
- Mediastinum axis: keep=0, drop=20
- Private KEEP buckets: 15
- ASSOC/DIFF buckets: 2

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| ordering | unknown | missing source scores |
| mediastinum_toggle | thin | med=keep 0; med=drop 20 |
| private_keep_mix | thin | buckets=15; none=0 |
| assoc_mix | thin | buckets=2 |

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
| broad_assoc | 17 |
| assocdiff | 3 |

## First-Wave Order

| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |
|---:|---|---:|---:|---|---|---|---:|---|---:|
| 1 | `submissions/v721_v296_icp_no_g96_g94_assocdiff.csv` |  |  | drop | prune_hidden | broad_assoc | 110 | ASSOCIATION,DIFF,KEEP | 1 |
| 2 | `submissions/v722_v296_gout_no_e79_assocdiff.csv` |  |  | drop | prune_gout | broad_assoc | 279 | ASSOCIATION,DIFF,KEEP | 1 |
| 3 | `submissions/v723_v296_pleurisy_no_r09_j95_assocdiff.csv` |  |  | drop | prune_pleurisy | broad_assoc | 41 | ASSOCIATION,DIFF,KEEP | 1 |
| 4 | `submissions/v724_v296_bronchitis_no_j43_j68_assocdiff.csv` |  |  | drop | prune_bronchitis | broad_assoc | 44 | ASSOCIATION,DIFF,KEEP | 1 |
| 5 | `submissions/v725_v296_thyroiditis_no_e03_assocdiff.csv` |  |  | drop | prune_thyroiditis | broad_assoc | 39 | ASSOCIATION,DIFF,KEEP | 1 |
| 6 | `submissions/v726_v296_npc_no_d00_c44_d10_assocdiff.csv` |  |  | drop | prune_npc | broad_assoc | 65 | ASSOCIATION,DIFF,KEEP | 1 |
| 7 | `submissions/v727_v296_ckd_no_q60_q61_q62_assocdiff.csv` |  |  | drop | prune_ckd | broad_assoc | 66 | ASSOCIATION,DIFF,KEEP | 1 |
| 8 | `submissions/v728_v296_ckd_no_i50_assocdiff.csv` |  |  | drop | prune_ckd | assocdiff | 26 | ASSOCIATION,DIFF,KEEP | 1 |

## Use

- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.
- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.
- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.
- Treat public-neutral results as private-hedge evidence, not proof of private improvement.
