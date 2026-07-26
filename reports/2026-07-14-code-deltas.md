# CohortX Plan Code Deltas - 2026-07-14

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-14.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 52
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v701_v633_med_add_e32.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v701: v633 plus E32 thymus diseases | C37 core plus low-volume non-neoplasm thymus family |
| 1 | `submissions/v701_v633_med_add_e32.csv` | Enlarged Mediastinum | KEEP | 6 | 0 | v701: v633 plus E32 thymus diseases | C37 core plus low-volume non-neoplasm thymus family |
| 2 | `submissions/v702_v633_med_add_e329.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v702: v633 plus E329 thymus disease unspecified | C37 core plus singleton thymus disease |
| 2 | `submissions/v702_v633_med_add_e329.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v702: v633 plus E329 thymus disease unspecified | C37 core plus singleton thymus disease |
| 3 | `submissions/v703_v633_med_add_e320_e328_e329.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v703: v633 plus E320/E328/E329 thymus disease | C37 core plus non-abscess thymus disease cluster |
| 3 | `submissions/v703_v633_med_add_e320_e328_e329.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v703: v633 plus E320/E328/E329 thymus disease | C37 core plus non-abscess thymus disease cluster |
| 4 | `submissions/v704_v633_med_add_e321.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v704: v633 plus E321 thymus abscess | C37 core plus abscess of thymus singleton |
| 4 | `submissions/v704_v633_med_add_e321.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v704: v633 plus E321 thymus abscess | C37 core plus abscess of thymus singleton |
| 5 | `submissions/v705_v633_med_add_c7a091.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v705: v633 plus C7A091 malignant thymus carcinoid | C37 core plus malignant carcinoid tumor of thymus |
| 5 | `submissions/v705_v633_med_add_c7a091.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v705: v633 plus C7A091 malignant thymus carcinoid | C37 core plus malignant carcinoid tumor of thymus |
| 6 | `submissions/v706_v633_med_add_d3a091.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v706: v633 plus D3A091 benign thymus carcinoid | C37 core plus benign carcinoid tumor of thymus |
| 6 | `submissions/v706_v633_med_add_d3a091.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v706: v633 plus D3A091 benign thymus carcinoid | C37 core plus benign carcinoid tumor of thymus |
| 7 | `submissions/v707_v633_med_add_thymus_carcinoids.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v707: v633 plus thymus carcinoids | C37 core plus malignant and benign thymus carcinoids |
| 7 | `submissions/v707_v633_med_add_thymus_carcinoids.csv` | Enlarged Mediastinum | KEEP | 3 | 0 | v707: v633 plus thymus carcinoids | C37 core plus malignant and benign thymus carcinoids |
| 8 | `submissions/v708_v633_med_add_z8523.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v708: v633 plus Z8523 thymus cancer history | C37 core plus personal history of malignant neoplasm of thymus |
| 8 | `submissions/v708_v633_med_add_z8523.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v708: v633 plus Z8523 thymus cancer history | C37 core plus personal history of malignant neoplasm of thymus |
| 9 | `submissions/v709_v633_med_add_z85230_z85238.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v709: v633 plus thymus cancer history detail | C37 core plus detailed thymus cancer history codes |
| 9 | `submissions/v709_v633_med_add_z85230_z85238.csv` | Enlarged Mediastinum | KEEP | 3 | 0 | v709: v633 plus thymus cancer history detail | C37 core plus detailed thymus cancer history codes |
| 10 | `submissions/v710_v633_med_add_c852.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v710: v633 plus C852 mediastinal B-cell lymphoma | C37 core plus root mediastinal thymic large B-cell lymphoma |
| 10 | `submissions/v710_v633_med_add_c852.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v710: v633 plus C852 mediastinal B-cell lymphoma | C37 core plus root mediastinal thymic large B-cell lymphoma |
| 11 | `submissions/v711_v633_med_add_c8522.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v711: v633 plus C8522 intrathoracic B-cell lymphoma | C37 core plus intrathoracic lymph node mediastinal lymphoma |
| 11 | `submissions/v711_v633_med_add_c8522.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v711: v633 plus C8522 intrathoracic B-cell lymphoma | C37 core plus intrathoracic lymph node mediastinal lymphoma |
| 12 | `submissions/v712_v633_med_add_c852_family.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v712: v633 plus C852 lymphoma family | C37 core plus full mediastinal thymic large B-cell lymphoma family |
| 12 | `submissions/v712_v633_med_add_c852_family.csv` | Enlarged Mediastinum | KEEP | 12 | 0 | v712: v633 plus C852 lymphoma family | C37 core plus full mediastinal thymic large B-cell lymphoma family |
| 13 | `submissions/v713_v633_med_add_p252.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v713: v633 plus P252 pneumomediastinum | C37 core plus pneumomediastinum singleton |
| 13 | `submissions/v713_v633_med_add_p252.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v713: v633 plus P252 pneumomediastinum | C37 core plus pneumomediastinum singleton |
| 14 | `submissions/v714_v633_med_add_n80b5.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v714: v633 plus N80B5 mediastinal endometriosis | C37 core plus mediastinal endometriosis singleton |
| 14 | `submissions/v714_v633_med_add_n80b5.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v714: v633 plus N80B5 mediastinal endometriosis | C37 core plus mediastinal endometriosis singleton |
| 15 | `submissions/v715_v633_med_add_c39.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v715: v633 plus C39 ill-defined intrathoracic malignancy | C37 core plus ill-defined intrathoracic malignancy |
| 15 | `submissions/v715_v633_med_add_c39.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v715: v633 plus C39 ill-defined intrathoracic malignancy | C37 core plus ill-defined intrathoracic malignancy |
| 16 | `submissions/v716_v633_med_add_d174.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v716: v633 plus D174 intrathoracic lipoma | C37 core plus benign intrathoracic lipoma singleton |
| 16 | `submissions/v716_v633_med_add_d174.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v716: v633 plus D174 intrathoracic lipoma | C37 core plus benign intrathoracic lipoma singleton |
| 17 | `submissions/v717_v638_med_add_e329.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v717: v638 plus E329 thymus disease unspecified | public-tied CKD/UTI hedge plus singleton thymus disease |
| 17 | `submissions/v717_v638_med_add_e329.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v717: v638 plus E329 thymus disease unspecified | public-tied CKD/UTI hedge plus singleton thymus disease |
| 17 | `submissions/v717_v638_med_add_e329.csv` | CKD | KEEP | 22 | 75 | v717: v638 plus E329 thymus disease unspecified | public-tied CKD/UTI hedge plus singleton thymus disease |
| 17 | `submissions/v717_v638_med_add_e329.csv` | UTI | KEEP | 0 | 76 | v717: v638 plus E329 thymus disease unspecified | public-tied CKD/UTI hedge plus singleton thymus disease |
| 18 | `submissions/v718_v639_med_add_e329.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v718: v639 plus E329 thymus disease unspecified | public-tied Diabetes/Pneumonia hedge plus singleton thymus disease |
| 18 | `submissions/v718_v639_med_add_e329.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v718: v639 plus E329 thymus disease unspecified | public-tied Diabetes/Pneumonia hedge plus singleton thymus disease |
| 18 | `submissions/v718_v639_med_add_e329.csv` | Diabetes | KEEP | 232 | 13 | v718: v639 plus E329 thymus disease unspecified | public-tied Diabetes/Pneumonia hedge plus singleton thymus disease |
| 18 | `submissions/v718_v639_med_add_e329.csv` | Pneumonia | KEEP | 1 | 28 | v718: v639 plus E329 thymus disease unspecified | public-tied Diabetes/Pneumonia hedge plus singleton thymus disease |
| 19 | `submissions/v719_v640_med_add_e329.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v719: v640 plus E329 thymus disease unspecified | public-tied full v185 hedge plus singleton thymus disease |
| 19 | `submissions/v719_v640_med_add_e329.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v719: v640 plus E329 thymus disease unspecified | public-tied full v185 hedge plus singleton thymus disease |
| 19 | `submissions/v719_v640_med_add_e329.csv` | CKD | KEEP | 22 | 75 | v719: v640 plus E329 thymus disease unspecified | public-tied full v185 hedge plus singleton thymus disease |
| 19 | `submissions/v719_v640_med_add_e329.csv` | UTI | KEEP | 0 | 76 | v719: v640 plus E329 thymus disease unspecified | public-tied full v185 hedge plus singleton thymus disease |
| 19 | `submissions/v719_v640_med_add_e329.csv` | Diabetes | KEEP | 232 | 13 | v719: v640 plus E329 thymus disease unspecified | public-tied full v185 hedge plus singleton thymus disease |
| 19 | `submissions/v719_v640_med_add_e329.csv` | Pneumonia | KEEP | 1 | 28 | v719: v640 plus E329 thymus disease unspecified | public-tied full v185 hedge plus singleton thymus disease |
| 20 | `submissions/v720_v640_med_add_c8522.csv` | Epistaxis | ASSOCIATION | 1 | 0 | v720: v640 plus C8522 intrathoracic B-cell lymphoma | public-tied full v185 hedge plus intrathoracic mediastinal lymphoma |
| 20 | `submissions/v720_v640_med_add_c8522.csv` | Enlarged Mediastinum | KEEP | 2 | 0 | v720: v640 plus C8522 intrathoracic B-cell lymphoma | public-tied full v185 hedge plus intrathoracic mediastinal lymphoma |
| 20 | `submissions/v720_v640_med_add_c8522.csv` | CKD | KEEP | 22 | 75 | v720: v640 plus C8522 intrathoracic B-cell lymphoma | public-tied full v185 hedge plus intrathoracic mediastinal lymphoma |
| 20 | `submissions/v720_v640_med_add_c8522.csv` | UTI | KEEP | 0 | 76 | v720: v640 plus C8522 intrathoracic B-cell lymphoma | public-tied full v185 hedge plus intrathoracic mediastinal lymphoma |
| 20 | `submissions/v720_v640_med_add_c8522.csv` | Diabetes | KEEP | 232 | 13 | v720: v640 plus C8522 intrathoracic B-cell lymphoma | public-tied full v185 hedge plus intrathoracic mediastinal lymphoma |
| 20 | `submissions/v720_v640_med_add_c8522.csv` | Pneumonia | KEEP | 1 | 28 | v720: v640 plus C8522 intrathoracic B-cell lymphoma | public-tied full v185 hedge plus intrathoracic mediastinal lymphoma |

## Exact Code Changes

### 1. `v701_v633_med_add_e32.csv` - Epistaxis / ASSOCIATION

- Message: v701: v633 plus E32 thymus diseases
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 1. `v701_v633_med_add_e32.csv` - Enlarged Mediastinum / KEEP

- Message: v701: v633 plus E32 thymus diseases
- Added (6): `C37` - Malignant neoplasm of thymus<br>`E32` - Diseases of thymus<br>`E320` - Persistent hyperplasia of thymus<br>`E321` - Abscess of thymus<br>`E328` - Other diseases of thymus<br>`E329` - Disease of thymus, unspecified
- Removed (0): none

### 2. `v702_v633_med_add_e329.csv` - Epistaxis / ASSOCIATION

- Message: v702: v633 plus E329 thymus disease unspecified
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 2. `v702_v633_med_add_e329.csv` - Enlarged Mediastinum / KEEP

- Message: v702: v633 plus E329 thymus disease unspecified
- Added (2): `C37` - Malignant neoplasm of thymus<br>`E329` - Disease of thymus, unspecified
- Removed (0): none

### 3. `v703_v633_med_add_e320_e328_e329.csv` - Epistaxis / ASSOCIATION

- Message: v703: v633 plus E320/E328/E329 thymus disease
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 3. `v703_v633_med_add_e320_e328_e329.csv` - Enlarged Mediastinum / KEEP

- Message: v703: v633 plus E320/E328/E329 thymus disease
- Added (4): `C37` - Malignant neoplasm of thymus<br>`E320` - Persistent hyperplasia of thymus<br>`E328` - Other diseases of thymus<br>`E329` - Disease of thymus, unspecified
- Removed (0): none

### 4. `v704_v633_med_add_e321.csv` - Epistaxis / ASSOCIATION

- Message: v704: v633 plus E321 thymus abscess
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 4. `v704_v633_med_add_e321.csv` - Enlarged Mediastinum / KEEP

- Message: v704: v633 plus E321 thymus abscess
- Added (2): `C37` - Malignant neoplasm of thymus<br>`E321` - Abscess of thymus
- Removed (0): none

### 5. `v705_v633_med_add_c7a091.csv` - Epistaxis / ASSOCIATION

- Message: v705: v633 plus C7A091 malignant thymus carcinoid
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 5. `v705_v633_med_add_c7a091.csv` - Enlarged Mediastinum / KEEP

- Message: v705: v633 plus C7A091 malignant thymus carcinoid
- Added (2): `C37` - Malignant neoplasm of thymus<br>`C7A091` - Malignant carcinoid tumor of the thymus
- Removed (0): none

### 6. `v706_v633_med_add_d3a091.csv` - Epistaxis / ASSOCIATION

- Message: v706: v633 plus D3A091 benign thymus carcinoid
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 6. `v706_v633_med_add_d3a091.csv` - Enlarged Mediastinum / KEEP

- Message: v706: v633 plus D3A091 benign thymus carcinoid
- Added (2): `C37` - Malignant neoplasm of thymus<br>`D3A091` - Benign carcinoid tumor of the thymus
- Removed (0): none

### 7. `v707_v633_med_add_thymus_carcinoids.csv` - Epistaxis / ASSOCIATION

- Message: v707: v633 plus thymus carcinoids
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 7. `v707_v633_med_add_thymus_carcinoids.csv` - Enlarged Mediastinum / KEEP

- Message: v707: v633 plus thymus carcinoids
- Added (3): `C37` - Malignant neoplasm of thymus<br>`C7A091` - Malignant carcinoid tumor of the thymus<br>`D3A091` - Benign carcinoid tumor of the thymus
- Removed (0): none

### 8. `v708_v633_med_add_z8523.csv` - Epistaxis / ASSOCIATION

- Message: v708: v633 plus Z8523 thymus cancer history
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 8. `v708_v633_med_add_z8523.csv` - Enlarged Mediastinum / KEEP

- Message: v708: v633 plus Z8523 thymus cancer history
- Added (2): `C37` - Malignant neoplasm of thymus<br>`Z8523` - Personal history of malignant neoplasm of thymus
- Removed (0): none

### 9. `v709_v633_med_add_z85230_z85238.csv` - Epistaxis / ASSOCIATION

- Message: v709: v633 plus thymus cancer history detail
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 9. `v709_v633_med_add_z85230_z85238.csv` - Enlarged Mediastinum / KEEP

- Message: v709: v633 plus thymus cancer history detail
- Added (3): `C37` - Malignant neoplasm of thymus<br>`Z85230` - Personal history of malignant carcinoid tumor of thymus<br>`Z85238` - Personal history of other malignant neoplasm of thymus
- Removed (0): none

### 10. `v710_v633_med_add_c852.csv` - Epistaxis / ASSOCIATION

- Message: v710: v633 plus C852 mediastinal B-cell lymphoma
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 10. `v710_v633_med_add_c852.csv` - Enlarged Mediastinum / KEEP

- Message: v710: v633 plus C852 mediastinal B-cell lymphoma
- Added (2): `C37` - Malignant neoplasm of thymus<br>`C852` - Mediastinal (thymic) large B-cell lymphoma
- Removed (0): none

### 11. `v711_v633_med_add_c8522.csv` - Epistaxis / ASSOCIATION

- Message: v711: v633 plus C8522 intrathoracic B-cell lymphoma
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 11. `v711_v633_med_add_c8522.csv` - Enlarged Mediastinum / KEEP

- Message: v711: v633 plus C8522 intrathoracic B-cell lymphoma
- Added (2): `C37` - Malignant neoplasm of thymus<br>`C8522` - Mediastinal (thymic) large B-cell lymphoma, intrathoracic lymph nodes
- Removed (0): none

### 12. `v712_v633_med_add_c852_family.csv` - Epistaxis / ASSOCIATION

- Message: v712: v633 plus C852 lymphoma family
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 12. `v712_v633_med_add_c852_family.csv` - Enlarged Mediastinum / KEEP

- Message: v712: v633 plus C852 lymphoma family
- Added (12): `C37` - Malignant neoplasm of thymus<br>`C852` - Mediastinal (thymic) large B-cell lymphoma<br>`C8520` - Mediastinal (thymic) large B-cell lymphoma, unspecified site<br>`C8521` - Mediastinal (thymic) large B-cell lymphoma, lymph nodes of head, face, and neck<br>`C8522` - Mediastinal (thymic) large B-cell lymphoma, intrathoracic lymph nodes<br>`C8523` - Mediastinal (thymic) large B-cell lymphoma, intra-abdominal lymph nodes<br>`C8524` - Mediastinal (thymic) large B-cell lymphoma, lymph nodes of axilla and upper limb<br>`C8525` - Mediastinal (thymic) large B-cell lymphoma, lymph nodes of inguinal region and lower limb<br>`C8526` - Mediastinal (thymic) large B-cell lymphoma, intrapelvic lymph nodes<br>`C8527` - Mediastinal (thymic) large B-cell lymphoma, spleen<br>`C8528` - Mediastinal (thymic) large B-cell lymphoma, lymph nodes of multiple sites<br>`C8529` - Mediastinal (thymic) large B-cell lymphoma, extranodal and solid organ sites
- Removed (0): none

### 13. `v713_v633_med_add_p252.csv` - Epistaxis / ASSOCIATION

- Message: v713: v633 plus P252 pneumomediastinum
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 13. `v713_v633_med_add_p252.csv` - Enlarged Mediastinum / KEEP

- Message: v713: v633 plus P252 pneumomediastinum
- Added (2): `C37` - Malignant neoplasm of thymus<br>`P252` - Pneumomediastinum originating in the perinatal period
- Removed (0): none

### 14. `v714_v633_med_add_n80b5.csv` - Epistaxis / ASSOCIATION

- Message: v714: v633 plus N80B5 mediastinal endometriosis
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 14. `v714_v633_med_add_n80b5.csv` - Enlarged Mediastinum / KEEP

- Message: v714: v633 plus N80B5 mediastinal endometriosis
- Added (2): `C37` - Malignant neoplasm of thymus<br>`N80B5` - Endometriosis of the mediastinal space
- Removed (0): none

### 15. `v715_v633_med_add_c39.csv` - Epistaxis / ASSOCIATION

- Message: v715: v633 plus C39 ill-defined intrathoracic malignancy
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 15. `v715_v633_med_add_c39.csv` - Enlarged Mediastinum / KEEP

- Message: v715: v633 plus C39 ill-defined intrathoracic malignancy
- Added (4): `C37` - Malignant neoplasm of thymus<br>`C39` - Malignant neoplasm of other and ill-defined sites in the respiratory system and intrathoracic organs<br>`C390` - Malignant neoplasm of upper respiratory tract, part unspecified<br>`C399` - Malignant neoplasm of lower respiratory tract, part unspecified
- Removed (0): none

### 16. `v716_v633_med_add_d174.csv` - Epistaxis / ASSOCIATION

- Message: v716: v633 plus D174 intrathoracic lipoma
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 16. `v716_v633_med_add_d174.csv` - Enlarged Mediastinum / KEEP

- Message: v716: v633 plus D174 intrathoracic lipoma
- Added (2): `C37` - Malignant neoplasm of thymus<br>`D174` - Benign lipomatous neoplasm of intrathoracic organs
- Removed (0): none

### 17. `v717_v638_med_add_e329.csv` - Epistaxis / ASSOCIATION

- Message: v717: v638 plus E329 thymus disease unspecified
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 17. `v717_v638_med_add_e329.csv` - Enlarged Mediastinum / KEEP

- Message: v717: v638 plus E329 thymus disease unspecified
- Added (2): `C37` - Malignant neoplasm of thymus<br>`E329` - Disease of thymus, unspecified
- Removed (0): none

### 17. `v717_v638_med_add_e329.csv` - CKD / KEEP

- Message: v717: v638 plus E329 thymus disease unspecified
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 17. `v717_v638_med_add_e329.csv` - UTI / KEEP

- Message: v717: v638 plus E329 thymus disease unspecified
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 18. `v718_v639_med_add_e329.csv` - Epistaxis / ASSOCIATION

- Message: v718: v639 plus E329 thymus disease unspecified
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 18. `v718_v639_med_add_e329.csv` - Enlarged Mediastinum / KEEP

- Message: v718: v639 plus E329 thymus disease unspecified
- Added (2): `C37` - Malignant neoplasm of thymus<br>`E329` - Disease of thymus, unspecified
- Removed (0): none

### 18. `v718_v639_med_add_e329.csv` - Diabetes / KEEP

- Message: v718: v639 plus E329 thymus disease unspecified
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 18. `v718_v639_med_add_e329.csv` - Pneumonia / KEEP

- Message: v718: v639 plus E329 thymus disease unspecified
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 19. `v719_v640_med_add_e329.csv` - Epistaxis / ASSOCIATION

- Message: v719: v640 plus E329 thymus disease unspecified
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 19. `v719_v640_med_add_e329.csv` - Enlarged Mediastinum / KEEP

- Message: v719: v640 plus E329 thymus disease unspecified
- Added (2): `C37` - Malignant neoplasm of thymus<br>`E329` - Disease of thymus, unspecified
- Removed (0): none

### 19. `v719_v640_med_add_e329.csv` - CKD / KEEP

- Message: v719: v640 plus E329 thymus disease unspecified
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 19. `v719_v640_med_add_e329.csv` - UTI / KEEP

- Message: v719: v640 plus E329 thymus disease unspecified
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 19. `v719_v640_med_add_e329.csv` - Diabetes / KEEP

- Message: v719: v640 plus E329 thymus disease unspecified
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 19. `v719_v640_med_add_e329.csv` - Pneumonia / KEEP

- Message: v719: v640 plus E329 thymus disease unspecified
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 20. `v720_v640_med_add_c8522.csv` - Epistaxis / ASSOCIATION

- Message: v720: v640 plus C8522 intrathoracic B-cell lymphoma
- Added (1): `I10` - Essential (primary) hypertension
- Removed (0): none

### 20. `v720_v640_med_add_c8522.csv` - Enlarged Mediastinum / KEEP

- Message: v720: v640 plus C8522 intrathoracic B-cell lymphoma
- Added (2): `C37` - Malignant neoplasm of thymus<br>`C8522` - Mediastinal (thymic) large B-cell lymphoma, intrathoracic lymph nodes
- Removed (0): none

### 20. `v720_v640_med_add_c8522.csv` - CKD / KEEP

- Message: v720: v640 plus C8522 intrathoracic B-cell lymphoma
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 20. `v720_v640_med_add_c8522.csv` - UTI / KEEP

- Message: v720: v640 plus C8522 intrathoracic B-cell lymphoma
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 20. `v720_v640_med_add_c8522.csv` - Diabetes / KEEP

- Message: v720: v640 plus C8522 intrathoracic B-cell lymphoma
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 20. `v720_v640_med_add_c8522.csv` - Pneumonia / KEEP

- Message: v720: v640 plus C8522 intrathoracic B-cell lymphoma
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more
