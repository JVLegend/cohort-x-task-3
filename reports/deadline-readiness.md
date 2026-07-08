# CohortX Deadline Readiness Calendar

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Audit current UTC date: 2026-07-08
- Competition deadline UTC/BRT: 2026-07-16 11:59:00 UTC / 2026-07-16 08:59:00 BRT
- Dates audited: 9
- Coverage ready/spent: 9/9
- Primary ready/spent days: 0
- Public contingency fallback days: 8
- Future unsubmitted slots protected: 160
- Gaps: 0

## Daily Coverage

| Date | Relation | Selected | Coverage | Valid | Unsubmitted | Duplicates | Decision | Auto-next | Notes |
|---|---|---|---|---:|---:|---:|---|---|---|
| 2026-07-08 | current | `plans/2026-07-08-public-contingency.csv` (public_contingency) | spent | 20 | 0 | 0 | ready (7; `reports/2026-07-08-public-contingency-decision.md`) | ready (`plans/2026-07-09.csv`) | ok |
| 2026-07-09 | future | `plans/2026-07-09-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (1; `reports/2026-07-09-public-contingency-decision.md`) | ready (`plans/2026-07-10.csv`) | primary_missing_using_public_contingency |
| 2026-07-10 | future | `plans/2026-07-10-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (1; `reports/2026-07-10-public-contingency-decision.md`) | ready (`plans/2026-07-11.csv`) | primary_missing_using_public_contingency |
| 2026-07-11 | future | `plans/2026-07-11-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (1; `reports/2026-07-11-public-contingency-decision.md`) | ready (`plans/2026-07-12.csv`) | primary_missing_using_public_contingency |
| 2026-07-12 | future | `plans/2026-07-12-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (5; `reports/2026-07-12-public-contingency-decision.md`) | ready (`plans/2026-07-13.csv`) | primary_missing_using_public_contingency |
| 2026-07-13 | future | `plans/2026-07-13-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (1; `reports/2026-07-13-public-contingency-decision.md`) | ready (`plans/2026-07-14.csv`) | primary_missing_using_public_contingency |
| 2026-07-14 | future | `plans/2026-07-14-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (5; `reports/2026-07-14-public-contingency-decision.md`) | ready (`plans/2026-07-15.csv`) | primary_missing_using_public_contingency |
| 2026-07-15 | future | `plans/2026-07-15-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (1; `reports/2026-07-15-public-contingency-decision.md`) | ready (`plans/2026-07-16.csv`) | primary_missing_using_public_contingency |
| 2026-07-16 | future | `plans/2026-07-16-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (7; `reports/2026-07-16-public-contingency-decision.md`) | final_day (`none`) | primary_missing_using_public_contingency |

## Gap Handling

- No hard coverage gaps in the audited window. Public contingencies protect days whose adaptive primary does not exist yet.

## Use

- `ready` means the primary plan can spend a full reset if it remains unsubmitted.
- `fallback_ready` means a public contingency can protect the reset if the adaptive primary has not been generated yet.
- Missing or thin decision matrices do not block fallback submissions, but they should be improved when a primary plan exists.
