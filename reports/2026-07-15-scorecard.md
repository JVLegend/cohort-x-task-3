# CohortX Plan Scorecard — 2026-07-15

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-15.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
- Anchor public: 0.43606
- Items: 20

## Plan Items

| Order | File | Status | Public | Delta vs anchor | Signal | Changed conditions | Message | Notes |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `submissions/v741_v633_med_add_c39_med_keep_v185keep_assoc_only.csv` | complete | 0.43606 | +0.00000 | tied | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) | v741: v633+C39 plus v185keep assoc-only | auto-next C39 hedge: full v185 private KEEP, assoc-only |
| 2 | `submissions/v742_v633_med_add_c39_med_keep_v185_ckd_uti_assocdiff.csv` | complete | 0.43606 | +0.00000 | tied | CKD (KEEP +22/-75); UTI (KEEP +0/-76) | v742: v633+C39 plus CKD/UTI assocdiff | auto-next C39 hedge: CKD/UTI private KEEP plus assocdiff |
| 3 | `submissions/v743_v633_med_add_c39_med_keep_v185_diab_pneu_assocdiff.csv` | complete | 0.43606 | +0.00000 | tied | Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) | v743: v633+C39 plus Diabetes/Pneumonia assocdiff | auto-next C39 hedge: Diabetes/Pneumonia private KEEP plus assocdiff |
| 4 | `submissions/v744_v633_med_add_c39_med_keep_v185keep_pulmonary_assocdiff.csv` | complete | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); +1 more | v744: v633+C39 plus v185keep pulmonary assocdiff | auto-next C39 hedge: full v185 private KEEP plus pulmonary assocdiff |
| 5 | `submissions/v745_v633_med_add_c39_med_keep_v185_ckd_assocdiff.csv` | complete | 0.43606 | +0.00000 | tied | CKD (KEEP +22/-75) | v745: v633+C39 plus CKD assocdiff | auto-next C39 hedge: CKD private KEEP plus assocdiff |
| 6 | `submissions/v746_v633_med_add_c39_med_keep_no_v185keep_pulmonary_assocdiff.csv` | complete | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1) | v746: v633+C39 plus no-v185 pulmonary assocdiff | auto-next C39 hedge: no private KEEP plus pulmonary assocdiff |
| 7 | `submissions/v747_v633_med_add_c39_med_keep_v185_uti_assocdiff.csv` | complete | 0.43606 | +0.00000 | tied | UTI (KEEP +0/-76) | v747: v633+C39 plus UTI assocdiff | auto-next C39 hedge: UTI private KEEP plus assocdiff |
| 8 | `submissions/v748_v633_med_add_c39_med_keep_v185_ckd_uti_pulmonary_assocdiff.csv` | complete | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); CKD (KEEP +22/-75); UTI (KEEP +0/-76) | v748: v633+C39 plus CKD/UTI pulmonary assocdiff | auto-next C39 hedge: CKD/UTI private KEEP plus pulmonary assocdiff |
| 9 | `submissions/v749_v633_med_add_c39_med_keep_v185_diabetes_assocdiff.csv` | complete | 0.43606 | +0.00000 | tied | Diabetes (KEEP +232/-13) | v749: v633+C39 plus Diabetes assocdiff | auto-next C39 hedge: Diabetes private KEEP plus assocdiff |
| 10 | `submissions/v750_v633_med_add_c39_med_keep_v185_pneumonia_assocdiff.csv` | complete | 0.43606 | +0.00000 | tied | Pneumonia (KEEP +1/-28) | v750: v633+C39 plus Pneumonia assocdiff | auto-next C39 hedge: Pneumonia private KEEP plus assocdiff |
| 11 | `submissions/v751_v633_med_add_c39_med_keep_v185_diab_pneu_pulmonary_assocdiff.csv` | complete | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) | v751: v633+C39 plus Diabetes/Pneumonia pulmonary assocdiff | auto-next C39 hedge: Diabetes/Pneumonia private KEEP plus pulmonary assocdiff |
| 12 | `submissions/v752_v633_med_add_c39_med_keep_v185_ckd_pulmonary_assocdiff.csv` | complete | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); CKD (KEEP +22/-75) | v752: v633+C39 plus CKD pulmonary assocdiff | auto-next C39 hedge: CKD private KEEP plus pulmonary assocdiff |
| 13 | `submissions/v753_v633_med_add_c39_med_keep_v185_uti_pulmonary_assocdiff.csv` | complete | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); UTI (KEEP +0/-76) | v753: v633+C39 plus UTI pulmonary assocdiff | auto-next C39 hedge: UTI private KEEP plus pulmonary assocdiff |
| 14 | `submissions/v754_v633_med_add_c39_med_keep_v185_diabetes_pulmonary_assocdiff.csv` | complete | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); Diabetes (KEEP +232/-13) | v754: v633+C39 plus Diabetes pulmonary assocdiff | auto-next C39 hedge: Diabetes private KEEP plus pulmonary assocdiff |
| 15 | `submissions/v821_v633_med_add_c39_root.csv` | complete | 0.43476 | -0.00130 | worse | Enlarged Mediastinum (KEEP +0/-2) | v821: v633 plus C39 root only | decompose v715: root C39 only |
| 16 | `submissions/v822_v633_med_add_c390.csv` | complete | 0.43476 | -0.00130 | worse | Enlarged Mediastinum (KEEP +0/-2) | v822: v633 plus C390 only | decompose v715: upper respiratory tract unspecified |
| 17 | `submissions/v823_v633_med_add_c399.csv` | complete | 0.43476 | -0.00130 | worse | Enlarged Mediastinum (KEEP +0/-2) | v823: v633 plus C399 only | decompose v715: lower respiratory tract unspecified |
| 18 | `submissions/v824_v633_med_add_c39_c390.csv` | complete | 0.43541 | -0.00065 | worse | Enlarged Mediastinum (KEEP +0/-1) | v824: v633 plus C39+C390 | decompose v715: root plus upper respiratory tract |
| 19 | `submissions/v825_v633_med_add_c39_c399.csv` | complete | 0.43541 | -0.00065 | worse | Enlarged Mediastinum (KEEP +0/-1) | v825: v633 plus C39+C399 | decompose v715: root plus lower respiratory tract |
| 20 | `submissions/v826_v633_med_add_c390_c399.csv` | complete | 0.43541 | -0.00065 | worse | Enlarged Mediastinum (KEEP +0/-1) | v826: v633 plus C390+C399 | decompose v715: children without root |

## Ranked Complete Signals

| Rank | File | Public | Delta vs anchor | Signal | Changed conditions |
|---:|---|---:|---:|---|---|
| 1 | `v741_v633_med_add_c39_med_keep_v185keep_assoc_only.csv` | 0.43606 | +0.00000 | tied | CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 2 | `v742_v633_med_add_c39_med_keep_v185_ckd_uti_assocdiff.csv` | 0.43606 | +0.00000 | tied | CKD (KEEP +22/-75); UTI (KEEP +0/-76) |
| 3 | `v743_v633_med_add_c39_med_keep_v185_diab_pneu_assocdiff.csv` | 0.43606 | +0.00000 | tied | Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 4 | `v745_v633_med_add_c39_med_keep_v185_ckd_assocdiff.csv` | 0.43606 | +0.00000 | tied | CKD (KEEP +22/-75) |
| 5 | `v747_v633_med_add_c39_med_keep_v185_uti_assocdiff.csv` | 0.43606 | +0.00000 | tied | UTI (KEEP +0/-76) |
| 6 | `v749_v633_med_add_c39_med_keep_v185_diabetes_assocdiff.csv` | 0.43606 | +0.00000 | tied | Diabetes (KEEP +232/-13) |
| 7 | `v750_v633_med_add_c39_med_keep_v185_pneumonia_assocdiff.csv` | 0.43606 | +0.00000 | tied | Pneumonia (KEEP +1/-28) |
| 8 | `v824_v633_med_add_c39_c390.csv` | 0.43541 | -0.00065 | worse | Enlarged Mediastinum (KEEP +0/-1) |
| 9 | `v825_v633_med_add_c39_c399.csv` | 0.43541 | -0.00065 | worse | Enlarged Mediastinum (KEEP +0/-1) |
| 10 | `v826_v633_med_add_c390_c399.csv` | 0.43541 | -0.00065 | worse | Enlarged Mediastinum (KEEP +0/-1) |
| 11 | `v821_v633_med_add_c39_root.csv` | 0.43476 | -0.00130 | worse | Enlarged Mediastinum (KEEP +0/-2) |
| 12 | `v822_v633_med_add_c390.csv` | 0.43476 | -0.00130 | worse | Enlarged Mediastinum (KEEP +0/-2) |
| 13 | `v823_v633_med_add_c399.csv` | 0.43476 | -0.00130 | worse | Enlarged Mediastinum (KEEP +0/-2) |
| 14 | `v744_v633_med_add_c39_med_keep_v185keep_pulmonary_assocdiff.csv` | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); CKD (KEEP +22/-75); UTI (KEEP +0/-76); Diabetes (KEEP +232/-13); +1 more |
| 15 | `v746_v633_med_add_c39_med_keep_no_v185keep_pulmonary_assocdiff.csv` | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1) |
| 16 | `v748_v633_med_add_c39_med_keep_v185_ckd_uti_pulmonary_assocdiff.csv` | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); CKD (KEEP +22/-75); UTI (KEEP +0/-76) |
| 17 | `v751_v633_med_add_c39_med_keep_v185_diab_pneu_pulmonary_assocdiff.csv` | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); Diabetes (KEEP +232/-13); Pneumonia (KEEP +1/-28) |
| 18 | `v752_v633_med_add_c39_med_keep_v185_ckd_pulmonary_assocdiff.csv` | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); CKD (KEEP +22/-75) |
| 19 | `v753_v633_med_add_c39_med_keep_v185_uti_pulmonary_assocdiff.csv` | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); UTI (KEEP +0/-76) |
| 20 | `v754_v633_med_add_c39_med_keep_v185_diabetes_pulmonary_assocdiff.csv` | 0.43259 | -0.00347 | worse | Epistaxis (ASSOCIATION +0/-1); Diabetes (KEEP +232/-13) |

## Strategy Use

- Improved rows are immediate candidates for promotion or cross-condition combinations.
- Tied rows are public-neutral and mainly useful as private hedges.
- Worse rows identify public-sensitive code families; use the direction of the edit before deciding whether to add back or remove codes.
- Missing rows mean the adaptive generator should wait rather than fill the next plan with weak guesses.
