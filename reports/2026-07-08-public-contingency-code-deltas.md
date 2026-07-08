# CohortX Plan Code Deltas - 2026-07-08-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-08-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 37
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v481_v296_zero_hf.csv` | Heart Failure | KEEP | 0 | 72 | v481: v296 zero Heart Failure KEEP | public-neutral zero probe v187 on v296 anchor |
| 2 | `submissions/v482_v296_zero_hyperthyroid.csv` | Hyperthyroidism | KEEP | 0 | 49 | v482: v296 zero Hyperthyroidism KEEP | public-neutral zero probe v188 on v296 anchor |
| 3 | `submissions/v483_v296_zero_ild.csv` | Interstitial Lung Disease | KEEP | 0 | 42 | v483: v296 zero ILD KEEP | public-neutral zero probe v189 on v296 anchor |
| 4 | `submissions/v484_v296_zero_derm.csv` | Dermatomycosis | KEEP | 0 | 38 | v484: v296 zero Dermatomycosis KEEP | public-neutral zero probe v190 on v296 anchor |
| 5 | `submissions/v485_v296_zero_bronchitis.csv` | Bronchitis | KEEP | 0 | 33 | v485: v296 zero Bronchitis KEEP | public-neutral zero probe v191 on v296 anchor |
| 6 | `submissions/v486_v296_zero_npc.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 42 | v486: v296 zero NPC KEEP | public-neutral zero probe v192 on v296 anchor |
| 7 | `submissions/v487_v296_zero_hypothyroid.csv` | Hypothyroidism | KEEP | 0 | 26 | v487: v296 zero Hypothyroidism KEEP | public-neutral zero probe v193 on v296 anchor |
| 8 | `submissions/v488_v296_add_hf_kw.csv` | Heart Failure | KEEP | 6 | 0 | v488: v296 add Heart Failure keyword KEEP | public-neutral keyword add v196 on v296 anchor |
| 9 | `submissions/v489_v296_add_ild_kw.csv` | Interstitial Lung Disease | KEEP | 9 | 0 | v489: v296 add ILD keyword KEEP | public-neutral keyword add v197 on v296 anchor |
| 10 | `submissions/v490_v296_add_derm_kw.csv` | Dermatomycosis | KEEP | 57 | 0 | v490: v296 add Dermatomycosis keyword KEEP | public-neutral keyword add v198 on v296 anchor |
| 11 | `submissions/v491_v296_add_npc_kw.csv` | Nasopharyngeal Carcinoma | KEEP | 5 | 0 | v491: v296 add NPC keyword KEEP | public-neutral keyword add v200 on v296 anchor |
| 12 | `submissions/v492_v296_zero_endocrine_pair.csv` | Hypothyroidism | KEEP | 0 | 26 | v492: v296 zero thyroid pair KEEP | paired public-neutral thyroid ablation |
| 12 | `submissions/v492_v296_zero_endocrine_pair.csv` | Hyperthyroidism | KEEP | 0 | 49 | v492: v296 zero thyroid pair KEEP | paired public-neutral thyroid ablation |
| 13 | `submissions/v493_v296_zero_pulmonary_pair.csv` | Bronchitis | KEEP | 0 | 33 | v493: v296 zero ILD/Bronchitis KEEP | paired public-neutral pulmonary hidden KEEP ablation |
| 13 | `submissions/v493_v296_zero_pulmonary_pair.csv` | Interstitial Lung Disease | KEEP | 0 | 42 | v493: v296 zero ILD/Bronchitis KEEP | paired public-neutral pulmonary hidden KEEP ablation |
| 14 | `submissions/v494_v296_zero_derm_npc_pair.csv` | Dermatomycosis | KEEP | 0 | 38 | v494: v296 zero Derm/NPC KEEP | paired public-neutral derm/NPC ablation |
| 14 | `submissions/v494_v296_zero_derm_npc_pair.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 42 | v494: v296 zero Derm/NPC KEEP | paired public-neutral derm/NPC ablation |
| 15 | `submissions/v495_v296_add_hidden_kw_group.csv` | Dermatomycosis | KEEP | 57 | 0 | v495: v296 add hidden keyword group | combined public-neutral keyword additions from v196/v197/v198/v200 |
| 15 | `submissions/v495_v296_add_hidden_kw_group.csv` | Nasopharyngeal Carcinoma | KEEP | 5 | 0 | v495: v296 add hidden keyword group | combined public-neutral keyword additions from v196/v197/v198/v200 |
| 15 | `submissions/v495_v296_add_hidden_kw_group.csv` | Heart Failure | KEEP | 6 | 0 | v495: v296 add hidden keyword group | combined public-neutral keyword additions from v196/v197/v198/v200 |
| 15 | `submissions/v495_v296_add_hidden_kw_group.csv` | Interstitial Lung Disease | KEEP | 9 | 0 | v495: v296 add hidden keyword group | combined public-neutral keyword additions from v196/v197/v198/v200 |
| 16 | `submissions/v496_v296_med_zero_hf.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v496: v296 mediastinum plus zero HF | med positive plus public-neutral HF ablation |
| 16 | `submissions/v496_v296_med_zero_hf.csv` | Heart Failure | KEEP | 0 | 72 | v496: v296 mediastinum plus zero HF | med positive plus public-neutral HF ablation |
| 17 | `submissions/v497_v296_med_zero_endocrine_pair.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v497: v296 mediastinum plus zero thyroid pair | med positive plus public-neutral thyroid ablation |
| 17 | `submissions/v497_v296_med_zero_endocrine_pair.csv` | Hypothyroidism | KEEP | 0 | 26 | v497: v296 mediastinum plus zero thyroid pair | med positive plus public-neutral thyroid ablation |
| 17 | `submissions/v497_v296_med_zero_endocrine_pair.csv` | Hyperthyroidism | KEEP | 0 | 49 | v497: v296 mediastinum plus zero thyroid pair | med positive plus public-neutral thyroid ablation |
| 18 | `submissions/v498_v296_med_zero_pulmonary_pair.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v498: v296 mediastinum plus zero ILD/Bronchitis | med positive plus public-neutral pulmonary ablation |
| 18 | `submissions/v498_v296_med_zero_pulmonary_pair.csv` | Bronchitis | KEEP | 0 | 33 | v498: v296 mediastinum plus zero ILD/Bronchitis | med positive plus public-neutral pulmonary ablation |
| 18 | `submissions/v498_v296_med_zero_pulmonary_pair.csv` | Interstitial Lung Disease | KEEP | 0 | 42 | v498: v296 mediastinum plus zero ILD/Bronchitis | med positive plus public-neutral pulmonary ablation |
| 19 | `submissions/v499_v296_med_zero_derm_npc_pair.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v499: v296 mediastinum plus zero Derm/NPC | med positive plus public-neutral derm/NPC ablation |
| 19 | `submissions/v499_v296_med_zero_derm_npc_pair.csv` | Dermatomycosis | KEEP | 0 | 38 | v499: v296 mediastinum plus zero Derm/NPC | med positive plus public-neutral derm/NPC ablation |
| 19 | `submissions/v499_v296_med_zero_derm_npc_pair.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 42 | v499: v296 mediastinum plus zero Derm/NPC | med positive plus public-neutral derm/NPC ablation |
| 20 | `submissions/v500_v296_med_add_hidden_kw_group.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v500: v296 mediastinum plus hidden keyword group | med positive plus combined public-neutral keyword additions |
| 20 | `submissions/v500_v296_med_add_hidden_kw_group.csv` | Dermatomycosis | KEEP | 57 | 0 | v500: v296 mediastinum plus hidden keyword group | med positive plus combined public-neutral keyword additions |
| 20 | `submissions/v500_v296_med_add_hidden_kw_group.csv` | Nasopharyngeal Carcinoma | KEEP | 5 | 0 | v500: v296 mediastinum plus hidden keyword group | med positive plus combined public-neutral keyword additions |
| 20 | `submissions/v500_v296_med_add_hidden_kw_group.csv` | Heart Failure | KEEP | 6 | 0 | v500: v296 mediastinum plus hidden keyword group | med positive plus combined public-neutral keyword additions |
| 20 | `submissions/v500_v296_med_add_hidden_kw_group.csv` | Interstitial Lung Disease | KEEP | 9 | 0 | v500: v296 mediastinum plus hidden keyword group | med positive plus combined public-neutral keyword additions |

## Exact Code Changes

### 1. `v481_v296_zero_hf.csv` - Heart Failure / KEEP

- Message: v481: v296 zero Heart Failure KEEP
- Added (0): none
- Removed (72): `I09` - Other rheumatic heart diseases<br>`I0981` - Rheumatic heart failure<br>`I11` - Hypertensive heart disease<br>`I110` - Hypertensive heart disease with heart failure<br>`I119` - Hypertensive heart disease without heart failure<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`I42` - Cardiomyopathy<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>... +54 more

### 2. `v482_v296_zero_hyperthyroid.csv` - Hyperthyroidism / KEEP

- Message: v482: v296 zero Hyperthyroidism KEEP
- Added (0): none
- Removed (49): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>... +31 more

### 3. `v483_v296_zero_ild.csv` - Interstitial Lung Disease / KEEP

- Message: v483: v296 zero ILD KEEP
- Added (0): none
- Removed (42): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent<br>`J84` - Other interstitial pulmonary diseases<br>`J840` - Alveolar and parieto-alveolar conditions<br>`J8401` - Alveolar proteinosis<br>`J8402` - Pulmonary alveolar microlithiasis<br>`J8403` - Idiopathic pulmonary hemosiderosis<br>`J8409` - Other alveolar and parieto-alveolar conditions<br>`J841` - Other interstitial pulmonary diseases with fibrosis<br>`J8410` - Pulmonary fibrosis, unspecified<br>`J8411` - Idiopathic interstitial pneumonia<br>... +24 more

### 4. `v484_v296_zero_derm.csv` - Dermatomycosis / KEEP

- Message: v484: v296 zero Dermatomycosis KEEP
- Added (0): none
- Removed (38): `B35` - Dermatophytosis<br>`B350` - Tinea barbae and tinea capitis<br>`B351` - Tinea unguium<br>`B352` - Tinea manuum<br>`B353` - Tinea pedis<br>`B354` - Tinea corporis<br>`B355` - Tinea imbricata<br>`B356` - Tinea cruris<br>`B358` - Other dermatophytoses<br>`B359` - Dermatophytosis, unspecified<br>`B36` - Other superficial mycoses<br>`B360` - Pityriasis versicolor<br>`B361` - Tinea nigra<br>`B362` - White piedra<br>`B363` - Black piedra<br>`B368` - Other specified superficial mycoses<br>`B369` - Superficial mycosis, unspecified<br>`B37` - Candidiasis<br>... +20 more

### 5. `v485_v296_zero_bronchitis.csv` - Bronchitis / KEEP

- Message: v485: v296 zero Bronchitis KEEP
- Added (0): none
- Removed (33): `J04` - Acute laryngitis and tracheitis<br>`J0410` - Acute tracheitis without obstruction<br>`J0411` - Acute tracheitis with obstruction<br>`J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J21` - Acute bronchiolitis<br>`J210` - Acute bronchiolitis due to respiratory syncytial virus<br>`J211` - Acute bronchiolitis due to human metapneumovirus<br>`J218` - Acute bronchiolitis due to other specified organisms<br>... +15 more

### 6. `v486_v296_zero_npc.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v486: v296 zero NPC KEEP
- Added (0): none
- Removed (42): `C10` - Malignant neoplasm of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C11` - Malignant neoplasm of nasopharynx<br>`C110` - Malignant neoplasm of superior wall of nasopharynx<br>`C111` - Malignant neoplasm of posterior wall of nasopharynx<br>`C112` - Malignant neoplasm of lateral wall of nasopharynx<br>`C113` - Malignant neoplasm of anterior wall of nasopharynx<br>`C118` - Malignant neoplasm of overlapping sites of nasopharynx<br>`C119` - Malignant neoplasm of nasopharynx, unspecified<br>`C13` - Malignant neoplasm of hypopharynx<br>`C132` - Malignant neoplasm of posterior wall of hypopharynx<br>`C30` - Malignant neoplasm of nasal cavity and middle ear<br>`C300` - Malignant neoplasm of nasal cavity<br>`C32` - Malignant neoplasm of larynx<br>`C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`C47` - Malignant neoplasm of peripheral nerves and autonomic nervous system<br>... +24 more

### 7. `v487_v296_zero_hypothyroid.csv` - Hypothyroidism / KEEP

- Message: v487: v296 zero Hypothyroidism KEEP
- Added (0): none
- Removed (26): `E00` - Congenital iodine-deficiency syndrome<br>`E000` - Congenital iodine-deficiency syndrome, neurological type<br>`E001` - Congenital iodine-deficiency syndrome, myxedematous type<br>`E002` - Congenital iodine-deficiency syndrome, mixed type<br>`E009` - Congenital iodine-deficiency syndrome, unspecified<br>`E02` - Subclinical iodine-deficiency hypothyroidism<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>... +8 more

### 8. `v488_v296_add_hf_kw.csv` - Heart Failure / KEEP

- Message: v488: v296 add Heart Failure keyword KEEP
- Added (6): `O2912` - Cardiac failure due to anesthesia during pregnancy<br>`O29121` - Cardiac failure due to anesthesia during pregnancy, first trimester<br>`O29122` - Cardiac failure due to anesthesia during pregnancy, second trimester<br>`O29123` - Cardiac failure due to anesthesia during pregnancy, third trimester<br>`O29129` - Cardiac failure due to anesthesia during pregnancy, unspecified trimester<br>`P290` - Neonatal cardiac failure
- Removed (0): none

### 9. `v489_v296_add_ild_kw.csv` - Interstitial Lung Disease / KEEP

- Message: v489: v296 add ILD keyword KEEP
- Added (9): `J60` - Coalworker's pneumoconiosis<br>`J61` - Pneumoconiosis due to asbestos and other mineral fibers<br>`J62` - Pneumoconiosis due to dust containing silica<br>`J620` - Pneumoconiosis due to talc dust<br>`J628` - Pneumoconiosis due to other dust containing silica<br>`J63` - Pneumoconiosis due to other inorganic dusts<br>`J636` - Pneumoconiosis due to other specified inorganic dusts<br>`J64` - Unspecified pneumoconiosis<br>`J65` - Pneumoconiosis associated with tuberculosis
- Removed (0): none

### 10. `v490_v296_add_derm_kw.csv` - Dermatomycosis / KEEP

- Message: v490: v296 add Dermatomycosis keyword KEEP
- Added (57): `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>`B380` - Acute pulmonary coccidioidomycosis<br>`B381` - Chronic pulmonary coccidioidomycosis<br>`B382` - Pulmonary coccidioidomycosis, unspecified<br>`B383` - Cutaneous coccidioidomycosis<br>`B384` - Coccidioidomycosis meningitis<br>`B387` - Disseminated coccidioidomycosis<br>`B388` - Other forms of coccidioidomycosis<br>`B3881` - Prostatic coccidioidomycosis<br>`B3889` - Other forms of coccidioidomycosis<br>`B389` - Coccidioidomycosis, unspecified<br>... +39 more
- Removed (0): none

### 11. `v491_v296_add_npc_kw.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v491: v296 add NPC keyword KEEP
- Added (5): `A361` - Nasopharyngeal diphtheria<br>`B873` - Nasopharyngeal myiasis<br>`J00` - Acute nasopharyngitis [common cold]<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J311` - Chronic nasopharyngitis
- Removed (0): none

### 12. `v492_v296_zero_endocrine_pair.csv` - Hypothyroidism / KEEP

- Message: v492: v296 zero thyroid pair KEEP
- Added (0): none
- Removed (26): `E00` - Congenital iodine-deficiency syndrome<br>`E000` - Congenital iodine-deficiency syndrome, neurological type<br>`E001` - Congenital iodine-deficiency syndrome, myxedematous type<br>`E002` - Congenital iodine-deficiency syndrome, mixed type<br>`E009` - Congenital iodine-deficiency syndrome, unspecified<br>`E02` - Subclinical iodine-deficiency hypothyroidism<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>... +8 more

### 12. `v492_v296_zero_endocrine_pair.csv` - Hyperthyroidism / KEEP

- Message: v492: v296 zero thyroid pair KEEP
- Added (0): none
- Removed (49): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>... +31 more

### 13. `v493_v296_zero_pulmonary_pair.csv` - Bronchitis / KEEP

- Message: v493: v296 zero ILD/Bronchitis KEEP
- Added (0): none
- Removed (33): `J04` - Acute laryngitis and tracheitis<br>`J0410` - Acute tracheitis without obstruction<br>`J0411` - Acute tracheitis with obstruction<br>`J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J21` - Acute bronchiolitis<br>`J210` - Acute bronchiolitis due to respiratory syncytial virus<br>`J211` - Acute bronchiolitis due to human metapneumovirus<br>`J218` - Acute bronchiolitis due to other specified organisms<br>... +15 more

### 13. `v493_v296_zero_pulmonary_pair.csv` - Interstitial Lung Disease / KEEP

- Message: v493: v296 zero ILD/Bronchitis KEEP
- Added (0): none
- Removed (42): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent<br>`J84` - Other interstitial pulmonary diseases<br>`J840` - Alveolar and parieto-alveolar conditions<br>`J8401` - Alveolar proteinosis<br>`J8402` - Pulmonary alveolar microlithiasis<br>`J8403` - Idiopathic pulmonary hemosiderosis<br>`J8409` - Other alveolar and parieto-alveolar conditions<br>`J841` - Other interstitial pulmonary diseases with fibrosis<br>`J8410` - Pulmonary fibrosis, unspecified<br>`J8411` - Idiopathic interstitial pneumonia<br>... +24 more

### 14. `v494_v296_zero_derm_npc_pair.csv` - Dermatomycosis / KEEP

- Message: v494: v296 zero Derm/NPC KEEP
- Added (0): none
- Removed (38): `B35` - Dermatophytosis<br>`B350` - Tinea barbae and tinea capitis<br>`B351` - Tinea unguium<br>`B352` - Tinea manuum<br>`B353` - Tinea pedis<br>`B354` - Tinea corporis<br>`B355` - Tinea imbricata<br>`B356` - Tinea cruris<br>`B358` - Other dermatophytoses<br>`B359` - Dermatophytosis, unspecified<br>`B36` - Other superficial mycoses<br>`B360` - Pityriasis versicolor<br>`B361` - Tinea nigra<br>`B362` - White piedra<br>`B363` - Black piedra<br>`B368` - Other specified superficial mycoses<br>`B369` - Superficial mycosis, unspecified<br>`B37` - Candidiasis<br>... +20 more

### 14. `v494_v296_zero_derm_npc_pair.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v494: v296 zero Derm/NPC KEEP
- Added (0): none
- Removed (42): `C10` - Malignant neoplasm of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C11` - Malignant neoplasm of nasopharynx<br>`C110` - Malignant neoplasm of superior wall of nasopharynx<br>`C111` - Malignant neoplasm of posterior wall of nasopharynx<br>`C112` - Malignant neoplasm of lateral wall of nasopharynx<br>`C113` - Malignant neoplasm of anterior wall of nasopharynx<br>`C118` - Malignant neoplasm of overlapping sites of nasopharynx<br>`C119` - Malignant neoplasm of nasopharynx, unspecified<br>`C13` - Malignant neoplasm of hypopharynx<br>`C132` - Malignant neoplasm of posterior wall of hypopharynx<br>`C30` - Malignant neoplasm of nasal cavity and middle ear<br>`C300` - Malignant neoplasm of nasal cavity<br>`C32` - Malignant neoplasm of larynx<br>`C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`C47` - Malignant neoplasm of peripheral nerves and autonomic nervous system<br>... +24 more

### 15. `v495_v296_add_hidden_kw_group.csv` - Dermatomycosis / KEEP

- Message: v495: v296 add hidden keyword group
- Added (57): `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>`B380` - Acute pulmonary coccidioidomycosis<br>`B381` - Chronic pulmonary coccidioidomycosis<br>`B382` - Pulmonary coccidioidomycosis, unspecified<br>`B383` - Cutaneous coccidioidomycosis<br>`B384` - Coccidioidomycosis meningitis<br>`B387` - Disseminated coccidioidomycosis<br>`B388` - Other forms of coccidioidomycosis<br>`B3881` - Prostatic coccidioidomycosis<br>`B3889` - Other forms of coccidioidomycosis<br>`B389` - Coccidioidomycosis, unspecified<br>... +39 more
- Removed (0): none

### 15. `v495_v296_add_hidden_kw_group.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v495: v296 add hidden keyword group
- Added (5): `A361` - Nasopharyngeal diphtheria<br>`B873` - Nasopharyngeal myiasis<br>`J00` - Acute nasopharyngitis [common cold]<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J311` - Chronic nasopharyngitis
- Removed (0): none

### 15. `v495_v296_add_hidden_kw_group.csv` - Heart Failure / KEEP

- Message: v495: v296 add hidden keyword group
- Added (6): `O2912` - Cardiac failure due to anesthesia during pregnancy<br>`O29121` - Cardiac failure due to anesthesia during pregnancy, first trimester<br>`O29122` - Cardiac failure due to anesthesia during pregnancy, second trimester<br>`O29123` - Cardiac failure due to anesthesia during pregnancy, third trimester<br>`O29129` - Cardiac failure due to anesthesia during pregnancy, unspecified trimester<br>`P290` - Neonatal cardiac failure
- Removed (0): none

### 15. `v495_v296_add_hidden_kw_group.csv` - Interstitial Lung Disease / KEEP

- Message: v495: v296 add hidden keyword group
- Added (9): `J60` - Coalworker's pneumoconiosis<br>`J61` - Pneumoconiosis due to asbestos and other mineral fibers<br>`J62` - Pneumoconiosis due to dust containing silica<br>`J620` - Pneumoconiosis due to talc dust<br>`J628` - Pneumoconiosis due to other dust containing silica<br>`J63` - Pneumoconiosis due to other inorganic dusts<br>`J636` - Pneumoconiosis due to other specified inorganic dusts<br>`J64` - Unspecified pneumoconiosis<br>`J65` - Pneumoconiosis associated with tuberculosis
- Removed (0): none

### 16. `v496_v296_med_zero_hf.csv` - Enlarged Mediastinum / KEEP

- Message: v496: v296 mediastinum plus zero HF
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 16. `v496_v296_med_zero_hf.csv` - Heart Failure / KEEP

- Message: v496: v296 mediastinum plus zero HF
- Added (0): none
- Removed (72): `I09` - Other rheumatic heart diseases<br>`I0981` - Rheumatic heart failure<br>`I11` - Hypertensive heart disease<br>`I110` - Hypertensive heart disease with heart failure<br>`I119` - Hypertensive heart disease without heart failure<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`I42` - Cardiomyopathy<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>... +54 more

### 17. `v497_v296_med_zero_endocrine_pair.csv` - Enlarged Mediastinum / KEEP

- Message: v497: v296 mediastinum plus zero thyroid pair
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 17. `v497_v296_med_zero_endocrine_pair.csv` - Hypothyroidism / KEEP

- Message: v497: v296 mediastinum plus zero thyroid pair
- Added (0): none
- Removed (26): `E00` - Congenital iodine-deficiency syndrome<br>`E000` - Congenital iodine-deficiency syndrome, neurological type<br>`E001` - Congenital iodine-deficiency syndrome, myxedematous type<br>`E002` - Congenital iodine-deficiency syndrome, mixed type<br>`E009` - Congenital iodine-deficiency syndrome, unspecified<br>`E02` - Subclinical iodine-deficiency hypothyroidism<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>... +8 more

### 17. `v497_v296_med_zero_endocrine_pair.csv` - Hyperthyroidism / KEEP

- Message: v497: v296 mediastinum plus zero thyroid pair
- Added (0): none
- Removed (49): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>... +31 more

### 18. `v498_v296_med_zero_pulmonary_pair.csv` - Enlarged Mediastinum / KEEP

- Message: v498: v296 mediastinum plus zero ILD/Bronchitis
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 18. `v498_v296_med_zero_pulmonary_pair.csv` - Bronchitis / KEEP

- Message: v498: v296 mediastinum plus zero ILD/Bronchitis
- Added (0): none
- Removed (33): `J04` - Acute laryngitis and tracheitis<br>`J0410` - Acute tracheitis without obstruction<br>`J0411` - Acute tracheitis with obstruction<br>`J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J21` - Acute bronchiolitis<br>`J210` - Acute bronchiolitis due to respiratory syncytial virus<br>`J211` - Acute bronchiolitis due to human metapneumovirus<br>`J218` - Acute bronchiolitis due to other specified organisms<br>... +15 more

### 18. `v498_v296_med_zero_pulmonary_pair.csv` - Interstitial Lung Disease / KEEP

- Message: v498: v296 mediastinum plus zero ILD/Bronchitis
- Added (0): none
- Removed (42): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent<br>`J84` - Other interstitial pulmonary diseases<br>`J840` - Alveolar and parieto-alveolar conditions<br>`J8401` - Alveolar proteinosis<br>`J8402` - Pulmonary alveolar microlithiasis<br>`J8403` - Idiopathic pulmonary hemosiderosis<br>`J8409` - Other alveolar and parieto-alveolar conditions<br>`J841` - Other interstitial pulmonary diseases with fibrosis<br>`J8410` - Pulmonary fibrosis, unspecified<br>`J8411` - Idiopathic interstitial pneumonia<br>... +24 more

### 19. `v499_v296_med_zero_derm_npc_pair.csv` - Enlarged Mediastinum / KEEP

- Message: v499: v296 mediastinum plus zero Derm/NPC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 19. `v499_v296_med_zero_derm_npc_pair.csv` - Dermatomycosis / KEEP

- Message: v499: v296 mediastinum plus zero Derm/NPC
- Added (0): none
- Removed (38): `B35` - Dermatophytosis<br>`B350` - Tinea barbae and tinea capitis<br>`B351` - Tinea unguium<br>`B352` - Tinea manuum<br>`B353` - Tinea pedis<br>`B354` - Tinea corporis<br>`B355` - Tinea imbricata<br>`B356` - Tinea cruris<br>`B358` - Other dermatophytoses<br>`B359` - Dermatophytosis, unspecified<br>`B36` - Other superficial mycoses<br>`B360` - Pityriasis versicolor<br>`B361` - Tinea nigra<br>`B362` - White piedra<br>`B363` - Black piedra<br>`B368` - Other specified superficial mycoses<br>`B369` - Superficial mycosis, unspecified<br>`B37` - Candidiasis<br>... +20 more

### 19. `v499_v296_med_zero_derm_npc_pair.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v499: v296 mediastinum plus zero Derm/NPC
- Added (0): none
- Removed (42): `C10` - Malignant neoplasm of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C11` - Malignant neoplasm of nasopharynx<br>`C110` - Malignant neoplasm of superior wall of nasopharynx<br>`C111` - Malignant neoplasm of posterior wall of nasopharynx<br>`C112` - Malignant neoplasm of lateral wall of nasopharynx<br>`C113` - Malignant neoplasm of anterior wall of nasopharynx<br>`C118` - Malignant neoplasm of overlapping sites of nasopharynx<br>`C119` - Malignant neoplasm of nasopharynx, unspecified<br>`C13` - Malignant neoplasm of hypopharynx<br>`C132` - Malignant neoplasm of posterior wall of hypopharynx<br>`C30` - Malignant neoplasm of nasal cavity and middle ear<br>`C300` - Malignant neoplasm of nasal cavity<br>`C32` - Malignant neoplasm of larynx<br>`C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`C47` - Malignant neoplasm of peripheral nerves and autonomic nervous system<br>... +24 more

### 20. `v500_v296_med_add_hidden_kw_group.csv` - Enlarged Mediastinum / KEEP

- Message: v500: v296 mediastinum plus hidden keyword group
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 20. `v500_v296_med_add_hidden_kw_group.csv` - Dermatomycosis / KEEP

- Message: v500: v296 mediastinum plus hidden keyword group
- Added (57): `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>`B380` - Acute pulmonary coccidioidomycosis<br>`B381` - Chronic pulmonary coccidioidomycosis<br>`B382` - Pulmonary coccidioidomycosis, unspecified<br>`B383` - Cutaneous coccidioidomycosis<br>`B384` - Coccidioidomycosis meningitis<br>`B387` - Disseminated coccidioidomycosis<br>`B388` - Other forms of coccidioidomycosis<br>`B3881` - Prostatic coccidioidomycosis<br>`B3889` - Other forms of coccidioidomycosis<br>`B389` - Coccidioidomycosis, unspecified<br>... +39 more
- Removed (0): none

### 20. `v500_v296_med_add_hidden_kw_group.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v500: v296 mediastinum plus hidden keyword group
- Added (5): `A361` - Nasopharyngeal diphtheria<br>`B873` - Nasopharyngeal myiasis<br>`J00` - Acute nasopharyngitis [common cold]<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J311` - Chronic nasopharyngitis
- Removed (0): none

### 20. `v500_v296_med_add_hidden_kw_group.csv` - Heart Failure / KEEP

- Message: v500: v296 mediastinum plus hidden keyword group
- Added (6): `O2912` - Cardiac failure due to anesthesia during pregnancy<br>`O29121` - Cardiac failure due to anesthesia during pregnancy, first trimester<br>`O29122` - Cardiac failure due to anesthesia during pregnancy, second trimester<br>`O29123` - Cardiac failure due to anesthesia during pregnancy, third trimester<br>`O29129` - Cardiac failure due to anesthesia during pregnancy, unspecified trimester<br>`P290` - Neonatal cardiac failure
- Removed (0): none

### 20. `v500_v296_med_add_hidden_kw_group.csv` - Interstitial Lung Disease / KEEP

- Message: v500: v296 mediastinum plus hidden keyword group
- Added (9): `J60` - Coalworker's pneumoconiosis<br>`J61` - Pneumoconiosis due to asbestos and other mineral fibers<br>`J62` - Pneumoconiosis due to dust containing silica<br>`J620` - Pneumoconiosis due to talc dust<br>`J628` - Pneumoconiosis due to other dust containing silica<br>`J63` - Pneumoconiosis due to other inorganic dusts<br>`J636` - Pneumoconiosis due to other specified inorganic dusts<br>`J64` - Unspecified pneumoconiosis<br>`J65` - Pneumoconiosis associated with tuberculosis
- Removed (0): none
