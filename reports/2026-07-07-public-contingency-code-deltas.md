# CohortX Plan Code Deltas - 2026-07-07-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-07-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 254
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v441_copd_j31_j98_med_add_thymus_nodes.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 8 | 5 | v441: COPD J31/J98 prune plus mediastinum thymus/nodes | public-only combo of v293 COPD and v300 mediastinum |
| 1 | `submissions/v441_copd_j31_j98_med_add_thymus_nodes.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v441: COPD J31/J98 prune plus mediastinum thymus/nodes | public-only combo of v293 COPD and v300 mediastinum |
| 2 | `submissions/v442_copd_j81_j82_med_add_thymus_nodes.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v442: COPD J81/J82 prune plus mediastinum thymus/nodes | public-only combo of v294 COPD and v300 mediastinum |
| 2 | `submissions/v442_copd_j81_j82_med_add_thymus_nodes.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v442: COPD J81/J82 prune plus mediastinum thymus/nodes | public-only combo of v294 COPD and v300 mediastinum |
| 3 | `submissions/v443_copd_j93_j95_med_add_thymus_nodes.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v443: COPD J93/J95 prune plus mediastinum thymus/nodes | public-only combo of v295 COPD and v300 mediastinum |
| 3 | `submissions/v443_copd_j93_j95_med_add_thymus_nodes.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v443: COPD J93/J95 prune plus mediastinum thymus/nodes | public-only combo of v295 COPD and v300 mediastinum |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 8 | 5 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v444: COPD J31/J98 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v445: COPD J81/J82 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v446: COPD J93/J95 plus highconf ASSOC | near-best COPD with high-confidence ASSOC-only source v283 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 8 | 5 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v447: COPD J31/J98 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v448: COPD J81/J82 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v449: COPD J93/J95 plus broad ASSOC | near-best COPD with broad ASSOC-only source v286 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 8 | 5 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Pleurisy | DIFF | 17 | 0 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Bronchitis | DIFF | 32 | 0 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | Pneumonia | DIFF | 71 | 0 | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Pleurisy | DIFF | 17 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Bronchitis | DIFF | 32 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | Pneumonia | DIFF | 71 | 0 | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Pleurisy | DIFF | 17 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Bronchitis | DIFF | 32 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | Pneumonia | DIFF | 71 | 0 | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF | near-best COPD with public-tied pulmonary ASSOC/DIFF source v287 |
| 13 | `submissions/v453_copd_j31_j98_cardiorenal_assocdiff.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 8 | 5 | v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 13 | `submissions/v453_copd_j31_j98_cardiorenal_assocdiff.csv` | CKD | ASSOCIATION | 17 | 0 | v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 13 | `submissions/v453_copd_j31_j98_cardiorenal_assocdiff.csv` | CKD | DIFF | 6 | 0 | v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 13 | `submissions/v453_copd_j31_j98_cardiorenal_assocdiff.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 13 | `submissions/v453_copd_j31_j98_cardiorenal_assocdiff.csv` | Heart Failure | DIFF | 15 | 0 | v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 13 | `submissions/v453_copd_j31_j98_cardiorenal_assocdiff.csv` | Diabetes | ASSOCIATION | 116 | 0 | v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 13 | `submissions/v453_copd_j31_j98_cardiorenal_assocdiff.csv` | Diabetes | DIFF | 7 | 0 | v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 14 | `submissions/v454_copd_j81_j82_cardiorenal_assocdiff.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 14 | `submissions/v454_copd_j81_j82_cardiorenal_assocdiff.csv` | CKD | ASSOCIATION | 17 | 0 | v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 14 | `submissions/v454_copd_j81_j82_cardiorenal_assocdiff.csv` | CKD | DIFF | 6 | 0 | v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 14 | `submissions/v454_copd_j81_j82_cardiorenal_assocdiff.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 14 | `submissions/v454_copd_j81_j82_cardiorenal_assocdiff.csv` | Heart Failure | DIFF | 15 | 0 | v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 14 | `submissions/v454_copd_j81_j82_cardiorenal_assocdiff.csv` | Diabetes | ASSOCIATION | 116 | 0 | v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 14 | `submissions/v454_copd_j81_j82_cardiorenal_assocdiff.csv` | Diabetes | DIFF | 7 | 0 | v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 15 | `submissions/v455_copd_j93_j95_cardiorenal_assocdiff.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 15 | `submissions/v455_copd_j93_j95_cardiorenal_assocdiff.csv` | CKD | ASSOCIATION | 17 | 0 | v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 15 | `submissions/v455_copd_j93_j95_cardiorenal_assocdiff.csv` | CKD | DIFF | 6 | 0 | v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 15 | `submissions/v455_copd_j93_j95_cardiorenal_assocdiff.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 15 | `submissions/v455_copd_j93_j95_cardiorenal_assocdiff.csv` | Heart Failure | DIFF | 15 | 0 | v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 15 | `submissions/v455_copd_j93_j95_cardiorenal_assocdiff.csv` | Diabetes | ASSOCIATION | 116 | 0 | v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 15 | `submissions/v455_copd_j93_j95_cardiorenal_assocdiff.csv` | Diabetes | DIFF | 7 | 0 | v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF | near-best COPD with public-tied cardiorenal ASSOC/DIFF source v288 |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 8 | 5 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v456: COPD J31/J98 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v457: COPD J81/J82 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v458: COPD J93/J95 med plus highconf ASSOC | public-only COPD+mediastinum combo with high-confidence ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 8 | 5 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v459: COPD J31/J98 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 4 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v460: COPD J81/J82 med plus broad ASSOC | public-only COPD+mediastinum combo with broad ASSOC |

## Exact Code Changes

### 1. `v441_copd_j31_j98_med_add_thymus_nodes.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v441: COPD J31/J98 prune plus mediastinum thymus/nodes
- Added (8): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (5): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 1. `v441_copd_j31_j98_med_add_thymus_nodes.csv` - Enlarged Mediastinum / KEEP

- Message: v441: COPD J31/J98 prune plus mediastinum thymus/nodes
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 2. `v442_copd_j81_j82_med_add_thymus_nodes.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v442: COPD J81/J82 prune plus mediastinum thymus/nodes
- Added (4): `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (0): none

### 2. `v442_copd_j81_j82_med_add_thymus_nodes.csv` - Enlarged Mediastinum / KEEP

- Message: v442: COPD J81/J82 prune plus mediastinum thymus/nodes
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 3. `v443_copd_j93_j95_med_add_thymus_nodes.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v443: COPD J93/J95 prune plus mediastinum thymus/nodes
- Added (4): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia
- Removed (0): none

### 3. `v443_copd_j93_j95_med_add_thymus_nodes.csv` - Enlarged Mediastinum / KEEP

- Message: v443: COPD J93/J95 prune plus mediastinum thymus/nodes
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (8): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (5): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 4. `v444_copd_j31_j98_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v444: COPD J31/J98 plus highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (4): `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 5. `v445_copd_j81_j82_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v445: COPD J81/J82 plus highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (4): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 6. `v446_copd_j93_j95_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v446: COPD J93/J95 plus highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (8): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (5): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 7. `v447_copd_j31_j98_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v447: COPD J31/J98 plus broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (4): `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 8. `v448_copd_j81_j82_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v448: COPD J81/J82 plus broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (4): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 9. `v449_copd_j93_j95_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v449: COPD J93/J95 plus broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (8): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (5): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Pleurisy / ASSOCIATION

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Pleurisy / DIFF

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Bronchitis / ASSOCIATION

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Bronchitis / DIFF

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Interstitial Lung Disease / DIFF

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Pneumonia / ASSOCIATION

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 10. `v450_copd_j31_j98_pulmonary_assocdiff.csv` - Pneumonia / DIFF

- Message: v450: COPD J31/J98 plus pulmonary ASSOC/DIFF
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (4): `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Pleurisy / ASSOCIATION

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Pleurisy / DIFF

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Bronchitis / ASSOCIATION

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Bronchitis / DIFF

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Interstitial Lung Disease / DIFF

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Pneumonia / ASSOCIATION

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 11. `v451_copd_j81_j82_pulmonary_assocdiff.csv` - Pneumonia / DIFF

- Message: v451: COPD J81/J82 plus pulmonary ASSOC/DIFF
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (4): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Pleurisy / ASSOCIATION

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Pleurisy / DIFF

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Bronchitis / ASSOCIATION

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Bronchitis / DIFF

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Interstitial Lung Disease / DIFF

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Pneumonia / ASSOCIATION

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 12. `v452_copd_j93_j95_pulmonary_assocdiff.csv` - Pneumonia / DIFF

- Message: v452: COPD J93/J95 plus pulmonary ASSOC/DIFF
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 13. `v453_copd_j31_j98_cardiorenal_assocdiff.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF
- Added (8): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (5): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 13. `v453_copd_j31_j98_cardiorenal_assocdiff.csv` - CKD / ASSOCIATION

- Message: v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 13. `v453_copd_j31_j98_cardiorenal_assocdiff.csv` - CKD / DIFF

- Message: v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 13. `v453_copd_j31_j98_cardiorenal_assocdiff.csv` - Heart Failure / ASSOCIATION

- Message: v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 13. `v453_copd_j31_j98_cardiorenal_assocdiff.csv` - Heart Failure / DIFF

- Message: v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 13. `v453_copd_j31_j98_cardiorenal_assocdiff.csv` - Diabetes / ASSOCIATION

- Message: v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 13. `v453_copd_j31_j98_cardiorenal_assocdiff.csv` - Diabetes / DIFF

- Message: v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 14. `v454_copd_j81_j82_cardiorenal_assocdiff.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF
- Added (4): `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (0): none

### 14. `v454_copd_j81_j82_cardiorenal_assocdiff.csv` - CKD / ASSOCIATION

- Message: v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 14. `v454_copd_j81_j82_cardiorenal_assocdiff.csv` - CKD / DIFF

- Message: v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 14. `v454_copd_j81_j82_cardiorenal_assocdiff.csv` - Heart Failure / ASSOCIATION

- Message: v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 14. `v454_copd_j81_j82_cardiorenal_assocdiff.csv` - Heart Failure / DIFF

- Message: v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 14. `v454_copd_j81_j82_cardiorenal_assocdiff.csv` - Diabetes / ASSOCIATION

- Message: v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 14. `v454_copd_j81_j82_cardiorenal_assocdiff.csv` - Diabetes / DIFF

- Message: v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 15. `v455_copd_j93_j95_cardiorenal_assocdiff.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF
- Added (4): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia
- Removed (0): none

### 15. `v455_copd_j93_j95_cardiorenal_assocdiff.csv` - CKD / ASSOCIATION

- Message: v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 15. `v455_copd_j93_j95_cardiorenal_assocdiff.csv` - CKD / DIFF

- Message: v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 15. `v455_copd_j93_j95_cardiorenal_assocdiff.csv` - Heart Failure / ASSOCIATION

- Message: v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 15. `v455_copd_j93_j95_cardiorenal_assocdiff.csv` - Heart Failure / DIFF

- Message: v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 15. `v455_copd_j93_j95_cardiorenal_assocdiff.csv` - Diabetes / ASSOCIATION

- Message: v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 15. `v455_copd_j93_j95_cardiorenal_assocdiff.csv` - Diabetes / DIFF

- Message: v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (8): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (5): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 16. `v456_copd_j31_j98_med_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v456: COPD J31/J98 med plus highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (4): `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 17. `v457_copd_j81_j82_med_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v457: COPD J81/J82 med plus highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (4): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 18. `v458_copd_j93_j95_med_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v458: COPD J93/J95 med plus highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (8): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (5): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 19. `v459_copd_j31_j98_med_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v459: COPD J31/J98 med plus broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (4): `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 20. `v460_copd_j81_j82_med_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v460: COPD J81/J82 med plus broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none
