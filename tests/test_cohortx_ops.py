from __future__ import annotations

import contextlib
import io
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from src import cohortx_ops as ops
from src import v221_240_adaptive_followups as adaptive
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

    def test_render_plan_scorecard_classifies_plan_scores(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
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
                "fileName": "v201_copd_no_j20.csv",
                "date": "2026-07-02 00:22:00",
                "description": "gain",
                "status": "complete",
                "publicScore": "0.42553",
                "privateScore": "",
            },
            {
                "fileName": "v202_copd_no_j31.csv",
                "date": "2026-07-02 00:23:00",
                "description": "tie",
                "status": "complete",
                "publicScore": "0.42453",
                "privateScore": "",
            },
            {
                "fileName": "v203_copd_no_j45.csv",
                "date": "2026-07-02 00:24:00",
                "description": "pending",
                "status": "pending",
                "publicScore": "",
                "privateScore": "",
            },
        ]

        report = ops.render_plan_scorecard(plan, rows, ops.DEFAULT_ANCHOR)

        self.assertIn("Anchor public: 0.42453", report)
        self.assertIn("`submissions/v201_copd_no_j20.csv` | complete | 0.42553 | +0.00100 | improved", report)
        self.assertIn("`submissions/v202_copd_no_j31.csv` | complete | 0.42453 | +0.00000 | tied", report)
        self.assertIn("`submissions/v203_copd_no_j45.csv` | pending |  |  | missing_score", report)
        ranked = report.split("## Ranked Complete Signals")[1]
        self.assertIn("`v201_copd_no_j20.csv`", ranked)
        self.assertNotIn("`v203_copd_no_j45.csv`", ranked)

    def test_render_intel_summarizes_external_watchpoints(self) -> None:
        report = ops.render_intel(
            "2026-07-02",
            kernels=[
                {
                    "ref": "author/known-notebook",
                    "title": "Known Notebook",
                    "author": "Author",
                    "lastRunTime": "2026-07-01 00:10:00",
                    "totalVotes": "2",
                },
                {
                    "ref": "author/new-notebook",
                    "title": "New Notebook",
                    "author": "Author",
                    "lastRunTime": "2026-07-02 00:10:00",
                    "totalVotes": "3",
                },
            ],
            leaderboard=[
                {"teamId": "1", "teamName": "Other", "submissionDate": "2026-07-02 00:00:00", "score": "0.50000"},
                {"teamId": "2", "teamName": "João Victor", "submissionDate": "2026-07-02 00:20:00", "score": "0.42453"},
            ],
            discussion={
                "url": "https://www.kaggle.com/competitions/cohort-x-task-3/discussion",
                "status": "js_shell_only",
                "chars": "5790",
                "markers": "cohortx",
            },
            submissions=[{
                "fileName": "v201_copd_no_j20.csv",
                "date": "2026-07-02 00:22:00",
                "description": "probe",
                "status": "complete",
                "publicScore": "0.42500",
                "privateScore": "",
            }],
            known_refs={"author/known-notebook"},
        )

        self.assertIn("# CohortX Intel — 2026-07-02", report)
        self.assertIn("JV leaderboard: #2 with 0.42453", report)
        self.assertIn("Public notebooks listed: 2", report)
        self.assertIn("Downloaded notebook refs: 1", report)
        self.assertIn("New public notebooks: 1", report)
        self.assertIn("Discussion page: js_shell_only", report)
        self.assertIn("`author/new-notebook`", report)
        new_section = report.split("## New Public Notebooks")[1].split("## Leaderboard Top")[0]
        self.assertIn("`author/new-notebook`", new_section)
        self.assertNotIn("`author/known-notebook`", new_section)
        self.assertIn("`v201_copd_no_j20.csv`", report)

    def test_render_signals_adds_scaled_public_sensitivity(self) -> None:
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
                "fileName": "v186_zero_copd.csv",
                "date": "2026-07-01 02:36:22",
                "description": "zero COPD",
                "status": "complete",
                "publicScore": "0.38913",
                "privateScore": "",
            },
            {
                "fileName": "v187_zero_hf.csv",
                "date": "2026-07-01 02:36:26",
                "description": "zero HF",
                "status": "complete",
                "publicScore": "0.42453",
                "privateScore": "",
            },
        ]

        report = ops.render_signals("2026-07-01", rows, ops.DEFAULT_ANCHOR)

        self.assertIn("scaled_x23", report)
        self.assertIn("| Chronic Obstructive Pulmonary Disease | `v186_zero_copd.csv` | 0.38913 | -0.03540 | -0.81420 | KEEP +0/-56 |", report)
        self.assertIn("| Chronic Obstructive Pulmonary Disease | `v186_zero_copd.csv` | -0.03540 | -0.81420 | public-sensitive |", report)
        self.assertIn("| Heart Failure | `v187_zero_hf.csv` | +0.00000 | +0.00000 | public-neutral so far |", report)

    def test_default_next_plan_path(self) -> None:
        self.assertEqual(
            ops.default_next_plan_path("2026-07-02"),
            ops.ROOT / "plans" / "2026-07-03.csv",
        )

    def test_quota_reset_uses_next_utc_midnight(self) -> None:
        now = datetime(2026, 7, 1, 3, 55, 48, tzinfo=timezone.utc)
        reset = ops.next_quota_reset(now)

        self.assertEqual(reset, datetime(2026, 7, 2, tzinfo=timezone.utc))
        self.assertEqual(ops.seconds_until_reset(now), 72252)
        self.assertEqual(ops.format_utc(reset), "2026-07-02 00:00:00 UTC")
        self.assertEqual(ops.format_brt(reset), "2026-07-01 21:00:00 BRT")

    def test_private_reserve_plan_has_twenty_dry_run_candidates(self) -> None:
        paths = reserve.write_reserve(241, ops.ROOT / "plans" / "_unit_reserve.csv", dry_run=True)

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v241_reserve_zero_hf.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v260_reserve_hyperpara_v153.csv")
        self.assertEqual(len({path.name for path in paths}), 20)

    def test_adaptive_candidate_pool_reserves_private_combo_slots(self) -> None:
        copd_items = [
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / f"v{version}_{slug}.csv", "message"),
                score=score,
                condition=adaptive.COPD,
            )
            for version, slug, score in [
                (201, "copd_no_j20", 0.43000),
                (202, "copd_no_j31", 0.42900),
                (203, "copd_no_j45", 0.42800),
                (204, "copd_no_j81_j82", 0.42700),
                (205, "copd_no_j93_j95", 0.42600),
            ]
        ]
        med_items = [
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / f"v{version}_{slug}.csv", "message"),
                score=score,
                condition=adaptive.MEDIASTINUM,
            )
            for version, slug, score in [
                (212, "med_no_j98", 0.43100),
                (213, "med_no_q34", 0.43000),
                (214, "med_no_d15", 0.42900),
                (215, "med_no_c38", 0.42800),
                (216, "med_only_mediastin_title", 0.42700),
            ]
        ]

        pool = adaptive.candidate_pool(copd_items, med_items)

        self.assertEqual(pool[0].slug, "combo_copd_no_j20_med_no_j98")
        self.assertEqual(sum(1 for candidate in pool[:20] if candidate.base == adaptive.BASE_PRIVATE), 4)
        self.assertTrue(all(candidate.base == adaptive.BASE_PRIVATE for candidate in pool[16:20]))

    def test_adaptive_candidate_pool_prefers_nonnegative_combos(self) -> None:
        copd_items = [
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v201_copd_no_j20.csv", "message"),
                score=0.41453,
                condition=adaptive.COPD,
                delta=-0.01000,
            ),
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v202_copd_no_j31.csv", "message"),
                score=0.42553,
                condition=adaptive.COPD,
                delta=0.00100,
            ),
        ]
        med_items = [
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v212_med_no_j98.csv", "message"),
                score=0.41453,
                condition=adaptive.MEDIASTINUM,
                delta=-0.01000,
            ),
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v213_med_no_q34.csv", "message"),
                score=0.42453,
                condition=adaptive.MEDIASTINUM,
                delta=0.00000,
            ),
        ]

        pool = adaptive.candidate_pool(copd_items, med_items)

        self.assertEqual(pool[0].slug, "combo_copd_no_j31_med_no_q34")
        self.assertIn("public nonnegative combo", pool[0].notes)
        fallback = next(candidate for candidate in pool if candidate.slug == "combo_copd_no_j20_med_no_j98")
        self.assertIn("negative fallback combo", fallback.notes)

    def test_adaptive_write_candidates_skips_used_version_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            submissions = root / "submissions"
            submissions.mkdir()
            base = submissions / "v178_FINAL.csv"
            existing = submissions / "v221_existing.csv"
            base.write_text(
                "Condition,KEEP,ASSOCIATION,DIFF\n"
                "Chronic Obstructive Pulmonary Disease,J44,Not Applicable,Not Applicable\n"
            )
            existing.write_text(
                "Condition,KEEP,ASSOCIATION,DIFF\n"
                "Chronic Obstructive Pulmonary Disease,J43,Not Applicable,Not Applicable\n"
            )
            candidate = adaptive.Candidate(
                changes={adaptive.COPD: ["J44", "J45"]},
                base=base,
                slug="unit_combo",
                message="unit combo",
                notes="unit notes",
            )

            with (
                patch.object(adaptive, "ROOT", root),
                patch.object(adaptive, "SUBMISSIONS", submissions),
                patch.object(adaptive, "TARGET_COUNT", 1),
            ):
                written = adaptive.write_candidates([candidate], 221, root / "plans" / "_unit.csv")

            self.assertEqual(written, [submissions / "v222_unit_combo.csv"])
            self.assertTrue(existing.exists())
            self.assertIn("submissions/v222_unit_combo.csv", (root / "plans" / "_unit.csv").read_text())

    def test_preflight_prefers_primary_plan_over_reserve(self) -> None:
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-02",
                ops.ROOT / "plans" / "2026-07-02.csv",
                ops.ROOT / "plans" / "2026-07-03-reserve.csv",
                allow_reserve=True,
                rows=[],
            )

        self.assertIn("recommended_action=submit_primary", report)
        self.assertIn("selected_plan=plans/2026-07-02.csv", report)
        self.assertIn("target_date_relation=current", report)

    def test_preflight_waits_for_future_plan_date(self) -> None:
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 1, 3, 55, 48, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-02",
                ops.ROOT / "plans" / "2026-07-02.csv",
                ops.ROOT / "plans" / "2026-07-03-reserve.csv",
                allow_reserve=True,
                rows=[],
            )

        self.assertIn("target_date_relation=future", report)
        self.assertIn("recommended_action=wait_for_target_date", report)
        self.assertIn("selected_plan=plans/2026-07-02.csv", report)
        self.assertIn("next_quota_reset_brt=2026-07-01 21:00:00 BRT", report)

    def test_preflight_requires_explicit_reserve_permission(self) -> None:
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 0, 20, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-03",
                ops.ROOT / "plans" / "_missing_primary.csv",
                ops.ROOT / "plans" / "2026-07-03-reserve.csv",
                allow_reserve=False,
                rows=[],
            )

        self.assertIn("reserve_exists=true", report)
        self.assertIn("target_date_relation=current", report)
        self.assertIn("recommended_action=hold_for_primary_or_rerun_adaptive", report)
        self.assertNotIn("selected_plan=", report)

    def test_preflight_blocks_after_competition_deadline(self) -> None:
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 16, 12, 0, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-16",
                ops.ROOT / "plans" / "2026-07-02.csv",
                None,
                allow_reserve=False,
                rows=[],
            )

        self.assertIn("competition_open=false", report)
        self.assertIn("seconds_until_deadline=0", report)
        self.assertIn("recommended_action=competition_closed", report)
        self.assertNotIn("selected_plan=", report)

    def test_preflight_rejects_target_date_after_deadline(self) -> None:
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 16, 10, 0, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-17",
                None,
                None,
                allow_reserve=False,
                rows=[],
            )

        self.assertIn("competition_open=true", report)
        self.assertIn("target_after_deadline=true", report)
        self.assertIn("recommended_action=target_after_deadline", report)
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
        self.assertIn("Recommended final selection: 2/20", report)
        recommended = report.split("## Recommended Final Selection")[1]
        recommended = recommended.split("## Neutral Hedge Watchlist")[0].split("## Top Public Submissions")[0]
        self.assertNotIn("v176_diab_all.csv", recommended)
        self.assertIn("97023", report)
        candidate_sections = report.split("## Top Public Submissions")[0]
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

    def test_duplicate_content_plan_item_is_not_submitted(self) -> None:
        source_csv = (ops.ROOT / "submissions" / "v178_FINAL.csv").read_text()
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "submissions").mkdir()
            (root / "plans").mkdir()
            old_file = root / "submissions" / "v001_old.csv"
            new_file = root / "submissions" / "v999_duplicate.csv"
            plan = root / "plans" / "unit.csv"
            old_file.write_text(source_csv)
            new_file.write_text(source_csv)
            plan.write_text("file,message\nsubmissions/v999_duplicate.csv,duplicate content\n")
            rows = [{
                "fileName": "v001_old.csv",
                "date": "2026-06-01 00:00:00",
                "description": "old",
                "status": "complete",
                "publicScore": "0.42453",
                "privateScore": "",
            }]

            with (
                patch.object(ops, "ROOT", root),
                patch.object(ops, "read_submissions", return_value=rows),
                patch.object(ops, "run") as run,
            ):
                report = ops.render_preflight("2026-07-02", plan, None, False, rows)
                result = ops.submit_plan(plan, dry_run=False, wait=False)

        self.assertIn("primary_unsubmitted_items=0", report)
        self.assertIn("primary_duplicate_content_items=1", report)
        self.assertTrue(result.plan_complete)
        self.assertEqual(result.unsubmitted_before, 0)
        run.assert_not_called()

    def test_validate_plan_rejects_duplicate_content_inside_plan(self) -> None:
        source_csv = (ops.ROOT / "submissions" / "v178_FINAL.csv").read_text()
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "submissions").mkdir()
            (root / "plans").mkdir()
            first = root / "submissions" / "v901_first.csv"
            second = root / "submissions" / "v902_second.csv"
            plan = root / "plans" / "dups.csv"
            first.write_text(source_csv)
            second.write_text(source_csv)
            plan.write_text(
                "file,message\n"
                "submissions/v901_first.csv,first\n"
                "submissions/v902_second.csv,second duplicate\n"
            )

            with patch.object(ops, "ROOT", root):
                with self.assertRaisesRegex(ValueError, "duplicate submission content within plan"):
                    ops.validate_plan(plan)

    def test_submit_plan_does_not_call_kaggle_after_deadline(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 16, 12, 0, tzinfo=timezone.utc)),
            patch.object(ops, "read_submissions", return_value=[]),
            patch.object(ops, "run") as run,
        ):
            result = ops.submit_plan(plan, dry_run=False, wait=True)

        self.assertEqual(result.plan_items, 20)
        self.assertEqual(result.unsubmitted_before, 20)
        self.assertEqual(result.submitted_now, 0)
        self.assertEqual(result.submitted_after, 0)
        run.assert_not_called()

    def test_daily_run_skip_reports_does_not_generate_next_plan(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
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
        write_plan_scorecard.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_future_date_does_not_submit_or_generate_next_plan(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 1, 3, 55, 48, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_final_candidates") as write_final_candidates,
            patch.object(ops, "generate_next_plan") as generate_next_plan,
        ):
            ops.daily_run(
                "2026-07-02",
                plan,
                dry_run=False,
                wait=True,
                skip_reports=True,
                next_plan_path=ops.ROOT / "plans" / "2026-07-03.csv",
                start_version=221,
            )

        print_status.assert_called_once()
        validate_plan.assert_called_once_with(plan)
        write_plan_report.assert_called_once()
        submit_plan.assert_not_called()
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_holds_reserve_without_permission(self) -> None:
        primary_plan = ops.ROOT / "plans" / "_missing_primary.csv"
        reserve_plan = ops.ROOT / "plans" / "2026-07-03-reserve.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "validate_plan") as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_final_candidates") as write_final_candidates,
            patch.object(ops, "generate_next_plan") as generate_next_plan,
        ):
            ops.daily_run(
                "2026-07-03",
                primary_plan,
                dry_run=False,
                wait=True,
                skip_reports=True,
                next_plan_path=ops.ROOT / "plans" / "2026-07-04.csv",
                start_version=261,
                reserve_plan_path=reserve_plan,
                allow_reserve=False,
            )

        output = buf.getvalue()
        self.assertIn("reserve_guard=requires_allow_reserve", output)
        self.assertNotIn("selected_plan=", output)
        print_status.assert_called_once()
        validate_plan.assert_not_called()
        write_plan_report.assert_not_called()
        submit_plan.assert_not_called()
        write_intel.assert_not_called()
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_uses_reserve_only_when_allowed(self) -> None:
        primary_plan = ops.ROOT / "plans" / "_missing_primary.csv"
        reserve_plan = ops.ROOT / "plans" / "2026-07-03-reserve.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-04.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(reserve_plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(1, 1, 1, 1)) as submit_plan,
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_final_candidates") as write_final_candidates,
            patch.object(ops, "generate_next_plan") as generate_next_plan,
        ):
            ops.daily_run(
                "2026-07-03",
                primary_plan,
                dry_run=False,
                wait=True,
                skip_reports=False,
                next_plan_path=next_plan,
                start_version=261,
                reserve_plan_path=reserve_plan,
                allow_reserve=True,
            )

        output = buf.getvalue()
        self.assertIn("selected_plan_kind=reserve", output)
        self.assertIn("next_plan_guard=reserve_plan", output)
        print_status.assert_called_once()
        validate_plan.assert_called_once_with(reserve_plan)
        write_plan_report.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
        submit_plan.assert_called_once_with(reserve_plan, dry_run=False, wait=True)
        write_intel.assert_called_once_with("2026-07-03", None)
        write_review.assert_called_once_with("2026-07-03", None)
        write_signals.assert_called_once_with("2026-07-03", ops.DEFAULT_ANCHOR, None)
        write_plan_scorecard.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
        write_final_candidates.assert_called_once_with(ops.DEFAULT_ANCHOR, None)
        generate_next_plan.assert_not_called()

    def test_daily_run_generates_next_plan_after_reports(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-03.csv"
        events: list[str] = []

        def record_intel(*_args: object, **_kwargs: object) -> None:
            events.append("intel")

        def record_submit(*_args: object, **_kwargs: object) -> ops.SubmitPlanResult:
            events.append("submit")
            return ops.SubmitPlanResult(1, 1, 1, 1)

        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status"),
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "submit_plan", side_effect=record_submit),
            patch.object(ops, "write_intel", side_effect=record_intel) as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
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

        write_intel.assert_called_once_with("2026-07-02", None)
        self.assertEqual(events, ["intel", "submit"])
        write_review.assert_called_once_with("2026-07-02", None)
        write_signals.assert_called_once_with("2026-07-02", ops.DEFAULT_ANCHOR, None)
        write_plan_scorecard.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_final_candidates.assert_called_once_with(ops.DEFAULT_ANCHOR, None)
        generate_next_plan.assert_called_once_with(plan, next_plan, 221)

    def test_daily_run_does_not_generate_next_plan_when_plan_incomplete(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-03.csv"
        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status"),
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(20, 20, 0, 0)),
            patch.object(ops, "write_intel"),
            patch.object(ops, "write_review"),
            patch.object(ops, "write_signals"),
            patch.object(ops, "write_plan_scorecard"),
            patch.object(ops, "write_final_candidates"),
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

        generate_next_plan.assert_not_called()


if __name__ == "__main__":
    unittest.main()
