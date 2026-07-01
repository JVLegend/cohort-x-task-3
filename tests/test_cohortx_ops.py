from __future__ import annotations

import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

from src import cohortx_ops as ops
from src import v241_260_private_reserve as reserve


class CohortxOpsTest(unittest.TestCase):
    def test_submission_changes_detects_single_condition_probe(self) -> None:
        changes = ops.submission_changes(
            ops.ROOT / "submissions" / "v178_FINAL.csv",
            ops.ROOT / "submissions" / "v186_zero_copd.csv",
        )
        self.assertEqual(changes, [("Chronic Obstructive Pulmonary Disease", "KEEP +0/-56")])

    def test_render_plan_report_summarizes_controlled_probe(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        items = ops.validate_plan(plan)
        report = ops.render_plan_report(plan, items[:2], ops.DEFAULT_ANCHOR)

        self.assertIn("Items: 2", report)
        self.assertIn("submissions/v201_copd_no_j20.csv", report)
        self.assertIn("Chronic Obstructive Pulmonary Disease (KEEP +0/-3)", report)
        self.assertNotIn("Enlarged Mediastinum", report)

    def test_default_next_plan_path(self) -> None:
        self.assertEqual(
            ops.default_next_plan_path("2026-07-02"),
            ops.ROOT / "plans" / "2026-07-03.csv",
        )

    def test_private_reserve_plan_has_twenty_dry_run_candidates(self) -> None:
        paths = reserve.write_reserve(241, ops.ROOT / "plans" / "_unit_reserve.csv", dry_run=True)

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v241_reserve_zero_hf.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v260_reserve_hyperpara_v153.csv")
        self.assertEqual(len({path.name for path in paths}), 20)

    def test_preflight_prefers_primary_plan_over_reserve(self) -> None:
        report = ops.render_preflight(
            "2026-07-02",
            ops.ROOT / "plans" / "2026-07-02.csv",
            ops.ROOT / "plans" / "2026-07-03-reserve.csv",
            allow_reserve=True,
            rows=[],
        )

        self.assertIn("recommended_action=submit_primary", report)
        self.assertIn("selected_plan=plans/2026-07-02.csv", report)

    def test_preflight_requires_explicit_reserve_permission(self) -> None:
        report = ops.render_preflight(
            "2026-07-03",
            ops.ROOT / "plans" / "_missing_primary.csv",
            ops.ROOT / "plans" / "2026-07-03-reserve.csv",
            allow_reserve=False,
            rows=[],
        )

        self.assertIn("reserve_exists=true", report)
        self.assertIn("recommended_action=hold_for_primary_or_rerun_adaptive", report)
        self.assertNotIn("selected_plan=", report)

    def test_render_final_candidates_prioritizes_anchor_and_private_hedge(self) -> None:
        rows = [
            {
                "fileName": "v178_FINAL.csv",
                "date": "2026-06-10 13:41:36",
                "description": "anchor",
                "status": "complete",
                "publicScore": "0.42453",
                "privateScore": "",
            },
            {
                "fileName": "v185_private_kw.csv",
                "date": "2026-07-01 02:34:58",
                "description": "private hedge",
                "status": "complete",
                "publicScore": "0.42453",
                "privateScore": "",
            },
            {
                "fileName": "v176_diab_all.csv",
                "date": "2026-06-10 03:02:06",
                "description": "legacy broad hedge",
                "status": "complete",
                "publicScore": "0.42453",
                "privateScore": "",
            },
            {
                "fileName": "v186_zero_copd.csv",
                "date": "2026-07-01 02:36:22",
                "description": "bad public probe",
                "status": "complete",
                "publicScore": "0.38913",
                "privateScore": "",
            },
        ]
        report = ops.render_final_candidates(rows, ops.DEFAULT_ANCHOR)

        self.assertIn("Public anchor", report)
        self.assertIn("Private hedge", report)
        self.assertIn("v185_private_kw.csv", report)
        candidate_sections = report.split("## Top Public Submissions")[0]
        recommended = candidate_sections.split("## Neutral Hedge Watchlist")[0]
        self.assertNotIn("v176_diab_all.csv", recommended)
        self.assertNotIn("v186_zero_copd.csv", candidate_sections)

    def test_generate_next_plan_nonzero_does_not_create_plan(self) -> None:
        target = ops.ROOT / "plans" / "_unit_next.csv"
        if target.exists():
            target.unlink()

        completed = subprocess.CompletedProcess(
            args=["fake"],
            returncode=1,
            stdout="not_ready: missing scores",
            stderr=None,
        )
        with patch.object(ops.subprocess, "run", return_value=completed):
            ops.generate_next_plan(ops.ROOT / "plans" / "2026-07-02.csv", target, None)

        self.assertFalse(target.exists())

    def test_daily_run_skip_reports_does_not_generate_next_plan(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        with (
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_final_candidates") as write_final_candidates,
            patch.object(ops, "generate_next_plan") as generate_next_plan,
        ):
            ops.daily_run(
                "2026-07-02",
                plan,
                dry_run=True,
                wait=False,
                skip_reports=True,
                next_plan_path=ops.ROOT / "plans" / "2026-07-03.csv",
                start_version=None,
            )

        print_status.assert_called_once()
        validate_plan.assert_called_once_with(plan)
        write_plan_report.assert_called_once()
        submit_plan.assert_called_once_with(plan, dry_run=True, wait=False)
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_generates_next_plan_after_reports(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-03.csv"
        with (
            patch.object(ops, "print_status"),
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "submit_plan"),
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_final_candidates") as write_final_candidates,
            patch.object(ops, "generate_next_plan") as generate_next_plan,
        ):
            ops.daily_run(
                "2026-07-02",
                plan,
                dry_run=False,
                wait=True,
                skip_reports=False,
                next_plan_path=next_plan,
                start_version=221,
            )

        write_review.assert_called_once_with("2026-07-02", None)
        write_signals.assert_called_once_with("2026-07-02", ops.DEFAULT_ANCHOR, None)
        write_final_candidates.assert_called_once_with(ops.DEFAULT_ANCHOR, None)
        generate_next_plan.assert_called_once_with(plan, next_plan, 221)


if __name__ == "__main__":
    unittest.main()
