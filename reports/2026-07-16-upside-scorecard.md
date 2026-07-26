# CohortX Plan Scorecard — 2026-07-16-upside

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-upside.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
- Anchor public: 0.43606
- Items: 20

## Plan Items

| Order | File | Status | Public | Delta vs anchor | Signal | Changed conditions | Message | Notes |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `submissions/v827_v715_med_drop_c78.csv` | complete | 0.43641 | +0.00035 | improved | Enlarged Mediastinum (KEEP +0/-2) | v827: v715 drop C78 mediastinal secondary neoplasm | fine public-upside ablation: remove C78/C781 while preserving C37+C39 |
| 2 | `submissions/v828_v715_med_drop_d38.csv` | complete | 0.43641 | +0.00035 | improved | Enlarged Mediastinum (KEEP +0/-2) | v828: v715 drop D38 uncertain mediastinal neoplasm | fine public-upside ablation: remove D38/D383 while preserving C37+C39 |
| 3 | `submissions/v829_v715_med_drop_j85.csv` | complete | 0.43476 | -0.00130 | worse | Enlarged Mediastinum (KEEP +0/-2) | v829: v715 drop J85 abscess mediastinum | fine public-upside ablation: remove J85/J853 while preserving C37+C39 |
| 4 | `submissions/v830_v715_med_drop_q34.csv` | complete | 0.43695 | +0.00089 | improved | Enlarged Mediastinum (KEEP +0/-5) | v830: v715 drop Q34 congenital mediastinum family | fine public-upside ablation: remove Q34 family while preserving C37+C39 |
| 5 | `submissions/v831_v715_med_drop_c38.csv` | complete | 0.43134 | -0.00472 | worse | Enlarged Mediastinum (KEEP +0/-7) | v831: v715 drop C38 heart/mediastinum/pleura malignancy | single-family ablation split from earlier D15+C38 negative combo |
| 6 | `submissions/v832_v715_med_drop_d15.csv` | complete | 0.43713 | +0.00107 | improved | Enlarged Mediastinum (KEEP +0/-6) | v832: v715 drop D15 benign intrathoracic family | single-family ablation split from earlier D15+C38 negative combo |
| 7 | `submissions/v833_v715_med_drop_j980_j981.csv` | complete | 0.43205 | -0.00401 | worse | Enlarged Mediastinum (KEEP +0/-6) | v833: v715 drop J980/J981 bronchus-collapse branch | J98 was important when removed as a block; test smaller likely-noisy branch |
| 8 | `submissions/v834_v715_med_drop_j982_j983_j984.csv` | complete | 0.43410 | -0.00196 | worse | Enlarged Mediastinum (KEEP +0/-3) | v834: v715 drop J982/J983/J984 emphysema-respiratory branch | J98 was important as a block; test smaller emphysema/other-respiratory branch |
| 9 | `submissions/v835_v715_med_drop_j985.csv` | complete | 0.43410 | -0.00196 | worse | Enlarged Mediastinum (KEEP +0/-3) | v835: v715 drop J985 mediastinum NEC branch | direct mediastinum disease branch ablation inside the broad J98 family |
| 10 | `submissions/v836_v715_med_drop_j986_j988_j989.csv` | complete | 0.43410 | -0.00196 | worse | Enlarged Mediastinum (KEEP +0/-3) | v836: v715 drop J986/J988/J989 other respiratory tail | J98 tail ablation while keeping J985 mediastinum-specific codes |
| 11 | `submissions/v837_v715_med_drop_c380_c384_c388.csv` | complete | 0.43410 | -0.00196 | worse | Enlarged Mediastinum (KEEP +0/-3) | v837: v715 drop non-mediastinum C38 children | keep C381/C382/C383 mediastinum children; remove heart/pleura/overlap children |
| 12 | `submissions/v838_v715_med_drop_q34_nonmediastinal.csv` | complete | 0.43658 | +0.00052 | improved | Enlarged Mediastinum (KEEP +0/-3) | v838: v715 drop non-mediastinum Q34 children | keep Q341 congenital mediastinum cyst; remove broader Q34 respiratory malformations |
| 13 | `submissions/v839_v301_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Intracranial Pressure (ASSOCIATION +9/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); +17 more | v839: v301 plus full C39 family | C39 overlay on old broad-assoc top composite |
| 14 | `submissions/v840_v302_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +13 more | v840: v302 plus full C39 family | C39 overlay on old highconf-assoc top composite |
| 15 | `submissions/v841_v341_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more | v841: v341 plus full C39 family | C39 overlay on old CKD/UTI top composite |
| 16 | `submissions/v842_v342_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more | v842: v342 plus full C39 family | C39 overlay on old Diabetes/Pneumonia top composite |
| 17 | `submissions/v843_v357_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0); +3 more | v843: v357 plus full C39 family | C39 overlay on old ENT/GI/Derm assoc top composite |
| 18 | `submissions/v844_v382_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Hematemesis (ASSOCIATION +65/-0) | v844: v382 plus full C39 family | C39 overlay on no-v185keep top composite |
| 19 | `submissions/v845_v384_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0); +1 more | v845: v384 plus full C39 family | C39 overlay on July 6 CKD/UTI top composite |
| 20 | `submissions/v846_v385_add_c39_family.csv` | complete | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Hematemesis (ASSOCIATION +65/-0); Diabetes (KEEP +232/-13); +1 more | v846: v385 plus full C39 family | C39 overlay on July 6 Diabetes/Pneumonia top composite |

## Ranked Complete Signals

| Rank | File | Public | Delta vs anchor | Signal | Changed conditions |
|---:|---|---:|---:|---|---|
| 1 | `v832_v715_med_drop_d15.csv` | 0.43713 | +0.00107 | improved | Enlarged Mediastinum (KEEP +0/-6) |
| 2 | `v830_v715_med_drop_q34.csv` | 0.43695 | +0.00089 | improved | Enlarged Mediastinum (KEEP +0/-5) |
| 3 | `v838_v715_med_drop_q34_nonmediastinal.csv` | 0.43658 | +0.00052 | improved | Enlarged Mediastinum (KEEP +0/-3) |
| 4 | `v827_v715_med_drop_c78.csv` | 0.43641 | +0.00035 | improved | Enlarged Mediastinum (KEEP +0/-2) |
| 5 | `v828_v715_med_drop_d38.csv` | 0.43641 | +0.00035 | improved | Enlarged Mediastinum (KEEP +0/-2) |
| 6 | `v829_v715_med_drop_j85.csv` | 0.43476 | -0.00130 | worse | Enlarged Mediastinum (KEEP +0/-2) |
| 7 | `v834_v715_med_drop_j982_j983_j984.csv` | 0.43410 | -0.00196 | worse | Enlarged Mediastinum (KEEP +0/-3) |
| 8 | `v835_v715_med_drop_j985.csv` | 0.43410 | -0.00196 | worse | Enlarged Mediastinum (KEEP +0/-3) |
| 9 | `v836_v715_med_drop_j986_j988_j989.csv` | 0.43410 | -0.00196 | worse | Enlarged Mediastinum (KEEP +0/-3) |
| 10 | `v837_v715_med_drop_c380_c384_c388.csv` | 0.43410 | -0.00196 | worse | Enlarged Mediastinum (KEEP +0/-3) |
| 11 | `v839_v301_add_c39_family.csv` | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Intracranial Pressure (ASSOCIATION +9/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); +17 more |
| 12 | `v840_v302_add_c39_family.csv` | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +13 more |
| 13 | `v841_v341_add_c39_family.csv` | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more |
| 14 | `v842_v342_add_c39_family.csv` | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more |
| 15 | `v843_v357_add_c39_family.csv` | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0); +3 more |
| 16 | `v844_v382_add_c39_family.csv` | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Hematemesis (ASSOCIATION +65/-0) |
| 17 | `v845_v384_add_c39_family.csv` | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0); +1 more |
| 18 | `v846_v385_add_c39_family.csv` | 0.43349 | -0.00257 | worse | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Hematemesis (ASSOCIATION +65/-0); Diabetes (KEEP +232/-13); +1 more |
| 19 | `v833_v715_med_drop_j980_j981.csv` | 0.43205 | -0.00401 | worse | Enlarged Mediastinum (KEEP +0/-6) |
| 20 | `v831_v715_med_drop_c38.csv` | 0.43134 | -0.00472 | worse | Enlarged Mediastinum (KEEP +0/-7) |

## Strategy Use

- Improved rows are immediate candidates for promotion or cross-condition combinations.
- Tied rows are public-neutral and mainly useful as private hedges.
- Worse rows identify public-sensitive code families; use the direction of the edit before deciding whether to add back or remove codes.
- Missing rows mean the adaptive generator should wait rather than fill the next plan with weak guesses.
