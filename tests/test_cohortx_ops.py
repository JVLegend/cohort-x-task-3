from __future__ import annotations

import contextlib
import io
import os
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from src import audit_plan_deltas as plan_deltas
from src import audit_public_notebooks as notebook_audit
from src import cohortx_ops as ops
from src import interpret_plan_scores as impact
from src import sync_public_notebooks as notebook_sync
from src import v221_240_adaptive_followups as adaptive
from src import v241_260_private_reserve as reserve
from src import v261_280_public_contingency as public_contingency
from src import v281_300_assoc_diff as assoc_diff
from src import v301_320_post_assocdiff_followups as post_assoc
from src import v321_340_july4_contingency as july4_contingency


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
                "status": "api_ok",
                "topic_count": "1",
                "latest_topic_date": "2026-06-12T08:11:23.300Z",
                "topics": [{
                    "id": 707828,
                    "title": "Use of external data sources for task 3",
                    "topicUrl": "/competitions/cohort-x-task-3/discussion/707828",
                    "commentCount": 2,
                    "votes": 0,
                    "lastCommentPostDate": "2026-06-12T08:11:23.300Z",
                }],
                "notes": ["Processing must stay offline; online APIs/services are not allowed."],
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
        self.assertIn("Discussion page: api_ok", report)
        self.assertIn("Competition discussion topics: 1", report)
        self.assertIn("Use of external data sources for task 3", report)
        self.assertIn("Processing must stay offline", report)
        self.assertIn("`author/new-notebook`", report)
        new_section = report.split("## New Public Notebooks")[1].split("## Leaderboard Top")[0]
        self.assertIn("`author/new-notebook`", new_section)
        self.assertNotIn("`author/known-notebook`", new_section)
        self.assertIn("`v201_copd_no_j20.csv`", report)

    def test_discussion_status_summarizes_api_topics(self) -> None:
        def fake_post(_service: str, method: str, payload: dict[str, object], timeout_s: int = 20) -> dict[str, object]:
            if method == "ListCompetitionTopics":
                self.assertEqual(payload["competitionName"], "cohort-x-task-3")
                return {
                    "topics": [{
                        "id": 707828,
                        "title": "Use of external data sources for task 3",
                        "topicUrl": "/competitions/cohort-x-task-3/discussion/707828",
                        "commentCount": 2,
                        "postDate": "2026-06-12T03:18:43.140911400Z",
                        "lastCommentPostDate": "2026-06-12T08:11:23.300Z",
                    }],
                    "totalCount": 1,
                }
            if method == "ListTopicMessages":
                self.assertEqual(payload["topicId"], 707828)
                return {
                    "messages": [{
                        "rawMarkdown": (
                            "Online APIs and services are not allowed. Proprietary data is not allowed. "
                            "Hugging Face models and Creative Commons or Public Domain data are allowed. "
                            "The algorithm should load on a server with 15 GB RAM."
                        )
                    }]
                }
            raise AssertionError(method)

        with patch.object(ops, "kaggle_api_post", side_effect=fake_post):
            status = ops.discussion_status()

        self.assertEqual(status["status"], "api_ok")
        self.assertEqual(status["topic_count"], "1")
        self.assertIn("Use of external data sources", str(status["topics"]))
        notes = " ".join(status["notes"])
        self.assertIn("Processing must stay offline", notes)
        self.assertIn("Proprietary data is not allowed", notes)
        self.assertIn("15 GB RAM", notes)

    def test_intel_new_public_notebooks_parses_refs(self) -> None:
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
                {
                    "ref": "author/updated-notebook",
                    "title": "Updated Notebook",
                    "author": "Author",
                    "lastRunTime": "2026-07-02 00:20:00",
                    "totalVotes": "4",
                },
            ],
            leaderboard=[],
            discussion={"status": "js_shell_only", "url": "https://example.test"},
            submissions=[],
            known_refs={"author/known-notebook", "author/updated-notebook"},
            known_versions={"author/updated-notebook": "2026-07-01 00:20:00"},
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "intel.md"
            path.write_text(report)
            count, refs = ops.intel_new_public_notebooks(path)

        self.assertEqual(count, 2)
        self.assertEqual(refs, ["author/new-notebook", "author/updated-notebook"])
        self.assertIn("Updated public notebooks: 1", report)
        self.assertIn("2026-07-01 00:20:00", report)

    def test_public_notebook_audit_flags_assoc_diff_baselines(self) -> None:
        audits = notebook_audit.audit_all()
        report = notebook_audit.render_report(audits)

        self.assertEqual(len(audits), 4)
        self.assertTrue(all(audit.fills_assoc_diff for audit in audits))
        self.assertIn("haradibots/identify-relevant-icd-10-cm-codes-ba3f6c", report)
        self.assertIn("fills ASSOC/DIFF", report)
        self.assertIn("do not copy these baselines directly", report)

    def test_sync_public_notebooks_dry_run_lists_only_new_refs(self) -> None:
        with (
            patch.object(notebook_sync, "known_notebook_refs", return_value={"author/known"}),
            patch.object(notebook_sync, "read_manifest", return_value={
                "author/known": {"lastRunTime": "2026-07-01 00:00:00"},
            }),
            patch.object(notebook_sync, "read_kernels", return_value=[
                {"ref": "author/known", "lastRunTime": "2026-07-02 00:00:00"},
                {"ref": "New Author/My Notebook!"},
            ]),
            patch.object(notebook_sync, "pull_kernel") as pull_kernel,
        ):
            results = notebook_sync.sync_public_notebooks(dry_run=True, audit=True)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].ref, "author/known")
        self.assertEqual(results[0].status, "dry_run_updated")
        self.assertEqual(results[1].ref, "New Author/My Notebook!")
        self.assertEqual(results[1].status, "dry_run_new")
        self.assertEqual(results[1].path.name, "new-author-my-notebook")
        self.assertEqual(notebook_sync.result_counts(results), (1, 1))
        pull_kernel.assert_not_called()

    def test_plan_delta_audit_lists_removed_icd_titles(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        deltas = plan_deltas.plan_deltas(plan, ops.DEFAULT_ANCHOR)
        report = plan_deltas.render_report(plan, ops.DEFAULT_ANCHOR, deltas)

        first = next(delta for delta in deltas if delta.item.file.name == "v201_copd_no_j20.csv")
        self.assertEqual(first.condition, "Chronic Obstructive Pulmonary Disease")
        self.assertEqual(first.column, "KEEP")
        self.assertEqual(len(first.added), 0)
        self.assertEqual(len(first.removed), 3)
        self.assertTrue(all(code.startswith("J20") for code in first.removed))
        self.assertIn("Acute bronchitis", report)
        self.assertIn("v220_med_add_p252_only.csv", report)

    def test_plan_impact_report_interprets_scored_deltas(self) -> None:
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
                "description": "improved prune",
                "status": "complete",
                "publicScore": "0.42553",
                "privateScore": "",
            },
            {
                "fileName": "v210_copd_add_p25_only.csv",
                "date": "2026-07-02 00:30:00",
                "description": "bad addition",
                "status": "complete",
                "publicScore": "0.42353",
                "privateScore": "",
            },
        ]

        with patch.object(impact, "read_submissions", return_value=rows):
            baseline, probes = impact.interpret_plan(plan, ops.DEFAULT_ANCHOR)
            report = impact.render_report(plan, ops.DEFAULT_ANCHOR, baseline, probes)

        self.assertEqual(baseline, 0.42453)
        self.assertIn("removal improved public score", report)
        self.assertIn("addition hurt public score", report)
        self.assertIn("Acute bronchitis", report)
        self.assertIn("P250", report)

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

    def test_inferred_next_start_version_uses_prior_plan_max_version(self) -> None:
        self.assertEqual(
            ops.inferred_next_start_version(ops.ROOT / "plans" / "2026-07-02.csv"),
            221,
        )
        self.assertEqual(
            ops.inferred_next_start_version(ops.ROOT / "plans" / "2026-07-03.csv"),
            301,
        )
        self.assertEqual(
            ops.inferred_next_start_version(ops.ROOT / "plans" / "2026-07-03-public-contingency.csv"),
            281,
        )

    def test_next_plan_script_uses_post_assocdiff_generator(self) -> None:
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-03.csv").name,
            "v301_320_post_assocdiff_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-02.csv").name,
            "v221_240_adaptive_followups.py",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-03.csv").name,
            "v209_copd_no_acute_bronch_asthma.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-03.csv").name,
            "v209_copd_no_acute_bronch_asthma.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-04.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )

    def test_quota_reset_uses_next_utc_midnight(self) -> None:
        now = datetime(2026, 7, 1, 3, 55, 48, tzinfo=timezone.utc)
        reset = ops.next_quota_reset(now)

        self.assertEqual(reset, datetime(2026, 7, 2, tzinfo=timezone.utc))
        self.assertEqual(ops.seconds_until_reset(now), 72252)
        self.assertEqual(ops.format_utc(reset), "2026-07-02 00:00:00 UTC")
        self.assertEqual(ops.format_brt(reset), "2026-07-01 21:00:00 BRT")

    def test_unique_submission_events_deduplicates_kaggle_mirrored_rows(self) -> None:
        now = datetime(2026, 7, 2, 1, 0, tzinfo=timezone.utc)
        first = {
            "fileName": "v201_copd_no_j20.csv",
            "date": "2026-07-02 00:21:49",
            "description": "v201: COPD remove J20 acute bronchitis",
            "status": "complete",
            "publicScore": "0.42550",
            "privateScore": "",
        }
        first_pending = {**first, "status": "pending", "publicScore": ""}
        second = {
            "fileName": "v202_copd_no_j31.csv",
            "date": "2026-07-02 00:21:54",
            "description": "v202: COPD remove J31 chronic rhinitis",
            "status": "complete",
            "publicScore": "0.42517",
            "privateScore": "",
        }

        rows = [first, first.copy(), first_pending, second]
        today = ops.submissions_today(rows, now)
        unique_today = ops.unique_submission_events(today)

        self.assertEqual(len(today), 4)
        self.assertEqual([row["fileName"] for row in unique_today], ["v201_copd_no_j20.csv", "v202_copd_no_j31.csv"])
        self.assertEqual(unique_today[0]["status"], "complete")

    def test_preflight_uses_raw_server_rows_for_quota_and_reports_duplicates(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        rows: list[dict[str, str]] = []
        for idx, item in enumerate(ops.read_plan(plan)[:10]):
            row = {
                "fileName": item.file.name,
                "date": f"2026-07-02 00:22:{idx:02d}",
                "description": item.message,
                "status": "complete",
                "publicScore": "0.42453",
                "privateScore": "",
            }
            rows.extend([row, row.copy()])

        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 1, 0, tzinfo=timezone.utc)):
            report = ops.render_preflight("2026-07-02", plan, None, False, rows)

        self.assertIn("quota_used_utc=20/20", report)
        self.assertIn("unique_submission_events_today=10", report)
        self.assertIn("duplicate_submission_rows_today=10", report)
        self.assertIn("quota_remaining=0", report)
        self.assertIn("primary_unsubmitted_items=10", report)
        self.assertIn("recommended_action=wait_for_quota", report)

    def test_private_reserve_plan_has_twenty_dry_run_candidates(self) -> None:
        paths = reserve.write_reserve(241, ops.ROOT / "plans" / "_unit_reserve.csv", dry_run=True)

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v241_reserve_zero_hf.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v260_reserve_hyperpara_v153.csv")
        self.assertEqual(len({path.name for path in paths}), 20)

    def test_public_contingency_plan_has_twenty_dry_run_candidates(self) -> None:
        paths = public_contingency.write_public_contingency(
            261,
            ops.ROOT / "plans" / "_unit_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v261_copd_no_j40.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v280_med_add_lymphoma_nodes.csv")
        self.assertEqual(len({path.name for path in paths}), 20)

    def test_assoc_diff_plan_has_twenty_dry_run_candidates(self) -> None:
        paths = assoc_diff.write_assoc_diff_batch(
            281,
            ops.ROOT / "plans" / "_unit_assoc_diff.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v281_assocdiff_highconf_both.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v300_med_add_thymus_nodes.csv")
        self.assertEqual(len({path.name for path in paths}), 20)

    def test_assoc_diff_keeps_public_mover_assoc_diff_empty(self) -> None:
        base = assoc_diff.pd.read_csv(assoc_diff.BASE_PUBLIC)
        df = assoc_diff.candidate_frame(base, assoc_diff.SPECS[0], assoc_diff.load_code_order())

        for condition in assoc_diff.PUBLIC_ASSOC_DIFF_EMPTY:
            row = df.loc[df["Condition"].eq(condition)].iloc[0]
            self.assertEqual(row["ASSOCIATION"], "Not Applicable")
            self.assertEqual(row["DIFF"], "Not Applicable")

        pleurisy = df.loc[df["Condition"].eq("Pleurisy")].iloc[0]
        self.assertNotEqual(pleurisy["ASSOCIATION"], "Not Applicable")
        self.assertNotEqual(pleurisy["DIFF"], "Not Applicable")

    def test_assoc_diff_private_keep_preserves_public_mover_keep(self) -> None:
        base = assoc_diff.pd.read_csv(assoc_diff.BASE_PUBLIC)
        spec = next(item for item in assoc_diff.SPECS if item.slug == "v209_private_keep_assocdiff")
        df = assoc_diff.candidate_frame(base, spec, assoc_diff.load_code_order())

        for condition in assoc_diff.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(
                assoc_diff.get_codes(df, condition, "KEEP"),
                assoc_diff.get_codes(base, condition, "KEEP"),
            )

    def test_july4_contingency_has_twenty_dry_run_candidates(self) -> None:
        paths = july4_contingency.write_july4_contingency(
            321,
            ops.ROOT / "plans" / "_unit_july4_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v321_v209_v185_keep_all.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v340_med_no_c78_d38_j85.csv")
        self.assertEqual(len({path.name for path in paths}), 20)

    def test_july4_contingency_preserves_public_mover_assoc_diff_empty(self) -> None:
        base = july4_contingency.pd.read_csv(july4_contingency.BASE_PUBLIC)
        private = july4_contingency.pd.read_csv(july4_contingency.BASE_PRIVATE)
        spec = next(item for item in july4_contingency.SPECS if item.slug == "v209_v185_keep_highconf_both")
        df = july4_contingency.candidate_frame(base, private, spec, july4_contingency.load_code_order())

        for condition in july4_contingency.PUBLIC_ASSOC_DIFF_EMPTY:
            row = df.loc[df["Condition"].eq(condition)].iloc[0]
            self.assertEqual(row["ASSOCIATION"], "Not Applicable")
            self.assertEqual(row["DIFF"], "Not Applicable")
            self.assertEqual(
                july4_contingency.get_codes(df, condition, "KEEP"),
                july4_contingency.get_codes(base, condition, "KEEP"),
            )

    def test_post_assocdiff_candidate_pool_combines_public_and_private_hedges(self) -> None:
        items = [
            post_assoc.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v281_assocdiff_highconf_both.csv", "assoc"),
                score=0.42687,
                delta=0.0,
                kind="assocdiff",
            ),
            post_assoc.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v284_assocdiff_broad_both.csv", "assoc"),
                score=0.42720,
                delta=0.00033,
                kind="assocdiff",
            ),
            post_assoc.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v293_copd_no_j20_j45_j31_j98.csv", "public"),
                score=0.42780,
                delta=0.00093,
                kind="public_keep",
            ),
        ]

        pool = post_assoc.candidate_pool(items)

        self.assertGreaterEqual(len(pool), 10)
        self.assertEqual(pool[0].public_base.name, "v293_copd_no_j20_j45_j31_j98.csv")
        self.assertTrue(pool[0].private_keep)
        self.assertIn("assocdiff_broad_both", pool[0].slug)

        frame = post_assoc.candidate_frame(pool[0])
        for condition in post_assoc.PUBLIC_ASSOC_DIFF_EMPTY:
            row = frame.loc[frame["Condition"].eq(condition)].iloc[0]
            self.assertEqual(row["ASSOCIATION"], "Not Applicable")
            self.assertEqual(row["DIFF"], "Not Applicable")
        self.assertEqual(
            post_assoc.get_codes(frame, "CKD", "KEEP"),
            post_assoc.get_codes(post_assoc.pd.read_csv(post_assoc.BASE_PRIVATE), "CKD", "KEEP"),
        )
        self.assertNotEqual(
            frame.loc[frame["Condition"].eq("Pleurisy"), "ASSOCIATION"].iloc[0],
            "Not Applicable",
        )

    def test_post_assocdiff_candidate_pool_prioritizes_public_public_combo(self) -> None:
        items = [
            post_assoc.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v286_assocdiff_broad_assoc.csv", "assoc"),
                score=0.42828,
                delta=0.00141,
                kind="assocdiff",
            ),
            post_assoc.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv", "copd"),
                score=0.42995,
                delta=0.00308,
                kind="public_keep",
            ),
            post_assoc.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v300_med_add_thymus_nodes.csv", "med"),
                score=0.42707,
                delta=0.00020,
                kind="public_keep",
            ),
        ]

        pool = post_assoc.candidate_pool(items)
        frame = post_assoc.candidate_frame(pool[0])

        self.assertEqual(pool[0].public_base.name, "v296_copd_no_j20_j45_j81_j82_j93_j95.csv")
        self.assertEqual(
            [path.name for path in pool[0].public_keep_sources],
            ["v300_med_add_thymus_nodes.csv"],
        )
        self.assertIn("med_add_thymus_nodes", pool[0].slug)
        self.assertIn("assocdiff_broad_assoc", pool[0].slug)
        self.assertTrue(pool[0].private_keep)
        self.assertEqual(
            post_assoc.get_codes(frame, post_assoc.COPD, "KEEP"),
            post_assoc.get_codes(post_assoc.pd.read_csv(ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"), post_assoc.COPD, "KEEP"),
        )
        self.assertEqual(
            post_assoc.get_codes(frame, post_assoc.MEDIASTINUM, "KEEP"),
            post_assoc.get_codes(post_assoc.pd.read_csv(ops.ROOT / "submissions" / "v300_med_add_thymus_nodes.csv"), post_assoc.MEDIASTINUM, "KEEP"),
        )

    def test_post_assocdiff_requires_public_neutral_assocdiff(self) -> None:
        items = [
            post_assoc.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v281_assocdiff_highconf_both.csv", "assoc"),
                score=0.42600,
                delta=-0.00087,
                kind="assocdiff",
            )
        ]

        with self.assertRaisesRegex(RuntimeError, "No public-neutral ASSOC/DIFF"):
            post_assoc.assoc_diff_candidates(items)

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

    def test_adaptive_requires_nonnegative_public_combo_for_primary_plan(self) -> None:
        copd_items = [
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v201_copd_no_j20.csv", "message"),
                score=0.42353,
                condition=adaptive.COPD,
                delta=-0.00100,
            ),
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v202_copd_no_j31.csv", "message"),
                score=0.42453,
                condition=adaptive.COPD,
                delta=0.00000,
            ),
        ]
        med_items = [
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v212_med_no_j98.csv", "message"),
                score=0.42353,
                condition=adaptive.MEDIASTINUM,
                delta=-0.00100,
            )
        ]

        with self.assertRaisesRegex(RuntimeError, "No nonnegative COPD\\+mediastinum"):
            adaptive.require_nonnegative_public_combo(copd_items, med_items)

        med_items.append(
            adaptive.ScoredPlanItem(
                item=ops.PlanItem(ops.ROOT / "submissions" / "v213_med_no_q34.csv", "message"),
                score=0.42453,
                condition=adaptive.MEDIASTINUM,
                delta=0.00000,
            )
        )
        adaptive.require_nonnegative_public_combo(copd_items, med_items)

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

    def test_preflight_waits_for_quota_before_creating_same_day_plan(self) -> None:
        rows = [
            {
                "fileName": f"v{idx}.csv",
                "date": f"2026-07-01 02:{idx:02d}:00",
                "description": "used",
                "status": "complete",
                "publicScore": "0.42453",
                "privateScore": "",
            }
            for idx in range(20)
        ]
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 1, 12, 30, 0, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-01",
                ops.ROOT / "plans" / "_missing_primary.csv",
                ops.ROOT / "plans" / "_missing_reserve.csv",
                allow_reserve=False,
                rows=rows,
            )

        self.assertIn("target_date_relation=current", report)
        self.assertIn("quota_remaining=0", report)
        self.assertIn("primary_exists=false", report)
        self.assertIn("reserve_exists=false", report)
        self.assertIn("recommended_action=wait_for_quota", report)
        self.assertNotIn("recommended_action=create_primary_plan", report)

    def test_preflight_requires_explicit_reserve_permission(self) -> None:
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 0, 20, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-03",
                ops.ROOT / "plans" / "_missing_primary.csv",
                ops.ROOT / "plans" / "2026-07-03-reserve.csv",
                allow_reserve=False,
                rows=[],
                contingency_path=ops.ROOT / "plans" / "_missing_public_contingency.csv",
            )

        self.assertIn("reserve_exists=true", report)
        self.assertIn("contingency_exists=false", report)
        self.assertIn("target_date_relation=current", report)
        self.assertIn("recommended_action=hold_for_primary_or_rerun_adaptive", report)
        self.assertNotIn("selected_plan=", report)

    def test_preflight_selects_public_contingency_before_reserve(self) -> None:
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 0, 20, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-03",
                ops.ROOT / "plans" / "_missing_primary.csv",
                ops.ROOT / "plans" / "2026-07-03-reserve.csv",
                allow_reserve=True,
                rows=[],
            )

        self.assertIn("primary_exists=false", report)
        self.assertIn("contingency_exists=true", report)
        self.assertIn("contingency_valid_items=20", report)
        self.assertIn("reserve_exists=true", report)
        self.assertIn("recommended_action=submit_public_contingency", report)
        self.assertIn("selected_plan=plans/2026-07-03-public-contingency.csv", report)

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

    def test_render_final_candidates_promotes_tied_assoc_diff_hedges(self) -> None:
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
                "fileName": "v209_copd_no_acute_bronch_asthma.csv",
                "date": "2026-07-02 00:22:27",
                "description": "best public",
                "status": "complete",
                "publicScore": "0.42687",
                "privateScore": "",
            },
            {
                "fileName": "v281_assocdiff_highconf_both.csv",
                "date": "2026-07-03 00:22:00",
                "description": "assoc diff hedge",
                "status": "complete",
                "publicScore": "0.42687",
                "privateScore": "",
            },
            {
                "fileName": "v284_assocdiff_broad_both.csv",
                "date": "2026-07-03 00:23:00",
                "description": "large assoc diff hedge",
                "status": "complete",
                "publicScore": "0.42687",
                "privateScore": "",
            },
        ]

        report = ops.render_final_candidates(rows, ops.ROOT / "submissions" / "v209_copd_no_acute_bronch_asthma.csv")
        recommended = report.split("## Recommended Final Selection")[1]
        recommended = recommended.split("## Neutral Hedge Watchlist")[0].split("## Top Public Submissions")[0]

        self.assertIn("Strategic ASSOC/DIFF hedge", recommended)
        self.assertIn("v281_assocdiff_highconf_both.csv", recommended)
        self.assertIn("v284_assocdiff_broad_both.csv", recommended)
        self.assertIn("public-neutral ASSOC/DIFF variants", report)

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

    def test_generate_next_plan_infers_start_version_from_prior_plan(self) -> None:
        target = ops.ROOT / "plans" / "_unit_next.csv"
        if target.exists():
            target.unlink()

        completed = subprocess.CompletedProcess(
            args=["fake"],
            returncode=1,
            stdout="not_ready: missing scores",
            stderr=None,
        )
        with patch.object(ops.subprocess, "run", return_value=completed) as run:
            ops.generate_next_plan(
                ops.ROOT / "plans" / "2026-07-03-public-contingency.csv",
                target,
                None,
            )

        args = run.call_args.args[0]
        self.assertIn("--start-version", args)
        self.assertEqual(args[args.index("--start-version") + 1], "281")
        self.assertFalse(target.exists())

    def test_generate_next_plan_uses_post_assocdiff_script(self) -> None:
        target = ops.ROOT / "plans" / "_unit_next.csv"
        if target.exists():
            target.unlink()

        completed = subprocess.CompletedProcess(
            args=["fake"],
            returncode=1,
            stdout="not_ready: missing scores",
            stderr=None,
        )
        with patch.object(ops.subprocess, "run", return_value=completed) as run:
            ops.generate_next_plan(
                ops.ROOT / "plans" / "2026-07-03.csv",
                target,
                None,
            )

        args = run.call_args.args[0]
        self.assertIn("v301_320_post_assocdiff_followups.py", args[1])
        self.assertEqual(args[args.index("--start-version") + 1], "301")
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

    def test_submit_plan_skips_local_ledger_success_not_yet_remote(self) -> None:
        first_csv = (ops.ROOT / "submissions" / "v178_FINAL.csv").read_text()
        second_csv = (ops.ROOT / "submissions" / "v201_copd_no_j20.csv").read_text()
        now = datetime(2026, 7, 2, 1, 0, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "submissions").mkdir()
            (root / "plans").mkdir()
            first = root / "submissions" / "v901_first.csv"
            second = root / "submissions" / "v902_second.csv"
            plan = root / "plans" / "unit.csv"
            first.write_text(first_csv)
            second.write_text(second_csv)
            plan.write_text(
                "file,message\n"
                "submissions/v901_first.csv,first\n"
                "submissions/v902_second.csv,second\n"
            )

            with patch.object(ops, "ROOT", root):
                ops.record_submission_ledger(ops.PlanItem(first, "first"), "first", now)

            completed = subprocess.CompletedProcess(args=["fake"], returncode=0, stdout="submitted", stderr=None)
            with (
                patch.object(ops, "ROOT", root),
                patch.object(ops, "utc_now", return_value=now),
                patch.object(ops, "read_submissions", return_value=[]),
                patch.object(ops, "run", return_value=completed) as run,
            ):
                result = ops.submit_plan(plan, dry_run=False, wait=False)

        submitted_args = run.call_args.args[0]
        self.assertIn("v902_second.csv", " ".join(submitted_args))
        self.assertNotIn("v901_first.csv", " ".join(submitted_args))
        self.assertEqual(result.unsubmitted_before, 1)
        self.assertEqual(result.submitted_now, 1)

    def test_submit_plan_stops_cleanly_on_kaggle_quota_error(self) -> None:
        now = datetime(2026, 7, 2, 1, 0, tzinfo=timezone.utc)
        completed = subprocess.CompletedProcess(
            args=["fake"],
            returncode=1,
            stdout="400 - Bad Request - Submission not allowed: Your team has used its daily Submission allowance (20) today.",
            stderr=None,
        )
        with (
            patch.object(ops, "utc_now", return_value=now),
            patch.object(ops, "read_submissions", return_value=[]),
            patch.object(ops, "run", return_value=completed),
        ):
            result = ops.submit_plan(ops.ROOT / "plans" / "2026-07-02.csv", dry_run=False, wait=False)

        self.assertEqual(result.submitted_now, 0)
        self.assertFalse(result.plan_complete)

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

    def test_submission_lock_refuses_active_process_lock(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            lock_dir = root / ".cohortx_locks"
            lock_dir.mkdir()
            lock_path = lock_dir / "submission.lock"
            lock_path.write_text(f'{{"pid": {os.getpid()}, "name": "submission"}}\n')

            with patch.object(ops, "ROOT", root):
                lock = ops.SubmissionLock()
                acquired = lock.acquire()

        self.assertFalse(acquired)
        self.assertFalse(lock.acquired)

    def test_submission_lock_reclaims_stale_process_lock(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            lock_dir = root / ".cohortx_locks"
            lock_dir.mkdir()
            lock_path = lock_dir / "submission.lock"
            lock_path.write_text('{"pid": 999999999, "name": "submission"}\n')

            with patch.object(ops, "ROOT", root):
                lock = ops.SubmissionLock()
                acquired = lock.acquire()
                created_payload = lock.path.read_text()
                lock.release()

            self.assertTrue(acquired)
            self.assertIn(f'"pid": {os.getpid()}', created_payload)
            self.assertFalse(lock_path.exists())

    def test_daily_run_skip_reports_does_not_generate_next_plan(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(1, 1, 1, 1)) as submit_plan,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
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
        print_preflight.assert_called_once_with(
            "2026-07-02",
            plan,
            ops.ROOT / "plans" / "2026-07-02-reserve.csv",
            False,
        )
        validate_plan.assert_called_once_with(plan)
        write_plan_report.assert_called_once()
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        submit_plan.assert_called_once_with(plan, dry_run=True, wait=False)
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_plan_impact_report.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_future_date_does_not_submit_or_generate_next_plan(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 1, 3, 55, 48, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
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
        print_preflight.assert_called_once_with(
            "2026-07-02",
            plan,
            ops.ROOT / "plans" / "2026-07-02-reserve.csv",
            False,
        )
        validate_plan.assert_called_once_with(plan)
        write_plan_report.assert_called_once()
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        submit_plan.assert_not_called()
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_plan_impact_report.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_future_date_keeps_post_reports_clean(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 1, 3, 55, 48, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
            patch.object(ops, "write_final_candidates") as write_final_candidates,
            patch.object(ops, "generate_next_plan") as generate_next_plan,
        ):
            ops.daily_run(
                "2026-07-02",
                plan,
                dry_run=False,
                wait=True,
                skip_reports=False,
                next_plan_path=ops.ROOT / "plans" / "2026-07-03.csv",
                start_version=221,
            )

        output = buf.getvalue()
        self.assertIn("date_guard=skip_submit", output)
        self.assertIn("post_reports_guard=no_current_plan_activity", output)
        print_status.assert_called_once()
        print_preflight.assert_called_once_with(
            "2026-07-02",
            plan,
            ops.ROOT / "plans" / "2026-07-02-reserve.csv",
            False,
        )
        validate_plan.assert_called_once_with(plan)
        write_intel.assert_called_once_with("2026-07-02", None)
        write_plan_report.assert_called_once()
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        submit_plan.assert_not_called()
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_plan_impact_report.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_stops_before_submit_when_intel_has_new_public_notebook(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        report = ops.render_intel(
            "2026-07-02",
            kernels=[{
                "ref": "author/new-notebook",
                "title": "New Notebook",
                "author": "Author",
                "lastRunTime": "2026-07-02 00:10:00",
                "totalVotes": "3",
            }],
            leaderboard=[],
            discussion={"status": "js_shell_only", "url": "https://example.test"},
            submissions=[],
            known_refs=set(),
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            intel_path = Path(tmpdir) / "intel.md"
            intel_path.write_text(report)
            buf = io.StringIO()
            with (
                contextlib.redirect_stdout(buf),
                patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
                patch.object(ops, "print_status") as print_status,
                patch.object(ops, "write_intel", return_value=intel_path) as write_intel,
                patch.object(ops, "print_preflight") as print_preflight,
                patch.object(ops, "validate_plan") as validate_plan,
                patch.object(ops, "submit_plan") as submit_plan,
            ):
                ops.daily_run(
                    "2026-07-02",
                    plan,
                    dry_run=False,
                    wait=True,
                    skip_reports=False,
                    next_plan_path=ops.ROOT / "plans" / "2026-07-03.csv",
                    start_version=221,
                )

        output = buf.getvalue()
        self.assertIn("new_public_notebooks_guard=1", output)
        self.assertIn("new_public_notebook=author/new-notebook", output)
        self.assertIn("new_public_notebooks_action=download_diff_audit_before_submit", output)
        self.assertIn("new_public_notebooks_command=.venv/bin/python src/sync_public_notebooks.py", output)
        print_status.assert_called_once()
        write_intel.assert_called_once_with("2026-07-02", None)
        print_preflight.assert_not_called()
        validate_plan.assert_not_called()
        submit_plan.assert_not_called()

    def test_daily_run_holds_reserve_without_permission(self) -> None:
        primary_plan = ops.ROOT / "plans" / "_missing_primary.csv"
        contingency_plan = ops.ROOT / "plans" / "_missing_public_contingency.csv"
        reserve_plan = ops.ROOT / "plans" / "2026-07-03-reserve.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan") as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
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
                contingency_plan_path=contingency_plan,
            )

        output = buf.getvalue()
        self.assertIn("contingency_plan_missing=plans/_missing_public_contingency.csv", output)
        self.assertIn("reserve_guard=requires_allow_reserve", output)
        self.assertNotIn("selected_plan=", output)
        print_status.assert_called_once()
        print_preflight.assert_called_once_with("2026-07-03", primary_plan, reserve_plan, False, contingency_plan)
        validate_plan.assert_not_called()
        write_plan_report.assert_not_called()
        write_plan_delta_report.assert_not_called()
        submit_plan.assert_not_called()
        write_intel.assert_not_called()
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_plan_impact_report.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_uses_reserve_only_when_allowed(self) -> None:
        primary_plan = ops.ROOT / "plans" / "_missing_primary.csv"
        contingency_plan = ops.ROOT / "plans" / "_missing_public_contingency.csv"
        reserve_plan = ops.ROOT / "plans" / "2026-07-03-reserve.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-04.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(reserve_plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(1, 1, 1, 1)) as submit_plan,
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
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
                contingency_plan_path=contingency_plan,
            )

        output = buf.getvalue()
        self.assertIn("selected_plan_kind=reserve", output)
        self.assertIn("next_plan_guard=reserve_plan", output)
        print_status.assert_called_once()
        print_preflight.assert_called_once_with("2026-07-03", primary_plan, reserve_plan, True, contingency_plan)
        validate_plan.assert_called_once_with(reserve_plan)
        write_plan_report.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
        write_plan_delta_report.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR)
        submit_plan.assert_called_once_with(reserve_plan, dry_run=False, wait=True)
        write_intel.assert_called_once_with("2026-07-03", None)
        write_review.assert_called_once_with("2026-07-03", None)
        write_signals.assert_called_once_with("2026-07-03", ops.DEFAULT_ANCHOR, None)
        write_plan_scorecard.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
        write_plan_impact_report.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR)
        write_final_candidates.assert_called_once_with(ops.DEFAULT_ANCHOR, None)
        generate_next_plan.assert_not_called()

    def test_daily_run_uses_public_contingency_before_reserve(self) -> None:
        primary_plan = ops.ROOT / "plans" / "_missing_primary.csv"
        contingency_plan = ops.ROOT / "plans" / "2026-07-03-public-contingency.csv"
        reserve_plan = ops.ROOT / "plans" / "2026-07-03-reserve.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status") as print_status,
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(contingency_plan, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(1, 1, 1, 1)) as submit_plan,
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
            patch.object(ops, "write_final_candidates") as write_final_candidates,
            patch.object(ops, "generate_next_plan") as generate_next_plan,
        ):
            ops.daily_run(
                "2026-07-03",
                primary_plan,
                dry_run=False,
                wait=True,
                skip_reports=False,
                next_plan_path=ops.ROOT / "plans" / "2026-07-04.csv",
                start_version=281,
                reserve_plan_path=reserve_plan,
                allow_reserve=True,
            )

        output = buf.getvalue()
        self.assertIn("selected_plan_kind=public_contingency", output)
        self.assertIn("selected_plan=plans/2026-07-03-public-contingency.csv", output)
        self.assertNotIn("selected_plan_kind=reserve", output)
        print_status.assert_called_once()
        print_preflight.assert_called_once_with("2026-07-03", primary_plan, reserve_plan, True)
        validate_plan.assert_called_once_with(contingency_plan)
        write_plan_report.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR, None)
        write_plan_delta_report.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR)
        submit_plan.assert_called_once_with(contingency_plan, dry_run=False, wait=True)
        write_intel.assert_called_once_with("2026-07-03", None)
        write_review.assert_called_once_with("2026-07-03", None)
        write_signals.assert_called_once_with("2026-07-03", ops.DEFAULT_ANCHOR, None)
        write_plan_scorecard.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR, None)
        write_plan_impact_report.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR)
        write_final_candidates.assert_called_once_with(ops.DEFAULT_ANCHOR, None)
        generate_next_plan.assert_called_once_with(contingency_plan, ops.ROOT / "plans" / "2026-07-04.csv", 281)

    def test_daily_run_generates_next_plan_after_reports(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-03.csv"
        events: list[str] = []

        def record_intel(*_args: object, **_kwargs: object) -> None:
            events.append("intel")

        def record_preflight(*_args: object, **_kwargs: object) -> None:
            events.append("preflight")

        def record_submit(*_args: object, **_kwargs: object) -> ops.SubmitPlanResult:
            events.append("submit")
            return ops.SubmitPlanResult(1, 1, 1, 1)

        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status"),
            patch.object(ops, "print_preflight", side_effect=record_preflight) as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", side_effect=record_submit),
            patch.object(ops, "write_intel", side_effect=record_intel) as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
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
        print_preflight.assert_called_once_with(
            "2026-07-02",
            plan,
            ops.ROOT / "plans" / "2026-07-02-reserve.csv",
            False,
        )
        self.assertEqual(events, ["intel", "preflight", "submit"])
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        write_review.assert_called_once_with("2026-07-02", None)
        write_signals.assert_called_once_with("2026-07-02", ops.DEFAULT_ANCHOR, None)
        write_plan_scorecard.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_impact_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        write_final_candidates.assert_called_once_with(ops.DEFAULT_ANCHOR, None)
        generate_next_plan.assert_called_once_with(plan, next_plan, 221)

    def test_daily_run_does_not_generate_next_plan_when_plan_incomplete(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-03.csv"
        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status"),
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(20, 20, 0, 0)),
            patch.object(ops, "write_intel"),
            patch.object(ops, "write_review"),
            patch.object(ops, "write_signals"),
            patch.object(ops, "write_plan_scorecard"),
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
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

        print_preflight.assert_called_once_with(
            "2026-07-02",
            plan,
            ops.ROOT / "plans" / "2026-07-02-reserve.csv",
            False,
        )
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        write_plan_impact_report.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_skips_post_reports_when_retry_sees_partial_plan(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-03.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 1, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status"),
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(20, 5, 0, 15)),
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_impact_report") as write_plan_impact_report,
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

        output = buf.getvalue()
        self.assertIn("next_plan_guard=prior_plan_incomplete", output)
        self.assertIn("post_reports_guard=no_current_plan_activity", output)
        print_preflight.assert_called_once_with(
            "2026-07-02",
            plan,
            ops.ROOT / "plans" / "2026-07-02-reserve.csv",
            False,
        )
        write_intel.assert_called_once_with("2026-07-02", None)
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_plan_impact_report.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()


if __name__ == "__main__":
    unittest.main()
