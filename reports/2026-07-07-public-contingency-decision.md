# CohortX Plan Decision Matrix — 2026-07-07-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-07-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Matched decision comparisons: 18

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| matched_comparisons | ready | comparisons=18 |

## Decision Comparisons

| Axis | Held constant | Variants | Files | Rule |
|---|---|---|---|---|
| med | source=copd_j31_j98; private_keep=none; assoc=highconf_assoc | `med=drop` (1); `med=keep` (1) | `drop`: `v444_copd_j31_j98_highconf_assoc.csv`; `keep`: `v456_copd_j31_j98_med_highconf_assoc.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=copd_j81_j82; private_keep=none; assoc=highconf_assoc | `med=drop` (1); `med=keep` (1) | `drop`: `v445_copd_j81_j82_highconf_assoc.csv`; `keep`: `v457_copd_j81_j82_med_highconf_assoc.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=copd_j93_j95; private_keep=none; assoc=highconf_assoc | `med=drop` (1); `med=keep` (1) | `drop`: `v446_copd_j93_j95_highconf_assoc.csv`; `keep`: `v458_copd_j93_j95_med_highconf_assoc.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=copd_j31_j98; private_keep=none; assoc=broad_assoc | `med=drop` (1); `med=keep` (1) | `drop`: `v447_copd_j31_j98_broad_assoc.csv`; `keep`: `v459_copd_j31_j98_med_broad_assoc.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| med | source=copd_j81_j82; private_keep=none; assoc=broad_assoc | `med=drop` (1); `med=keep` (1) | `drop`: `v448_copd_j81_j82_broad_assoc.csv`; `keep`: `v460_copd_j81_j82_med_broad_assoc.csv` | If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites. |
| assoc | source=copd_j31_j98; med=keep; private_keep=none | `assoc=broad_assoc` (1); `assoc=highconf_assoc` (1); `assoc=none` (1) | `broad_assoc`: `v459_copd_j31_j98_med_broad_assoc.csv`; `highconf_assoc`: `v456_copd_j31_j98_med_highconf_assoc.csv`; `none`: `v441_copd_j31_j98_med_add_thymus_nodes.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=copd_j81_j82; med=keep; private_keep=none | `assoc=broad_assoc` (1); `assoc=highconf_assoc` (1); `assoc=none` (1) | `broad_assoc`: `v460_copd_j81_j82_med_broad_assoc.csv`; `highconf_assoc`: `v457_copd_j81_j82_med_highconf_assoc.csv`; `none`: `v442_copd_j81_j82_med_add_thymus_nodes.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=copd_j93_j95; med=keep; private_keep=none | `assoc=highconf_assoc` (1); `assoc=none` (1) | `highconf_assoc`: `v458_copd_j93_j95_med_highconf_assoc.csv`; `none`: `v443_copd_j93_j95_med_add_thymus_nodes.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=copd_j31_j98; med=drop; private_keep=none | `assoc=broad_assoc` (1); `assoc=cardiorenal_assocdiff` (1); `assoc=highconf_assoc` (1); `assoc=pulmonary_assocdiff` (1) | `broad_assoc`: `v447_copd_j31_j98_broad_assoc.csv`; `cardiorenal_assocdiff`: `v453_copd_j31_j98_cardiorenal_assocdiff.csv`; `highconf_assoc`: `v444_copd_j31_j98_highconf_assoc.csv`; `pulmonary_assocdiff`: `v450_copd_j31_j98_pulmonary_assocdiff.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=copd_j81_j82; med=drop; private_keep=none | `assoc=broad_assoc` (1); `assoc=cardiorenal_assocdiff` (1); `assoc=highconf_assoc` (1); `assoc=pulmonary_assocdiff` (1) | `broad_assoc`: `v448_copd_j81_j82_broad_assoc.csv`; `cardiorenal_assocdiff`: `v454_copd_j81_j82_cardiorenal_assocdiff.csv`; `highconf_assoc`: `v445_copd_j81_j82_highconf_assoc.csv`; `pulmonary_assocdiff`: `v451_copd_j81_j82_pulmonary_assocdiff.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| assoc | source=copd_j93_j95; med=drop; private_keep=none | `assoc=broad_assoc` (1); `assoc=cardiorenal_assocdiff` (1); `assoc=highconf_assoc` (1); `assoc=pulmonary_assocdiff` (1) | `broad_assoc`: `v449_copd_j93_j95_broad_assoc.csv`; `cardiorenal_assocdiff`: `v455_copd_j93_j95_cardiorenal_assocdiff.csv`; `highconf_assoc`: `v446_copd_j93_j95_highconf_assoc.csv`; `pulmonary_assocdiff`: `v452_copd_j93_j95_pulmonary_assocdiff.csv` | Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity. |
| source | med=keep; private_keep=none; assoc=none | `source=copd_j31_j98` (1); `source=copd_j81_j82` (1); `source=copd_j93_j95` (1) | `copd_j31_j98`: `v441_copd_j31_j98_med_add_thymus_nodes.csv`; `copd_j81_j82`: `v442_copd_j81_j82_med_add_thymus_nodes.csv`; `copd_j93_j95`: `v443_copd_j93_j95_med_add_thymus_nodes.csv` | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |
| source | med=drop; private_keep=none; assoc=highconf_assoc | `source=copd_j31_j98` (1); `source=copd_j81_j82` (1); `source=copd_j93_j95` (1) | `copd_j31_j98`: `v444_copd_j31_j98_highconf_assoc.csv`; `copd_j81_j82`: `v445_copd_j81_j82_highconf_assoc.csv`; `copd_j93_j95`: `v446_copd_j93_j95_highconf_assoc.csv` | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |
| source | med=drop; private_keep=none; assoc=broad_assoc | `source=copd_j31_j98` (1); `source=copd_j81_j82` (1); `source=copd_j93_j95` (1) | `copd_j31_j98`: `v447_copd_j31_j98_broad_assoc.csv`; `copd_j81_j82`: `v448_copd_j81_j82_broad_assoc.csv`; `copd_j93_j95`: `v449_copd_j93_j95_broad_assoc.csv` | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |
| source | med=drop; private_keep=none; assoc=pulmonary_assocdiff | `source=copd_j31_j98` (1); `source=copd_j81_j82` (1); `source=copd_j93_j95` (1) | `copd_j31_j98`: `v450_copd_j31_j98_pulmonary_assocdiff.csv`; `copd_j81_j82`: `v451_copd_j81_j82_pulmonary_assocdiff.csv`; `copd_j93_j95`: `v452_copd_j93_j95_pulmonary_assocdiff.csv` | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |
| source | med=drop; private_keep=none; assoc=cardiorenal_assocdiff | `source=copd_j31_j98` (1); `source=copd_j81_j82` (1); `source=copd_j93_j95` (1) | `copd_j31_j98`: `v453_copd_j31_j98_cardiorenal_assocdiff.csv`; `copd_j81_j82`: `v454_copd_j81_j82_cardiorenal_assocdiff.csv`; `copd_j93_j95`: `v455_copd_j93_j95_cardiorenal_assocdiff.csv` | Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites. |

## Post-Score Checklist

1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-07-public-contingency.csv` after all 20 scores are complete.
2. Run `.venv/bin/python src/cohortx_ops.py plan-decision-outcome plans/2026-07-07-public-contingency.csv` to convert matched comparisons into axis winners.
3. Run `.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-07-public-contingency.csv --out reports/2026-07-07-public-contingency-impact.md`.
4. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.
5. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.

## Use

- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.
- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.
