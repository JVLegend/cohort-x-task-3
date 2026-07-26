# CohortX Reset Readiness - 2026-07-16

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

- Plan: `plans/2026-07-16.csv`
- Anchor: `submissions/v715_v633_med_add_c39.csv`
- Validation: `validated_plan_items=20`
- Preflight selection: `next_reset_selected_plan=plans/2026-07-16.csv`
- Unsubmitted items after reset: 20
- Duplicate content items: 0
- Manifest: `ready`, `reports/2026-07-16-manifest.md`, `drift=0`
- Decision matrix: `ready`, `reports/2026-07-16-decision.md`
- Recommended action after reset: `submit_primary_after_reset`

## Operational Note

The automatic `readiness` command could not complete on 2026-07-15 because the Kaggle
kernels endpoint returned `500 - Internal Server Error`. Local guards are still clean:
`validate-plan` passed, `preflight` selected the primary 2026-07-16 plan, and every planned
CSV is unique against local submission history.

## Plan Thesis

- Slots `v781`-`v788`: complete the untested public-neutral private KEEP subset matrix
  for CKD, UTI, Diabetes, and Pneumonia on top of `v715`.
- Slots `v789`-`v800`: test small Enlarged Mediastinum additions on top of the confirmed
  full `C39/C390/C399` family.
- Avoid `pulmonary_assocdiff` and C39 decomposition: both were negative in the 2026-07-15
  public scores.

## Submit Command After Reset

```bash
.venv/bin/python src/cohortx_ops.py preflight
.venv/bin/python src/cohortx_ops.py submit-plan plans/2026-07-16.csv
```

Use `submit-plan` directly if `daily-run --auto-next-plan` is blocked by the same Kaggle
kernels 500 error, but only after `preflight` still selects `plans/2026-07-16.csv`.
