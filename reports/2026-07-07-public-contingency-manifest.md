# CohortX Plan Integrity Manifest — 2026-07-07-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-07-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20
- Unique SHA-256 files: 20
- High-volume watchlist: 0 over 1000

## Gates

| Gate | Status | Detail |
|---|---|---|
| item_count | ready | items=20/20 |
| row_counts | ready | expected=23; files=20 |
| unique_hashes | ready | unique=20/20 |
| change_volume_watch | clear | max_volume=703; over_limit=0; limit=1000 |

## Manifest

| Order | File | SHA-256 | Rows | Change volume | Conditions | Axes | Message |
|---:|---|---|---:|---:|---:|---|---|
| 1 | `submissions/v441_copd_j31_j98_med_add_thymus_nodes.csv` | `6a56c5d3bbd1511c69b3b072fab03cc383b8e516bcd5e91a9d540d3a0a516c78` | 23 | 17 | 2 | source=copd_j31_j98; med=keep; private_keep=none; assoc=none | v441: COPD J31/J98 prune plus mediastinum thymus/nodes |
| 2 | `submissions/v442_copd_j81_j82_med_add_thymus_nodes.csv` | `3eb82dfcf4a0c0356bf3f7ddc47a5d1f292441fef23c62503752144d0e9a1c32` | 23 | 8 | 2 | source=copd_j81_j82; med=keep; private_keep=none; assoc=none | v442: COPD J81/J82 prune plus mediastinum thymus/nodes |
| 3 | `submissions/v443_copd_j93_j95_med_add_thymus_nodes.csv` | `5c566dfeb8c6ef42b23c8068e8ddd5b5c77f6f9efb210e46c7fe75cd2fd8da7a` | 23 | 8 | 2 | source=copd_j93_j95; med=keep; private_keep=none; assoc=none | v443: COPD J93/J95 prune plus mediastinum thymus/nodes |
| 4 | `submissions/v444_copd_j31_j98_highconf_assoc.csv` | `815cf819951236f9e8554ca4cefea73dc5c638030e3e271bafc115e3517e12b4` | 23 | 368 | 15 | source=copd_j31_j98; med=drop; private_keep=none; assoc=highconf_assoc | v444: COPD J31/J98 plus highconf ASSOC |
| 5 | `submissions/v445_copd_j81_j82_highconf_assoc.csv` | `842207776e24b96a7e7c518e0f12b08225a131c06782db4f3b235aef55651d98` | 23 | 359 | 15 | source=copd_j81_j82; med=drop; private_keep=none; assoc=highconf_assoc | v445: COPD J81/J82 plus highconf ASSOC |
| 6 | `submissions/v446_copd_j93_j95_highconf_assoc.csv` | `4c0264bc706d0e5c43d04199433fbc664e591a017aa78182c84b77363b381be1` | 23 | 359 | 15 | source=copd_j93_j95; med=drop; private_keep=none; assoc=highconf_assoc | v446: COPD J93/J95 plus highconf ASSOC |
| 7 | `submissions/v447_copd_j31_j98_broad_assoc.csv` | `31ac7e253c944ff85237c78ca46bda1a55347793119aab52ae75cbdf7acba847` | 23 | 699 | 21 | source=copd_j31_j98; med=drop; private_keep=none; assoc=broad_assoc | v447: COPD J31/J98 plus broad ASSOC |
| 8 | `submissions/v448_copd_j81_j82_broad_assoc.csv` | `7e9a3afb3c6f86fc1d9cbaff2a4a3786f771dee5023d093d3ae9b5772ce84c99` | 23 | 690 | 21 | source=copd_j81_j82; med=drop; private_keep=none; assoc=broad_assoc | v448: COPD J81/J82 plus broad ASSOC |
| 9 | `submissions/v449_copd_j93_j95_broad_assoc.csv` | `0533a0d96422ad8c6f13b6b6d58fe0211f0dc1206a41d8ff12bbfebcfc9af3f2` | 23 | 690 | 21 | source=copd_j93_j95; med=drop; private_keep=none; assoc=broad_assoc | v449: COPD J93/J95 plus broad ASSOC |
| 10 | `submissions/v450_copd_j31_j98_pulmonary_assocdiff.csv` | `77425fd7a517ca5af0810be1b3f048c7b4053409f44e36bc1769d70691adedcd` | 23 | 261 | 5 | source=copd_j31_j98; med=drop; private_keep=none; assoc=pulmonary_assocdiff | v450: COPD J31/J98 plus pulmonary ASSOC/DIFF |
| 11 | `submissions/v451_copd_j81_j82_pulmonary_assocdiff.csv` | `818c04023eaccd213b82677ae420fc9564537cefff79bc1583485b1219f0647b` | 23 | 252 | 5 | source=copd_j81_j82; med=drop; private_keep=none; assoc=pulmonary_assocdiff | v451: COPD J81/J82 plus pulmonary ASSOC/DIFF |
| 12 | `submissions/v452_copd_j93_j95_pulmonary_assocdiff.csv` | `1b4370063b1988d2a769aa27f0f271d38d0fabf90c2e0427578923a39ef23f5e` | 23 | 252 | 5 | source=copd_j93_j95; med=drop; private_keep=none; assoc=pulmonary_assocdiff | v452: COPD J93/J95 plus pulmonary ASSOC/DIFF |
| 13 | `submissions/v453_copd_j31_j98_cardiorenal_assocdiff.csv` | `95d315c655fcba6b6f03c15847c694f40a7ebe62d32496d9ca4ccf2ae0792a35` | 23 | 209 | 4 | source=copd_j31_j98; med=drop; private_keep=none; assoc=cardiorenal_assocdiff | v453: COPD J31/J98 plus cardiorenal ASSOC/DIFF |
| 14 | `submissions/v454_copd_j81_j82_cardiorenal_assocdiff.csv` | `59ff92cac57c4fdff072ce3c0aada0a79e5d9295b51784260bf47bd98c53bff6` | 23 | 200 | 4 | source=copd_j81_j82; med=drop; private_keep=none; assoc=cardiorenal_assocdiff | v454: COPD J81/J82 plus cardiorenal ASSOC/DIFF |
| 15 | `submissions/v455_copd_j93_j95_cardiorenal_assocdiff.csv` | `4395f1e9783bf92e2e28de269f412afc18ca825a4dcea383fdb645c276eddeb6` | 23 | 200 | 4 | source=copd_j93_j95; med=drop; private_keep=none; assoc=cardiorenal_assocdiff | v455: COPD J93/J95 plus cardiorenal ASSOC/DIFF |
| 16 | `submissions/v456_copd_j31_j98_med_highconf_assoc.csv` | `dcbfaef4ef7a1a10981c99307645b4e918afd25c76b9ddf66b98412de5ce6643` | 23 | 372 | 16 | source=copd_j31_j98; med=keep; private_keep=none; assoc=highconf_assoc | v456: COPD J31/J98 med plus highconf ASSOC |
| 17 | `submissions/v457_copd_j81_j82_med_highconf_assoc.csv` | `648b07ee6bd1f6d85f61f457a9400e25523c82309aff39ddca057f79b81a6da6` | 23 | 363 | 16 | source=copd_j81_j82; med=keep; private_keep=none; assoc=highconf_assoc | v457: COPD J81/J82 med plus highconf ASSOC |
| 18 | `submissions/v458_copd_j93_j95_med_highconf_assoc.csv` | `1803b47d6564fed37759317a35700b62597e19825427e7061e73d65539599d45` | 23 | 363 | 16 | source=copd_j93_j95; med=keep; private_keep=none; assoc=highconf_assoc | v458: COPD J93/J95 med plus highconf ASSOC |
| 19 | `submissions/v459_copd_j31_j98_med_broad_assoc.csv` | `ad657f2ffdf457072680f65499b52202c5808ce2c22b6386c07c86b3bbb003ad` | 23 | 703 | 22 | source=copd_j31_j98; med=keep; private_keep=none; assoc=broad_assoc | v459: COPD J31/J98 med plus broad ASSOC |
| 20 | `submissions/v460_copd_j81_j82_med_broad_assoc.csv` | `67b0af38eac501fbf35e9bc86782c98dd37ada2f87957df6faa4d4b3d2e44988` | 23 | 694 | 22 | source=copd_j81_j82; med=keep; private_keep=none; assoc=broad_assoc | v460: COPD J81/J82 med plus broad ASSOC |

## Use

- Re-run this manifest immediately before the reset submission window.
- Any SHA-256, row-count, or change-volume drift means the plan changed and should be inspected before upload.
- The high-volume watchlist is strategic, not a hard stop; review files over 1000 as broad private hedges before promoting them.
- This complements `validate-plan`: validation checks shape and duplicate content; the manifest locks the exact file bytes and strategic axes.
