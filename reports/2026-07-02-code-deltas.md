# CohortX Plan Code Deltas - 2026-07-02

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-02.csv`
- Anchor: `submissions/v178_FINAL.csv`
- Changed rows: 20
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v201_copd_no_j20.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 3 | v201: COPD remove J20 acute bronchitis | public COPD family ablation |
| 2 | `submissions/v202_copd_no_j31.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 2 | v202: COPD remove J31 chronic rhinitis | public COPD family ablation |
| 3 | `submissions/v203_copd_no_j45.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 4 | v203: COPD remove J45 asthma | public COPD family ablation |
| 4 | `submissions/v204_copd_no_j81_j82.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 4 | v204: COPD remove J81/J82 edema eosinophilia | public COPD family ablation |
| 5 | `submissions/v205_copd_no_j93_j95.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 4 | v205: COPD remove J93/J95 pneumothorax postop | public COPD family ablation |
| 6 | `submissions/v206_copd_no_j96.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 17 | v206: COPD remove J96 respiratory failure | public COPD family ablation |
| 7 | `submissions/v207_copd_no_j98.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 3 | v207: COPD remove J98 other respiratory disorders | public COPD family ablation |
| 8 | `submissions/v208_copd_core_j41_j42_j43_j44.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 41 | v208: COPD core J41/J42/J43/J44 only | public COPD precision probe |
| 9 | `submissions/v209_copd_no_acute_bronch_asthma.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 7 | v209: COPD remove J20 and J45 together | public COPD combined ablation |
| 10 | `submissions/v210_copd_add_p25_only.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 3 | 0 | v210: COPD add P25 perinatal emphysema only | public COPD isolated addition |
| 11 | `submissions/v211_copd_add_t79_t81_only.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 8 | 0 | v211: COPD add T79/T81 emphysema only | public COPD isolated addition |
| 12 | `submissions/v212_med_no_j98.csv` | Enlarged Mediastinum | KEEP | 0 | 16 | v212: mediastinum remove J98 | public mediastinum family ablation |
| 13 | `submissions/v213_med_no_q34.csv` | Enlarged Mediastinum | KEEP | 0 | 5 | v213: mediastinum remove Q34 | public mediastinum family ablation |
| 14 | `submissions/v214_med_no_d15.csv` | Enlarged Mediastinum | KEEP | 0 | 6 | v214: mediastinum remove D15 | public mediastinum family ablation |
| 15 | `submissions/v215_med_no_c38.csv` | Enlarged Mediastinum | KEEP | 0 | 7 | v215: mediastinum remove C38 | public mediastinum family ablation |
| 16 | `submissions/v216_med_only_mediastin_title.csv` | Enlarged Mediastinum | KEEP | 0 | 26 | v216: mediastinum keep titles containing mediastin | public mediastinum precision probe |
| 17 | `submissions/v217_med_keep_neoplasm_only.csv` | Enlarged Mediastinum | KEEP | 0 | 23 | v217: mediastinum neoplasm-only set | public mediastinum precision probe |
| 18 | `submissions/v218_med_add_c852_only.csv` | Enlarged Mediastinum | KEEP | 11 | 0 | v218: mediastinum add C852 lymphoma only | public mediastinum isolated addition |
| 19 | `submissions/v219_med_add_n80b5_only.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v219: mediastinum add N80B5 only | public mediastinum isolated addition |
| 20 | `submissions/v220_med_add_p252_only.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v220: mediastinum add P252 only | public mediastinum isolated addition |

## Exact Code Changes

### 1. `v201_copd_no_j20.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v201: COPD remove J20 acute bronchitis
- Added (0): none
- Removed (3): `J20` - Acute bronchitis<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J204` - Acute bronchitis due to parainfluenza virus

### 2. `v202_copd_no_j31.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v202: COPD remove J31 chronic rhinitis
- Added (0): none
- Removed (2): `J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis

### 3. `v203_copd_no_j45.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v203: COPD remove J45 asthma
- Added (0): none
- Removed (4): `J45` - Asthma<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>`J4551` - Severe persistent asthma with (acute) exacerbation

### 4. `v204_copd_no_j81_j82.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v204: COPD remove J81/J82 edema eosinophilia
- Added (0): none
- Removed (4): `J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia

### 5. `v205_copd_no_j93_j95.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v205: COPD remove J93/J95 pneumothorax postop
- Added (0): none
- Removed (4): `J93` - Pneumothorax and air leak<br>`J9381` - Chronic pneumothorax<br>`J95` - Intraoperative and postprocedural complications and disorders of respiratory system, not elsewhere classified<br>`J95822` - Acute and chronic postprocedural respiratory failure

### 6. `v206_copd_no_j96.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v206: COPD remove J96 respiratory failure
- Added (0): none
- Removed (17): `J96` - Respiratory failure, not elsewhere classified<br>`J960` - Acute respiratory failure<br>`J9600` - Acute respiratory failure, unspecified whether with hypoxia or hypercapnia<br>`J9601` - Acute respiratory failure with hypoxia<br>`J9602` - Acute respiratory failure with hypercapnia<br>`J961` - Chronic respiratory failure<br>`J9610` - Chronic respiratory failure, unspecified whether with hypoxia or hypercapnia<br>`J9611` - Chronic respiratory failure with hypoxia<br>`J9612` - Chronic respiratory failure with hypercapnia<br>`J962` - Acute and chronic respiratory failure<br>`J9620` - Acute and chronic respiratory failure, unspecified whether with hypoxia or hypercapnia<br>`J9621` - Acute and chronic respiratory failure with hypoxia<br>`J9622` - Acute and chronic respiratory failure with hypercapnia<br>`J969` - Respiratory failure, unspecified<br>`J9690` - Respiratory failure, unspecified, unspecified whether with hypoxia or hypercapnia<br>`J9691` - Respiratory failure, unspecified with hypoxia<br>`J9692` - Respiratory failure, unspecified with hypercapnia

### 7. `v207_copd_no_j98.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v207: COPD remove J98 other respiratory disorders
- Added (0): none
- Removed (3): `J98` - Other respiratory disorders<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema

### 8. `v208_copd_core_j41_j42_j43_j44.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v208: COPD core J41/J42/J43/J44 only
- Added (0): none
- Removed (41): `J20` - Acute bronchitis<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J310` - Chronic rhinitis<br>`J40` - Bronchitis, not specified as acute or chronic<br>`J45` - Asthma<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>`J4551` - Severe persistent asthma with (acute) exacerbation<br>`J47` - Bronchiectasis<br>`J470` - Bronchiectasis with acute lower respiratory infection<br>`J471` - Bronchiectasis with (acute) exacerbation<br>`J81` - Pulmonary edema<br>`J811` - Chronic pulmonary edema<br>`J82` - Pulmonary eosinophilia, not elsewhere classified<br>`J8281` - Chronic eosinophilic pneumonia<br>`J93` - Pneumothorax and air leak<br>... +23 more

### 9. `v209_copd_no_acute_bronch_asthma.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v209: COPD remove J20 and J45 together
- Added (0): none
- Removed (7): `J20` - Acute bronchitis<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J45` - Asthma<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>`J4551` - Severe persistent asthma with (acute) exacerbation

### 10. `v210_copd_add_p25_only.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v210: COPD add P25 perinatal emphysema only
- Added (3): `P25` - Interstitial emphysema and related conditions originating in the perinatal period<br>`P250` - Interstitial emphysema originating in the perinatal period<br>`P258` - Other conditions related to interstitial emphysema originating in the perinatal period
- Removed (0): none

### 11. `v211_copd_add_t79_t81_only.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v211: COPD add T79/T81 emphysema only
- Added (8): `T797` - Traumatic subcutaneous emphysema<br>`T797XXA` - Traumatic subcutaneous emphysema, initial encounter<br>`T797XXD` - Traumatic subcutaneous emphysema, subsequent encounter<br>`T797XXS` - Traumatic subcutaneous emphysema, sequela<br>`T8182` - Emphysema (subcutaneous) resulting from a procedure<br>`T8182XA` - Emphysema (subcutaneous) resulting from a procedure, initial encounter<br>`T8182XD` - Emphysema (subcutaneous) resulting from a procedure, subsequent encounter<br>`T8182XS` - Emphysema (subcutaneous) resulting from a procedure, sequela
- Removed (0): none

### 12. `v212_med_no_j98.csv` - Enlarged Mediastinum / KEEP

- Message: v212: mediastinum remove J98
- Added (0): none
- Removed (16): `J98` - Other respiratory disorders<br>`J980` - Diseases of bronchus, not elsewhere classified<br>`J9801` - Acute bronchospasm<br>`J9809` - Other diseases of bronchus, not elsewhere classified<br>`J981` - Pulmonary collapse<br>`J9811` - Atelectasis<br>`J9819` - Other pulmonary collapse<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema<br>`J984` - Other disorders of lung<br>`J985` - Diseases of mediastinum, not elsewhere classified<br>`J9851` - Mediastinitis<br>`J9859` - Other diseases of mediastinum, not elsewhere classified<br>`J986` - Disorders of diaphragm<br>`J988` - Other specified respiratory disorders<br>`J989` - Respiratory disorder, unspecified

### 13. `v213_med_no_q34.csv` - Enlarged Mediastinum / KEEP

- Message: v213: mediastinum remove Q34
- Added (0): none
- Removed (5): `Q34` - Other congenital malformations of respiratory system<br>`Q340` - Anomaly of pleura<br>`Q341` - Congenital cyst of mediastinum<br>`Q348` - Other specified congenital malformations of respiratory system<br>`Q349` - Congenital malformation of respiratory system, unspecified

### 14. `v214_med_no_d15.csv` - Enlarged Mediastinum / KEEP

- Message: v214: mediastinum remove D15
- Added (0): none
- Removed (6): `D15` - Benign neoplasm of other and unspecified intrathoracic organs<br>`D150` - Benign neoplasm of thymus<br>`D151` - Benign neoplasm of heart<br>`D152` - Benign neoplasm of mediastinum<br>`D157` - Benign neoplasm of other specified intrathoracic organs<br>`D159` - Benign neoplasm of intrathoracic organ, unspecified

### 15. `v215_med_no_c38.csv` - Enlarged Mediastinum / KEEP

- Message: v215: mediastinum remove C38
- Added (0): none
- Removed (7): `C38` - Malignant neoplasm of heart, mediastinum and pleura<br>`C380` - Malignant neoplasm of heart<br>`C381` - Malignant neoplasm of anterior mediastinum<br>`C382` - Malignant neoplasm of posterior mediastinum<br>`C383` - Malignant neoplasm of mediastinum, part unspecified<br>`C384` - Malignant neoplasm of pleura<br>`C388` - Malignant neoplasm of overlapping sites of heart, mediastinum and pleura

### 16. `v216_med_only_mediastin_title.csv` - Enlarged Mediastinum / KEEP

- Message: v216: mediastinum keep titles containing mediastin
- Added (0): none
- Removed (26): `C380` - Malignant neoplasm of heart<br>`C384` - Malignant neoplasm of pleura<br>`C78` - Secondary malignant neoplasm of respiratory and digestive organs<br>`D15` - Benign neoplasm of other and unspecified intrathoracic organs<br>`D150` - Benign neoplasm of thymus<br>`D151` - Benign neoplasm of heart<br>`D157` - Benign neoplasm of other specified intrathoracic organs<br>`D159` - Benign neoplasm of intrathoracic organ, unspecified<br>`D38` - Neoplasm of uncertain behavior of middle ear and respiratory and intrathoracic organs<br>`J98` - Other respiratory disorders<br>`J980` - Diseases of bronchus, not elsewhere classified<br>`J9801` - Acute bronchospasm<br>`J9809` - Other diseases of bronchus, not elsewhere classified<br>`J981` - Pulmonary collapse<br>`J9811` - Atelectasis<br>`J9819` - Other pulmonary collapse<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema<br>... +8 more

### 17. `v217_med_keep_neoplasm_only.csv` - Enlarged Mediastinum / KEEP

- Message: v217: mediastinum neoplasm-only set
- Added (0): none
- Removed (23): `J85` - Abscess of lung and mediastinum<br>`J853` - Abscess of mediastinum<br>`J98` - Other respiratory disorders<br>`J980` - Diseases of bronchus, not elsewhere classified<br>`J9801` - Acute bronchospasm<br>`J9809` - Other diseases of bronchus, not elsewhere classified<br>`J981` - Pulmonary collapse<br>`J9811` - Atelectasis<br>`J9819` - Other pulmonary collapse<br>`J982` - Interstitial emphysema<br>`J983` - Compensatory emphysema<br>`J984` - Other disorders of lung<br>`J985` - Diseases of mediastinum, not elsewhere classified<br>`J9851` - Mediastinitis<br>`J9859` - Other diseases of mediastinum, not elsewhere classified<br>`J986` - Disorders of diaphragm<br>`J988` - Other specified respiratory disorders<br>`J989` - Respiratory disorder, unspecified<br>... +5 more

### 18. `v218_med_add_c852_only.csv` - Enlarged Mediastinum / KEEP

- Message: v218: mediastinum add C852 lymphoma only
- Added (11): `C852` - Mediastinal (thymic) large B-cell lymphoma<br>`C8520` - Mediastinal (thymic) large B-cell lymphoma, unspecified site<br>`C8521` - Mediastinal (thymic) large B-cell lymphoma, lymph nodes of head, face, and neck<br>`C8522` - Mediastinal (thymic) large B-cell lymphoma, intrathoracic lymph nodes<br>`C8523` - Mediastinal (thymic) large B-cell lymphoma, intra-abdominal lymph nodes<br>`C8524` - Mediastinal (thymic) large B-cell lymphoma, lymph nodes of axilla and upper limb<br>`C8525` - Mediastinal (thymic) large B-cell lymphoma, lymph nodes of inguinal region and lower limb<br>`C8526` - Mediastinal (thymic) large B-cell lymphoma, intrapelvic lymph nodes<br>`C8527` - Mediastinal (thymic) large B-cell lymphoma, spleen<br>`C8528` - Mediastinal (thymic) large B-cell lymphoma, lymph nodes of multiple sites<br>`C8529` - Mediastinal (thymic) large B-cell lymphoma, extranodal and solid organ sites
- Removed (0): none

### 19. `v219_med_add_n80b5_only.csv` - Enlarged Mediastinum / KEEP

- Message: v219: mediastinum add N80B5 only
- Added (1): `N80B5` - Endometriosis of the mediastinal space
- Removed (0): none

### 20. `v220_med_add_p252_only.csv` - Enlarged Mediastinum / KEEP

- Message: v220: mediastinum add P252 only
- Added (1): `P252` - Pneumomediastinum originating in the perinatal period
- Removed (0): none

