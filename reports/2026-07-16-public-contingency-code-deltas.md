# CohortX Plan Code Deltas - 2026-07-16-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Changed rows: 420
- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.

## Delta Summary

| Order | File | Condition | Column | Added | Removed | Message | Notes |
|---:|---|---|---|---:|---:|---|---|
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Hypothyroidism | KEEP | 0 | 26 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | UTI | KEEP | 0 | 76 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Diabetes | KEEP | 232 | 13 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Hyperthyroidism | KEEP | 0 | 49 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 1 | `submissions/v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v801: v296 final med+v185 zero thyroid highconf ASSOC | final fallback: public anchor plus med, v185, zero thyroid KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Bronchitis | KEEP | 0 | 33 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | UTI | KEEP | 0 | 76 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Diabetes | KEEP | 232 | 13 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Interstitial Lung Disease | KEEP | 0 | 42 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 2 | `submissions/v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v802: v296 final med+v185 zero pulmonary highconf ASSOC | final fallback: public anchor plus med, v185, zero pulmonary KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Dermatomycosis | KEEP | 0 | 38 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 42 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | UTI | KEEP | 0 | 76 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Diabetes | KEEP | 232 | 13 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 3 | `submissions/v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v803: v296 final med+v185 zero Derm/NPC highconf ASSOC | final fallback: public anchor plus med, v185, zero Derm/NPC KEEP, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Dermatomycosis | KEEP | 57 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Nasopharyngeal Carcinoma | KEEP | 5 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Heart Failure | KEEP | 6 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | UTI | KEEP | 0 | 76 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Diabetes | KEEP | 232 | 13 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Interstitial Lung Disease | KEEP | 9 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 4 | `submissions/v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v804: v296 final med+v185 add hidden highconf ASSOC | final fallback: public anchor plus med, v185, hidden keyword KEEP adds, highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | UTI | KEEP | 0 | 86 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Diabetes | KEEP | 232 | 70 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 5 | `submissions/v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v805: v296 final med+v185 renal/metabolic prune highconf ASSOC | final fallback: med+v185 plus renal/metabolic KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Heart Failure | KEEP | 0 | 31 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | UTI | KEEP | 0 | 76 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Diabetes | KEEP | 232 | 13 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 6 | `submissions/v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v806: v296 final med+v185 cardio/pulm prune highconf ASSOC | final fallback: med+v185 plus cardio/pulm KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Thyroiditis | KEEP | 0 | 2 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Hypothyroidism | KEEP | 0 | 6 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | UTI | KEEP | 0 | 76 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Diabetes | KEEP | 232 | 13 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Hyperthyroidism | KEEP | 0 | 12 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 7 | `submissions/v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v807: v296 final med+v185 thyroid prune highconf ASSOC | final fallback: med+v185 plus thyroid KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Pleurisy | KEEP | 0 | 12 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Bronchitis | KEEP | 0 | 8 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | CKD | KEEP | 22 | 75 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | UTI | KEEP | 0 | 76 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Diabetes | KEEP | 232 | 13 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Pneumonia | KEEP | 1 | 53 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 8 | `submissions/v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v808: v296 final med+v185 respiratory prune highconf ASSOC | final fallback: med+v185 plus respiratory KEEP prune and highconf ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | CKD | KEEP | 22 | 75 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Hypothyroidism | KEEP | 0 | 26 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | UTI | KEEP | 0 | 76 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Diabetes | KEEP | 232 | 13 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Hyperthyroidism | KEEP | 0 | 49 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 9 | `submissions/v809_v296_final_v185_zero_thyroid_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v809: v296 final v185 zero thyroid broad ASSOC | final fallback: no-med private hedge with zero thyroid KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Bronchitis | KEEP | 0 | 33 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | CKD | KEEP | 22 | 75 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | UTI | KEEP | 0 | 76 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Diabetes | KEEP | 232 | 13 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Interstitial Lung Disease | KEEP | 0 | 42 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 10 | `submissions/v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v810: v296 final v185 zero pulmonary broad ASSOC | final fallback: no-med private hedge with zero pulmonary KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Dermatomycosis | KEEP | 0 | 38 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 42 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | CKD | KEEP | 22 | 75 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | UTI | KEEP | 0 | 76 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Diabetes | KEEP | 232 | 13 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 11 | `submissions/v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v811: v296 final v185 zero Derm/NPC broad ASSOC | final fallback: no-med private hedge with zero Derm/NPC KEEP and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Dermatomycosis | KEEP | 57 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Nasopharyngeal Carcinoma | KEEP | 5 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | CKD | KEEP | 22 | 75 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Heart Failure | KEEP | 6 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | UTI | KEEP | 0 | 76 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Diabetes | KEEP | 232 | 13 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Interstitial Lung Disease | KEEP | 9 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 12 | `submissions/v812_v296_final_v185_add_hidden_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v812: v296 final v185 add hidden broad ASSOC | final fallback: no-med private hedge with hidden keyword KEEP adds and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | CKD | KEEP | 22 | 75 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | UTI | KEEP | 0 | 86 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Diabetes | KEEP | 232 | 70 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 13 | `submissions/v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v813: v296 final v185 renal/metabolic prune broad ASSOC | final fallback: no-med v185 plus renal/metabolic KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Gout | KEEP | 0 | 2 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | CKD | KEEP | 22 | 75 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Hematemesis | KEEP | 0 | 4 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Heart Failure | KEEP | 0 | 31 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | UTI | KEEP | 0 | 76 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Diabetes | KEEP | 232 | 13 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 14 | `submissions/v814_v296_final_v185_prune_small_precision_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v814: v296 final v185 small precision prune broad ASSOC | final fallback: no-med v185 plus small high-precision KEEP prune and broad ASSOC |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Epistaxis | ASSOCIATION | 48 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Intracranial Pressure | KEEP | 0 | 4 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Gout | KEEP | 0 | 2 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Dermatomycosis | KEEP | 0 | 21 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Dermatomycosis | ASSOCIATION | 137 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Pleurisy | KEEP | 0 | 12 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Bronchitis | KEEP | 0 | 8 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Thyroiditis | KEEP | 0 | 2 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Nasopharyngeal Carcinoma | KEEP | 0 | 18 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Nasopharyngeal Carcinoma | ASSOCIATION | 30 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | CKD | KEEP | 22 | 75 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hypothyroidism | KEEP | 0 | 6 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hematemesis | KEEP | 0 | 4 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hematemesis | ASSOCIATION | 65 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Heart Failure | KEEP | 0 | 31 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hypergonadism | KEEP | 0 | 11 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | UTI | KEEP | 0 | 86 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | UTI | ASSOCIATION | 20 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Diabetes | KEEP | 232 | 71 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Interstitial Lung Disease | KEEP | 0 | 9 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hypoparathyroidism | KEEP | 0 | 8 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hyperthyroidism | KEEP | 0 | 12 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Pneumonia | KEEP | 1 | 53 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 15 | `submissions/v815_v296_final_v185_broad_private_prune_broad_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v815: v296 final v185 broad private prune broad ASSOC | aggressive final fallback: broad private KEEP prune plus broad ASSOC, DIFF empty |
| 16 | `submissions/v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC | targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC |
| 16 | `submissions/v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` | CKD | KEEP | 22 | 75 | v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC | targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC |
| 16 | `submissions/v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` | CKD | ASSOCIATION | 17 | 0 | v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC | targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC |
| 16 | `submissions/v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` | Heart Failure | KEEP | 6 | 0 | v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC | targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC |
| 16 | `submissions/v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` | Heart Failure | ASSOCIATION | 35 | 0 | v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC | targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC |
| 16 | `submissions/v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` | UTI | KEEP | 0 | 76 | v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC | targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC |
| 16 | `submissions/v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC | targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC |
| 16 | `submissions/v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` | Interstitial Lung Disease | KEEP | 9 | 0 | v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC | targeted final fallback: med, CKD/UTI v185, HF/ILD adds, cardiorenal ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Dermatomycosis | KEEP | 57 | 0 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Pleurisy | ASSOCIATION | 12 | 0 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Bronchitis | ASSOCIATION | 4 | 0 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Nasopharyngeal Carcinoma | KEEP | 5 | 0 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Diabetes | KEEP | 232 | 13 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Interstitial Lung Disease | ASSOCIATION | 41 | 0 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 17 | `submissions/v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` | Pneumonia | ASSOCIATION | 36 | 0 | v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC | targeted final fallback: med, Diabetes/Pneumonia v185, Derm/NPC adds, pulmonary ASSOC |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Enlarged Mediastinum | KEEP | 4 | 0 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Latent Adrenal Insufficiency | ASSOCIATION | 19 | 0 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Thyroiditis | ASSOCIATION | 31 | 0 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | CKD | KEEP | 22 | 75 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Hypothyroidism | KEEP | 0 | 26 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Hypothyroidism | ASSOCIATION | 19 | 0 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | UTI | KEEP | 0 | 76 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Diabetes | KEEP | 232 | 13 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Diabetes | ASSOCIATION | 116 | 0 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Hypoparathyroidism | ASSOCIATION | 1 | 0 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Hyperparathyroidism | ASSOCIATION | 8 | 0 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Hyperthyroidism | KEEP | 0 | 49 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Hyperthyroidism | ASSOCIATION | 21 | 0 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 18 | `submissions/v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` | Pneumonia | KEEP | 1 | 28 | v818: v296 final med+v185 zero endocrine ASSOC | targeted final fallback: med, v185, zero thyroid KEEP, endocrine ASSOC only |
| 19 | `submissions/v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` | Intracranial Pressure | KEEP | 0 | 4 | v819: v296 final CKD/UTI neuro-rheum prune ASSOC | targeted final fallback: CKD/UTI v185, ICP/Gout/CKD prune, neuro-rheum ASSOC |
| 19 | `submissions/v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` | Intracranial Pressure | ASSOCIATION | 9 | 0 | v819: v296 final CKD/UTI neuro-rheum prune ASSOC | targeted final fallback: CKD/UTI v185, ICP/Gout/CKD prune, neuro-rheum ASSOC |
| 19 | `submissions/v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` | Gout | KEEP | 0 | 2 | v819: v296 final CKD/UTI neuro-rheum prune ASSOC | targeted final fallback: CKD/UTI v185, ICP/Gout/CKD prune, neuro-rheum ASSOC |
| 19 | `submissions/v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` | Gout | ASSOCIATION | 17 | 0 | v819: v296 final CKD/UTI neuro-rheum prune ASSOC | targeted final fallback: CKD/UTI v185, ICP/Gout/CKD prune, neuro-rheum ASSOC |
| 19 | `submissions/v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` | CKD | KEEP | 22 | 75 | v819: v296 final CKD/UTI neuro-rheum prune ASSOC | targeted final fallback: CKD/UTI v185, ICP/Gout/CKD prune, neuro-rheum ASSOC |
| 19 | `submissions/v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` | UTI | KEEP | 0 | 76 | v819: v296 final CKD/UTI neuro-rheum prune ASSOC | targeted final fallback: CKD/UTI v185, ICP/Gout/CKD prune, neuro-rheum ASSOC |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Intracranial Pressure | KEEP | 0 | 4 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Gout | KEEP | 0 | 2 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Dermatomycosis | KEEP | 57 | 21 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Pleurisy | KEEP | 0 | 12 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Bronchitis | KEEP | 0 | 8 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Thyroiditis | KEEP | 0 | 2 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Nasopharyngeal Carcinoma | KEEP | 5 | 18 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | CKD | KEEP | 22 | 75 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Hypothyroidism | KEEP | 0 | 6 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Hematemesis | KEEP | 0 | 4 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Heart Failure | KEEP | 6 | 31 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Hypergonadism | KEEP | 0 | 11 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | UTI | KEEP | 0 | 86 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Diabetes | KEEP | 232 | 71 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Interstitial Lung Disease | KEEP | 9 | 9 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Hypoparathyroidism | KEEP | 0 | 8 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Hyperthyroidism | KEEP | 0 | 12 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |
| 20 | `submissions/v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` | Pneumonia | KEEP | 1 | 53 | v820: v296 final v185 hidden add broad private prune | private-only final fallback: hidden keyword KEEP adds plus broad private KEEP prune, ASSOC/DIFF empty |

## Exact Code Changes

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - CKD / KEEP

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Hypothyroidism / KEEP

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (0): none
- Removed (26): `E00` - Congenital iodine-deficiency syndrome<br>`E000` - Congenital iodine-deficiency syndrome, neurological type<br>`E001` - Congenital iodine-deficiency syndrome, myxedematous type<br>`E002` - Congenital iodine-deficiency syndrome, mixed type<br>`E009` - Congenital iodine-deficiency syndrome, unspecified<br>`E02` - Subclinical iodine-deficiency hypothyroidism<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>... +8 more

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - UTI / KEEP

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Diabetes / KEEP

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Hyperthyroidism / KEEP

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (0): none
- Removed (49): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>... +31 more

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 1. `v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v801: v296 final med+v185 zero thyroid highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Bronchitis / KEEP

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (0): none
- Removed (33): `J04` - Acute laryngitis and tracheitis<br>`J0410` - Acute tracheitis without obstruction<br>`J0411` - Acute tracheitis with obstruction<br>`J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J21` - Acute bronchiolitis<br>`J210` - Acute bronchiolitis due to respiratory syncytial virus<br>`J211` - Acute bronchiolitis due to human metapneumovirus<br>`J218` - Acute bronchiolitis due to other specified organisms<br>... +15 more

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - CKD / KEEP

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - UTI / KEEP

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Diabetes / KEEP

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (0): none
- Removed (42): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent<br>`J84` - Other interstitial pulmonary diseases<br>`J840` - Alveolar and parieto-alveolar conditions<br>`J8401` - Alveolar proteinosis<br>`J8402` - Pulmonary alveolar microlithiasis<br>`J8403` - Idiopathic pulmonary hemosiderosis<br>`J8409` - Other alveolar and parieto-alveolar conditions<br>`J841` - Other interstitial pulmonary diseases with fibrosis<br>`J8410` - Pulmonary fibrosis, unspecified<br>`J8411` - Idiopathic interstitial pneumonia<br>... +24 more

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 2. `v802_v296_final_med_v185_zero_pulmonary_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v802: v296 final med+v185 zero pulmonary highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Dermatomycosis / KEEP

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (0): none
- Removed (38): `B35` - Dermatophytosis<br>`B350` - Tinea barbae and tinea capitis<br>`B351` - Tinea unguium<br>`B352` - Tinea manuum<br>`B353` - Tinea pedis<br>`B354` - Tinea corporis<br>`B355` - Tinea imbricata<br>`B356` - Tinea cruris<br>`B358` - Other dermatophytoses<br>`B359` - Dermatophytosis, unspecified<br>`B36` - Other superficial mycoses<br>`B360` - Pityriasis versicolor<br>`B361` - Tinea nigra<br>`B362` - White piedra<br>`B363` - Black piedra<br>`B368` - Other specified superficial mycoses<br>`B369` - Superficial mycosis, unspecified<br>`B37` - Candidiasis<br>... +20 more

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (0): none
- Removed (42): `C10` - Malignant neoplasm of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C11` - Malignant neoplasm of nasopharynx<br>`C110` - Malignant neoplasm of superior wall of nasopharynx<br>`C111` - Malignant neoplasm of posterior wall of nasopharynx<br>`C112` - Malignant neoplasm of lateral wall of nasopharynx<br>`C113` - Malignant neoplasm of anterior wall of nasopharynx<br>`C118` - Malignant neoplasm of overlapping sites of nasopharynx<br>`C119` - Malignant neoplasm of nasopharynx, unspecified<br>`C13` - Malignant neoplasm of hypopharynx<br>`C132` - Malignant neoplasm of posterior wall of hypopharynx<br>`C30` - Malignant neoplasm of nasal cavity and middle ear<br>`C300` - Malignant neoplasm of nasal cavity<br>`C32` - Malignant neoplasm of larynx<br>`C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`C47` - Malignant neoplasm of peripheral nerves and autonomic nervous system<br>... +24 more

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - CKD / KEEP

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - UTI / KEEP

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Diabetes / KEEP

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 3. `v803_v296_final_med_v185_zero_derm_npc_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v803: v296 final med+v185 zero Derm/NPC highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Dermatomycosis / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (57): `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>`B380` - Acute pulmonary coccidioidomycosis<br>`B381` - Chronic pulmonary coccidioidomycosis<br>`B382` - Pulmonary coccidioidomycosis, unspecified<br>`B383` - Cutaneous coccidioidomycosis<br>`B384` - Coccidioidomycosis meningitis<br>`B387` - Disseminated coccidioidomycosis<br>`B388` - Other forms of coccidioidomycosis<br>`B3881` - Prostatic coccidioidomycosis<br>`B3889` - Other forms of coccidioidomycosis<br>`B389` - Coccidioidomycosis, unspecified<br>... +39 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (5): `A361` - Nasopharyngeal diphtheria<br>`B873` - Nasopharyngeal myiasis<br>`J00` - Acute nasopharyngitis [common cold]<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J311` - Chronic nasopharyngitis
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - CKD / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Heart Failure / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (6): `O2912` - Cardiac failure due to anesthesia during pregnancy<br>`O29121` - Cardiac failure due to anesthesia during pregnancy, first trimester<br>`O29122` - Cardiac failure due to anesthesia during pregnancy, second trimester<br>`O29123` - Cardiac failure due to anesthesia during pregnancy, third trimester<br>`O29129` - Cardiac failure due to anesthesia during pregnancy, unspecified trimester<br>`P290` - Neonatal cardiac failure
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - UTI / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Diabetes / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (9): `J60` - Coalworker's pneumoconiosis<br>`J61` - Pneumoconiosis due to asbestos and other mineral fibers<br>`J62` - Pneumoconiosis due to dust containing silica<br>`J620` - Pneumoconiosis due to talc dust<br>`J628` - Pneumoconiosis due to other dust containing silica<br>`J63` - Pneumoconiosis due to other inorganic dusts<br>`J636` - Pneumoconiosis due to other specified inorganic dusts<br>`J64` - Unspecified pneumoconiosis<br>`J65` - Pneumoconiosis associated with tuberculosis
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 4. `v804_v296_final_med_v185_add_hidden_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v804: v296 final med+v185 add hidden highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - CKD / KEEP

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - UTI / KEEP

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (0): none
- Removed (86): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +68 more

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Diabetes / KEEP

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (70): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>... +52 more

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 5. `v805_v296_final_med_v185_prune_renal_metabolic_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v805: v296 final med+v185 renal/metabolic prune highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - CKD / KEEP

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Heart Failure / KEEP

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - UTI / KEEP

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Diabetes / KEEP

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 6. `v806_v296_final_med_v185_prune_cardio_pulm_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v806: v296 final med+v185 cardio/pulm prune highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Thyroiditis / KEEP

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - CKD / KEEP

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Hypothyroidism / KEEP

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - UTI / KEEP

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Diabetes / KEEP

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Hyperthyroidism / KEEP

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 7. `v807_v296_final_med_v185_prune_thyroid_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v807: v296 final med+v185 thyroid prune highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Gout / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Pleurisy / KEEP

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Bronchitis / KEEP

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - CKD / KEEP

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - CKD / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - UTI / KEEP

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Diabetes / KEEP

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Pneumonia / KEEP

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (53): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>... +35 more
### 8. `v808_v296_final_med_v185_prune_resp_highconf_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v808: v296 final med+v185 respiratory prune highconf ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - CKD / KEEP

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Hypothyroidism / KEEP

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (0): none
- Removed (26): `E00` - Congenital iodine-deficiency syndrome<br>`E000` - Congenital iodine-deficiency syndrome, neurological type<br>`E001` - Congenital iodine-deficiency syndrome, myxedematous type<br>`E002` - Congenital iodine-deficiency syndrome, mixed type<br>`E009` - Congenital iodine-deficiency syndrome, unspecified<br>`E02` - Subclinical iodine-deficiency hypothyroidism<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>... +8 more

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - UTI / KEEP

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Diabetes / KEEP

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Hyperthyroidism / KEEP

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (0): none
- Removed (49): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>... +31 more

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Pneumonia / KEEP

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 9. `v809_v296_final_v185_zero_thyroid_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v809: v296 final v185 zero thyroid broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Bronchitis / KEEP

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (0): none
- Removed (33): `J04` - Acute laryngitis and tracheitis<br>`J0410` - Acute tracheitis without obstruction<br>`J0411` - Acute tracheitis with obstruction<br>`J20` - Acute bronchitis<br>`J200` - Acute bronchitis due to Mycoplasma pneumoniae<br>`J201` - Acute bronchitis due to Hemophilus influenzae<br>`J202` - Acute bronchitis due to streptococcus<br>`J203` - Acute bronchitis due to coxsackievirus<br>`J204` - Acute bronchitis due to parainfluenza virus<br>`J205` - Acute bronchitis due to respiratory syncytial virus<br>`J206` - Acute bronchitis due to rhinovirus<br>`J207` - Acute bronchitis due to echovirus<br>`J208` - Acute bronchitis due to other specified organisms<br>`J209` - Acute bronchitis, unspecified<br>`J21` - Acute bronchiolitis<br>`J210` - Acute bronchiolitis due to respiratory syncytial virus<br>`J211` - Acute bronchiolitis due to human metapneumovirus<br>`J218` - Acute bronchiolitis due to other specified organisms<br>... +15 more

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - CKD / KEEP

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - UTI / KEEP

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Diabetes / KEEP

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (0): none
- Removed (42): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent<br>`J84` - Other interstitial pulmonary diseases<br>`J840` - Alveolar and parieto-alveolar conditions<br>`J8401` - Alveolar proteinosis<br>`J8402` - Pulmonary alveolar microlithiasis<br>`J8403` - Idiopathic pulmonary hemosiderosis<br>`J8409` - Other alveolar and parieto-alveolar conditions<br>`J841` - Other interstitial pulmonary diseases with fibrosis<br>`J8410` - Pulmonary fibrosis, unspecified<br>`J8411` - Idiopathic interstitial pneumonia<br>... +24 more

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Pneumonia / KEEP

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 10. `v810_v296_final_v185_zero_pulmonary_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v810: v296 final v185 zero pulmonary broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Dermatomycosis / KEEP

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (0): none
- Removed (38): `B35` - Dermatophytosis<br>`B350` - Tinea barbae and tinea capitis<br>`B351` - Tinea unguium<br>`B352` - Tinea manuum<br>`B353` - Tinea pedis<br>`B354` - Tinea corporis<br>`B355` - Tinea imbricata<br>`B356` - Tinea cruris<br>`B358` - Other dermatophytoses<br>`B359` - Dermatophytosis, unspecified<br>`B36` - Other superficial mycoses<br>`B360` - Pityriasis versicolor<br>`B361` - Tinea nigra<br>`B362` - White piedra<br>`B363` - Black piedra<br>`B368` - Other specified superficial mycoses<br>`B369` - Superficial mycosis, unspecified<br>`B37` - Candidiasis<br>... +20 more

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (0): none
- Removed (42): `C10` - Malignant neoplasm of oropharynx<br>`C103` - Malignant neoplasm of posterior wall of oropharynx<br>`C11` - Malignant neoplasm of nasopharynx<br>`C110` - Malignant neoplasm of superior wall of nasopharynx<br>`C111` - Malignant neoplasm of posterior wall of nasopharynx<br>`C112` - Malignant neoplasm of lateral wall of nasopharynx<br>`C113` - Malignant neoplasm of anterior wall of nasopharynx<br>`C118` - Malignant neoplasm of overlapping sites of nasopharynx<br>`C119` - Malignant neoplasm of nasopharynx, unspecified<br>`C13` - Malignant neoplasm of hypopharynx<br>`C132` - Malignant neoplasm of posterior wall of hypopharynx<br>`C30` - Malignant neoplasm of nasal cavity and middle ear<br>`C300` - Malignant neoplasm of nasal cavity<br>`C32` - Malignant neoplasm of larynx<br>`C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`C47` - Malignant neoplasm of peripheral nerves and autonomic nervous system<br>... +24 more

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - CKD / KEEP

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - UTI / KEEP

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Diabetes / KEEP

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Pneumonia / KEEP

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 11. `v811_v296_final_v185_zero_derm_npc_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v811: v296 final v185 zero Derm/NPC broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Dermatomycosis / KEEP

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (57): `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>`B380` - Acute pulmonary coccidioidomycosis<br>`B381` - Chronic pulmonary coccidioidomycosis<br>`B382` - Pulmonary coccidioidomycosis, unspecified<br>`B383` - Cutaneous coccidioidomycosis<br>`B384` - Coccidioidomycosis meningitis<br>`B387` - Disseminated coccidioidomycosis<br>`B388` - Other forms of coccidioidomycosis<br>`B3881` - Prostatic coccidioidomycosis<br>`B3889` - Other forms of coccidioidomycosis<br>`B389` - Coccidioidomycosis, unspecified<br>... +39 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (5): `A361` - Nasopharyngeal diphtheria<br>`B873` - Nasopharyngeal myiasis<br>`J00` - Acute nasopharyngitis [common cold]<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J311` - Chronic nasopharyngitis
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - CKD / KEEP

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Heart Failure / KEEP

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (6): `O2912` - Cardiac failure due to anesthesia during pregnancy<br>`O29121` - Cardiac failure due to anesthesia during pregnancy, first trimester<br>`O29122` - Cardiac failure due to anesthesia during pregnancy, second trimester<br>`O29123` - Cardiac failure due to anesthesia during pregnancy, third trimester<br>`O29129` - Cardiac failure due to anesthesia during pregnancy, unspecified trimester<br>`P290` - Neonatal cardiac failure
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - UTI / KEEP

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Diabetes / KEEP

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (9): `J60` - Coalworker's pneumoconiosis<br>`J61` - Pneumoconiosis due to asbestos and other mineral fibers<br>`J62` - Pneumoconiosis due to dust containing silica<br>`J620` - Pneumoconiosis due to talc dust<br>`J628` - Pneumoconiosis due to other dust containing silica<br>`J63` - Pneumoconiosis due to other inorganic dusts<br>`J636` - Pneumoconiosis due to other specified inorganic dusts<br>`J64` - Unspecified pneumoconiosis<br>`J65` - Pneumoconiosis associated with tuberculosis
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Pneumonia / KEEP

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 12. `v812_v296_final_v185_add_hidden_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v812: v296 final v185 add hidden broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - CKD / KEEP

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - UTI / KEEP

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (0): none
- Removed (86): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +68 more

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Diabetes / KEEP

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (70): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>... +52 more

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Pneumonia / KEEP

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 13. `v813_v296_final_v185_prune_renal_metabolic_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v813: v296 final v185 renal/metabolic prune broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Gout / KEEP

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - CKD / KEEP

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Hematemesis / KEEP

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Heart Failure / KEEP

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - UTI / KEEP

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Diabetes / KEEP

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Pneumonia / KEEP

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 14. `v814_v296_final_v185_prune_small_precision_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v814: v296 final v185 small precision prune broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Epistaxis / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (48): `D68` - Other coagulation defects<br>`D680` - Von Willebrand disease<br>`D6800` - Von Willebrand disease, unspecified<br>`D6801` - Von Willebrand disease, type 1<br>`D6802` - Von Willebrand disease, type 2<br>`D68020` - Von Willebrand disease, type 2A<br>`D68021` - Von Willebrand disease, type 2B<br>`D68022` - Von Willebrand disease, type 2M<br>`D68023` - Von Willebrand disease, type 2N<br>`D68029` - Von Willebrand disease, type 2, unspecified<br>`D6803` - Von Willebrand disease, type 3<br>`D6804` - Acquired von Willebrand disease<br>`D6809` - Other von Willebrand disease<br>`D681` - Hereditary factor XI deficiency<br>`D682` - Hereditary deficiency of other clotting factors<br>`D683` - Hemorrhagic disorder due to circulating anticoagulants<br>`D6831` - Hemorrhagic disorder due to intrinsic circulating anticoagulants, antibodies, or inhibitors<br>`D68311` - Acquired hemophilia<br>... +30 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Intracranial Pressure / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Gout / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Gout / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Dermatomycosis / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (21): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +3 more

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Dermatomycosis / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (137): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +119 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Pleurisy / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Bronchitis / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Thyroiditis / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (18): `C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`D00` - Carcinoma in situ of oral cavity, esophagus and stomach<br>`D000` - Carcinoma in situ of lip, oral cavity and pharynx<br>`D0000` - Carcinoma in situ of oral cavity, unspecified site<br>`D0001` - Carcinoma in situ of labial mucosa and vermilion border<br>`D0002` - Carcinoma in situ of buccal mucosa<br>`D0003` - Carcinoma in situ of gingiva and edentulous alveolar ridge<br>`D0004` - Carcinoma in situ of soft palate<br>`D0005` - Carcinoma in situ of hard palate<br>`D0006` - Carcinoma in situ of floor of mouth<br>`D0007` - Carcinoma in situ of tongue<br>`D0008` - Carcinoma in situ of pharynx<br>`D10` - Benign neoplasm of mouth and pharynx<br>`D101` - Benign neoplasm of tongue<br>`D106` - Benign neoplasm of nasopharynx<br>`D107` - Benign neoplasm of hypopharynx

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Nasopharyngeal Carcinoma / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (30): `B27` - Infectious mononucleosis<br>`B270` - Gammaherpesviral mononucleosis<br>`B2700` - Gammaherpesviral mononucleosis without complication<br>`B2701` - Gammaherpesviral mononucleosis with polyneuropathy<br>`B2702` - Gammaherpesviral mononucleosis with meningitis<br>`B2709` - Gammaherpesviral mononucleosis with other complications<br>`B271` - Cytomegaloviral mononucleosis<br>`B2710` - Cytomegaloviral mononucleosis without complications<br>`B2711` - Cytomegaloviral mononucleosis with polyneuropathy<br>`B2712` - Cytomegaloviral mononucleosis with meningitis<br>`B2719` - Cytomegaloviral mononucleosis with other complication<br>`B278` - Other infectious mononucleosis<br>`B2780` - Other infectious mononucleosis without complication<br>`B2781` - Other infectious mononucleosis with polyneuropathy<br>`B2782` - Other infectious mononucleosis with meningitis<br>`B2789` - Other infectious mononucleosis with other complication<br>`B279` - Infectious mononucleosis, unspecified<br>`B2790` - Infectious mononucleosis, unspecified without complication<br>... +12 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - CKD / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - CKD / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hypothyroidism / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hematemesis / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hematemesis / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (65): `K25` - Gastric ulcer<br>`K250` - Acute gastric ulcer with hemorrhage<br>`K251` - Acute gastric ulcer with perforation<br>`K252` - Acute gastric ulcer with both hemorrhage and perforation<br>`K253` - Acute gastric ulcer without hemorrhage or perforation<br>`K254` - Chronic or unspecified gastric ulcer with hemorrhage<br>`K255` - Chronic or unspecified gastric ulcer with perforation<br>`K256` - Chronic or unspecified gastric ulcer with both hemorrhage and perforation<br>`K257` - Chronic gastric ulcer without hemorrhage or perforation<br>`K259` - Gastric ulcer, unspecified as acute or chronic, without hemorrhage or perforation<br>`K26` - Duodenal ulcer<br>`K260` - Acute duodenal ulcer with hemorrhage<br>`K261` - Acute duodenal ulcer with perforation<br>`K262` - Acute duodenal ulcer with both hemorrhage and perforation<br>`K263` - Acute duodenal ulcer without hemorrhage or perforation<br>`K264` - Chronic or unspecified duodenal ulcer with hemorrhage<br>`K265` - Chronic or unspecified duodenal ulcer with perforation<br>`K266` - Chronic or unspecified duodenal ulcer with both hemorrhage and perforation<br>... +47 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Heart Failure / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hypergonadism / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (11): `E27` - Other disorders of adrenal gland<br>`E270` - Other adrenocortical overactivity<br>`E271` - Primary adrenocortical insufficiency<br>`E272` - Addisonian crisis<br>`E273` - Drug-induced adrenocortical insufficiency<br>`E274` - Other and unspecified adrenocortical insufficiency<br>`E2740` - Unspecified adrenocortical insufficiency<br>`E2749` - Other adrenocortical insufficiency<br>`E275` - Adrenomedullary hyperfunction<br>`E278` - Other specified disorders of adrenal gland<br>`E279` - Disorder of adrenal gland, unspecified

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - UTI / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (86): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +68 more

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - UTI / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (20): `N10` - Acute pyelonephritis<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>... +2 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Diabetes / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (71): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>... +53 more

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Diabetes / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hypoparathyroidism / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (8): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E230` - Hypopituitarism<br>`E231` - Drug-induced hypopituitarism<br>`E87` - Other disorders of fluid, electrolyte and acid-base balance<br>`E876` - Hypokalemia<br>`P71` - Transitory neonatal disorders of calcium and magnesium metabolism<br>`P714` - Transitory neonatal hypoparathyroidism

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hyperthyroidism / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Pneumonia / KEEP

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (53): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>... +35 more

### 15. `v815_v296_final_v185_broad_private_prune_broad_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v815: v296 final v185 broad private prune broad ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 16. `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 16. `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` - CKD / KEEP

- Message: v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 16. `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` - CKD / ASSOCIATION

- Message: v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC
- Added (17): `I12` - Hypertensive chronic kidney disease<br>`I120` - Hypertensive chronic kidney disease with stage 5 chronic kidney disease or end stage renal disease<br>`I129` - Hypertensive chronic kidney disease with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I13` - Hypertensive heart and chronic kidney disease<br>`I130` - Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I131` - Hypertensive heart and chronic kidney disease without heart failure<br>`I1310` - Hypertensive heart and chronic kidney disease without heart failure, with stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease<br>`I1311` - Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease<br>`I132` - Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease<br>`E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`D63` - Anemia in chronic diseases classified elsewhere<br>`D630` - Anemia in neoplastic disease<br>`D631` - Anemia in chronic kidney disease<br>`D638` - Anemia in other chronic diseases classified elsewhere
- Removed (0): none

### 16. `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` - Heart Failure / KEEP

- Message: v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC
- Added (6): `O2912` - Cardiac failure due to anesthesia during pregnancy<br>`O29121` - Cardiac failure due to anesthesia during pregnancy, first trimester<br>`O29122` - Cardiac failure due to anesthesia during pregnancy, second trimester<br>`O29123` - Cardiac failure due to anesthesia during pregnancy, third trimester<br>`O29129` - Cardiac failure due to anesthesia during pregnancy, unspecified trimester<br>`P290` - Neonatal cardiac failure
- Removed (0): none

### 16. `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` - Heart Failure / ASSOCIATION

- Message: v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC
- Added (35): `I42` - Cardiomyopathy<br>`I420` - Dilated cardiomyopathy<br>`I421` - Obstructive hypertrophic cardiomyopathy<br>`I422` - Other hypertrophic cardiomyopathy<br>`I423` - Endomyocardial (eosinophilic) disease<br>`I424` - Endocardial fibroelastosis<br>`I425` - Other restrictive cardiomyopathy<br>`I426` - Alcoholic cardiomyopathy<br>`I427` - Cardiomyopathy due to drug and external agent<br>`I428` - Other cardiomyopathies<br>`I429` - Cardiomyopathy, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>... +17 more
- Removed (0): none

### 16. `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` - UTI / KEEP

- Message: v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 16. `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` - Diabetes / ASSOCIATION

- Message: v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 16. `v816_v296_final_med_ckd_uti_add_hf_ild_cardiorenal_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v816: v296 final med CKD/UTI + HF/ILD add cardiorenal ASSOC
- Added (9): `J60` - Coalworker's pneumoconiosis<br>`J61` - Pneumoconiosis due to asbestos and other mineral fibers<br>`J62` - Pneumoconiosis due to dust containing silica<br>`J620` - Pneumoconiosis due to talc dust<br>`J628` - Pneumoconiosis due to other dust containing silica<br>`J63` - Pneumoconiosis due to other inorganic dusts<br>`J636` - Pneumoconiosis due to other specified inorganic dusts<br>`J64` - Unspecified pneumoconiosis<br>`J65` - Pneumoconiosis associated with tuberculosis
- Removed (0): none

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Dermatomycosis / KEEP

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (57): `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>`B380` - Acute pulmonary coccidioidomycosis<br>`B381` - Chronic pulmonary coccidioidomycosis<br>`B382` - Pulmonary coccidioidomycosis, unspecified<br>`B383` - Cutaneous coccidioidomycosis<br>`B384` - Coccidioidomycosis meningitis<br>`B387` - Disseminated coccidioidomycosis<br>`B388` - Other forms of coccidioidomycosis<br>`B3881` - Prostatic coccidioidomycosis<br>`B3889` - Other forms of coccidioidomycosis<br>`B389` - Coccidioidomycosis, unspecified<br>... +39 more
- Removed (0): none

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Pleurisy / ASSOCIATION

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (12): `J90` - Pleural effusion, not elsewhere classified<br>`J91` - Pleural effusion in conditions classified elsewhere<br>`J910` - Malignant pleural effusion<br>`J918` - Pleural effusion in other conditions classified elsewhere<br>`A15` - Respiratory tuberculosis<br>`A150` - Tuberculosis of lung<br>`A154` - Tuberculosis of intrathoracic lymph nodes<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A156` - Tuberculous pleurisy<br>`A157` - Primary respiratory tuberculosis<br>`A158` - Other respiratory tuberculosis<br>`A159` - Respiratory tuberculosis unspecified
- Removed (0): none

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Bronchitis / ASSOCIATION

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (4): `J44` - Other chronic obstructive pulmonary disease<br>`J440` - Chronic obstructive pulmonary disease with (acute) lower respiratory infection<br>`J441` - Chronic obstructive pulmonary disease with (acute) exacerbation<br>`J449` - Chronic obstructive pulmonary disease, unspecified
- Removed (0): none

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (5): `A361` - Nasopharyngeal diphtheria<br>`B873` - Nasopharyngeal myiasis<br>`J00` - Acute nasopharyngitis [common cold]<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J311` - Chronic nasopharyngitis
- Removed (0): none

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Diabetes / KEEP

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Interstitial Lung Disease / ASSOCIATION

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (41): `M35` - Other systemic involvement of connective tissue<br>`M350` - Sjogren syndrome<br>`M3500` - Sjogren syndrome, unspecified<br>`M3501` - Sjogren syndrome with keratoconjunctivitis<br>`M3502` - Sjogren syndrome with lung involvement<br>`M3503` - Sjogren syndrome with myopathy<br>`M3504` - Sjogren syndrome with tubulo-interstitial nephropathy<br>`M3505` - Sjogren syndrome with inflammatory arthritis<br>`M3506` - Sjogren syndrome with peripheral nervous system involvement<br>`M3507` - Sjogren syndrome with central nervous system involvement<br>`M3508` - Sjogren syndrome with gastrointestinal involvement<br>`M3509` - Sjogren syndrome with other organ involvement<br>`M350A` - Sjogren syndrome with glomerular disease<br>`M350B` - Sjogren syndrome with vasculitis<br>`M350C` - Sjogren syndrome with dental involvement<br>`M351` - Other overlap syndromes<br>`M352` - Behcet's disease<br>`M353` - Polymyalgia rheumatica<br>... +23 more
- Removed (0): none

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Pneumonia / KEEP

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 17. `v817_v296_final_med_diab_pneu_add_derm_npc_pulmonary_assoc.csv` - Pneumonia / ASSOCIATION

- Message: v817: v296 final med Diabetes/Pneumonia + Derm/NPC add pulmonary ASSOC
- Added (36): `A41` - Other sepsis<br>`A410` - Sepsis due to Staphylococcus aureus<br>`A4101` - Sepsis due to Methicillin susceptible Staphylococcus aureus<br>`A4102` - Sepsis due to Methicillin resistant Staphylococcus aureus<br>`A411` - Sepsis due to other specified staphylococcus<br>`A412` - Sepsis due to unspecified staphylococcus<br>`A413` - Sepsis due to Hemophilus influenzae<br>`A414` - Sepsis due to anaerobes<br>`A415` - Sepsis due to other Gram-negative organisms<br>`A4150` - Gram-negative sepsis, unspecified<br>`A4151` - Sepsis due to Escherichia coli [E. coli]<br>`A4152` - Sepsis due to Pseudomonas<br>`A4153` - Sepsis due to Serratia<br>`A4159` - Other Gram-negative sepsis<br>`A418` - Other specified sepsis<br>`A4181` - Sepsis due to Enterococcus<br>`A4189` - Other specified sepsis<br>`A419` - Sepsis, unspecified organism<br>... +18 more
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Enlarged Mediastinum / KEEP

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (4): `C37` - Malignant neoplasm of thymus<br>`D384` - Neoplasm of uncertain behavior of thymus<br>`C771` - Secondary and unspecified malignant neoplasm of intrathoracic lymph nodes<br>`A154` - Tuberculosis of intrathoracic lymph nodes
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Latent Adrenal Insufficiency / ASSOCIATION

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (19): `E31` - Polyglandular dysfunction<br>`E310` - Autoimmune polyglandular failure<br>`E311` - Polyglandular hyperfunction<br>`E312` - Multiple endocrine neoplasia [MEN] syndromes<br>`E3120` - Multiple endocrine neoplasia [MEN] syndrome, unspecified<br>`E3121` - Multiple endocrine neoplasia [MEN] type I<br>`E3122` - Multiple endocrine neoplasia [MEN] type IIA<br>`E3123` - Multiple endocrine neoplasia [MEN] type IIB<br>`E318` - Other polyglandular dysfunction<br>`E319` - Polyglandular dysfunction, unspecified<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>... +1 more
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Thyroiditis / ASSOCIATION

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (31): `E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>`E0520` - Thyrotoxicosis with toxic multinodular goiter without thyrotoxic crisis or storm<br>... +13 more
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - CKD / KEEP

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Hypothyroidism / KEEP

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (0): none
- Removed (26): `E00` - Congenital iodine-deficiency syndrome<br>`E000` - Congenital iodine-deficiency syndrome, neurological type<br>`E001` - Congenital iodine-deficiency syndrome, myxedematous type<br>`E002` - Congenital iodine-deficiency syndrome, mixed type<br>`E009` - Congenital iodine-deficiency syndrome, unspecified<br>`E02` - Subclinical iodine-deficiency hypothyroidism<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances<br>`E033` - Postinfectious hypothyroidism<br>`E034` - Atrophy of thyroid (acquired)<br>`E035` - Myxedema coma<br>`E038` - Other specified hypothyroidism<br>`E039` - Hypothyroidism, unspecified<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>... +8 more

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Hypothyroidism / ASSOCIATION

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (19): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E010` - Iodine-deficiency related diffuse (endemic) goiter<br>`E011` - Iodine-deficiency related multinodular (endemic) goiter<br>`E012` - Iodine-deficiency related (endemic) goiter, unspecified<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>... +1 more
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - UTI / KEEP

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Diabetes / KEEP

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (13): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`P70` - Transitory disorders of carbohydrate metabolism specific to newborn<br>`P701` - Syndrome of infant of a diabetic mother<br>`Z13` - Encounter for screening for other diseases and disorders<br>`Z79` - Long term (current) drug therapy<br>`Z794` - Long term (current) use of insulin<br>`Z7985` - Long-term (current) use of injectable non-insulin antidiabetic drugs<br>`Z83` - Family history of other specific disorders<br>`Z86` - Personal history of certain other diseases<br>`Z8631` - Personal history of diabetic foot ulcer<br>`Z8632` - Personal history of gestational diabetes

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Diabetes / ASSOCIATION

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (116): `E112` - Type 2 diabetes mellitus with kidney complications<br>`E1121` - Type 2 diabetes mellitus with diabetic nephropathy<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1129` - Type 2 diabetes mellitus with other diabetic kidney complication<br>`E113` - Type 2 diabetes mellitus with ophthalmic complications<br>`E1131` - Type 2 diabetes mellitus with unspecified diabetic retinopathy<br>`E11311` - Type 2 diabetes mellitus with unspecified diabetic retinopathy with macular edema<br>`E11319` - Type 2 diabetes mellitus with unspecified diabetic retinopathy without macular edema<br>`E1132` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy<br>`E11321` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema<br>`E113211` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>`E113212` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, left eye<br>`E113213` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, bilateral<br>`E113219` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy with macular edema, unspecified eye<br>`E11329` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema<br>`E113291` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, right eye<br>`E113292` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, left eye<br>`E113293` - Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy without macular edema, bilateral<br>... +98 more
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Hypoparathyroidism / ASSOCIATION

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (1): `E8351` - Hypocalcemia
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Hyperparathyroidism / ASSOCIATION

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (8): `E8352` - Hypercalcemia<br>`N25` - Disorders resulting from impaired renal tubular function<br>`N250` - Renal osteodystrophy<br>`N251` - Nephrogenic diabetes insipidus<br>`N258` - Other disorders resulting from impaired renal tubular function<br>`N2581` - Secondary hyperparathyroidism of renal origin<br>`N2589` - Other disorders resulting from impaired renal tubular function<br>`N259` - Disorder resulting from impaired renal tubular function, unspecified
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Hyperthyroidism / KEEP

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (0): none
- Removed (49): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`E05` - Thyrotoxicosis [hyperthyroidism]<br>`E050` - Thyrotoxicosis with diffuse goiter<br>`E0500` - Thyrotoxicosis with diffuse goiter without thyrotoxic crisis or storm<br>`E0501` - Thyrotoxicosis with diffuse goiter with thyrotoxic crisis or storm<br>`E051` - Thyrotoxicosis with toxic single thyroid nodule<br>`E0510` - Thyrotoxicosis with toxic single thyroid nodule without thyrotoxic crisis or storm<br>`E0511` - Thyrotoxicosis with toxic single thyroid nodule with thyrotoxic crisis or storm<br>`E052` - Thyrotoxicosis with toxic multinodular goiter<br>... +31 more

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Hyperthyroidism / ASSOCIATION

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (21): `E06` - Thyroiditis<br>`E060` - Acute thyroiditis<br>`E061` - Subacute thyroiditis<br>`E062` - Chronic thyroiditis with transient thyrotoxicosis<br>`E063` - Autoimmune thyroiditis<br>`E064` - Drug-induced thyroiditis<br>`E065` - Other chronic thyroiditis<br>`E069` - Thyroiditis, unspecified<br>`I48` - Atrial fibrillation and flutter<br>`I480` - Paroxysmal atrial fibrillation<br>`I481` - Persistent atrial fibrillation<br>`I4811` - Longstanding persistent atrial fibrillation<br>`I4819` - Other persistent atrial fibrillation<br>`I482` - Chronic atrial fibrillation<br>`I4820` - Chronic atrial fibrillation, unspecified<br>`I4821` - Permanent atrial fibrillation<br>`I483` - Typical atrial flutter<br>`I484` - Atypical atrial flutter<br>... +3 more
- Removed (0): none

### 18. `v818_v296_final_med_v185_zero_endocrine_endocrine_assoc.csv` - Pneumonia / KEEP

- Message: v818: v296 final med+v185 zero endocrine ASSOC
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (28): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>`B06` - Rubella [German measles]<br>`B77` - Ascariasis<br>`B95` - Streptococcus, Staphylococcus, and Enterococcus as the cause of diseases classified elsewhere<br>`B96` - Other bacterial agents as the cause of diseases classified elsewhere<br>`J09` - Influenza due to certain identified influenza viruses<br>`J10` - Influenza due to other identified influenza virus<br>`J11` - Influenza due to unidentified influenza virus<br>`J20` - Acute bronchitis<br>... +10 more

### 19. `v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` - Intracranial Pressure / KEEP

- Message: v819: v296 final CKD/UTI neuro-rheum prune ASSOC
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 19. `v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` - Intracranial Pressure / ASSOCIATION

- Message: v819: v296 final CKD/UTI neuro-rheum prune ASSOC
- Added (9): `G91` - Hydrocephalus<br>`G910` - Communicating hydrocephalus<br>`G911` - Obstructive hydrocephalus<br>`G912` - (Idiopathic) normal pressure hydrocephalus<br>`G913` - Post-traumatic hydrocephalus, unspecified<br>`G914` - Hydrocephalus in diseases classified elsewhere<br>`G918` - Other hydrocephalus<br>`G919` - Hydrocephalus, unspecified<br>`H4711` - Papilledema associated with increased intracranial pressure
- Removed (0): none

### 19. `v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` - Gout / KEEP

- Message: v819: v296 final CKD/UTI neuro-rheum prune ASSOC
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 19. `v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` - Gout / ASSOCIATION

- Message: v819: v296 final CKD/UTI neuro-rheum prune ASSOC
- Added (17): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease<br>`E791` - Lesch-Nyhan syndrome<br>`E792` - Myoadenylate deaminase deficiency<br>`E798` - Other disorders of purine and pyrimidine metabolism<br>`E799` - Disorder of purine and pyrimidine metabolism, unspecified<br>`N18` - Chronic kidney disease (CKD)<br>`N181` - Chronic kidney disease, stage 1<br>`N182` - Chronic kidney disease, stage 2 (mild)<br>`N183` - Chronic kidney disease, stage 3 (moderate)<br>`N1830` - Chronic kidney disease, stage 3 unspecified<br>`N1831` - Chronic kidney disease, stage 3a<br>`N1832` - Chronic kidney disease, stage 3b<br>`N184` - Chronic kidney disease, stage 4 (severe)<br>`N185` - Chronic kidney disease, stage 5<br>`N186` - End stage renal disease<br>`N189` - Chronic kidney disease, unspecified
- Removed (0): none

### 19. `v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` - CKD / KEEP

- Message: v819: v296 final CKD/UTI neuro-rheum prune ASSOC
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 19. `v819_v296_final_v185_ckd_uti_gout_ckd_neuro_assoc.csv` - UTI / KEEP

- Message: v819: v296 final CKD/UTI neuro-rheum prune ASSOC
- Added (0): none
- Removed (76): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +58 more

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Intracranial Pressure / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (4): `G94` - Other disorders of brain in diseases classified elsewhere<br>`G96` - Other disorders of central nervous system<br>`G9681` - Intracranial hypotension<br>`G96811` - Intracranial hypotension, spontaneous

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Gout / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (2): `E79` - Disorders of purine and pyrimidine metabolism<br>`E790` - Hyperuricemia without signs of inflammatory arthritis and tophaceous disease

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Dermatomycosis / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (57): `A42` - Actinomycosis<br>`A420` - Pulmonary actinomycosis<br>`A421` - Abdominal actinomycosis<br>`A422` - Cervicofacial actinomycosis<br>`A428` - Other forms of actinomycosis<br>`A4289` - Other forms of actinomycosis<br>`A429` - Actinomycosis, unspecified<br>`B38` - Coccidioidomycosis<br>`B380` - Acute pulmonary coccidioidomycosis<br>`B381` - Chronic pulmonary coccidioidomycosis<br>`B382` - Pulmonary coccidioidomycosis, unspecified<br>`B383` - Cutaneous coccidioidomycosis<br>`B384` - Coccidioidomycosis meningitis<br>`B387` - Disseminated coccidioidomycosis<br>`B388` - Other forms of coccidioidomycosis<br>`B3881` - Prostatic coccidioidomycosis<br>`B3889` - Other forms of coccidioidomycosis<br>`B389` - Coccidioidomycosis, unspecified<br>... +39 more
- Removed (21): `B37` - Candidiasis<br>`B370` - Candidal stomatitis<br>`B371` - Pulmonary candidiasis<br>`B372` - Candidiasis of skin and nail<br>`B373` - Candidiasis of vulva and vagina<br>`B3731` - Acute candidiasis of vulva and vagina<br>`B3732` - Chronic candidiasis of vulva and vagina<br>`B374` - Candidiasis of other urogenital sites<br>`B3741` - Candidal cystitis and urethritis<br>`B3742` - Candidal balanitis<br>`B3749` - Other urogenital candidiasis<br>`B375` - Candidal meningitis<br>`B376` - Candidal endocarditis<br>`B377` - Candidal sepsis<br>`B378` - Candidiasis of other sites<br>`B3781` - Candidal esophagitis<br>`B3782` - Candidal enteritis<br>`B3783` - Candidal cheilitis<br>... +3 more

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Pleurisy / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (12): `J950` - Tracheostomy complications<br>`R09` - Other symptoms and signs involving the circulatory and respiratory system<br>`R090` - Asphyxia and hypoxemia<br>`R0901` - Asphyxia<br>`R0902` - Hypoxemia<br>`R091` - Pleurisy<br>`R092` - Respiratory arrest<br>`R093` - Abnormal sputum<br>`R098` - Other specified symptoms and signs involving the circulatory and respiratory systems<br>`R0981` - Nasal congestion<br>`R0982` - Postnasal drip<br>`R0989` - Other specified symptoms and signs involving the circulatory and respiratory systems

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Bronchitis / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (8): `J43` - Emphysema<br>`J430` - Unilateral pulmonary emphysema [MacLeod's syndrome]<br>`J431` - Panlobular emphysema<br>`J432` - Centrilobular emphysema<br>`J438` - Other emphysema<br>`J439` - Emphysema, unspecified<br>`J68` - Respiratory conditions due to inhalation of chemicals, gases, fumes and vapors<br>`J680` - Bronchitis and pneumonitis due to chemicals, gases, fumes and vapors

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Thyroiditis / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (2): `E031` - Congenital hypothyroidism without goiter<br>`E032` - Hypothyroidism due to medicaments and other exogenous substances

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Nasopharyngeal Carcinoma / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (5): `A361` - Nasopharyngeal diphtheria<br>`B873` - Nasopharyngeal myiasis<br>`J00` - Acute nasopharyngitis [common cold]<br>`J31` - Chronic rhinitis, nasopharyngitis and pharyngitis<br>`J311` - Chronic nasopharyngitis
- Removed (18): `C44` - Other and unspecified malignant neoplasm of skin<br>`C44311` - Basal cell carcinoma of skin of nose<br>`C44321` - Squamous cell carcinoma of skin of nose<br>`D00` - Carcinoma in situ of oral cavity, esophagus and stomach<br>`D000` - Carcinoma in situ of lip, oral cavity and pharynx<br>`D0000` - Carcinoma in situ of oral cavity, unspecified site<br>`D0001` - Carcinoma in situ of labial mucosa and vermilion border<br>`D0002` - Carcinoma in situ of buccal mucosa<br>`D0003` - Carcinoma in situ of gingiva and edentulous alveolar ridge<br>`D0004` - Carcinoma in situ of soft palate<br>`D0005` - Carcinoma in situ of hard palate<br>`D0006` - Carcinoma in situ of floor of mouth<br>`D0007` - Carcinoma in situ of tongue<br>`D0008` - Carcinoma in situ of pharynx<br>`D10` - Benign neoplasm of mouth and pharynx<br>`D101` - Benign neoplasm of tongue<br>`D106` - Benign neoplasm of nasopharynx<br>`D107` - Benign neoplasm of hypopharynx

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - CKD / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (22): `D631` - Anemia in chronic kidney disease<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0922` - Drug or chemical induced diabetes mellitus with diabetic chronic kidney disease<br>`E1022` - Type 1 diabetes mellitus with diabetic chronic kidney disease<br>`E1122` - Type 2 diabetes mellitus with diabetic chronic kidney disease<br>`E1322` - Other specified diabetes mellitus with diabetic chronic kidney disease<br>`O102` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1021` - Pre-existing hypertensive chronic kidney disease complicating pregnancy<br>`O10211` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, first trimester<br>`O10212` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, second trimester<br>`O10213` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester<br>`O10219` - Pre-existing hypertensive chronic kidney disease complicating pregnancy, unspecified trimester<br>`O1022` - Pre-existing hypertensive chronic kidney disease complicating childbirth<br>`O1023` - Pre-existing hypertensive chronic kidney disease complicating the puerperium<br>`O103` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, childbirth and the puerperium<br>`O1031` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy<br>`O10311` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, first trimester<br>`O10312` - Pre-existing hypertensive heart and chronic kidney disease complicating pregnancy, second trimester<br>... +4 more
- Removed (75): `I25` - Chronic ischemic heart disease<br>`I50` - Heart failure<br>`I5032` - Chronic diastolic (congestive) heart failure<br>`I50812` - Chronic right heart failure<br>`N00` - Acute nephritic syndrome<br>`N007` - Acute nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03` - Chronic nephritic syndrome<br>`N030` - Chronic nephritic syndrome with minor glomerular abnormality<br>`N031` - Chronic nephritic syndrome with focal and segmental glomerular lesions<br>`N032` - Chronic nephritic syndrome with diffuse membranous glomerulonephritis<br>`N033` - Chronic nephritic syndrome with diffuse mesangial proliferative glomerulonephritis<br>`N034` - Chronic nephritic syndrome with diffuse endocapillary proliferative glomerulonephritis<br>`N035` - Chronic nephritic syndrome with diffuse mesangiocapillary glomerulonephritis<br>`N036` - Chronic nephritic syndrome with dense deposit disease<br>`N037` - Chronic nephritic syndrome with diffuse crescentic glomerulonephritis<br>`N03A` - Chronic nephritic syndrome with C3 glomerulonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>... +57 more

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Hypothyroidism / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (6): `E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Hematemesis / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (4): `K660` - Peritoneal adhesions (postprocedural) (postinfection)<br>`K661` - Hemoperitoneum<br>`R36` - Urethral discharge<br>`R361` - Hematospermia

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Heart Failure / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (6): `O2912` - Cardiac failure due to anesthesia during pregnancy<br>`O29121` - Cardiac failure due to anesthesia during pregnancy, first trimester<br>`O29122` - Cardiac failure due to anesthesia during pregnancy, second trimester<br>`O29123` - Cardiac failure due to anesthesia during pregnancy, third trimester<br>`O29129` - Cardiac failure due to anesthesia during pregnancy, unspecified trimester<br>`P290` - Neonatal cardiac failure
- Removed (31): `I97` - Intraoperative and postprocedural complications and disorders of circulatory system, not elsewhere classified<br>`I970` - Postcardiotomy syndrome<br>`I971` - Other postprocedural cardiac functional disturbances<br>`I9711` - Postprocedural cardiac insufficiency<br>`I97110` - Postprocedural cardiac insufficiency following cardiac surgery<br>`I97111` - Postprocedural cardiac insufficiency following other surgery<br>`I9712` - Postprocedural cardiac arrest<br>`I97120` - Postprocedural cardiac arrest following cardiac surgery<br>`I97121` - Postprocedural cardiac arrest following other surgery<br>`I9713` - Postprocedural heart failure<br>`I97130` - Postprocedural heart failure following cardiac surgery<br>`I97131` - Postprocedural heart failure following other surgery<br>`I9719` - Other postprocedural cardiac functional disturbances<br>`I97190` - Other postprocedural cardiac functional disturbances following cardiac surgery<br>`I97191` - Other postprocedural cardiac functional disturbances following other surgery<br>`I972` - Postmastectomy lymphedema syndrome<br>`I973` - Postprocedural hypertension<br>`I974` - Intraoperative hemorrhage and hematoma of a circulatory system organ or structure complicating a procedure<br>... +13 more

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Hypergonadism / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (11): `E27` - Other disorders of adrenal gland<br>`E270` - Other adrenocortical overactivity<br>`E271` - Primary adrenocortical insufficiency<br>`E272` - Addisonian crisis<br>`E273` - Drug-induced adrenocortical insufficiency<br>`E274` - Other and unspecified adrenocortical insufficiency<br>`E2740` - Unspecified adrenocortical insufficiency<br>`E2749` - Other adrenocortical insufficiency<br>`E275` - Adrenomedullary hyperfunction<br>`E278` - Other specified disorders of adrenal gland<br>`E279` - Disorder of adrenal gland, unspecified

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - UTI / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (86): `N10` - Acute pyelonephritis<br>`N11` - Chronic tubulo-interstitial nephritis<br>`N110` - Nonobstructive reflux-associated chronic pyelonephritis<br>`N111` - Chronic obstructive pyelonephritis<br>`N118` - Other chronic tubulo-interstitial nephritis<br>`N119` - Chronic tubulo-interstitial nephritis, unspecified<br>`N12` - Tubulo-interstitial nephritis, not specified as acute or chronic<br>`N30` - Cystitis<br>`N300` - Acute cystitis<br>`N3000` - Acute cystitis without hematuria<br>`N3001` - Acute cystitis with hematuria<br>`N301` - Interstitial cystitis (chronic)<br>`N3010` - Interstitial cystitis (chronic) without hematuria<br>`N3011` - Interstitial cystitis (chronic) with hematuria<br>`N302` - Other chronic cystitis<br>`N3020` - Other chronic cystitis without hematuria<br>`N3021` - Other chronic cystitis with hematuria<br>`N303` - Trigonitis<br>... +68 more

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Diabetes / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (232): `E08` - Diabetes mellitus due to underlying condition<br>`E080` - Diabetes mellitus due to underlying condition with hyperosmolarity<br>`E0800` - Diabetes mellitus due to underlying condition with hyperosmolarity without nonketotic hyperglycemic-hyperosmolar coma (NKHHC)<br>`E0801` - Diabetes mellitus due to underlying condition with hyperosmolarity with coma<br>`E081` - Diabetes mellitus due to underlying condition with ketoacidosis<br>`E0810` - Diabetes mellitus due to underlying condition with ketoacidosis without coma<br>`E0811` - Diabetes mellitus due to underlying condition with ketoacidosis with coma<br>`E082` - Diabetes mellitus due to underlying condition with kidney complications<br>`E0821` - Diabetes mellitus due to underlying condition with diabetic nephropathy<br>`E0822` - Diabetes mellitus due to underlying condition with diabetic chronic kidney disease<br>`E0829` - Diabetes mellitus due to underlying condition with other diabetic kidney complication<br>`E083` - Diabetes mellitus due to underlying condition with ophthalmic complications<br>`E0831` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy<br>`E08311` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy with macular edema<br>`E08319` - Diabetes mellitus due to underlying condition with unspecified diabetic retinopathy without macular edema<br>`E0832` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy<br>`E08321` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema<br>`E083211` - Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy with macular edema, right eye<br>... +214 more
- Removed (71): `E15` - Nondiabetic hypoglycemic coma<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E232` - Diabetes insipidus<br>`O24` - Diabetes mellitus in pregnancy, childbirth, and the puerperium<br>`O240` - Pre-existing type 1 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2401` - Pre-existing type 1 diabetes mellitus, in pregnancy<br>`O24011` - Pre-existing type 1 diabetes mellitus, in pregnancy, first trimester<br>`O24012` - Pre-existing type 1 diabetes mellitus, in pregnancy, second trimester<br>`O24013` - Pre-existing type 1 diabetes mellitus, in pregnancy, third trimester<br>`O24019` - Pre-existing type 1 diabetes mellitus, in pregnancy, unspecified trimester<br>`O2402` - Pre-existing type 1 diabetes mellitus, in childbirth<br>`O2403` - Pre-existing type 1 diabetes mellitus, in the puerperium<br>`O241` - Pre-existing type 2 diabetes mellitus, in pregnancy, childbirth and the puerperium<br>`O2411` - Pre-existing type 2 diabetes mellitus, in pregnancy<br>`O24111` - Pre-existing type 2 diabetes mellitus, in pregnancy, first trimester<br>`O24112` - Pre-existing type 2 diabetes mellitus, in pregnancy, second trimester<br>`O24113` - Pre-existing type 2 diabetes mellitus, in pregnancy, third trimester<br>`O24119` - Pre-existing type 2 diabetes mellitus, in pregnancy, unspecified trimester<br>... +53 more

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Interstitial Lung Disease / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (9): `J60` - Coalworker's pneumoconiosis<br>`J61` - Pneumoconiosis due to asbestos and other mineral fibers<br>`J62` - Pneumoconiosis due to dust containing silica<br>`J620` - Pneumoconiosis due to talc dust<br>`J628` - Pneumoconiosis due to other dust containing silica<br>`J63` - Pneumoconiosis due to other inorganic dusts<br>`J636` - Pneumoconiosis due to other specified inorganic dusts<br>`J64` - Unspecified pneumoconiosis<br>`J65` - Pneumoconiosis associated with tuberculosis
- Removed (9): `J70` - Respiratory conditions due to other external agents<br>`J700` - Acute pulmonary manifestations due to radiation<br>`J701` - Chronic and other pulmonary manifestations due to radiation<br>`J702` - Acute drug-induced interstitial lung disorders<br>`J703` - Chronic drug-induced interstitial lung disorders<br>`J704` - Drug-induced interstitial lung disorders, unspecified<br>`J705` - Respiratory conditions due to smoke inhalation<br>`J708` - Respiratory conditions due to other specified external agents<br>`J709` - Respiratory conditions due to unspecified external agent

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Hypoparathyroidism / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (8): `E21` - Hyperparathyroidism and other disorders of parathyroid gland<br>`E23` - Hypofunction and other disorders of the pituitary gland<br>`E230` - Hypopituitarism<br>`E231` - Drug-induced hypopituitarism<br>`E87` - Other disorders of fluid, electrolyte and acid-base balance<br>`E876` - Hypokalemia<br>`P71` - Transitory neonatal disorders of calcium and magnesium metabolism<br>`P714` - Transitory neonatal hypoparathyroidism

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Hyperthyroidism / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (0): none
- Removed (12): `E01` - Iodine-deficiency related thyroid disorders and allied conditions<br>`E018` - Other iodine-deficiency related thyroid disorders and allied conditions<br>`E03` - Other hypothyroidism<br>`E030` - Congenital hypothyroidism with diffuse goiter<br>`E04` - Other nontoxic goiter<br>`E040` - Nontoxic diffuse goiter<br>`E041` - Nontoxic single thyroid nodule<br>`E042` - Nontoxic multinodular goiter<br>`E048` - Other specified nontoxic goiter<br>`E049` - Nontoxic goiter, unspecified<br>`P72` - Other transitory neonatal endocrine disorders<br>`P721` - Transitory neonatal hyperthyroidism

### 20. `v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv` - Pneumonia / KEEP

- Message: v820: v296 final v185 hidden add broad private prune
- Added (1): `Z8701` - Personal history of pneumonia (recurrent)
- Removed (53): `A01` - Typhoid and paratyphoid fevers<br>`A02` - Other salmonella infections<br>`A15` - Respiratory tuberculosis<br>`A155` - Tuberculosis of larynx, trachea and bronchus<br>`A37` - Whooping cough<br>`A3700` - Whooping cough due to Bordetella pertussis without pneumonia<br>`A3701` - Whooping cough due to Bordetella pertussis with pneumonia<br>`A3710` - Whooping cough due to Bordetella parapertussis without pneumonia<br>`A3711` - Whooping cough due to Bordetella parapertussis with pneumonia<br>`A3780` - Whooping cough due to other Bordetella species without pneumonia<br>`A3781` - Whooping cough due to other Bordetella species with pneumonia<br>`A3790` - Whooping cough, unspecified species without pneumonia<br>`A3791` - Whooping cough, unspecified species with pneumonia<br>`A40` - Streptococcal sepsis<br>`A50` - Congenital syphilis<br>`A54` - Gonococcal infection<br>`B01` - Varicella [chickenpox]<br>`B05` - Measles<br>... +35 more
