# CohortX Plan Report — 2026-07-03-reserve

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-03-reserve.csv`
- Anchor: `submissions/v185_private_kw.csv`
- Items: 20

## Planned Changes

| Order | File | Changed conditions | Message | Notes |
|---:|---|---|---|---|
| 1 | `submissions/v241_reserve_zero_hf.csv` | Heart Failure (KEEP +0/-72) | v241: reserve: v185 plus zero HF | public-neutral v187 on top of v185 private hedge |
| 2 | `submissions/v242_reserve_zero_hyperthyroid.csv` | Hyperthyroidism (KEEP +0/-49) | v242: reserve: v185 plus zero Hyperthyroidism | public-neutral v188 on top of v185 private hedge |
| 3 | `submissions/v243_reserve_zero_ild.csv` | Interstitial Lung Disease (KEEP +0/-42) | v243: reserve: v185 plus zero ILD | public-neutral v189 on top of v185 private hedge |
| 4 | `submissions/v244_reserve_zero_derm.csv` | Dermatomycosis (KEEP +0/-38) | v244: reserve: v185 plus zero Dermatomycosis | public-neutral v190 on top of v185 private hedge |
| 5 | `submissions/v245_reserve_zero_bronchitis.csv` | Bronchitis (KEEP +0/-33) | v245: reserve: v185 plus zero Bronchitis | public-neutral v191 on top of v185 private hedge |
| 6 | `submissions/v246_reserve_zero_npc.csv` | Nasopharyngeal Carcinoma (KEEP +0/-42) | v246: reserve: v185 plus zero NPC | public-neutral v192 on top of v185 private hedge |
| 7 | `submissions/v247_reserve_zero_hypothyroid.csv` | Hypothyroidism (KEEP +0/-26) | v247: reserve: v185 plus zero Hypothyroidism | public-neutral v193 on top of v185 private hedge |
| 8 | `submissions/v248_reserve_add_hf_kw.csv` | Heart Failure (KEEP +6/-0) | v248: reserve: v185 plus HF keyword extras | public-neutral v196 on top of v185 private hedge |
| 9 | `submissions/v249_reserve_add_ild_kw.csv` | Interstitial Lung Disease (KEEP +9/-0) | v249: reserve: v185 plus ILD keyword extras | public-neutral v197 on top of v185 private hedge |
| 10 | `submissions/v250_reserve_add_derm_kw.csv` | Dermatomycosis (KEEP +57/-0) | v250: reserve: v185 plus Derm keyword extras | public-neutral v198 on top of v185 private hedge |
| 11 | `submissions/v251_reserve_add_npc_kw.csv` | Nasopharyngeal Carcinoma (KEEP +5/-0) | v251: reserve: v185 plus NPC keyword extras | public-neutral v200 on top of v185 private hedge |
| 12 | `submissions/v252_reserve_derm_v148.csv` | Dermatomycosis (KEEP +68/-0) | v252: reserve: v185 plus Derm v148 enrich | v148 tied public with Dermatomycosis enrichment |
| 13 | `submissions/v253_reserve_pleurisy_v148.csv` | Pleurisy (KEEP +41/-0) | v253: reserve: v185 plus Pleurisy v148 enrich | v148 tied public with Pleurisy enrichment |
| 14 | `submissions/v254_reserve_bronchitis_v148.csv` | Bronchitis (KEEP +1/-0) | v254: reserve: v185 plus Bronchitis v148 enrich | v148 tied public with Bronchitis enrichment |
| 15 | `submissions/v255_reserve_hematemesis_v148.csv` | Hematemesis (KEEP +4/-0) | v255: reserve: v185 plus Hematemesis v148 enrich | v148 tied public with Hematemesis enrichment |
| 16 | `submissions/v256_reserve_thyroiditis_v153.csv` | Thyroiditis (KEEP +7/-0) | v256: reserve: v185 plus Thyroiditis v153 expand | v153 tied public with Thyroiditis expansion |
| 17 | `submissions/v257_reserve_hypothyroid_v153.csv` | Hypothyroidism (KEEP +25/-0) | v257: reserve: v185 plus Hypothyroidism v153 expand | v153 tied public with Hypothyroidism expansion |
| 18 | `submissions/v258_reserve_hypergonadism_v153.csv` | Hypergonadism (KEEP +8/-0) | v258: reserve: v185 plus Hypergonadism v153 expand | v153 tied public with Hypergonadism expansion |
| 19 | `submissions/v259_reserve_hypopara_v153.csv` | Hypoparathyroidism (KEEP +17/-0) | v259: reserve: v185 plus Hypoparathyroidism v153 expand | v153 tied public with Hypoparathyroidism expansion |
| 20 | `submissions/v260_reserve_hyperpara_v153.csv` | Hyperparathyroidism (KEEP +33/-0) | v260: reserve: v185 plus Hyperparathyroidism v153 expand | v153 tied public with Hyperparathyroidism expansion |

## Pre-Submit Checklist

- The report should show one controlled condition change for each public probe.
- Any accidental multi-condition change should be regenerated before submission.
- Run `validate-plan` immediately before `submit-plan`.

