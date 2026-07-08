# CohortX Reset Readiness — 2026-07-08

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Recommended action: `submit_public_contingency`
- Selected plan: `plans/2026-07-08-public-contingency.csv`
- Selected plan items: 20 valid, 20 unsubmitted, 0 duplicate_content
- Quota now: 0/20 used, 20 remaining
- Next reset UTC/BRT: 2026-07-09 00:00:00 UTC / 2026-07-08 21:00:00 BRT
- Deadline UTC/BRT: 2026-07-16 11:59:00 UTC / 2026-07-16 08:59:00 BRT
- Best public: 0.43156
- Public notebooks: new=0, updated=0
- Final selection: 20/20
- Manifest: `reports/2026-07-08-public-contingency-manifest.md` with 20 unique SHA-256 files; drift=0
- Decision matrix: `reports/2026-07-08-public-contingency-decision.md` with 7 matched comparisons
- Auto next plan: `plans/2026-07-09.csv` via `src/v341_360_post_july4_followups.py` start_version=501; contingency_exists=true

## Gates

| Gate | Status | Detail |
|---|---|---|
| target_date | ready_now | relation=current; target_after_deadline=false; competition_open=true |
| quota | ready_now | quota_remaining=20; reset=2026-07-09 00:00:00 UTC |
| selected_plan | ready | plan=`plans/2026-07-08-public-contingency.csv`; valid=20; duplicates=0 |
| manifest | ready | report=`reports/2026-07-08-public-contingency-manifest.md`; hashes=20/20; drift=0 |
| decision_matrix | ready | report=`reports/2026-07-08-public-contingency-decision.md`; matched=7 |
| auto_next_plan | ready | next=`plans/2026-07-09.csv`; script=`src/v341_360_post_july4_followups.py`; start=501; contingency=`plans/2026-07-09-public-contingency.csv`; contingency_exists=true |
| notebook_guard | ready | public_notebooks_new=0; public_notebooks_updated=0 |
| final_selection | ready | selected=20/20; report=`reports/final-candidates.md`; csv=`reports/final-selection.csv` |

## Reset Command

```bash
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

## Submit Rules

- Run the reset command only when `preflight` returns `recommended_action=submit_primary` for the current UTC date.
- Do not pass `--date` during the live reset run; let the CLI resolve the current UTC day.
- Use the selected plan `plans/2026-07-08-public-contingency.csv` unless the preflight switches to a newer primary plan.
- Stop before submission if any new or updated public notebook appears, then sync/audit it first.

## Raw Preflight

Volatile countdown fields are omitted so this report stays stable between readiness checks.

```text
preflight_date=2026-07-08
current_utc_date=2026-07-08
target_date_relation=current
competition_deadline_utc=2026-07-16 11:59:00 UTC
competition_deadline_brt=2026-07-16 08:59:00 BRT
competition_open=true
target_after_deadline=false
quota_used_utc=0/20
unique_submission_events_today=0
duplicate_submission_rows_today=0
local_ledger_submissions_today=0
quota_remaining=20
next_quota_reset_utc=2026-07-09 00:00:00 UTC
next_quota_reset_brt=2026-07-08 21:00:00 BRT
best_public=0.43156
primary_plan=plans/2026-07-08.csv
primary_exists=false
contingency_plan=plans/2026-07-08-public-contingency.csv
contingency_exists=true
contingency_valid_items=20
contingency_unsubmitted_items=20
contingency_duplicate_content_items=0
reserve_plan=plans/2026-07-08-reserve.csv
reserve_exists=false
reserve_allowed=false
recommended_action=submit_public_contingency
selected_plan=plans/2026-07-08-public-contingency.csv
selected_plan_semantic_role_status=clear_assocdiff_empty
selected_plan_semantic_note=selected_plan_keeps_ASSOC_DIFF_empty
selected_plan_semantic_files=20
selected_plan_assoc_populated_files=0
selected_plan_diff_populated_files=0
selected_plan_role_overlap_files=0
selected_plan_max_assocdiff_codes=0
selected_plan_max_assocdiff_conditions=0
```
