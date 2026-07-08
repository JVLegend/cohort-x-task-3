# CohortX Plan Impact Readout - 2026-07-08-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-08-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Anchor public: 0.43156
- Scored items: 20/20
- Improved/tied/worse/missing: 0/0/20/0

## Decision Table

| Order | File | Status | Public | Delta | Signal | Edit | Interpretation |
|---:|---|---|---:|---:|---|---|---|
| 1 | `v481_v296_zero_hf.csv` | complete | 0.42995 | -0.00161 | worse | removed 72 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 2 | `v482_v296_zero_hyperthyroid.csv` | complete | 0.42995 | -0.00161 | worse | removed 49 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 3 | `v483_v296_zero_ild.csv` | complete | 0.42995 | -0.00161 | worse | removed 42 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 4 | `v484_v296_zero_derm.csv` | complete | 0.42995 | -0.00161 | worse | removed 38 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 5 | `v485_v296_zero_bronchitis.csv` | complete | 0.42995 | -0.00161 | worse | removed 33 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 6 | `v486_v296_zero_npc.csv` | complete | 0.42995 | -0.00161 | worse | removed 42 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 7 | `v487_v296_zero_hypothyroid.csv` | complete | 0.42995 | -0.00161 | worse | removed 26 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 8 | `v488_v296_add_hf_kw.csv` | complete | 0.42995 | -0.00161 | worse | added 6 | addition hurt public score; treat these codes as public false positives |
| 9 | `v489_v296_add_ild_kw.csv` | complete | 0.42995 | -0.00161 | worse | added 9 | addition hurt public score; treat these codes as public false positives |
| 10 | `v490_v296_add_derm_kw.csv` | complete | 0.42995 | -0.00161 | worse | added 57 | addition hurt public score; treat these codes as public false positives |
| 11 | `v491_v296_add_npc_kw.csv` | complete | 0.42995 | -0.00161 | worse | added 5 | addition hurt public score; treat these codes as public false positives |
| 12 | `v492_v296_zero_endocrine_pair.csv` | complete | 0.42995 | -0.00161 | worse | removed 26 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 13 | `v493_v296_zero_pulmonary_pair.csv` | complete | 0.42995 | -0.00161 | worse | removed 33 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 14 | `v494_v296_zero_derm_npc_pair.csv` | complete | 0.42995 | -0.00161 | worse | removed 38 | removal hurt public score; keep/restore these codes in public-facing candidates |
| 15 | `v495_v296_add_hidden_kw_group.csv` | complete | 0.42995 | -0.00161 | worse | added 57 | addition hurt public score; treat these codes as public false positives |
| 16 | `v496_v296_med_zero_hf.csv` | complete | 0.43015 | -0.00141 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 17 | `v497_v296_med_zero_endocrine_pair.csv` | complete | 0.43015 | -0.00141 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 18 | `v498_v296_med_zero_pulmonary_pair.csv` | complete | 0.43015 | -0.00141 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 19 | `v499_v296_med_zero_derm_npc_pair.csv` | complete | 0.43015 | -0.00141 | worse | added 4 | addition hurt public score; treat these codes as public false positives |
| 20 | `v500_v296_med_add_hidden_kw_group.csv` | complete | 0.43015 | -0.00141 | worse | added 4 | addition hurt public score; treat these codes as public false positives |

## Ranked Scored Probes

| Rank | File | Delta | ICD change | Exact codes |
|---:|---|---:|---|---|
| 1 | `v496_v296_med_zero_hf.csv` | -0.00141 | added 4 | `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes |
| 2 | `v497_v296_med_zero_endocrine_pair.csv` | -0.00141 | added 4 | `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes |
| 3 | `v498_v296_med_zero_pulmonary_pair.csv` | -0.00141 | added 4 | `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes |
| 4 | `v499_v296_med_zero_derm_npc_pair.csv` | -0.00141 | added 4 | `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes |
| 5 | `v500_v296_med_add_hidden_kw_group.csv` | -0.00141 | added 4 | `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes |
| 6 | `v481_v296_zero_hf.csv` | -0.00161 | removed 72 | `I09` - Other rheumatic heart diseases<br>`I0981` - Rheumatic heart failure<br>`I11` - Hypertensive heart disease<br>`I110` - Hypertensive heart disease with heart failure<br>`I119` - Hypertensive heart disease without heart failure<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>... +64 more |
| 7 | `v482_v296_zero_hyperthyroid.csv` | -0.00161 | removed 49 | `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>... +41 more |
| 8 | `v483_v296_zero_ild.csv` | -0.00161 | removed 42 | `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>... +34 more |
| 9 | `v484_v296_zero_derm.csv` | -0.00161 | removed 38 | `B35` - Dermatophytosis<br>`B350` - Tinea barbae and tinea capitis<br>`B351` - Tinea unguium<br>`B352` - Tinea manuum<br>`B353` - Tinea pedis<br>`B354` - Tinea corporis<br>`B355` - Tinea imbricata<br>`B356` - Tinea cruris<br>... +30 more |
| 10 | `v485_v296_zero_bronchitis.csv` | -0.00161 | removed 33 | `J04` - Acute laryngitis and tracheitis<br>`J0410` - Acute tracheitis without obstruction<br>`J0411` - Acute tracheitis with obstruction<br>`J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>... +25 more |
| 11 | `v486_v296_zero_npc.csv` | -0.00161 | removed 42 | `C10` - Malignant neoplasm of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C11` - Malignant neoplasm of nasopharynx<br>`C110` - Malignant neoplasm of superior wall of nasopharynx<br>`C111` - Malignant neoplasm of posterior wall of nasopharynx<br>`C112` - Malignant neoplasm of lateral wall of nasopharynx<br>`C113` - Malignant neoplasm of anterior wall of nasopharynx<br>`C118` - Malignant neoplasm of overlapping sites of nasopharynx<br>... +34 more |
| 12 | `v487_v296_zero_hypothyroid.csv` | -0.00161 | removed 26 | `E00` - Congenital iodine-deficiency syndrome<br>`E000` - Congenital iodine-deficiency syndrome, neurological type<br>`E001` - Congenital iodine-deficiency syndrome, myxedematous type<br>`E002` - Congenital iodine-deficiency syndrome, mixed type<br>`E009` - Congenital iodine-deficiency syndrome, unspecified<br>`E02` - Subclinical iodine-deficiency hypothyroidism<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>... +18 more |
| 13 | `v488_v296_add_hf_kw.csv` | -0.00161 | added 6 | `O2912` - Cardiac failure due to anesthesia during pregnancy<br>`O29121` - Cardiac failure due to anesthesia during pregnancy, first trimester<br>`O29122` - Cardiac failure due to anesthesia during pregnancy, second trimester<br>`O29123` - Cardiac failure due to anesthesia during pregnancy, third trimester<br>`O29129` - Cardiac failure due to anesthesia during pregnancy, unspecified trimester<br>`P290` - Neonatal cardiac failure |
| 14 | `v489_v296_add_ild_kw.csv` | -0.00161 | added 9 | `J60` - Coalworker's pneumoconiosis<br>`J61` - Pneumoconiosis due to asbestos and other mineral fibers<br>`J62` - Pneumoconiosis due to dust containing silica<br>`J620` - Pneumoconiosis due to talc dust<br>`J628` - Pneumoconiosis due to other dust containing silica<br>`J63` - Pneumoconiosis due to other inorganic dusts<br>`J636` - Pneumoconiosis due to other specified inorganic dusts<br>`J64` - Unspecified pneumoconiosis<br>... +1 more |
| 15 | `v490_v296_add_derm_kw.csv` | -0.00161 | added 57 | `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>... +49 more |
| 16 | `v491_v296_add_npc_kw.csv` | -0.00161 | added 5 | `A361` - Nasopharyngeal diphtheria<br>`B873` - Nasopharyngeal myiasis<br>`J00` - Acute nasopharyngitis [common cold]<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J311` - Chronic nasopharyngitis |
| 17 | `v492_v296_zero_endocrine_pair.csv` | -0.00161 | removed 26 | `E00` - Congenital iodine-deficiency syndrome<br>`E000` - Congenital iodine-deficiency syndrome, neurological type<br>`E001` - Congenital iodine-deficiency syndrome, myxedematous type<br>`E002` - Congenital iodine-deficiency syndrome, mixed type<br>`E009` - Congenital iodine-deficiency syndrome, unspecified<br>`E02` - Subclinical iodine-deficiency hypothyroidism<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>... +18 more |
| 18 | `v493_v296_zero_pulmonary_pair.csv` | -0.00161 | removed 33 | `J04` - Acute laryngitis and tracheitis<br>`J0410` - Acute tracheitis without obstruction<br>`J0411` - Acute tracheitis with obstruction<br>`J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>... +25 more |
| 19 | `v494_v296_zero_derm_npc_pair.csv` | -0.00161 | removed 38 | `B35` - Dermatophytosis<br>`B350` - Tinea barbae and tinea capitis<br>`B351` - Tinea unguium<br>`B352` - Tinea manuum<br>`B353` - Tinea pedis<br>`B354` - Tinea corporis<br>`B355` - Tinea imbricata<br>`B356` - Tinea cruris<br>... +30 more |
| 20 | `v495_v296_add_hidden_kw_group.csv` | -0.00161 | added 57 | `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>... +49 more |

## Use

- Improved removals are pruning candidates for public-facing combos.
- Improved additions are promotion candidates for public-facing combos.
- Tied edits are mainly private hedges unless later combo evidence says otherwise.
- Worse removals indicate codes that likely belong in the public gold slice; worse additions are public false positives.
