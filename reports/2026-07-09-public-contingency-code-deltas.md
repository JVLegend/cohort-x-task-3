# CohortX Plan Code Deltas - 2026-07-09-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-09-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 20
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v521_v296_assoc_epistaxis.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v521: v296 isolate Epistaxis ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 2 | `submissions/v522_v296_assoc_gout.csv` | Gout | ASSOCIATION | 17 | 0 | v522: v296 isolate Gout ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 3 | `submissions/v523_v296_assoc_pleurisy.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v523: v296 isolate Pleurisy ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 4 | `submissions/v524_v296_assoc_bronchitis.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v524: v296 isolate Bronchitis ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 5 | `submissions/v525_v296_assoc_thyroiditis.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v525: v296 isolate Thyroiditis ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 6 | `submissions/v526_v296_assoc_ckd.csv` | CKD | ASSOCIATION | 17 | 0 | v526: v296 isolate CKD ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 7 | `submissions/v527_v296_assoc_hypothyroidism.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v527: v296 isolate Hypothyroidism ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 8 | `submissions/v528_v296_assoc_hematemesis.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v528: v296 isolate Hematemesis ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 9 | `submissions/v529_v296_assoc_hf.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v529: v296 isolate Heart Failure ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 10 | `submissions/v530_v296_assoc_ild.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v530: v296 isolate Interstitial Lung Disease ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 11 | `submissions/v531_v296_assoc_hypoparathyroidism.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v531: v296 isolate Hypoparathyroidism ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 12 | `submissions/v532_v296_assoc_hyperparathyroidism.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v532: v296 isolate Hyperparathyroidism ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 13 | `submissions/v533_v296_assoc_hyperthyroidism.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v533: v296 isolate Hyperthyroidism ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 14 | `submissions/v534_v296_assoc_pneumonia.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v534: v296 isolate Pneumonia ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 15 | `submissions/v535_v296_assoc_icp.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v535: v296 isolate Intracranial Pressure ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 16 | `submissions/v536_v296_assoc_adrenal.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v536: v296 isolate Latent Adrenal Insufficiency ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 17 | `submissions/v537_v296_assoc_derm.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v537: v296 isolate Dermatomycosis ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 18 | `submissions/v538_v296_assoc_npc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v538: v296 isolate Nasopharyngeal Carcinoma ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 19 | `submissions/v539_v296_assoc_uti.csv` | UTI | ASSOCIATION | 20 | 0 | v539: v296 isolate UTI ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |
| 20 | `submissions/v540_v296_assoc_diabetes.csv` | Diabetes | ASSOCIATION | 116 | 0 | v540: v296 isolate Diabetes ASSOC only | single-condition ASSOC isolation from v286 broad ASSOC; DIFF kept empty |

## Exact Code Changes

### 1. `v521_v296_assoc_epistaxis.csv` - Epistaxis / ASSOCIATION

- Message: v521: v296 isolate Epistaxis ASSOC only
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 2. `v522_v296_assoc_gout.csv` - Gout / ASSOCIATION

- Message: v522: v296 isolate Gout ASSOC only
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 3. `v523_v296_assoc_pleurisy.csv` - Pleurisy / ASSOCIATION

- Message: v523: v296 isolate Pleurisy ASSOC only
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 4. `v524_v296_assoc_bronchitis.csv` - Bronchitis / ASSOCIATION

- Message: v524: v296 isolate Bronchitis ASSOC only
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 5. `v525_v296_assoc_thyroiditis.csv` - Thyroiditis / ASSOCIATION

- Message: v525: v296 isolate Thyroiditis ASSOC only
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 6. `v526_v296_assoc_ckd.csv` - CKD / ASSOCIATION

- Message: v526: v296 isolate CKD ASSOC only
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 7. `v527_v296_assoc_hypothyroidism.csv` - Hypothyroidism / ASSOCIATION

- Message: v527: v296 isolate Hypothyroidism ASSOC only
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 8. `v528_v296_assoc_hematemesis.csv` - Hematemesis / ASSOCIATION

- Message: v528: v296 isolate Hematemesis ASSOC only
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 9. `v529_v296_assoc_hf.csv` - Heart Failure / ASSOCIATION

- Message: v529: v296 isolate Heart Failure ASSOC only
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 10. `v530_v296_assoc_ild.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v530: v296 isolate Interstitial Lung Disease ASSOC only
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 11. `v531_v296_assoc_hypoparathyroidism.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v531: v296 isolate Hypoparathyroidism ASSOC only
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 12. `v532_v296_assoc_hyperparathyroidism.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v532: v296 isolate Hyperparathyroidism ASSOC only
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 13. `v533_v296_assoc_hyperthyroidism.csv` - Hyperthyroidism / ASSOCIATION

- Message: v533: v296 isolate Hyperthyroidism ASSOC only
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 14. `v534_v296_assoc_pneumonia.csv` - Pneumonia / ASSOCIATION

- Message: v534: v296 isolate Pneumonia ASSOC only
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 15. `v535_v296_assoc_icp.csv` - Intracranial Pressure / ASSOCIATION

- Message: v535: v296 isolate Intracranial Pressure ASSOC only
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 16. `v536_v296_assoc_adrenal.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v536: v296 isolate Latent Adrenal Insufficiency ASSOC only
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 17. `v537_v296_assoc_derm.csv` - Dermatomycosis / ASSOCIATION

- Message: v537: v296 isolate Dermatomycosis ASSOC only
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 18. `v538_v296_assoc_npc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v538: v296 isolate Nasopharyngeal Carcinoma ASSOC only
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 19. `v539_v296_assoc_uti.csv` - UTI / ASSOCIATION

- Message: v539: v296 isolate UTI ASSOC only
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 20. `v540_v296_assoc_diabetes.csv` - Diabetes / ASSOCIATION

- Message: v540: v296 isolate Diabetes ASSOC only
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

