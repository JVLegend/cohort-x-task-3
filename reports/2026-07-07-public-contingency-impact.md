# CohortX Plan Impact Readout - 2026-07-07-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-07-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Anchor public: 0.43156
- Scored items: 20/20
- Improved/tied/worse/missing: 0/0/20/0

## Decision Table

| Order | File | Status | Public | Delta | Signal | Edit | Interpretation |
|---:|---|---|---:|---:|---|---|---|
| 1 | `v441_copd_j31_j98_med_add_thymus_nodes.csv` | complete | 0.42894 | -0.00262 | worse | +8/-5 | mixed edit hurt public score; avoid as-is and decompose |
| 2 | `v442_copd_j81_j82_med_add_thymus_nodes.csv` | complete | 0.42855 | -0.00301 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 3 | `v443_copd_j93_j95_med_add_thymus_nodes.csv` | complete | 0.42855 | -0.00301 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 4 | `v444_copd_j31_j98_highconf_assoc.csv` | complete | 0.43015 | -0.00141 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 5 | `v445_copd_j81_j82_highconf_assoc.csv` | complete | 0.42976 | -0.00180 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 6 | `v446_copd_j93_j95_highconf_assoc.csv` | complete | 0.42976 | -0.00180 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 7 | `v447_copd_j31_j98_broad_assoc.csv` | complete | 0.43015 | -0.00141 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 8 | `v448_copd_j81_j82_broad_assoc.csv` | complete | 0.42976 | -0.00180 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 9 | `v449_copd_j93_j95_broad_assoc.csv` | complete | 0.42976 | -0.00180 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 10 | `v450_copd_j31_j98_pulmonary_assocdiff.csv` | complete | 0.42874 | -0.00282 | worse | +8/-5 | mixed edit hurt public score; avoid as-is and decompose |
| 11 | `v451_copd_j81_j82_pulmonary_assocdiff.csv` | complete | 0.42835 | -0.00321 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 12 | `v452_copd_j93_j95_pulmonary_assocdiff.csv` | complete | 0.42835 | -0.00321 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 13 | `v453_copd_j31_j98_cardiorenal_assocdiff.csv` | complete | 0.42874 | -0.00282 | worse | +8/-5 | mixed edit hurt public score; avoid as-is and decompose |
| 14 | `v454_copd_j81_j82_cardiorenal_assocdiff.csv` | complete | 0.42835 | -0.00321 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 15 | `v455_copd_j93_j95_cardiorenal_assocdiff.csv` | complete | 0.42835 | -0.00321 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 16 | `v456_copd_j31_j98_med_highconf_assoc.csv` | complete | 0.43035 | -0.00121 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 17 | `v457_copd_j81_j82_med_highconf_assoc.csv` | complete | 0.42996 | -0.00160 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 18 | `v458_copd_j93_j95_med_highconf_assoc.csv` | complete | 0.42996 | -0.00160 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 19 | `v459_copd_j31_j98_med_broad_assoc.csv` | complete | 0.43035 | -0.00121 | worse | added 48 | addition hurt public score; treat these codes as public false positives |
| 20 | `v460_copd_j81_j82_med_broad_assoc.csv` | complete | 0.42996 | -0.00160 | worse | added 48 | addition hurt public score; treat these codes as public false positives |

## Ranked Scored Probes

| Rank | File | Delta | ICD change | Exact codes |
|---:|---|---:|---|---|
| 1 | `v456_copd_j31_j98_med_highconf_assoc.csv` | -0.00121 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 2 | `v459_copd_j31_j98_med_broad_assoc.csv` | -0.00121 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 3 | `v444_copd_j31_j98_highconf_assoc.csv` | -0.00141 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 4 | `v447_copd_j31_j98_broad_assoc.csv` | -0.00141 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 5 | `v457_copd_j81_j82_med_highconf_assoc.csv` | -0.00160 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 6 | `v458_copd_j93_j95_med_highconf_assoc.csv` | -0.00160 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 7 | `v460_copd_j81_j82_med_broad_assoc.csv` | -0.00160 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 8 | `v445_copd_j81_j82_highconf_assoc.csv` | -0.00180 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 9 | `v446_copd_j93_j95_highconf_assoc.csv` | -0.00180 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 10 | `v448_copd_j81_j82_broad_assoc.csv` | -0.00180 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 11 | `v449_copd_j93_j95_broad_assoc.csv` | -0.00180 | added 48 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +40 more |
| 12 | `v441_copd_j31_j98_med_add_thymus_nodes.csv` | -0.00262 | +8/-5 | `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure |
| 13 | `v450_copd_j31_j98_pulmonary_assocdiff.csv` | -0.00282 | +8/-5 | `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure |
| 14 | `v453_copd_j31_j98_cardiorenal_assocdiff.csv` | -0.00282 | +8/-5 | `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure |
| 15 | `v442_copd_j81_j82_med_add_thymus_nodes.csv` | -0.00301 | added 4 | `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure |
| 16 | `v443_copd_j93_j95_med_add_thymus_nodes.csv` | -0.00301 | added 4 | `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia |
| 17 | `v451_copd_j81_j82_pulmonary_assocdiff.csv` | -0.00321 | added 4 | `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure |
| 18 | `v452_copd_j93_j95_pulmonary_assocdiff.csv` | -0.00321 | added 4 | `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia |
| 19 | `v454_copd_j81_j82_cardiorenal_assocdiff.csv` | -0.00321 | added 4 | `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure |
| 20 | `v455_copd_j93_j95_cardiorenal_assocdiff.csv` | -0.00321 | added 4 | `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia |

## Use

- Improved removals are pruning candidates for public-facing combos.
- Improved additions are promotion candidates for public-facing combos.
- Tied edits are mainly private hedges unless later combo evidence says otherwise.
- Worse removals indicate codes that likely belong in the public gold slice; worse additions are public false positives.
