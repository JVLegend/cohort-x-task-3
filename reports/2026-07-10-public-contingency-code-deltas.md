# CohortX Plan Code Deltas - 2026-07-10-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-10-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 20
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v561_v296_diff_epistaxis.csv` | Epistaxis | DIFF | 2 | 0 | v561: v296 isolate Epistaxis DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 2 | `submissions/v562_v296_diff_gout.csv` | Gout | DIFF | 260 | 0 | v562: v296 isolate Gout DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 3 | `submissions/v563_v296_diff_pleurisy.csv` | Pleurisy | DIFF | 17 | 0 | v563: v296 isolate Pleurisy DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 4 | `submissions/v564_v296_diff_bronchitis.csv` | Bronchitis | DIFF | 32 | 0 | v564: v296 isolate Bronchitis DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 5 | `submissions/v565_v296_diff_thyroiditis.csv` | Thyroiditis | DIFF | 6 | 0 | v565: v296 isolate Thyroiditis DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 6 | `submissions/v566_v296_diff_ckd.csv` | CKD | DIFF | 6 | 0 | v566: v296 isolate CKD DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 7 | `submissions/v567_v296_diff_hypothyroidism.csv` | Hypothyroidism | DIFF | 22 | 0 | v567: v296 isolate Hypothyroidism DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 8 | `submissions/v568_v296_diff_hematemesis.csv` | Hematemesis | DIFF | 2 | 0 | v568: v296 isolate Hematemesis DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 9 | `submissions/v569_v296_diff_hf.csv` | Heart Failure | DIFF | 15 | 0 | v569: v296 isolate Heart Failure DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 10 | `submissions/v570_v296_diff_ild.csv` | Interstitial Lung Disease | DIFF | 35 | 0 | v570: v296 isolate Interstitial Lung Disease DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 11 | `submissions/v571_v296_diff_hypoparathyroidism.csv` | Hypoparathyroidism | DIFF | 10 | 0 | v571: v296 isolate Hypoparathyroidism DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 12 | `submissions/v572_v296_diff_hyperparathyroidism.csv` | Hyperparathyroidism | DIFF | 5 | 0 | v572: v296 isolate Hyperparathyroidism DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 13 | `submissions/v573_v296_diff_hyperthyroidism.csv` | Hyperthyroidism | DIFF | 15 | 0 | v573: v296 isolate Hyperthyroidism DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 14 | `submissions/v574_v296_diff_pneumonia.csv` | Pneumonia | DIFF | 71 | 0 | v574: v296 isolate Pneumonia DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 15 | `submissions/v575_v296_diff_icp.csv` | Intracranial Pressure | DIFF | 97 | 0 | v575: v296 isolate Intracranial Pressure DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 16 | `submissions/v576_v296_diff_adrenal.csv` | Latent Adrenal Insufficiency | DIFF | 12 | 0 | v576: v296 isolate Latent Adrenal Insufficiency DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 17 | `submissions/v577_v296_diff_derm.csv` | Dermatomycosis | DIFF | 33 | 0 | v577: v296 isolate Dermatomycosis DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 18 | `submissions/v578_v296_diff_npc.csv` | Nasopharyngeal Carcinoma | DIFF | 17 | 0 | v578: v296 isolate Nasopharyngeal Carcinoma DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 19 | `submissions/v579_v296_diff_uti.csv` | UTI | DIFF | 39 | 0 | v579: v296 isolate UTI DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |
| 20 | `submissions/v580_v296_diff_diabetes.csv` | Diabetes | DIFF | 7 | 0 | v580: v296 isolate Diabetes DIFF only | single-condition DIFF isolation from v285 broad DIFF; ASSOC kept empty |

## Exact Code Changes

### 1. `v561_v296_diff_epistaxis.csv` - Epistaxis / DIFF

- Message: v561: v296 isolate Epistaxis DIFF only
- Added (2): `R58` - Hemorrhage, not elsewhere classified<br>`K920` - Hematemesis
- Removed (0): none

### 2. `v562_v296_diff_gout.csv` - Gout / DIFF

- Message: v562: v296 isolate Gout DIFF only
- Added (260): `M00` - Pyogenic arthritis<br>`M000` - Staphylococcal arthritis and polyarthritis<br>`M0000` - Staphylococcal arthritis, unspecified joint<br>`M0001` - Staphylococcal arthritis, shoulder<br>`M00011` - Staphylococcal arthritis, right shoulder<br>`M00012` - Staphylococcal arthritis, left shoulder<br>`M00019` - Staphylococcal arthritis, unspecified shoulder<br>`M0002` - Staphylococcal arthritis, elbow<br>`M00021` - Staphylococcal arthritis, right elbow<br>`M00022` - Staphylococcal arthritis, left elbow<br>`M00029` - Staphylococcal arthritis, unspecified elbow<br>`M0003` - Staphylococcal arthritis, wrist<br>`M00031` - Staphylococcal arthritis, right wrist<br>`M00032` - Staphylococcal arthritis, left wrist<br>`M00039` - Staphylococcal arthritis, unspecified wrist<br>`M0004` - Staphylococcal arthritis, hand<br>`M00041` - Staphylococcal arthritis, right hand<br>`M00042` - Staphylococcal arthritis, left hand<br>... +242 more
- Removed (0): none

### 3. `v563_v296_diff_pleurisy.csv` - Pleurisy / DIFF

- Message: v563: v296 isolate Pleurisy DIFF only
- Added (17): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 4. `v564_v296_diff_bronchitis.csv` - Bronchitis / DIFF

- Message: v564: v296 isolate Bronchitis DIFF only
- Added (32): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`J45` - Asthma<br>`J452` - Mild intermittent asthma<br>`J4520` - Mild intermittent asthma, uncomplicated<br>`J4521` - Mild intermittent asthma with (acute) exacerbation<br>`J4522` - Mild intermittent asthma with status asthmaticus<br>`J453` - Mild persistent asthma<br>`J4530` - Mild persistent asthma, uncomplicated<br>`J4531` - Mild persistent asthma with (acute) exacerbation<br>`J4532` - Mild persistent asthma with status asthmaticus<br>`J454` - Moderate persistent asthma<br>`J4540` - Moderate persistent asthma, uncomplicated<br>`J4541` - Moderate persistent asthma with (acute) exacerbation<br>... +14 more
- Removed (0): none

### 5. `v565_v296_diff_thyroiditis.csv` - Thyroiditis / DIFF

- Message: v565: v296 isolate Thyroiditis DIFF only
- Added (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified
- Removed (0): none

### 6. `v566_v296_diff_ckd.csv` - CKD / DIFF

- Message: v566: v296 isolate CKD DIFF only
- Added (6): `N17` - Acute kidney failure<br>`N170` - Acute kidney failure with tubular necrosis<br>`N171` - Acute kidney failure with acute cortical necrosis<br>`N172` - Acute kidney failure with medullary necrosis<br>`N178` - Other acute kidney failure<br>`N179` - Acute kidney failure, unspecified
- Removed (0): none

### 7. `v567_v296_diff_hypothyroidism.csv` - Hypothyroidism / DIFF

- Message: v567: v296 isolate Hypothyroidism DIFF only
- Added (22): `E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>`E0521` - Thyrotoxicosis with toxic multinodular goiter with thyrotoxic crisis or storm<br>`E053` - Thyrotoxicosis from ectopic thyroid tissue<br>`E0530` - Thyrotoxicosis from ectopic thyroid tissue without thyrotoxic crisis or storm<br>`E0531` - Thyrotoxicosis from ectopic thyroid tissue with thyrotoxic crisis or storm<br>`E054` - Thyrotoxicosis factitia<br>`E0540` - Thyrotoxicosis factitia without thyrotoxic crisis or storm<br>`E0541` - Thyrotoxicosis factitia with thyrotoxic crisis or storm<br>`E058` - Other thyrotoxicosis<br>`E0580` - Other thyrotoxicosis without thyrotoxic crisis or storm<br>... +4 more
- Removed (0): none

### 8. `v568_v296_diff_hematemesis.csv` - Hematemesis / DIFF

- Message: v568: v296 isolate Hematemesis DIFF only
- Added (2): `K921` - Melena<br>`R042` - Hemoptysis
- Removed (0): none

### 9. `v569_v296_diff_hf.csv` - Heart Failure / DIFF

- Message: v569: v296 isolate Heart Failure DIFF only
- Added (15): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified<br>`I26` - Pulmonary embolism<br>`I260` - Pulmonary embolism with acute cor pulmonale<br>`I2601` - Septic pulmonary embolism with acute cor pulmonale<br>`I2602` - Saddle embolus of pulmonary artery with acute cor pulmonale<br>`I2609` - Other pulmonary embolism with acute cor pulmonale<br>`I269` - Pulmonary embolism without acute cor pulmonale<br>`I2690` - Septic pulmonary embolism without acute cor pulmonale<br>`I2692` - Saddle embolus of pulmonary artery without acute cor pulmonale<br>`I2693` - Single subsegmental pulmonary embolism without acute cor pulmonale<br>`I2694` - Multiple subsegmental pulmonary emboli without acute cor pulmonale<br>`I2699` - Other pulmonary embolism without acute cor pulmonale
- Removed (0): none

### 10. `v570_v296_diff_ild.csv` - Interstitial Lung Disease / DIFF

- Message: v570: v296 isolate Interstitial Lung Disease DIFF only
- Added (35): `J18` - Pneumonia, unspecified organism<br>`J180` - Bronchopneumonia, unspecified organism<br>`J181` - Lobar pneumonia, unspecified organism<br>`J182` - Hypostatic pneumonia, unspecified organism<br>`J188` - Other pneumonia, unspecified organism<br>`J189` - Pneumonia, unspecified organism<br>`I50` - Heart failure<br>`I501` - Left ventricular failure, unspecified<br>`I502` - Systolic (congestive) heart failure<br>`I5020` - Unspecified systolic (congestive) heart failure<br>`I5021` - Acute systolic (congestive) heart failure<br>`I5022` - Chronic systolic (congestive) heart failure<br>`I5023` - Acute on chronic systolic (congestive) heart failure<br>`I503` - Diastolic (congestive) heart failure<br>`I5030` - Unspecified diastolic (congestive) heart failure<br>`I5031` - Acute diastolic (congestive) heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I5033` - Acute on chronic diastolic (congestive) heart failure<br>... +17 more
- Removed (0): none

### 11. `v571_v296_diff_hypoparathyroidism.csv` - Hypoparathyroidism / DIFF

- Message: v571: v296 isolate Hypoparathyroidism DIFF only
- Added (10): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E210` - Primary hyperparathyroidism<br>`E211` - Secondary hyperparathyroidism, not elsewhere classified<br>`E212` - Other hyperparathyroidism<br>`E213` - Hyperparathyroidism, unspecified<br>`E214` - Other specified disorders of parathyroid gland<br>`E215` - Disorder of parathyroid gland, unspecified<br>`E55` - Vitamin D deficiency<br>`E550` - Rickets, active<br>`E559` - Vitamin D deficiency, unspecified
- Removed (0): none

### 12. `v572_v296_diff_hyperparathyroidism.csv` - Hyperparathyroidism / DIFF

- Message: v572: v296 isolate Hyperparathyroidism DIFF only
- Added (5): `E20` - Hypoparathyroidism<br>`E200` - Idiopathic hypoparathyroidism<br>`E201` - Pseudohypoparathyroidism<br>`E208` - Other hypoparathyroidism<br>`E209` - Hypoparathyroidism, unspecified
- Removed (0): none

### 13. `v573_v296_diff_hyperthyroidism.csv` - Hyperthyroidism / DIFF

- Message: v573: v296 isolate Hyperthyroidism DIFF only
- Added (15): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`F41` - Other anxiety disorders<br>`F410` - Panic disorder [episodic paroxysmal anxiety]<br>`F411` - Generalized anxiety disorder<br>`F413` - Other mixed anxiety disorders<br>`F418` - Other specified anxiety disorders<br>`F419` - Anxiety disorder, unspecified
- Removed (0): none

### 14. `v574_v296_diff_pneumonia.csv` - Pneumonia / DIFF

- Message: v574: v296 isolate Pneumonia DIFF only
- Added (71): `J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J40` - Bronchitis, not specified as acute or chronic<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>... +53 more
- Removed (0): none

### 15. `v575_v296_diff_icp.csv` - Intracranial Pressure / DIFF

- Message: v575: v296 isolate Intracranial Pressure DIFF only
- Added (97): `G43` - Migraine<br>`G430` - Migraine without aura<br>`G4300` - Migraine without aura, not intractable<br>`G43001` - Migraine without aura, not intractable, with status migrainosus<br>`G43009` - Migraine without aura, not intractable, without status migrainosus<br>`G4301` - Migraine without aura, intractable<br>`G43011` - Migraine without aura, intractable, with status migrainosus<br>`G43019` - Migraine without aura, intractable, without status migrainosus<br>`G431` - Migraine with aura<br>`G4310` - Migraine with aura, not intractable<br>`G43101` - Migraine with aura, not intractable, with status migrainosus<br>`G43109` - Migraine with aura, not intractable, without status migrainosus<br>`G4311` - Migraine with aura, intractable<br>`G43111` - Migraine with aura, intractable, with status migrainosus<br>`G43119` - Migraine with aura, intractable, without status migrainosus<br>`G434` - Hemiplegic migraine<br>`G4340` - Hemiplegic migraine, not intractable<br>`G43401` - Hemiplegic migraine, not intractable, with status migrainosus<br>... +79 more
- Removed (0): none

### 16. `v576_v296_diff_adrenal.csv` - Latent Adrenal Insufficiency / DIFF

- Message: v576: v296 isolate Latent Adrenal Insufficiency DIFF only
- Added (12): `E86` - Volume depletion<br>`E860` - Dehydration<br>`E861` - Hypovolemia<br>`E869` - Volume depletion, unspecified<br>`R53` - Malaise and fatigue<br>`R530` - Neoplastic (malignant) related fatigue<br>`R531` - Weakness<br>`R532` - Functional quadriplegia<br>`R538` - Other malaise and fatigue<br>`R5381` - Other malaise<br>`R5382` - Chronic fatigue, unspecified<br>`R5383` - Other fatigue
- Removed (0): none

### 17. `v577_v296_diff_derm.csv` - Dermatomycosis / DIFF

- Message: v577: v296 isolate Dermatomycosis DIFF only
- Added (33): `L40` - Psoriasis<br>`L400` - Psoriasis vulgaris<br>`L401` - Generalized pustular psoriasis<br>`L402` - Acrodermatitis continua<br>`L403` - Pustulosis palmaris et plantaris<br>`L404` - Guttate psoriasis<br>`L405` - Arthropathic psoriasis<br>`L4050` - Arthropathic psoriasis, unspecified<br>`L4051` - Distal interphalangeal psoriatic arthropathy<br>`L4052` - Psoriatic arthritis mutilans<br>`L4053` - Psoriatic spondylitis<br>`L4054` - Psoriatic juvenile arthropathy<br>`L4059` - Other psoriatic arthropathy<br>`L408` - Other psoriasis<br>`L409` - Psoriasis, unspecified<br>`L20` - Atopic dermatitis<br>`L200` - Besnier's prurigo<br>`L208` - Other atopic dermatitis<br>... +15 more
- Removed (0): none

### 18. `v578_v296_diff_npc.csv` - Nasopharyngeal Carcinoma / DIFF

- Message: v578: v296 isolate Nasopharyngeal Carcinoma DIFF only
- Added (17): `C10` - Malignant neoplasm of oropharynx<br>`C100` - Malignant neoplasm of vallecula<br>`C101` - Malignant neoplasm of anterior surface of epiglottis<br>`C102` - Malignant neoplasm of lateral wall of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C104` - Malignant neoplasm of branchial cleft<br>`C108` - Malignant neoplasm of overlapping sites of oropharynx<br>`C109` - Malignant neoplasm of oropharynx, unspecified<br>`C14` - Malignant neoplasm of other and ill-defined sites in the lip, oral cavity and pharynx<br>`C140` - Malignant neoplasm of pharynx, unspecified<br>`C142` - Malignant neoplasm of Waldeyer's ring<br>`C148` - Malignant neoplasm of overlapping sites of lip, oral cavity and pharynx<br>`J33` - Nasal polyp<br>`J330` - Polyp of nasal cavity<br>`J331` - Polypoid sinus degeneration<br>`J338` - Other polyp of sinus<br>`J339` - Nasal polyp, unspecified
- Removed (0): none

### 19. `v579_v296_diff_uti.csv` - UTI / DIFF

- Message: v579: v296 isolate UTI DIFF only
- Added (39): `N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>`N3030` - Trigonitis without hematuria<br>`N3031` - Trigonitis with hematuria<br>`N304` - Irradiation cystitis<br>`N3040` - Irradiation cystitis without hematuria<br>`N3041` - Irradiation cystitis with hematuria<br>`N308` - Other cystitis<br>`N3080` - Other cystitis without hematuria<br>... +21 more
- Removed (0): none

### 20. `v580_v296_diff_diabetes.csv` - Diabetes / DIFF

- Message: v580: v296 isolate Diabetes DIFF only
- Added (7): `R73` - Elevated blood glucose level<br>`R730` - Abnormal glucose<br>`R7301` - Impaired fasting glucose<br>`R7302` - Impaired glucose tolerance (oral)<br>`R7303` - Prediabetes<br>`R7309` - Other abnormal glucose<br>`R739` - Hyperglycemia, unspecified
- Removed (0): none

