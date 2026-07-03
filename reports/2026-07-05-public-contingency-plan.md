# CohortX Plan Report — 2026-07-05-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-05-public-contingency.csv`
- Anchor: `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`
- Items: 20

## Planned Changes

| Order | File | Changed conditions | Message | Notes |
|---:|---|---|---|---|
| 1 | `submissions/v361_v296_v185_keep_all.csv` | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) | v361: v296 plus v185 private KEEP | best public COPD prune plus all v185 hidden KEEP, no mediastinum add |
| 2 | `submissions/v362_v296_v185_keep_ckd.csv` | CKD (KEEP +22/-75) | v362: v296 plus v185 CKD KEEP | isolates CKD private KEEP on the v296 public anchor |
| 3 | `submissions/v363_v296_v185_keep_uti.csv` | UTI (KEEP +0/-76) | v363: v296 plus v185 UTI KEEP | isolates UTI private KEEP on the v296 public anchor |
| 4 | `submissions/v364_v296_v185_keep_diabetes.csv` | Diabetes (KEEP +232/-13) | v364: v296 plus v185 Diabetes KEEP | isolates Diabetes private KEEP on the v296 public anchor |
| 5 | `submissions/v365_v296_v185_keep_pneumonia.csv` | Pneumonia (KEEP +1/-28) | v365: v296 plus v185 Pneumonia KEEP | isolates Pneumonia private KEEP on the v296 public anchor |
| 6 | `submissions/v366_v296_highconf_assoc.csv` | Epistaxis (ASSOCIATION +48/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); Bronchitis (ASSOCIATION +4/-0); +10 more | v366: v296 plus highconf ASSOC | public anchor plus high-confidence ASSOC only, no private KEEP |
| 7 | `submissions/v367_v296_broad_assoc.csv` | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Gout (ASSOCIATION +17/-0); Latent Adrenal Insufficiency (ASSOCIATION +19/-0); +16 more | v367: v296 plus broad ASSOC | public anchor plus broad ASSOC only, no private KEEP |
| 8 | `submissions/v368_v296_pulmonary_assocdiff.csv` | Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); Interstitial Lung Disease (ASSOCIATION +41/-0, DIFF +35/-0); Pneumonia (ASSOCIATION +36/-0, DIFF +71/-0) | v368: v296 plus pulmonary ASSOC/DIFF | public anchor plus public-neutral pulmonary ASSOC/DIFF group |
| 9 | `submissions/v369_v296_cardiorenal_assocdiff.csv` | CKD (ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); Diabetes (ASSOCIATION +116/-0, DIFF +7/-0) | v369: v296 plus cardiorenal ASSOC/DIFF | public anchor plus public-neutral CKD/HF/Diabetes ASSOC/DIFF group |
| 10 | `submissions/v370_v296_highconf_assoc_v185keep.csv` | Epistaxis (ASSOCIATION +48/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); Bronchitis (ASSOCIATION +4/-0); +12 more | v370: v296 highconf ASSOC plus v185 KEEP | v296 plus high-confidence ASSOC and all v185 hidden KEEP, no mediastinum add |
| 11 | `submissions/v371_v296_broad_assoc_v185keep.csv` | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Gout (ASSOCIATION +17/-0); Latent Adrenal Insufficiency (ASSOCIATION +19/-0); +16 more | v371: v296 broad ASSOC plus v185 KEEP | v296 plus broad ASSOC and all v185 hidden KEEP, no mediastinum add |
| 12 | `submissions/v372_v296_pulmonary_assocdiff_v185keep.csv` | Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76); +3 more | v372: v296 pulmonary ASSOC/DIFF plus v185 KEEP | public-neutral pulmonary ASSOC/DIFF plus all v185 hidden KEEP, no mediastinum add |
| 13 | `submissions/v373_v296_cardiorenal_assocdiff_v185keep.csv` | CKD (KEEP +22/-75, ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13, ASSOCIATION +116/-0, DIFF +7/-0); +1 more | v373: v296 cardiorenal ASSOC/DIFF plus v185 KEEP | public-neutral cardiorenal ASSOC/DIFF plus all v185 hidden KEEP, no mediastinum add |
| 14 | `submissions/v374_v296_med_add_thymus_nodes.csv` | Enlarged Mediastinum (KEEP +4/-0) | v374: v296 plus mediastinum thymus/nodes | pure public combo of best COPD prune with small positive mediastinum add |
| 15 | `submissions/v375_v296_med_add_thymus_nodes_highconf_assoc.csv` | Epistaxis (ASSOCIATION +48/-0); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +11 more | v375: v296 mediastinum plus highconf ASSOC | pure public combo plus high-confidence ASSOC only, no private KEEP |
| 16 | `submissions/v376_v296_med_add_thymus_nodes_broad_assoc.csv` | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Enlarged Mediastinum (KEEP +4/-0); Gout (ASSOCIATION +17/-0); +17 more | v376: v296 mediastinum plus broad ASSOC | pure public combo plus broad ASSOC only, no private KEEP |
| 17 | `submissions/v377_v296_med_add_thymus_nodes_pulmonary_assocdiff.csv` | Enlarged Mediastinum (KEEP +4/-0); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); Interstitial Lung Disease (ASSOCIATION +41/-0, DIFF +35/-0); +1 more | v377: v296 mediastinum plus pulmonary ASSOC/DIFF | pure public combo plus pulmonary ASSOC/DIFF, no private KEEP |
| 18 | `submissions/v378_v296_med_add_thymus_nodes_cardiorenal_assocdiff.csv` | Enlarged Mediastinum (KEEP +4/-0); CKD (ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); Diabetes (ASSOCIATION +116/-0, DIFF +7/-0) | v378: v296 mediastinum plus cardiorenal ASSOC/DIFF | pure public combo plus cardiorenal ASSOC/DIFF, no private KEEP |
| 19 | `submissions/v379_v296_med_add_thymus_nodes_v185_keep_ckd_uti.csv` | Enlarged Mediastinum (KEEP +4/-0); CKD (KEEP +22/-75); UTI (KEEP +0/-76) | v379: v296 mediastinum plus v185 CKD/UTI KEEP | public combo plus renal/urinary hidden KEEP isolation |
| 20 | `submissions/v380_v296_med_add_thymus_nodes_v185_keep_diab_pneumonia.csv` | Enlarged Mediastinum (KEEP +4/-0); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) | v380: v296 mediastinum plus v185 Diabetes/Pneumonia KEEP | public combo plus diabetes/pneumonia hidden KEEP isolation |

## Pre-Submit Checklist

- The report should show one controlled condition change for each public probe.
- Any accidental multi-condition change should be regenerated before submission.
- Run `validate-plan` immediately before `submit-plan`.

