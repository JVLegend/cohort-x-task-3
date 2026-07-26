# CohortX Plan Report — 2026-07-16-upside

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16-upside.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
- Items: 20

## Planned Changes

| Order | File | Changed conditions | Message | Notes |
|---:|---|---|---|---|
| 1 | `submissions/v827_v715_med_drop_c78.csv` | Enlarged Mediastinum (KEEP +0/-2) | v827: v715 drop C78 mediastinal secondary neoplasm | fine public-upside ablation: remove C78/C781 while preserving C37+C39 |
| 2 | `submissions/v828_v715_med_drop_d38.csv` | Enlarged Mediastinum (KEEP +0/-2) | v828: v715 drop D38 uncertain mediastinal neoplasm | fine public-upside ablation: remove D38/D383 while preserving C37+C39 |
| 3 | `submissions/v829_v715_med_drop_j85.csv` | Enlarged Mediastinum (KEEP +0/-2) | v829: v715 drop J85 abscess mediastinum | fine public-upside ablation: remove J85/J853 while preserving C37+C39 |
| 4 | `submissions/v830_v715_med_drop_q34.csv` | Enlarged Mediastinum (KEEP +0/-5) | v830: v715 drop Q34 congenital mediastinum family | fine public-upside ablation: remove Q34 family while preserving C37+C39 |
| 5 | `submissions/v831_v715_med_drop_c38.csv` | Enlarged Mediastinum (KEEP +0/-7) | v831: v715 drop C38 heart/mediastinum/pleura malignancy | single-family ablation split from earlier D15+C38 negative combo |
| 6 | `submissions/v832_v715_med_drop_d15.csv` | Enlarged Mediastinum (KEEP +0/-6) | v832: v715 drop D15 benign intrathoracic family | single-family ablation split from earlier D15+C38 negative combo |
| 7 | `submissions/v833_v715_med_drop_j980_j981.csv` | Enlarged Mediastinum (KEEP +0/-6) | v833: v715 drop J980/J981 bronchus-collapse branch | J98 was important when removed as a block; test smaller likely-noisy branch |
| 8 | `submissions/v834_v715_med_drop_j982_j983_j984.csv` | Enlarged Mediastinum (KEEP +0/-3) | v834: v715 drop J982/J983/J984 emphysema-respiratory branch | J98 was important as a block; test smaller emphysema/other-respiratory branch |
| 9 | `submissions/v835_v715_med_drop_j985.csv` | Enlarged Mediastinum (KEEP +0/-3) | v835: v715 drop J985 mediastinum NEC branch | direct mediastinum disease branch ablation inside the broad J98 family |
| 10 | `submissions/v836_v715_med_drop_j986_j988_j989.csv` | Enlarged Mediastinum (KEEP +0/-3) | v836: v715 drop J986/J988/J989 other respiratory tail | J98 tail ablation while keeping J985 mediastinum-specific codes |
| 11 | `submissions/v837_v715_med_drop_c380_c384_c388.csv` | Enlarged Mediastinum (KEEP +0/-3) | v837: v715 drop non-mediastinum C38 children | keep C381/C382/C383 mediastinum children; remove heart/pleura/overlap children |
| 12 | `submissions/v838_v715_med_drop_q34_nonmediastinal.csv` | Enlarged Mediastinum (KEEP +0/-3) | v838: v715 drop non-mediastinum Q34 children | keep Q341 congenital mediastinum cyst; remove broader Q34 respiratory malformations |
| 13 | `submissions/v839_v301_add_c39_family.csv` | Epistaxis (ASSOCIATION +47/-0); Intracranial Pressure (ASSOCIATION +9/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); +17 more | v839: v301 plus full C39 family | C39 overlay on old broad-assoc top composite |
| 14 | `submissions/v840_v302_add_c39_family.csv` | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +13 more | v840: v302 plus full C39 family | C39 overlay on old highconf-assoc top composite |
| 15 | `submissions/v841_v341_add_c39_family.csv` | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more | v841: v341 plus full C39 family | C39 overlay on old CKD/UTI top composite |
| 16 | `submissions/v842_v342_add_c39_family.csv` | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Gout (ASSOCIATION +17/-0); Pleurisy (ASSOCIATION +12/-0); +12 more | v842: v342 plus full C39 family | C39 overlay on old Diabetes/Pneumonia top composite |
| 17 | `submissions/v843_v357_add_c39_family.csv` | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0); +3 more | v843: v357 plus full C39 family | C39 overlay on old ENT/GI/Derm assoc top composite |
| 18 | `submissions/v844_v382_add_c39_family.csv` | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Hematemesis (ASSOCIATION +65/-0) | v844: v382 plus full C39 family | C39 overlay on no-v185keep top composite |
| 19 | `submissions/v845_v384_add_c39_family.csv` | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); CKD (KEEP +22/-75); Hematemesis (ASSOCIATION +65/-0); +1 more | v845: v384 plus full C39 family | C39 overlay on July 6 CKD/UTI top composite |
| 20 | `submissions/v846_v385_add_c39_family.csv` | Epistaxis (ASSOCIATION +47/-0); Enlarged Mediastinum (KEEP +3/-0); Hematemesis (ASSOCIATION +65/-0); Diabetes (KEEP +232/-13); +1 more | v846: v385 plus full C39 family | C39 overlay on July 6 Diabetes/Pneumonia top composite |

## Pre-Submit Checklist

- The report should show one controlled condition change for each public probe.
- Any accidental multi-condition change should be regenerated before submission.
- Run `validate-plan` immediately before `submit-plan`.
