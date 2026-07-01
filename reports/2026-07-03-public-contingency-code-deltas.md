# CohortX Plan Code Deltas - 2026-07-03-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-03-public-contingency.csv`
- Anchor: `submissions/v178_FINAL.csv`
- Changed rows: 20
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v261_copd_no_j40.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 1 | v261: contingency: COPD remove J40 | core COPD ablation: unspecified bronchitis |
| 2 | `submissions/v262_copd_no_j41.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 4 | v262: contingency: COPD remove J41 | core COPD ablation: simple/mucopurulent chronic bronchitis |
| 3 | `submissions/v263_copd_no_j42.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 1 | v263: contingency: COPD remove J42 | core COPD ablation: unspecified chronic bronchitis |
| 4 | `submissions/v264_copd_no_j43.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 6 | v264: contingency: COPD remove J43 | core COPD ablation: emphysema |
| 5 | `submissions/v265_copd_no_j44.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 4 | v265: contingency: COPD remove J44 | core COPD ablation: explicit COPD codes |
| 6 | `submissions/v266_copd_no_j47.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 3 | v266: contingency: COPD remove J47 | core COPD ablation: bronchiectasis |
| 7 | `submissions/v267_copd_no_j40_j47.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 0 | 4 | v267: contingency: COPD remove J40/J47 | combined non-COPD-ish bronchitis/bronchiectasis ablation |
| 8 | `submissions/v268_copd_add_j479.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 1 | 0 | v268: contingency: COPD add J479 | isolated bronchiectasis uncomplicated addition |
| 9 | `submissions/v269_copd_add_q334.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 1 | 0 | v269: contingency: COPD add Q334 | isolated congenital bronchiectasis addition |
| 10 | `submissions/v270_copd_add_j479_q334.csv` | Chronic Obstructive Pulmonary Disease | KEEP | 2 | 0 | v270: contingency: COPD add J479/Q334 | small bronchiectasis completion addition |
| 11 | `submissions/v271_med_no_c78.csv` | Enlarged Mediastinum | KEEP | 0 | 2 | v271: contingency: mediastinum remove C78 | mediastinum ablation: secondary neoplasm of mediastinum |
| 12 | `submissions/v272_med_no_d38.csv` | Enlarged Mediastinum | KEEP | 0 | 2 | v272: contingency: mediastinum remove D38 | mediastinum ablation: uncertain behavior neoplasm |
| 13 | `submissions/v273_med_no_j85.csv` | Enlarged Mediastinum | KEEP | 0 | 2 | v273: contingency: mediastinum remove J85 | mediastinum ablation: abscess of mediastinum |
| 14 | `submissions/v274_med_add_thymus_neoplasm.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v274: contingency: mediastinum add thymus neoplasm | targeted thymus/thymic neoplasm addition |
| 15 | `submissions/v275_med_add_e32_thymus.csv` | Enlarged Mediastinum | KEEP | 5 | 0 | v275: contingency: mediastinum add E32 thymus | targeted non-neoplasm thymus disease addition |
| 16 | `submissions/v276_med_add_c771_nodes.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v276: contingency: mediastinum add C771 | isolated intrathoracic lymph-node metastasis addition |
| 17 | `submissions/v277_med_add_c39_intrathoracic.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v277: contingency: mediastinum add C39 | isolated ill-defined intrathoracic malignancy addition |
| 18 | `submissions/v278_med_add_a154_tb_nodes.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v278: contingency: mediastinum add A154 | isolated intrathoracic lymph-node tuberculosis addition |
| 19 | `submissions/v279_med_add_d174_lipoma.csv` | Enlarged Mediastinum | KEEP | 1 | 0 | v279: contingency: mediastinum add D174 | isolated benign intrathoracic lipoma addition |
| 20 | `submissions/v280_med_add_lymphoma_nodes.csv` | Enlarged Mediastinum | KEEP | 34 | 0 | v280: contingency: mediastinum add lymphoma nodes | intrathoracic lymph-node lymphoma addition, separate from C852 mediastinal B-cell probe |

## Exact Code Changes

### 1. `v261_copd_no_j40.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v261: contingency: COPD remove J40
- Added (0): none
- Removed (1): `J40` - Bronchitis, not specified as acute or chronic

### 2. `v262_copd_no_j41.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v262: contingency: COPD remove J41
- Added (0): none
- Removed (4): `J41` - Simple and mucopurulent chronic bronchitis<br>`J410` - Simple chronic bronchitis<br>`J411` - Mucopurulent chronic bronchitis<br>`J418` - Mixed simple and mucopurulent chronic bronchitis

### 3. `v263_copd_no_j42.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v263: contingency: COPD remove J42
- Added (0): none
- Removed (1): `J42` - Unspecified chronic bronchitis

### 4. `v264_copd_no_j43.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v264: contingency: COPD remove J43
- Added (0): none
- Removed (6): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified

### 5. `v265_copd_no_j44.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v265: contingency: COPD remove J44
- Added (0): none
- Removed (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified

### 6. `v266_copd_no_j47.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v266: contingency: COPD remove J47
- Added (0): none
- Removed (3): `J47` - Bronchiectasis<br>`J470` - Bronchiectasis with acute lower respiratory infection<br>`J471` - Bronchiectasis with (acute) exacerbation

### 7. `v267_copd_no_j40_j47.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v267: contingency: COPD remove J40/J47
- Added (0): none
- Removed (4): `J40` - Bronchitis, not specified as acute or chronic<br>`J47` - Bronchiectasis<br>`J470` - Bronchiectasis with acute lower respiratory infection<br>`J471` - Bronchiectasis with (acute) exacerbation

### 8. `v268_copd_add_j479.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v268: contingency: COPD add J479
- Added (1): `J479` - Bronchiectasis, uncomplicated
- Removed (0): none

### 9. `v269_copd_add_q334.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v269: contingency: COPD add Q334
- Added (1): `Q334` - Congenital bronchiectasis
- Removed (0): none

### 10. `v270_copd_add_j479_q334.csv` - Chronic Obstructive Pulmonary Disease / KEEP

- Message: v270: contingency: COPD add J479/Q334
- Added (2): `J479` - Bronchiectasis, uncomplicated<br>`Q334` - Congenital bronchiectasis
- Removed (0): none

### 11. `v271_med_no_c78.csv` - Enlarged Mediastinum / KEEP

- Message: v271: contingency: mediastinum remove C78
- Added (0): none
- Removed (2): `C78` - Secondary malignant neoplasm of respiratory and digestive organs<br>`C781` - Secondary malignant neoplasm of mediastinum

### 12. `v272_med_no_d38.csv` - Enlarged Mediastinum / KEEP

- Message: v272: contingency: mediastinum remove D38
- Added (0): none
- Removed (2): `D38` - Neoplasm of uncertain behavior of middle ear and respiratory and intrathoracic organs<br>`D383` - Neoplasm of uncertain behavior of mediastinum

### 13. `v273_med_no_j85.csv` - Enlarged Mediastinum / KEEP

- Message: v273: contingency: mediastinum remove J85
- Added (0): none
- Removed (2): `J85` - Abscess of lung and mediastinum<br>`J853` - Abscess of mediastinum

### 14. `v274_med_add_thymus_neoplasm.csv` - Enlarged Mediastinum / KEEP

- Message: v274: contingency: mediastinum add thymus neoplasm
- Added (4): `C37` - Malignant neoplasm of thymus<br>`C7A091` - Malignant carcinoid tumor of the thymus<br>`D3A091` - Benign carcinoid tumor of the thymus<br>`D384` - Neoplasm of uncertain behavior of thymus
- Removed (0): none

### 15. `v275_med_add_e32_thymus.csv` - Enlarged Mediastinum / KEEP

- Message: v275: contingency: mediastinum add E32 thymus
- Added (5): `E32` - Diseases of thymus<br>`E320` - Persistent hyperplasia of thymus<br>`E321` - Abscess of thymus<br>`E328` - Other diseases of thymus<br>`E329` - Disease of thymus, unspecified
- Removed (0): none

### 16. `v276_med_add_c771_nodes.csv` - Enlarged Mediastinum / KEEP

- Message: v276: contingency: mediastinum add C771
- Added (1): `C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes
- Removed (0): none

### 17. `v277_med_add_c39_intrathoracic.csv` - Enlarged Mediastinum / KEEP

- Message: v277: contingency: mediastinum add C39
- Added (1): `C39` - Malignant neoplasm of other and ill-defined sites in the respiratory system and intrathoracic organs
- Removed (0): none

### 18. `v278_med_add_a154_tb_nodes.csv` - Enlarged Mediastinum / KEEP

- Message: v278: contingency: mediastinum add A154
- Added (1): `A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 19. `v279_med_add_d174_lipoma.csv` - Enlarged Mediastinum / KEEP

- Message: v279: contingency: mediastinum add D174
- Added (1): `D174` - Benign lipomatous neoplasm of intrathoracic organs
- Removed (0): none

### 20. `v280_med_add_lymphoma_nodes.csv` - Enlarged Mediastinum / KEEP

- Message: v280: contingency: mediastinum add lymphoma nodes
- Added (34): `C8102` - Nodular lymphocyte predominant Hodgkin lymphoma, intrathoracic lymph nodes<br>`C8112` - Nodular sclerosis Hodgkin lymphoma, intrathoracic lymph nodes<br>`C8122` - Mixed cellularity Hodgkin lymphoma, intrathoracic lymph nodes<br>`C8132` - Lymphocyte depleted Hodgkin lymphoma, intrathoracic lymph nodes<br>`C8142` - Lymphocyte-rich Hodgkin lymphoma, intrathoracic lymph nodes<br>`C8172` - Other Hodgkin lymphoma, intrathoracic lymph nodes<br>`C8192` - Hodgkin lymphoma, unspecified, intrathoracic lymph nodes<br>`C8202` - Follicular lymphoma grade I, intrathoracic lymph nodes<br>`C8212` - Follicular lymphoma grade II, intrathoracic lymph nodes<br>`C8222` - Follicular lymphoma grade III, unspecified, intrathoracic lymph nodes<br>`C8232` - Follicular lymphoma grade IIIa, intrathoracic lymph nodes<br>`C8242` - Follicular lymphoma grade IIIb, intrathoracic lymph nodes<br>`C8252` - Diffuse follicle center lymphoma, intrathoracic lymph nodes<br>`C8262` - Cutaneous follicle center lymphoma, intrathoracic lymph nodes<br>`C8282` - Other types of follicular lymphoma, intrathoracic lymph nodes<br>`C8292` - Follicular lymphoma, unspecified, intrathoracic lymph nodes<br>`C8302` - Small cell B-cell lymphoma, intrathoracic lymph nodes<br>`C8312` - Mantle cell lymphoma, intrathoracic lymph nodes<br>... +16 more
- Removed (0): none

