# CohortX Plan Report — 2026-07-04-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-04-public-contingency.csv`
- Anchor: `submissions/v209_copd_no_acute_bronch_asthma.csv`
- Items: 20

## Planned Changes

| Order | File | Changed conditions | Message | Notes |
|---:|---|---|---|---|
| 1 | `submissions/v321_v209_v185_keep_all.csv` | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) | v321: v209 plus v185 private KEEP | best public COPD prune plus v185 hidden KEEP hedge |
| 2 | `submissions/v322_v209_v185_keep_ckd.csv` | CKD (KEEP +22/-75) | v322: v209 plus v185 CKD KEEP | isolates v185 CKD private KEEP on v209 |
| 3 | `submissions/v323_v209_v185_keep_uti.csv` | UTI (KEEP +0/-76) | v323: v209 plus v185 UTI KEEP | isolates v185 UTI private KEEP on v209 |
| 4 | `submissions/v324_v209_v185_keep_diabetes.csv` | Diabetes (KEEP +232/-13) | v324: v209 plus v185 Diabetes KEEP | isolates v185 Diabetes private KEEP on v209 |
| 5 | `submissions/v325_v209_v185_keep_pneumonia.csv` | Pneumonia (KEEP +1/-28) | v325: v209 plus v185 Pneumonia KEEP | isolates v185 Pneumonia private KEEP on v209 |
| 6 | `submissions/v326_v209_v185_keep_ckd_uti.csv` | CKD (KEEP +22/-75); UTI (KEEP +0/-76) | v326: v209 plus v185 CKD/UTI KEEP | paired renal/urinary private KEEP hedge |
| 7 | `submissions/v327_v209_v185_keep_diab_pneumonia.csv` | Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) | v327: v209 plus v185 Diabetes/Pneumonia KEEP | paired high-volume private KEEP hedge |
| 8 | `submissions/v328_v209_v185_keep_highconf_both.csv` | Epistaxis (ASSOCIATION +48/-0, DIFF +2/-0); Gout (ASSOCIATION +17/-0, DIFF +260/-0); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); +12 more | v328: v209 v185 KEEP plus highconf assoc/diff | v185 private KEEP plus high-confidence ASSOC+DIFF |
| 9 | `submissions/v329_v209_v185_keep_highconf_diff.csv` | Epistaxis (DIFF +2/-0); Gout (DIFF +260/-0); Pleurisy (DIFF +17/-0); Bronchitis (DIFF +32/-0); +12 more | v329: v209 v185 KEEP plus highconf DIFF | v185 private KEEP plus high-confidence DIFF only |
| 10 | `submissions/v330_v209_v185_keep_highconf_assoc.csv` | Epistaxis (ASSOCIATION +48/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); Bronchitis (ASSOCIATION +4/-0); +12 more | v330: v209 v185 KEEP plus highconf ASSOC | v185 private KEEP plus high-confidence ASSOC only |
| 11 | `submissions/v331_v209_v185_keep_pulmonary_assocdiff.csv` | Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +3 more | v331: v209 v185 KEEP plus pulmonary assoc/diff | v185 private KEEP plus pulmonary ASSOC/DIFF group |
| 12 | `submissions/v332_v209_v185_keep_cardiorenal_assocdiff.csv` | CKD (KEEP +22/-75, ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13, ASSOCIATION +116/-0, DIFF +7/-0); +1 more | v332: v209 v185 KEEP plus cardiorenal assoc/diff | v185 private KEEP plus CKD/HF/Diabetes ASSOC/DIFF group |
| 13 | `submissions/v333_v209_v185_keep_endocrine_assocdiff.csv` | Latent Adrenal Insufficiency (ASSOCIATION +19/-0, DIFF +12/-0); Thyroiditis (ASSOCIATION +31/-0, DIFF +6/-0); CKD (KEEP +22/-75); Hypothyroidism (ASSOCIATION +19/-0, DIFF +22/-0); +6 more | v333: v209 v185 KEEP plus endocrine assoc/diff | v185 private KEEP plus endocrine ASSOC/DIFF group |
| 14 | `submissions/v334_v209_v185_keep_ent_gi_derm_assocdiff.csv` | Epistaxis (ASSOCIATION +48/-0, DIFF +2/-0); Dermatomycosis (ASSOCIATION +137/-0, DIFF +33/-0); Nasopharyngeal Carcinoma (ASSOCIATION +30/-0, DIFF +17/-0); CKD (KEEP +22/-75); +4 more | v334: v209 v185 KEEP plus ENT/GI/derm assoc/diff | v185 private KEEP plus ENT/GI/derm ASSOC/DIFF group |
| 15 | `submissions/v335_v209_v185_keep_neuro_rheum_assocdiff.csv` | Intracranial Pressure (ASSOCIATION +9/-0, DIFF +97/-0); Gout (ASSOCIATION +17/-0, DIFF +260/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +2 more | v335: v209 v185 KEEP plus neuro/rheum assoc/diff | v185 private KEEP plus neuro/rheum ASSOC/DIFF group |
| 16 | `submissions/v336_copd_no_j20_j45_j31.csv` | Chronic Obstructive Pulmonary Disease (KEEP +0/-2) | v336: COPD remove J20/J45/J31 | v209 plus J31 removal, isolating one extra positive public signal |
| 17 | `submissions/v337_copd_no_j20_j45_j98.csv` | Chronic Obstructive Pulmonary Disease (KEEP +0/-3) | v337: COPD remove J20/J45/J98 | v209 plus J98 removal, isolating one extra positive public signal |
| 18 | `submissions/v338_copd_no_j20_j45_j31_j81_j82_j93_j95.csv` | Chronic Obstructive Pulmonary Disease (KEEP +0/-10) | v338: COPD remove J20/J45/J31/J81/J82/J93/J95 | v209 plus strongest non-J96 COPD removals, excluding J98 |
| 19 | `submissions/v339_med_no_q34.csv` | Enlarged Mediastinum (KEEP +0/-5) | v339: mediastinum remove Q34 | unsubmitted mediastinum family ablation on v209 |
| 20 | `submissions/v340_med_no_c78_d38_j85.csv` | Enlarged Mediastinum (KEEP +0/-6) | v340: mediastinum remove C78/D38/J85 | small mediastinum false-positive ablation bundle on v209 |

## Pre-Submit Checklist

- The report should show one controlled condition change for each public probe.
- Any accidental multi-condition change should be regenerated before submission.
- Run `validate-plan` immediately before `submit-plan`.
