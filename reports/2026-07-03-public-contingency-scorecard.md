# CohortX Plan Scorecard — 2026-07-03-public-contingency

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-03-public-contingency.csv`
- Anchor: `submissions/v178_FINAL.csv`
- Anchor public: 0.42453
- Items: 20

## Plan Items

| Order | File | Status | Public | Delta vs anchor | Signal | Changed conditions | Message | Notes |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `submissions/v261_copd_no_j40.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-1) | v261: contingency: COPD remove J40 | core COPD ablation: unspecified bronchitis |
| 2 | `submissions/v262_copd_no_j41.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) | v262: contingency: COPD remove J41 | core COPD ablation: simple/mucopurulent chronic bronchitis |
| 3 | `submissions/v263_copd_no_j42.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-1) | v263: contingency: COPD remove J42 | core COPD ablation: unspecified chronic bronchitis |
| 4 | `submissions/v264_copd_no_j43.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-6) | v264: contingency: COPD remove J43 | core COPD ablation: emphysema |
| 5 | `submissions/v265_copd_no_j44.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) | v265: contingency: COPD remove J44 | core COPD ablation: explicit COPD codes |
| 6 | `submissions/v266_copd_no_j47.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-3) | v266: contingency: COPD remove J47 | core COPD ablation: bronchiectasis |
| 7 | `submissions/v267_copd_no_j40_j47.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +0/-4) | v267: contingency: COPD remove J40/J47 | combined non-COPD-ish bronchitis/bronchiectasis ablation |
| 8 | `submissions/v268_copd_add_j479.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +1/-0) | v268: contingency: COPD add J479 | isolated bronchiectasis uncomplicated addition |
| 9 | `submissions/v269_copd_add_q334.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +1/-0) | v269: contingency: COPD add Q334 | isolated congenital bronchiectasis addition |
| 10 | `submissions/v270_copd_add_j479_q334.csv` | missing |  |  | missing_score | Chronic Obstructive Pulmonary Disease (KEEP +2/-0) | v270: contingency: COPD add J479/Q334 | small bronchiectasis completion addition |
| 11 | `submissions/v271_med_no_c78.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-2) | v271: contingency: mediastinum remove C78 | mediastinum ablation: secondary neoplasm of mediastinum |
| 12 | `submissions/v272_med_no_d38.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-2) | v272: contingency: mediastinum remove D38 | mediastinum ablation: uncertain behavior neoplasm |
| 13 | `submissions/v273_med_no_j85.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +0/-2) | v273: contingency: mediastinum remove J85 | mediastinum ablation: abscess of mediastinum |
| 14 | `submissions/v274_med_add_thymus_neoplasm.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +4/-0) | v274: contingency: mediastinum add thymus neoplasm | targeted thymus/thymic neoplasm addition |
| 15 | `submissions/v275_med_add_e32_thymus.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +5/-0) | v275: contingency: mediastinum add E32 thymus | targeted non-neoplasm thymus disease addition |
| 16 | `submissions/v276_med_add_c771_nodes.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +1/-0) | v276: contingency: mediastinum add C771 | isolated intrathoracic lymph-node metastasis addition |
| 17 | `submissions/v277_med_add_c39_intrathoracic.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +1/-0) | v277: contingency: mediastinum add C39 | isolated ill-defined intrathoracic malignancy addition |
| 18 | `submissions/v278_med_add_a154_tb_nodes.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +1/-0) | v278: contingency: mediastinum add A154 | isolated intrathoracic lymph-node tuberculosis addition |
| 19 | `submissions/v279_med_add_d174_lipoma.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +1/-0) | v279: contingency: mediastinum add D174 | isolated benign intrathoracic lipoma addition |
| 20 | `submissions/v280_med_add_lymphoma_nodes.csv` | missing |  |  | missing_score | Enlarged Mediastinum (KEEP +34/-0) | v280: contingency: mediastinum add lymphoma nodes | intrathoracic lymph-node lymphoma addition, separate from C852 mediastinal B-cell probe |

## Ranked Complete Signals

No completed plan items yet.

## Strategy Use

- Improved rows are immediate candidates for promotion or cross-condition combinations.
- Tied rows are public-neutral and mainly useful as private hedges.
- Worse rows identify public-sensitive code families; use the direction of the edit before deciding whether to add back or remove codes.
- Missing rows mean the adaptive generator should wait rather than fill the next plan with weak guesses.

