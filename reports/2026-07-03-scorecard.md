# CohortX Plan Scorecard — 2026-07-03

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-03.csv`
- Anchor: `submissions/v209_copd_no_acute_bronch_asthma.csv`
- Anchor public: 0.42687
- Items: 20

## Plan Items

| Order | File | Status | Public | Delta vs anchor | Signal | Changed conditions | Message | Notes |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `submissions/v281_assocdiff_highconf_both.csv` | missing |  |  | missing_score | Epistaxis (ASSOCIATION +48/-0, DIFF +2/-0); Gout (ASSOCIATION +17/-0, DIFF +260/-0); Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); +10 more | v281: assoc/diff high-confidence both | ASSOC+DIFF on high-confidence hidden conditions |
| 2 | `submissions/v282_assocdiff_highconf_diff.csv` | missing |  |  | missing_score | Epistaxis (DIFF +2/-0); Gout (DIFF +260/-0); Pleurisy (DIFF +17/-0); Bronchitis (DIFF +32/-0); +10 more | v282: assoc/diff high-confidence DIFF only | isolates DIFF signal on high-confidence hidden conditions |
| 3 | `submissions/v283_assocdiff_highconf_assoc.csv` | missing |  |  | missing_score | Epistaxis (ASSOCIATION +48/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); Bronchitis (ASSOCIATION +4/-0); +10 more | v283: assoc/diff high-confidence ASSOC only | isolates ASSOC signal on high-confidence hidden conditions |
| 4 | `submissions/v284_assocdiff_broad_both.csv` | missing |  |  | missing_score | Epistaxis (ASSOCIATION +48/-0, DIFF +2/-0); Intracranial Pressure (ASSOCIATION +9/-0, DIFF +97/-0); Gout (ASSOCIATION +17/-0, DIFF +260/-0); Latent Adrenal Insufficiency (ASSOCIATION +19/-0, DIFF +12/-0); +16 more | v284: assoc/diff broad both | adds broader curated hidden-condition map |
| 5 | `submissions/v285_assocdiff_broad_diff.csv` | missing |  |  | missing_score | Epistaxis (DIFF +2/-0); Intracranial Pressure (DIFF +97/-0); Gout (DIFF +260/-0); Latent Adrenal Insufficiency (DIFF +12/-0); +16 more | v285: assoc/diff broad DIFF only | broad DIFF-only private hedge |
| 6 | `submissions/v286_assocdiff_broad_assoc.csv` | missing |  |  | missing_score | Epistaxis (ASSOCIATION +48/-0); Intracranial Pressure (ASSOCIATION +9/-0); Gout (ASSOCIATION +17/-0); Latent Adrenal Insufficiency (ASSOCIATION +19/-0); +16 more | v286: assoc/diff broad ASSOC only | broad ASSOC-only private hedge |
| 7 | `submissions/v287_assocdiff_pulmonary.csv` | missing |  |  | missing_score | Pleurisy (ASSOCIATION +12/-0, DIFF +17/-0); Bronchitis (ASSOCIATION +4/-0, DIFF +32/-0); Interstitial Lung Disease (ASSOCIATION +41/-0, DIFF +35/-0); Pneumonia (ASSOCIATION +36/-0, DIFF +71/-0) | v287: assoc/diff pulmonary hidden set | pulmonary private conditions only |
| 8 | `submissions/v288_assocdiff_cardiorenal.csv` | missing |  |  | missing_score | CKD (ASSOCIATION +17/-0, DIFF +6/-0); Heart Failure (ASSOCIATION +35/-0, DIFF +15/-0); Diabetes (ASSOCIATION +116/-0, DIFF +7/-0) | v288: assoc/diff cardio-renal hidden set | CKD/HF/Diabetes private-condition map |
| 9 | `submissions/v289_assocdiff_endocrine.csv` | missing |  |  | missing_score | Latent Adrenal Insufficiency (ASSOCIATION +19/-0, DIFF +12/-0); Thyroiditis (ASSOCIATION +31/-0, DIFF +6/-0); Hypothyroidism (ASSOCIATION +19/-0, DIFF +22/-0); Diabetes (ASSOCIATION +116/-0, DIFF +7/-0); +3 more | v289: assoc/diff endocrine hidden set | thyroid/parathyroid/adrenal/diabetes private-condition map |
| 10 | `submissions/v290_assocdiff_ent_gi_derm.csv` | missing |  |  | missing_score | Epistaxis (ASSOCIATION +48/-0, DIFF +2/-0); Dermatomycosis (ASSOCIATION +137/-0, DIFF +33/-0); Nasopharyngeal Carcinoma (ASSOCIATION +30/-0, DIFF +17/-0); Hematemesis (ASSOCIATION +65/-0, DIFF +2/-0) | v290: assoc/diff ENT GI derm hidden set | Epistaxis/Derm/GI/NPC private-condition map |
| 11 | `submissions/v291_assocdiff_neuro_rheum.csv` | missing |  |  | missing_score | Intracranial Pressure (ASSOCIATION +9/-0, DIFF +97/-0); Gout (ASSOCIATION +17/-0, DIFF +260/-0) | v291: assoc/diff neuro rheum hidden set | Intracranial pressure plus gout map |
| 12 | `submissions/v292_v209_private_keep_assocdiff.csv` | missing |  |  | missing_score | Epistaxis (ASSOCIATION +48/-0, DIFF +2/-0); Intracranial Pressure (ASSOCIATION +9/-0, DIFF +97/-0); Gout (ASSOCIATION +17/-0, DIFF +260/-0); Latent Adrenal Insufficiency (ASSOCIATION +19/-0, DIFF +12/-0); +16 more | v292: v209 plus v185 private KEEP and assoc/diff | combines best public COPD prune, v185 private KEEP hedge, and broad ASSOC/DIFF |
| 13 | `submissions/v293_copd_no_j20_j45_j31_j98.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-5) | v293: COPD remove J20/J45/J31/J98 | public combo: v209 plus J31/J98 removals |
| 14 | `submissions/v294_copd_no_j20_j45_j81_j82.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) | v294: COPD remove J20/J45/J81/J82 | public combo: v209 plus pulmonary edema/eosinophilia removals |
| 15 | `submissions/v295_copd_no_j20_j45_j93_j95.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) | v295: COPD remove J20/J45/J93/J95 | public combo: v209 plus pneumothorax/postprocedural removals |
| 16 | `submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-8) | v296: COPD remove J20/J45/J81/J82/J93/J95 | public combo: combine strongest non-J96 COPD removals |
| 17 | `submissions/v297_med_no_j98.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-16) | v297: mediastinum remove J98 | unsubmitted mediastinum public ablation |
| 18 | `submissions/v298_med_no_d15_c38.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-13) | v298: mediastinum remove D15/C38 | mediastinum neoplasm-family ablation combo |
| 19 | `submissions/v299_med_add_c852.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +11/-0) | v299: mediastinum add C852 lymphoma | unsubmitted mediastinal B-cell lymphoma addition |
| 20 | `submissions/v300_med_add_thymus_nodes.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +4/-0) | v300: mediastinum add thymus/nodes | small thymus and intrathoracic-node addition |

## Ranked Complete Signals

No completed plan items yet.

## Strategy Use

- Improved rows are immediate candidates for promotion or cross-condition combinations.
- Tied rows are public-neutral and mainly useful as private hedges.
- Worse rows identify public-sensitive code families; use the direction of the edit before deciding whether to add back or remove codes.
- Missing rows mean the adaptive generator should wait rather than fill the next plan with weak guesses.
