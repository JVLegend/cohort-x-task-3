# CohortX Reset Readiness — 2026-07-05

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Recommended action: `wait_for_target_date`
- Selected plan: `plans/2026-07-05.csv`
- Selected plan items: 20 valid, 20 unsubmitted, 0 duplicate_content
- Quota now: 20/20 used, 0 remaining
- Next reset UTC/BRT: 2026-07-05 00:00:00 UTC / 2026-07-04 21:00:00 BRT
- Deadline UTC/BRT: 2026-07-16 11:59:00 UTC / 2026-07-16 08:59:00 BRT
- Best public: 0.43156
- Public notebooks: new=0, updated=0
- Final selection: 20/20
- Decision matrix: `reports/2026-07-05-decision.md` with 20 matched comparisons

## Gates

| Gate | Status | Detail |
|---|---|---|
| target_date | wait_future | relation=future; target_after_deadline=false; competition_open=true |
| quota | ready_at_reset | quota_remaining=0; reset=2026-07-05 00:00:00 UTC |
| selected_plan | ready | plan=`plans/2026-07-05.csv`; valid=20; duplicates=0 |
| decision_matrix | ready | report=`reports/2026-07-05-decision.md`; matched=20 |
| notebook_guard | ready | public_notebooks_new=0; public_notebooks_updated=0 |
| final_selection | ready | selected=20/20; report=`reports/final-candidates.md`; csv=`reports/final-selection.csv` |

## Reset Command

```bash
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

## Submit Rules

- Run the reset command only when `preflight` returns `recommended_action=submit_primary` for the current UTC date.
- Do not pass `--date` during the live reset run; let the CLI resolve the current UTC day.
- Use the selected plan `plans/2026-07-05.csv` unless the preflight switches to a newer primary plan.
- Stop before submission if any new or updated public notebook appears, then sync/audit it first.

## Raw Preflight

Volatile countdown fields are omitted so this report stays stable between readiness checks.

```text
preflight_date=2026-07-05
current_utc_date=2026-07-04
target_date_relation=future
competition_deadline_utc=2026-07-16 11:59:00 UTC
competition_deadline_brt=2026-07-16 08:59:00 BRT
competition_open=true
target_after_deadline=false
quota_used_utc=20/20
unique_submission_events_today=20
duplicate_submission_rows_today=0
local_ledger_submissions_today=20
quota_remaining=0
next_quota_reset_utc=2026-07-05 00:00:00 UTC
next_quota_reset_brt=2026-07-04 21:00:00 BRT
best_public=0.43156
primary_plan=plans/2026-07-05.csv
primary_exists=true
primary_valid_items=20
primary_unsubmitted_items=20
primary_duplicate_content_items=0
contingency_plan=plans/2026-07-05-public-contingency.csv
contingency_exists=true
contingency_valid_items=20
contingency_unsubmitted_items=20
contingency_duplicate_content_items=0
reserve_plan=plans/2026-07-05-reserve.csv
reserve_exists=false
reserve_allowed=false
recommended_action=wait_for_target_date
selected_plan=plans/2026-07-05.csv
```
