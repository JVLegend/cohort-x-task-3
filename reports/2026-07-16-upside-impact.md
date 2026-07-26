# CohortX Plan Impact Readout - 2026-07-16-upside

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-upside.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
- Anchor public: 0.43606
- Scored items: 20/20
- Improved/tied/worse/missing: 5/0/15/0

## Decision Table

| Order | File | Status | Public | Delta | Signal | Edit | Interpretation |
|---:|---|---|---:|---:|---|---|---|
| 1 | `v827_v715_med_drop_c78.csv` | complete | 0.43641 | +0.00035 | improved | removed 2 | removal improved public score; consider pruning these codes or combining this removal |
| 2 | `v828_v715_med_drop_d38.csv` | complete | 0.43641 | +0.00035 | improved | removed 2 | removal improved public score; consider pruning these codes or combining this removal |
| 3 | `v829_v715_med_drop_j85.csv` | complete | 0.43476 | -0.00130 | worse | removed 2 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 4 | `v830_v715_med_drop_q34.csv` | complete | 0.43695 | +0.00089 | improved | removed 5 | removal improved public score; consider pruning these codes or combining this removal |
| 5 | `v831_v715_med_drop_c38.csv` | complete | 0.43134 | -0.00472 | worse | removed 7 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 6 | `v832_v715_med_drop_d15.csv` | complete | 0.43713 | +0.00107 | improved | removed 6 | removal improved public score; consider pruning these codes or combining this removal |
| 7 | `v833_v715_med_drop_j980_j981.csv` | complete | 0.43205 | -0.00401 | worse | removed 6 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 8 | `v834_v715_med_drop_j982_j983_j984.csv` | complete | 0.43410 | -0.00196 | worse | removed 3 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 9 | `v835_v715_med_drop_j985.csv` | complete | 0.43410 | -0.00196 | worse | removed 3 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 10 | `v836_v715_med_drop_j986_j988_j989.csv` | complete | 0.43410 | -0.00196 | worse | removed 3 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 11 | `v837_v715_med_drop_c380_c384_c388.csv` | complete | 0.43410 | -0.00196 | worse | removed 3 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 12 | `v838_v715_med_drop_q34_nonmediastinal.csv` | complete | 0.43658 | +0.00052 | improved | removed 3 | removal improved public score; consider pruning these codes or combining this removal |
| 13 | `v839_v301_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | added 47 | addition hurt public score; treat these codes as public false positives |
| 14 | `v840_v302_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | added 47 | addition hurt public score; treat these codes as public false positives |
| 15 | `v841_v341_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | added 47 | addition hurt public score; treat these codes as public false positives |
| 16 | `v842_v342_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | added 47 | addition hurt public score; treat these codes as public false positives |
| 17 | `v843_v357_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | added 47 | addition hurt public score; treat these codes as public false positives |
| 18 | `v844_v382_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | added 47 | addition hurt public score; treat these codes as public false positives |
| 19 | `v845_v384_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | added 47 | addition hurt public score; treat these codes as public false positives |
| 20 | `v846_v385_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | added 47 | addition hurt public score; treat these codes as public false positives |

## Ranked Scored Probes

| Rank | File | Delta | ICD change | Exact codes |
|---:|---|---:|---|---|
| 1 | `v832_v715_med_drop_d15.csv` | +0.00107 | removed 6 | `D15` - Benign neoplasm of other and unspecified intrathoracic organs<br>`D150` - Benign neoplasm of thymus<br>`D151` - Benign neoplasm of heart<br>`D152` - Benign neoplasm of mediastinum<br>`D157` - Benign neoplasm of other specified intrathoracic organs<br>`D159` - Benign neoplasm of intrathoracic organ, unspecified |
| 2 | `v830_v715_med_drop_q34.csv` | +0.00089 | removed 5 | `Q34` - Other congenital malformations of respiratory system<br>`Q340` - Anomaly of pleura<br>`Q341` - Congenital cyst of mediastinum<br>`Q348` - Other specified congenital malformations of respiratory system<br>`Q349` - Congenital malformation of respiratory system, unspecified |
| 3 | `v838_v715_med_drop_q34_nonmediastinal.csv` | +0.00052 | removed 3 | `Q340` - Anomaly of pleura<br>`Q348` - Other specified congenital malformations of respiratory system<br>`Q349` - Congenital malformation of respiratory system, unspecified |
| 4 | `v827_v715_med_drop_c78.csv` | +0.00035 | removed 2 | `C78` - Secondary malignant neoplasm of respiratory and digestive organs<br>`C781` - Secondary malignant neoplasm of mediastinum |
| 5 | `v828_v715_med_drop_d38.csv` | +0.00035 | removed 2 | `D38` - Neoplasm of uncertain behavior of middle ear and respiratory and intrathoracic organs<br>`D383` - Neoplasm of uncertain behavior of mediastinum |
| 6 | `v829_v715_med_drop_j85.csv` | -0.00130 | removed 2 | `J85` - Abscess of lung and mediastinum<br>`J853` - Abscess of mediastinum |
| 7 | `v834_v715_med_drop_j982_j983_j984.csv` | -0.00196 | removed 3 | `J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema<br>`J984` - Other disorders of lung |
| 8 | `v835_v715_med_drop_j985.csv` | -0.00196 | removed 3 | `J985` - Diseases of mediastinum, not elsewhere classified<br>`J9851` - Mediastinitis<br>`J9859` - Other diseases of mediastinum, not elsewhere classified |
| 9 | `v836_v715_med_drop_j986_j988_j989.csv` | -0.00196 | removed 3 | `J986` - Disorders of diaphragm<br>`J988` - Other specified respiratory disorders<br>`J989` - Respiratory disorder, unspecified |
| 10 | `v837_v715_med_drop_c380_c384_c388.csv` | -0.00196 | removed 3 | `C380` - Malignant neoplasm of heart<br>`C384` - Malignant neoplasm of pleura<br>`C388` - Malignant neoplasm of overlapping sites of heart, mediastinum and pleura |
| 11 | `v839_v301_add_c39_family.csv` | -0.00257 | added 47 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +39 more |
| 12 | `v840_v302_add_c39_family.csv` | -0.00257 | added 47 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +39 more |
| 13 | `v841_v341_add_c39_family.csv` | -0.00257 | added 47 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +39 more |
| 14 | `v842_v342_add_c39_family.csv` | -0.00257 | added 47 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +39 more |
| 15 | `v843_v357_add_c39_family.csv` | -0.00257 | added 47 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +39 more |
| 16 | `v844_v382_add_c39_family.csv` | -0.00257 | added 47 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +39 more |
| 17 | `v845_v384_add_c39_family.csv` | -0.00257 | added 47 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +39 more |
| 18 | `v846_v385_add_c39_family.csv` | -0.00257 | added 47 | `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>... +39 more |
| 19 | `v833_v715_med_drop_j980_j981.csv` | -0.00401 | removed 6 | `J980` - Diseases of bronchus, not elsewhere classified<br>`J9801` - Acute bronchospasm<br>`J9809` - Other diseases of bronchus, not elsewhere classified<br>`J981` - Pulmonary collapse<br>`J9811` - Atelectasis<br>`J9819` - Other pulmonary collapse |
| 20 | `v831_v715_med_drop_c38.csv` | -0.00472 | removed 7 | `C38` - Malignant neoplasm of heart, mediastinum and pleura<br>`C380` - Malignant neoplasm of heart<br>`C381` - Malignant neoplasm of anterior mediastinum<br>`C382` - Malignant neoplasm of posterior mediastinum<br>`C383` - Malignant neoplasm of mediastinum, part unspecified<br>`C384` - Malignant neoplasm of pleura<br>`C388` - Malignant neoplasm of overlapping sites of heart, mediastinum and pleura |

## Use

- Improved removals are pruning candidates for public-facing combos.
- Improved additions are promotion candidates for public-facing combos.
- Tied edits are mainly private hedges unless later combo evidence says otherwise.
- Worse removals indicate codes that likely belong in the public gold slice; worse additions are public false positives.
