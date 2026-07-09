from __future__ import annotations

import contextlib
import csv
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
from src import train_scorer
from src import v221_240_adaptive_followups as adaptive
from src import v241_260_private_reserve as reserve
from src import v261_280_public_contingency as public_contingency
from src import v281_300_assoc_diff as assoc_diff
from src import v301_320_post_assocdiff_followups as post_assoc
from src import v321_340_july4_contingency as july4_contingency
from src import v341_360_post_july4_followups as post_july4
from src import v341_360_july5_contingency as july5_contingency
from src import v401_420_july6_contingency as july6_contingency
from src import v441_460_july7_contingency as july7_contingency
from src import v481_500_july8_contingency as july8_contingency
from src import v521_540_july9_assoc_isolations as july9_assoc_isolations
from src import v561_580_july10_diff_isolations as july10_diff_isolations
from src import v601_620_july11_keep_prunes as july11_keep_prunes
from src import v641_660_july12_prune_assoc as july12_prune_assoc
from src import v681_700_july13_prune_diff as july13_prune_diff
from src import v721_740_july14_prune_assocdiff as july14_prune_assocdiff
from src import v761_780_july15_multi_keep_prunes as july15_multi_prunes
from src import v801_820_july16_final_blends as july16_final_blends


class CohortxOpsTest(unittest.TestCase):
    def test_train_scorer_rejects_unknown_icd_nodes(self) -> None:
        with self.assertRaisesRegex(ValueError, "NO_SUCH_NODE"):
            train_scorer.expand_nodes(["NO_SUCH_NODE"], {"A00", "A000"})

    def test_train_scorer_minimal_spec_captures_gold_granularity(self) -> None:
        codes = train_scorer.load_codes()
        gold = train_scorer.load_train_gold()
        spec = train_scorer.minimal_spec(gold, codes)

        self.assertEqual(train_scorer.score_spec(spec, gold, codes, verbose=False), 1.0)
        self.assertEqual(spec["Stroke"]["ASSOCIATION"], ["H340", "H341"])
        self.assertEqual(spec["Aortic Aneurysm"]["ASSOCIATION"], ["A50", "A539", "M352"])
        self.assertEqual(spec["Shortness of Breadth"]["DIFF"], ["R53", "T17", "T180"])

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

    def test_write_plan_report_uses_single_trailing_newline(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        with tempfile.TemporaryDirectory(dir=ops.REPORTS) as tmpdir:
            target = Path(tmpdir) / "plan.md"
            ops.write_plan_report(plan, ops.DEFAULT_ANCHOR, target)

            content = target.read_bytes()

        self.assertTrue(content.endswith(b"\n"))
        self.assertFalse(content.endswith(b"\n\n"))

    def test_render_plan_strategy_audit_summarizes_july5_axes(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-05.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        items = ops.validate_plan(plan)

        report = ops.render_plan_strategy_audit(plan, items, anchor)

        self.assertIn("# CohortX Plan Strategy Audit — 2026-07-05", report)
        self.assertIn("- Items: 20", report)
        self.assertIn("- Best source public: 0.43156", report)
        self.assertIn("| item_count | ready | items=20/20 |", report)
        self.assertIn("| ordering | ready | first_source=0.43156; best_source=0.43156 |", report)
        self.assertIn("| mediastinum_toggle | ready | med=keep 13; med=drop 7 |", report)
        self.assertIn("| private_keep_mix | ready | buckets=4; none=2 |", report)
        self.assertIn("| assoc_mix | ready | buckets=5 |", report)
        self.assertIn("| med=keep | 13 |", report)
        self.assertIn("| med=drop | 7 |", report)
        self.assertIn("| none | 2 |", report)
        self.assertIn("| assocdiff | 11 |", report)
        self.assertIn("v341_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_v185_ckd_uti_assocdiff.csv", report)

    def test_render_plan_strategy_audit_infers_july7_contingency_axes(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-07-public-contingency.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        items = ops.validate_plan(plan)

        report = ops.render_plan_strategy_audit(plan, items, anchor)

        self.assertIn("- Distinct source submissions: 3", report)
        self.assertIn("- Mediastinum axis: keep=8, drop=12", report)
        self.assertIn("- Private KEEP buckets: 1", report)
        self.assertIn("- ASSOC/DIFF buckets: 5", report)
        self.assertIn("| private_keep_mix | thin | buckets=1; none=20 |", report)
        self.assertIn("`private_keep_mix` is thin; read the plan as a fallback/hedge batch", report)
        self.assertIn("| `copd_j31_j98` | 7 |", report)
        self.assertIn("| highconf_assoc | 6 |", report)

    def test_render_plan_strategy_audit_notes_thin_assoc_mix(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-06.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        items = ops.validate_plan(plan)

        report = ops.render_plan_strategy_audit(plan, items, anchor)

        self.assertIn("| assoc_mix | thin | buckets=3 |", report)
        self.assertIn("## Axis Risk Notes", report)
        self.assertIn("`assoc_mix` is thin; use scored comparisons for the submitted ASSOC/DIFF buckets", report)

    def test_render_plan_manifest_records_hashes_and_axes(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-05.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        items = ops.validate_plan(plan)

        report = ops.render_plan_manifest(plan, items, anchor)

        self.assertIn("# CohortX Plan Integrity Manifest — 2026-07-05", report)
        self.assertIn("- Items: 20", report)
        self.assertIn("- Unique SHA-256 files: 20", report)
        self.assertIn("- High-volume watchlist: 1 over 1000", report)
        self.assertIn("| item_count | ready | items=20/20 |", report)
        self.assertIn("| row_counts | ready | expected=23; files=20 |", report)
        self.assertIn("| change_volume_watch | review | max_volume=1146; over_limit=1; limit=1000 |", report)
        self.assertIn("`" + ops.file_sha256(items[0].file) + "`", report)
        self.assertIn("source=v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep", report)
        self.assertIn("med=keep; private_keep=CKD+UTI; assoc=assocdiff", report)
        self.assertIn("## High-Volume Watchlist", report)
        self.assertIn("v347_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_bro_no_med_add_v185keep_assocdiff.csv", report)

    def test_manifest_status_flags_hash_drift_against_current_plan(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-05.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        items = ops.validate_plan(plan)
        current_hash = ops.file_sha256(items[0].file)

        with tempfile.TemporaryDirectory() as tmpdir:
            report = Path(tmpdir) / "manifest.md"
            report.write_text(
                ops.render_plan_manifest(plan, items, anchor).replace(
                    f"`{current_hash}`",
                    f"`{'0' * 64}`",
                    1,
                )
            )

            self.assertEqual(ops.manifest_hash_count(report), 20)
            self.assertEqual(ops.manifest_status(report, 20, plan), "drift")
            drift = ops.manifest_hash_drift(report, plan)

        self.assertIsNotNone(drift)
        self.assertEqual(len(drift or []), 1)
        self.assertIn(items[0].file.name, (drift or [""])[0])

    def test_render_plan_decision_matrix_summarizes_july5_comparisons(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-05.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        items = ops.validate_plan(plan)

        report = ops.render_plan_decision_matrix(plan, items, anchor)

        self.assertIn("# CohortX Plan Decision Matrix — 2026-07-05", report)
        self.assertIn("| matched_comparisons | ready |", report)
        self.assertIn("| med |", report)
        self.assertIn("`med=drop`", report)
        self.assertIn("`med=keep`", report)
        self.assertIn("| private_keep |", report)
        self.assertIn("| assoc |", report)
        self.assertIn("| source |", report)
        self.assertIn("Post-Score Checklist", report)
        self.assertIn("plan-scorecard plans/2026-07-05.csv", report)

    def test_render_plan_decision_matrix_infers_july7_contingency_comparisons(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-07-public-contingency.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        items = ops.validate_plan(plan)

        report = ops.render_plan_decision_matrix(plan, items, anchor)

        self.assertIn("- Matched decision comparisons: 18", report)
        self.assertIn("| matched_comparisons | ready | comparisons=18 |", report)
        self.assertIn("source=copd_j31_j98; private_keep=none; assoc=highconf_assoc", report)
        self.assertIn("source=copd_j31_j98; med=keep; private_keep=none", report)

    def test_render_plan_decision_outcome_summarizes_axis_winners(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-05.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        rows = [{
            "fileName": anchor.name,
            "date": "2026-07-03 00:22:54",
            "description": "anchor",
            "status": "complete",
            "publicScore": "0.42995",
            "privateScore": "",
        }]
        for idx, item in enumerate(ops.read_plan(plan), start=1):
            axes = ops.parse_plan_strategy_axes(item.notes)
            score = 0.43000
            if axes["med"] == "keep":
                score += 0.00100
            if axes["private_keep"] == "none":
                score += 0.00030
            if axes["assoc"] == "cardiorenal_assocdiff":
                score += 0.00020
            rows.append({
                "fileName": item.file.name,
                "date": f"2026-07-05 00:{idx:02d}:00",
                "description": item.message,
                "status": "complete",
                "publicScore": f"{score:.5f}",
                "privateScore": "",
            })

        report = ops.render_plan_decision_outcome(plan, rows, anchor)

        self.assertIn("# CohortX Plan Decision Outcome — 2026-07-05", report)
        self.assertIn("- Scored plan items: 20/20", report)
        self.assertIn("- Matched decision comparisons: 20", report)
        self.assertIn("- Pending comparisons: 0", report)
        self.assertIn("| item_scores | ready | scored=20/20 |", report)
        self.assertIn("| outcome_comparisons | ready | resolved=20; pending=0; comparisons=20 |", report)
        self.assertIn("| Axis | Public wins | Tie-breaks | Pending | Readout |", report)
        self.assertIn("| med | `med=keep`", report)
        self.assertIn("| private_keep |", report)
        self.assertIn("| assoc |", report)
        self.assertIn("## Detailed Comparisons", report)
        self.assertIn("| Axis | Held constant | Status | Public winner | Recommended | Scores | Volumes | Files | Rule |", report)
        self.assertIn("`keep`", report)

    def test_render_plan_decision_outcome_recommends_low_volume_tie_breaks(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-05.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        rows = [{
            "fileName": anchor.name,
            "date": "2026-07-03 00:22:54",
            "description": "anchor",
            "status": "complete",
            "publicScore": "0.42995",
            "privateScore": "",
        }]
        for idx, item in enumerate(ops.read_plan(plan), start=1):
            rows.append({
                "fileName": item.file.name,
                "date": f"2026-07-05 00:{idx:02d}:00",
                "description": item.message,
                "status": "complete",
                "publicScore": "0.43100",
                "privateScore": "",
            })

        report = ops.render_plan_decision_outcome(plan, rows, anchor)

        self.assertIn("| med | `med=tie`", report)
        self.assertIn("tie_low_volume", report)
        self.assertIn("`drop` min=528; `keep` min=532", report)
        self.assertIn("`drop (tie_low_volume)`", report)

    def test_render_plan_decision_outcome_waits_for_missing_scores(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-05.csv"
        anchor = ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
        first = ops.read_plan(plan)[0]
        rows = [{
            "fileName": first.file.name,
            "date": "2026-07-05 00:01:00",
            "description": first.message,
            "status": "complete",
            "publicScore": "0.43100",
            "privateScore": "",
        }]

        report = ops.render_plan_decision_outcome(plan, rows, anchor)

        self.assertIn("- Scored plan items: 1/20", report)
        self.assertIn("| item_scores | waiting | scored=1/20 |", report)
        self.assertIn("| outcome_comparisons | waiting |", report)
        self.assertIn("pending_scores", report)

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
        self.assertIn("Next rank target: #1 `Other` at 0.50000", report)
        self.assertIn("Gap to next rank: 0.07547", report)
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

    def test_plan_delta_audit_write_report_uses_single_trailing_newline(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        with tempfile.TemporaryDirectory(dir=ops.REPORTS) as tmpdir:
            target = Path(tmpdir) / "deltas.md"
            plan_deltas.write_report(plan, ops.DEFAULT_ANCHOR, target)

            content = target.read_bytes()

        self.assertTrue(content.endswith(b"\n"))
        self.assertFalse(content.endswith(b"\n\n"))

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
        self.assertEqual(
            ops.next_available_start_version(ops.ROOT / "plans" / "2026-07-03-public-contingency.csv"),
            421,
        )
        self.assertEqual(
            ops.inferred_next_start_version(ops.ROOT / "plans" / "2026-07-04.csv"),
            321,
        )
        self.assertEqual(
            ops.next_available_start_version(ops.ROOT / "plans" / "2026-07-04.csv"),
            421,
        )
        self.assertEqual(
            ops.inferred_next_start_version(ops.ROOT / "plans" / "2026-07-05.csv"),
            361,
        )
        self.assertEqual(
            ops.next_available_start_version(ops.ROOT / "plans" / "2026-07-05.csv"),
            421,
        )

    def test_next_plan_script_uses_post_assocdiff_generator(self) -> None:
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-03.csv").name,
            "v301_320_post_assocdiff_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-04.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-05.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-05-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-06-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-07-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-08-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-09-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-10-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-11-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-12-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-13-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-14-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-15-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
        )
        self.assertEqual(
            ops.next_plan_script_for(ops.ROOT / "plans" / "2026-07-16-public-contingency.csv").name,
            "v341_360_post_july4_followups.py",
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
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-04.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-05-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-06-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-07-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-08-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-09-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-10-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-11-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-12-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-13-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-14-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-15-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.next_plan_report_anchor(ops.ROOT / "plans" / "2026-07-16-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-03.csv").name,
            "v209_copd_no_acute_bronch_asthma.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-04.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-05-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-07-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-08-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-09-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-10-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-11-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-12-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-13-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-14-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-15-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )
        self.assertEqual(
            ops.plan_report_anchor_for(ops.ROOT / "plans" / "2026-07-16-public-contingency.csv").name,
            "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
        )

    def test_plan_report_cli_infers_modern_anchor(self) -> None:
        plan = Path("plans/2026-07-07-public-contingency.csv")
        with patch.object(ops, "write_plan_report") as write_plan_report:
            ops.main(["plan-report", str(plan)])

        write_plan_report.assert_called_once_with(
            plan,
            ops.ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
            None,
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

    def test_semantic_role_audit_marks_assocdiff_empty_plan_clear(self) -> None:
        items = ops.validate_plan(ops.ROOT / "plans" / "2026-07-08-public-contingency.csv")

        audit = ops.semantic_role_audit(items)

        self.assertEqual(audit["status"], "clear_assocdiff_empty")
        self.assertEqual(audit["assoc_populated_files"], 0)
        self.assertEqual(audit["diff_populated_files"], 0)
        self.assertEqual(audit["role_overlap_files"], 0)

    def test_semantic_role_audit_flags_assoc_overlap_for_review(self) -> None:
        items = ops.validate_plan(ops.ROOT / "plans" / "2026-07-09-public-contingency.csv")

        audit = ops.semantic_role_audit(items)

        self.assertEqual(audit["status"], "review_role_overlap")
        self.assertEqual(audit["assoc_populated_files"], 20)
        self.assertGreater(audit["role_overlap_files"], 0)
        self.assertGreater(audit["max_assocdiff_codes"], 0)

    def test_preflight_includes_selected_plan_semantic_role_audit(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-08-public-contingency.csv"

        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 8, 1, 0, tzinfo=timezone.utc)):
            report = ops.render_preflight("2026-07-08", None, None, False, [], plan)

        self.assertIn("recommended_action=", report)
        self.assertIn("selected_plan=plans/2026-07-08-public-contingency.csv", report)
        self.assertIn("selected_plan_semantic_role_status=clear_assocdiff_empty", report)
        self.assertIn("selected_plan_assoc_populated_files=0", report)
        self.assertIn("selected_plan_diff_populated_files=0", report)

    def test_best_public_supplements_known_tied_top_when_recent_history_is_truncated(self) -> None:
        rows = [
            {
                "fileName": "v540_v296_assoc_diabetes.csv",
                "date": "2026-07-09 11:25:31",
                "description": "recent lower score",
                "status": "complete",
                "publicScore": "0.42995",
                "privateScore": "",
            },
        ]

        self.assertAlmostEqual(ops.best_public(rows) or 0.0, 0.43156)

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

    def test_july5_contingency_has_twenty_dry_run_candidates(self) -> None:
        paths = july5_contingency.write_july5_contingency(
            361,
            ops.ROOT / "plans" / "_unit_july5_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v361_v296_v185_keep_all.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v380_v296_med_add_thymus_nodes_v185_keep_diab_pneumonia.csv")
        self.assertEqual(len({path.name for path in paths}), 20)

    def test_july5_contingency_preserves_public_mover_assoc_diff_empty(self) -> None:
        base = july5_contingency.pd.read_csv(july5_contingency.BASE_BEST)
        private = july5_contingency.pd.read_csv(july5_contingency.BASE_PRIVATE)
        med_positive = july5_contingency.pd.read_csv(july5_contingency.MED_POSITIVE)
        spec = next(item for item in july5_contingency.SPECS if item.slug == "v296_highconf_assoc_v185keep")
        df = july5_contingency.candidate_frame(base, private, med_positive, spec, july5_contingency.load_code_order())

        for condition in july5_contingency.PUBLIC_ASSOC_DIFF_EMPTY:
            row = df.loc[df["Condition"].eq(condition)].iloc[0]
            self.assertEqual(row["ASSOCIATION"], "Not Applicable")
            self.assertEqual(row["DIFF"], "Not Applicable")
            self.assertEqual(
                july5_contingency.get_codes(df, condition, "KEEP"),
                july5_contingency.get_codes(base, condition, "KEEP"),
            )

    def test_july5_contingency_can_add_mediastinum_positive_without_changing_copd(self) -> None:
        base = july5_contingency.pd.read_csv(july5_contingency.BASE_BEST)
        private = july5_contingency.pd.read_csv(july5_contingency.BASE_PRIVATE)
        med_positive = july5_contingency.pd.read_csv(july5_contingency.MED_POSITIVE)
        spec = next(item for item in july5_contingency.SPECS if item.slug == "v296_med_add_thymus_nodes")
        df = july5_contingency.candidate_frame(base, private, med_positive, spec, july5_contingency.load_code_order())

        self.assertEqual(
            july5_contingency.get_codes(df, "Chronic Obstructive Pulmonary Disease", "KEEP"),
            july5_contingency.get_codes(base, "Chronic Obstructive Pulmonary Disease", "KEEP"),
        )
        self.assertEqual(
            july5_contingency.get_codes(df, july5_contingency.MEDIASTINUM, "KEEP"),
            july5_contingency.get_codes(med_positive, july5_contingency.MEDIASTINUM, "KEEP"),
        )

    def test_july6_contingency_has_twenty_dry_run_candidates(self) -> None:
        paths = july6_contingency.write_july6_contingency(
            401,
            ops.ROOT / "plans" / "_unit_july6_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v401_v296_med_v185_keep_ckd.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v420_v296_cardiorenal_assocdiff_v185_diab_pneumonia.csv")

    def test_july6_contingency_preserves_public_mover_assoc_diff_empty(self) -> None:
        base = july6_contingency.pd.read_csv(july6_contingency.BASE_BEST)
        private = july6_contingency.pd.read_csv(july6_contingency.BASE_PRIVATE)
        med_positive = july6_contingency.pd.read_csv(july6_contingency.MED_POSITIVE)
        spec = next(item for item in july6_contingency.SPECS if item.slug == "v296_med_highconf_assoc_v185_ckd")
        df = july6_contingency.candidate_frame(base, private, med_positive, spec, july6_contingency.load_code_order())

        for condition in july6_contingency.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july6_contingency.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july6_contingency.get_codes(df, condition, "DIFF"), [])
        self.assertEqual(
            july6_contingency.get_codes(df, "Chronic Obstructive Pulmonary Disease", "KEEP"),
            july6_contingency.get_codes(base, "Chronic Obstructive Pulmonary Disease", "KEEP"),
        )
        self.assertEqual(
            july6_contingency.get_codes(df, july6_contingency.MEDIASTINUM, "KEEP"),
            july6_contingency.get_codes(med_positive, july6_contingency.MEDIASTINUM, "KEEP"),
        )
        self.assertEqual(
            july6_contingency.get_codes(df, "CKD", "KEEP"),
            july6_contingency.get_codes(private, "CKD", "KEEP"),
        )

    def test_july7_contingency_has_twenty_dry_run_candidates(self) -> None:
        paths = july7_contingency.write_july7_contingency(
            441,
            ops.ROOT / "plans" / "_unit_july7_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v441_copd_j31_j98_med_add_thymus_nodes.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v460_copd_j81_j82_med_broad_assoc.csv")

    def test_july7_contingency_preserves_public_mover_assoc_diff_empty(self) -> None:
        med_positive = july7_contingency.pd.read_csv(july7_contingency.MED_POSITIVE)
        assoc_frames = {
            path: july7_contingency.pd.read_csv(path)
            for path in {spec.assoc_source for spec in july7_contingency.SPECS if spec.assoc_source is not None}
        }
        spec = next(item for item in july7_contingency.SPECS if item.slug == "copd_j31_j98_med_highconf_assoc")
        df = july7_contingency.candidate_frame(spec, med_positive, assoc_frames)
        base = july7_contingency.pd.read_csv(spec.base_path)

        for condition in july7_contingency.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july7_contingency.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july7_contingency.get_codes(df, condition, "DIFF"), [])
        self.assertEqual(
            july7_contingency.get_codes(df, "Chronic Obstructive Pulmonary Disease", "KEEP"),
            july7_contingency.get_codes(base, "Chronic Obstructive Pulmonary Disease", "KEEP"),
        )
        self.assertEqual(
            july7_contingency.get_codes(df, july7_contingency.MEDIASTINUM, "KEEP"),
            july7_contingency.get_codes(med_positive, july7_contingency.MEDIASTINUM, "KEEP"),
        )
        self.assertNotEqual(july7_contingency.get_codes(df, "Epistaxis", "ASSOCIATION"), [])
        self.assertEqual(july7_contingency.get_codes(df, "Epistaxis", "DIFF"), [])

    def test_july8_contingency_has_twenty_dry_run_candidates(self) -> None:
        paths = july8_contingency.write_july8_contingency(
            481,
            ops.ROOT / "plans" / "_unit_july8_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v481_v296_zero_hf.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v500_v296_med_add_hidden_kw_group.csv")

    def test_july8_contingency_applies_public_neutral_keep_sources(self) -> None:
        base = july8_contingency.pd.read_csv(july8_contingency.BASE_BEST)
        med_positive = july8_contingency.pd.read_csv(july8_contingency.MED_POSITIVE)
        zero_frames = {
            condition: july8_contingency.pd.read_csv(path)
            for condition, path in july8_contingency.ZERO_SOURCES.items()
        }
        add_frames = {
            condition: july8_contingency.pd.read_csv(path)
            for condition, path in july8_contingency.ADD_SOURCES.items()
        }
        spec = next(item for item in july8_contingency.SPECS if item.slug == "v296_med_add_hidden_kw_group")
        df = july8_contingency.candidate_frame(base, med_positive, zero_frames, add_frames, spec)

        for condition in july8_contingency.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july8_contingency.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july8_contingency.get_codes(df, condition, "DIFF"), [])
        self.assertEqual(
            july8_contingency.get_codes(df, "Chronic Obstructive Pulmonary Disease", "KEEP"),
            july8_contingency.get_codes(base, "Chronic Obstructive Pulmonary Disease", "KEEP"),
        )
        self.assertEqual(
            july8_contingency.get_codes(df, july8_contingency.MEDIASTINUM, "KEEP"),
            july8_contingency.get_codes(med_positive, july8_contingency.MEDIASTINUM, "KEEP"),
        )
        for condition in (
            july8_contingency.HEART_FAILURE,
            july8_contingency.ILD,
            july8_contingency.DERMATOMYCOSIS,
            july8_contingency.NPC,
        ):
            self.assertEqual(
                july8_contingency.get_codes(df, condition, "KEEP"),
                july8_contingency.get_codes(add_frames[condition], condition, "KEEP"),
            )

    def test_july9_assoc_isolations_have_twenty_dry_run_candidates(self) -> None:
        paths = july9_assoc_isolations.write_july9_assoc_isolations(
            521,
            ops.ROOT / "plans" / "_unit_july9_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v521_v296_assoc_epistaxis.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v540_v296_assoc_diabetes.csv")

    def test_july9_assoc_isolations_only_populate_one_assoc_bucket(self) -> None:
        base = july9_assoc_isolations.pd.read_csv(july9_assoc_isolations.BASE_BEST)
        code_order = july9_assoc_isolations.load_code_order()
        spec = next(item for item in july9_assoc_isolations.SPECS if item.condition == july9_assoc_isolations.EPISTAXIS)
        df = july9_assoc_isolations.candidate_frame(base, spec, code_order)

        expected_assoc = july9_assoc_isolations.expand_nodes(
            july9_assoc_isolations.ASSOC_DIFF_BROAD[july9_assoc_isolations.EPISTAXIS]["ASSOCIATION"],
            code_order,
        )
        self.assertEqual(july9_assoc_isolations.get_codes(df, july9_assoc_isolations.EPISTAXIS, "ASSOCIATION"), expected_assoc)
        self.assertEqual(july9_assoc_isolations.get_codes(df, july9_assoc_isolations.EPISTAXIS, "DIFF"), [])
        self.assertEqual(july9_assoc_isolations.get_codes(df, july9_assoc_isolations.GOUT, "ASSOCIATION"), [])
        self.assertEqual(
            july9_assoc_isolations.get_codes(df, "Chronic Obstructive Pulmonary Disease", "KEEP"),
            july9_assoc_isolations.get_codes(base, "Chronic Obstructive Pulmonary Disease", "KEEP"),
        )
        for condition in july9_assoc_isolations.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july9_assoc_isolations.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july9_assoc_isolations.get_codes(df, condition, "DIFF"), [])

    def test_july10_diff_isolations_have_twenty_dry_run_candidates(self) -> None:
        paths = july10_diff_isolations.write_july10_diff_isolations(
            561,
            ops.ROOT / "plans" / "_unit_july10_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v561_v296_diff_epistaxis.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v580_v296_diff_diabetes.csv")

    def test_july10_diff_isolations_only_populate_one_diff_bucket(self) -> None:
        base = july10_diff_isolations.pd.read_csv(july10_diff_isolations.BASE_BEST)
        code_order = july10_diff_isolations.load_code_order()
        spec = next(item for item in july10_diff_isolations.SPECS if item.condition == july10_diff_isolations.EPISTAXIS)
        df = july10_diff_isolations.candidate_frame(base, spec, code_order)

        expected_diff = july10_diff_isolations.expand_nodes(
            july10_diff_isolations.ASSOC_DIFF_BROAD[july10_diff_isolations.EPISTAXIS]["DIFF"],
            code_order,
        )
        self.assertEqual(july10_diff_isolations.get_codes(df, july10_diff_isolations.EPISTAXIS, "DIFF"), expected_diff)
        self.assertEqual(july10_diff_isolations.get_codes(df, july10_diff_isolations.EPISTAXIS, "ASSOCIATION"), [])
        self.assertEqual(july10_diff_isolations.get_codes(df, july10_diff_isolations.GOUT, "DIFF"), [])
        self.assertEqual(
            july10_diff_isolations.get_codes(df, "Chronic Obstructive Pulmonary Disease", "KEEP"),
            july10_diff_isolations.get_codes(base, "Chronic Obstructive Pulmonary Disease", "KEEP"),
        )
        for condition in july10_diff_isolations.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july10_diff_isolations.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july10_diff_isolations.get_codes(df, condition, "DIFF"), [])

    def test_july11_keep_prunes_have_twenty_dry_run_candidates(self) -> None:
        paths = july11_keep_prunes.write_july11_keep_prunes(
            601,
            ops.ROOT / "plans" / "_unit_july11_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v601_v296_icp_no_g96_g94.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v620_v296_pneumonia_no_a37_p23_j84_j85.csv")

    def test_july11_keep_prunes_only_remove_target_keep_prefixes(self) -> None:
        base = july11_keep_prunes.pd.read_csv(july11_keep_prunes.BASE_BEST)
        spec = next(item for item in july11_keep_prunes.SPECS if item.slug == "v296_hf_no_i97")
        df = july11_keep_prunes.candidate_frame(base, spec)
        original_hf = july11_keep_prunes.get_codes(base, july11_keep_prunes.HEART_FAILURE, "KEEP")
        pruned_hf = july11_keep_prunes.get_codes(df, july11_keep_prunes.HEART_FAILURE, "KEEP")

        self.assertTrue(any(code.startswith("I97") for code in original_hf))
        self.assertFalse(any(code.startswith("I97") for code in pruned_hf))
        self.assertLess(len(pruned_hf), len(original_hf))
        self.assertEqual(
            july11_keep_prunes.get_codes(df, "Chronic Obstructive Pulmonary Disease", "KEEP"),
            july11_keep_prunes.get_codes(base, "Chronic Obstructive Pulmonary Disease", "KEEP"),
        )
        self.assertEqual(july11_keep_prunes.get_codes(df, july11_keep_prunes.CKD, "KEEP"), july11_keep_prunes.get_codes(base, july11_keep_prunes.CKD, "KEEP"))
        for condition in july11_keep_prunes.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july11_keep_prunes.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july11_keep_prunes.get_codes(df, condition, "DIFF"), [])

    def test_july12_prune_assoc_has_twenty_dry_run_candidates(self) -> None:
        paths = july12_prune_assoc.write_july12_prune_assoc(
            641,
            ops.ROOT / "plans" / "_unit_july12_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v641_v296_icp_no_g96_g94_assoc.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v660_v296_derm_no_b37_assoc.csv")

    def test_july12_prune_assoc_combines_keep_prune_and_assoc_without_diff(self) -> None:
        base = july12_prune_assoc.pd.read_csv(july12_prune_assoc.BASE_BEST)
        code_order = july12_prune_assoc.load_code_order()
        spec = next(item for item in july12_prune_assoc.SPECS if item.slug == "v296_hf_no_i97_assoc")
        df = july12_prune_assoc.candidate_frame(base, spec, code_order)
        original_hf = july12_prune_assoc.get_codes(base, july12_prune_assoc.HEART_FAILURE, "KEEP")
        pruned_hf = july12_prune_assoc.get_codes(df, july12_prune_assoc.HEART_FAILURE, "KEEP")
        expected_assoc = july12_prune_assoc.expand_nodes(
            july12_prune_assoc.ASSOC_DIFF_BROAD[july12_prune_assoc.HEART_FAILURE]["ASSOCIATION"],
            code_order,
        )

        self.assertTrue(any(code.startswith("I97") for code in original_hf))
        self.assertFalse(any(code.startswith("I97") for code in pruned_hf))
        self.assertEqual(july12_prune_assoc.get_codes(df, july12_prune_assoc.HEART_FAILURE, "ASSOCIATION"), expected_assoc)
        self.assertEqual(july12_prune_assoc.get_codes(df, july12_prune_assoc.HEART_FAILURE, "DIFF"), [])
        self.assertEqual(
            july12_prune_assoc.get_codes(df, july12_prune_assoc.CKD, "KEEP"),
            july12_prune_assoc.get_codes(base, july12_prune_assoc.CKD, "KEEP"),
        )
        for condition in july12_prune_assoc.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july12_prune_assoc.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july12_prune_assoc.get_codes(df, condition, "DIFF"), [])

    def test_july13_prune_diff_has_twenty_dry_run_candidates(self) -> None:
        paths = july13_prune_diff.write_july13_prune_diff(
            681,
            ops.ROOT / "plans" / "_unit_july13_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v681_v296_icp_no_g96_g94_diff.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v700_v296_derm_no_b37_diff.csv")

    def test_july13_prune_diff_combines_keep_prune_and_diff_without_assoc(self) -> None:
        base = july13_prune_diff.pd.read_csv(july13_prune_diff.BASE_BEST)
        code_order = july13_prune_diff.load_code_order()
        spec = next(item for item in july13_prune_diff.SPECS if item.slug == "v296_hf_no_i97_diff")
        df = july13_prune_diff.candidate_frame(base, spec, code_order)
        original_hf = july13_prune_diff.get_codes(base, july13_prune_diff.HEART_FAILURE, "KEEP")
        pruned_hf = july13_prune_diff.get_codes(df, july13_prune_diff.HEART_FAILURE, "KEEP")
        expected_diff = july13_prune_diff.expand_nodes(
            july13_prune_diff.ASSOC_DIFF_BROAD[july13_prune_diff.HEART_FAILURE]["DIFF"],
            code_order,
        )

        self.assertTrue(any(code.startswith("I97") for code in original_hf))
        self.assertFalse(any(code.startswith("I97") for code in pruned_hf))
        self.assertEqual(july13_prune_diff.get_codes(df, july13_prune_diff.HEART_FAILURE, "ASSOCIATION"), [])
        self.assertEqual(july13_prune_diff.get_codes(df, july13_prune_diff.HEART_FAILURE, "DIFF"), expected_diff)
        self.assertEqual(
            july13_prune_diff.get_codes(df, july13_prune_diff.CKD, "KEEP"),
            july13_prune_diff.get_codes(base, july13_prune_diff.CKD, "KEEP"),
        )
        for condition in july13_prune_diff.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july13_prune_diff.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july13_prune_diff.get_codes(df, condition, "DIFF"), [])

    def test_july14_prune_assocdiff_has_twenty_dry_run_candidates(self) -> None:
        paths = july14_prune_assocdiff.write_july14_prune_assocdiff(
            721,
            ops.ROOT / "plans" / "_unit_july14_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v721_v296_icp_no_g96_g94_assocdiff.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v740_v296_derm_no_b37_assocdiff.csv")

    def test_july14_prune_assocdiff_combines_keep_prune_assoc_and_diff(self) -> None:
        base = july14_prune_assocdiff.pd.read_csv(july14_prune_assocdiff.BASE_BEST)
        code_order = july14_prune_assocdiff.load_code_order()
        spec = next(item for item in july14_prune_assocdiff.SPECS if item.slug == "v296_hf_no_i97_assocdiff")
        df = july14_prune_assocdiff.candidate_frame(base, spec, code_order)
        original_hf = july14_prune_assocdiff.get_codes(base, july14_prune_assocdiff.HEART_FAILURE, "KEEP")
        pruned_hf = july14_prune_assocdiff.get_codes(df, july14_prune_assocdiff.HEART_FAILURE, "KEEP")
        expected_assoc = july14_prune_assocdiff.expand_nodes(
            july14_prune_assocdiff.ASSOC_DIFF_BROAD[july14_prune_assocdiff.HEART_FAILURE]["ASSOCIATION"],
            code_order,
        )
        expected_diff = july14_prune_assocdiff.expand_nodes(
            july14_prune_assocdiff.ASSOC_DIFF_BROAD[july14_prune_assocdiff.HEART_FAILURE]["DIFF"],
            code_order,
        )

        self.assertTrue(any(code.startswith("I97") for code in original_hf))
        self.assertFalse(any(code.startswith("I97") for code in pruned_hf))
        self.assertEqual(july14_prune_assocdiff.get_codes(df, july14_prune_assocdiff.HEART_FAILURE, "ASSOCIATION"), expected_assoc)
        self.assertEqual(july14_prune_assocdiff.get_codes(df, july14_prune_assocdiff.HEART_FAILURE, "DIFF"), expected_diff)
        self.assertEqual(
            july14_prune_assocdiff.get_codes(df, july14_prune_assocdiff.CKD, "KEEP"),
            july14_prune_assocdiff.get_codes(base, july14_prune_assocdiff.CKD, "KEEP"),
        )
        for condition in july14_prune_assocdiff.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july14_prune_assocdiff.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july14_prune_assocdiff.get_codes(df, condition, "DIFF"), [])

    def test_july15_multi_keep_prunes_have_twenty_dry_run_candidates(self) -> None:
        paths = july15_multi_prunes.write_july15_multi_keep_prunes(
            761,
            ops.ROOT / "plans" / "_unit_july15_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v761_v296_portfolio_renal_metabolic_obstetric_prune.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v780_v296_portfolio_broad_private_prune.csv")

    def test_july15_multi_keep_prunes_combine_multiple_hidden_keep_edits(self) -> None:
        base = july15_multi_prunes.pd.read_csv(july15_multi_prunes.BASE_BEST)
        spec = next(item for item in july15_multi_prunes.SPECS if item.slug == "v296_portfolio_renal_metabolic_obstetric_prune")
        df = july15_multi_prunes.candidate_frame(base, spec)

        self.assertTrue(any(code.startswith("Q60") for code in july15_multi_prunes.get_codes(base, july15_multi_prunes.CKD, "KEEP")))
        self.assertFalse(any(code.startswith(("Q60", "Q61", "Q62")) for code in july15_multi_prunes.get_codes(df, july15_multi_prunes.CKD, "KEEP")))
        self.assertTrue(any(code.startswith("O24") for code in july15_multi_prunes.get_codes(base, july15_multi_prunes.DIABETES, "KEEP")))
        self.assertFalse(any(code.startswith("O24") for code in july15_multi_prunes.get_codes(df, july15_multi_prunes.DIABETES, "KEEP")))
        self.assertTrue(any(code.startswith("O23") for code in july15_multi_prunes.get_codes(base, july15_multi_prunes.UTI, "KEEP")))
        self.assertFalse(any(code.startswith(("O23", "O86", "O03")) for code in july15_multi_prunes.get_codes(df, july15_multi_prunes.UTI, "KEEP")))
        self.assertEqual(
            july15_multi_prunes.get_codes(df, "Chronic Obstructive Pulmonary Disease", "KEEP"),
            july15_multi_prunes.get_codes(base, "Chronic Obstructive Pulmonary Disease", "KEEP"),
        )
        for condition in july15_multi_prunes.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july15_multi_prunes.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july15_multi_prunes.get_codes(df, condition, "DIFF"), [])

    def test_july16_final_blends_have_twenty_dry_run_candidates(self) -> None:
        paths = july16_final_blends.write_july16_final_blends(
            801,
            ops.ROOT / "plans" / "_unit_july16_public_contingency.csv",
            dry_run=True,
        )

        self.assertEqual(len(paths), 20)
        self.assertEqual(paths[0], ops.ROOT / "submissions" / "v801_v296_final_med_v185_zero_thyroid_highconf_assoc.csv")
        self.assertEqual(paths[-1], ops.ROOT / "submissions" / "v820_v296_final_v185_add_hidden_broad_private_no_assoc.csv")

    def test_july16_final_blends_combine_final_private_axes(self) -> None:
        base = july16_final_blends.pd.read_csv(july16_final_blends.BASE_BEST)
        private = july16_final_blends.pd.read_csv(july16_final_blends.BASE_PRIVATE)
        med_positive = july16_final_blends.pd.read_csv(july16_final_blends.MED_POSITIVE)
        zero_frames = {
            condition: july16_final_blends.pd.read_csv(path)
            for condition, path in july16_final_blends.ZERO_SOURCES.items()
        }
        add_frames = {
            condition: july16_final_blends.pd.read_csv(path)
            for condition, path in july16_final_blends.ADD_SOURCES.items()
        }
        spec = next(item for item in july16_final_blends.SPECS if item.slug == "v296_final_med_v185_zero_thyroid_highconf_assoc")
        df = july16_final_blends.candidate_frame(
            base,
            private,
            med_positive,
            zero_frames,
            add_frames,
            spec,
            july16_final_blends.load_code_order(),
        )

        self.assertEqual(
            july16_final_blends.get_codes(df, july16_final_blends.MEDIASTINUM, "KEEP"),
            july16_final_blends.get_codes(med_positive, july16_final_blends.MEDIASTINUM, "KEEP"),
        )
        self.assertEqual(
            july16_final_blends.get_codes(df, july16_final_blends.CKD, "KEEP"),
            july16_final_blends.get_codes(private, july16_final_blends.CKD, "KEEP"),
        )
        self.assertEqual(
            july16_final_blends.get_codes(df, july16_final_blends.HYPERTHYROIDISM, "KEEP"),
            july16_final_blends.get_codes(zero_frames[july16_final_blends.HYPERTHYROIDISM], july16_final_blends.HYPERTHYROIDISM, "KEEP"),
        )
        self.assertNotEqual(july16_final_blends.get_codes(df, july16_final_blends.GOUT, "ASSOCIATION"), [])
        self.assertEqual(july16_final_blends.get_codes(df, july16_final_blends.GOUT, "DIFF"), [])
        for condition in july16_final_blends.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(july16_final_blends.get_codes(df, condition, "ASSOCIATION"), [])
            self.assertEqual(july16_final_blends.get_codes(df, condition, "DIFF"), [])

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

    def test_post_july4_candidate_pool_toggles_composite_dimensions(self) -> None:
        items = [
            post_july4.ScoredJuly4Item(
                item=ops.PlanItem(
                    ops.ROOT / "submissions" / "v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv",
                    "winner",
                ),
                score=0.43100,
                delta=0.00105,
            ),
            post_july4.ScoredJuly4Item(
                item=ops.PlanItem(
                    ops.ROOT / "submissions" / "v317_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_v185keep.csv",
                    "public private",
                ),
                score=0.43010,
                delta=0.00015,
            ),
        ]

        pool = post_july4.candidate_pool(items)

        self.assertGreaterEqual(len(pool), 20)
        self.assertTrue(any("no_v185keep" in candidate.slug for candidate in pool))
        self.assertTrue(any("no_med_add" in candidate.slug for candidate in pool))
        self.assertTrue(any("pulmonary_assocdiff" in candidate.slug for candidate in pool))

    def test_post_july4_candidate_pool_penalizes_high_volume_candidates(self) -> None:
        items = [
            post_july4.ScoredJuly4Item(
                item=ops.PlanItem(
                    ops.ROOT / "submissions" / "v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv",
                    "top source",
                ),
                score=0.43156,
                delta=0.00161,
            ),
            post_july4.ScoredJuly4Item(
                item=ops.PlanItem(
                    ops.ROOT / "submissions" / "v303_copd_no_j20_j45_j31_j98_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv",
                    "broad source",
                ),
                score=0.43035,
                delta=0.00040,
            ),
        ]

        pool = post_july4.candidate_pool(items)
        base = post_july4.pd.read_csv(post_july4.BASE_BEST)
        top_volumes = [
            post_july4.dataframe_change_volume(base, post_july4.candidate_frame(candidate))
            for candidate in pool[:20]
        ]

        self.assertLessEqual(max(top_volumes), post_july4.HIGH_VOLUME_SOFT_LIMIT)
        self.assertGreater(post_july4.high_volume_penalty(post_july4.HIGH_VOLUME_SOFT_LIMIT + 1), 0.0)

    def test_post_july4_candidate_frame_can_strip_v185_and_mediastinum(self) -> None:
        candidate = post_july4.Candidate(
            source=ops.ROOT / "submissions" / "v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv",
            slug="unit",
            message="unit",
            notes="unit",
            priority=1.0,
            private_keep_conditions=(),
            drop_mediastinum=True,
            assoc_buckets=("ASSOCIATION",),
        )

        frame = post_july4.candidate_frame(candidate)
        base = post_july4.pd.read_csv(post_july4.BASE_BEST)
        private = post_july4.pd.read_csv(post_july4.BASE_PRIVATE)

        self.assertEqual(
            post_july4.get_codes(frame, post_july4.MEDIASTINUM, "KEEP"),
            post_july4.get_codes(base, post_july4.MEDIASTINUM, "KEEP"),
        )
        self.assertEqual(
            post_july4.get_codes(frame, "CKD", "KEEP"),
            post_july4.get_codes(base, "CKD", "KEEP"),
        )
        self.assertNotEqual(
            post_july4.get_codes(frame, "CKD", "KEEP"),
            post_july4.get_codes(private, "CKD", "KEEP"),
        )
        for condition in post_july4.PUBLIC_ASSOC_DIFF_EMPTY:
            self.assertEqual(post_july4.get_codes(frame, condition, "ASSOCIATION"), [])
            self.assertEqual(post_july4.get_codes(frame, condition, "DIFF"), [])
        self.assertNotEqual(post_july4.get_codes(frame, "Pleurisy", "ASSOCIATION"), [])
        self.assertEqual(post_july4.get_codes(frame, "Pleurisy", "DIFF"), [])

    def test_post_july4_requires_public_neutral_source(self) -> None:
        items = [
            post_july4.ScoredJuly4Item(
                item=ops.PlanItem(
                    ops.ROOT / "submissions" / "v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv",
                    "loser",
                ),
                score=0.42800,
                delta=-0.00195,
            )
        ]

        with self.assertRaisesRegex(RuntimeError, "No July 4 composite"):
            post_july4.usable_sources(items)

    def test_post_july4_scored_items_falls_back_to_best_public_when_anchor_missing(self) -> None:
        rows = [
            {
                "fileName": "v382_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_no_v185keep_assocdiff.csv",
                "date": "2026-07-06 00:22:20",
                "description": "v382",
                "status": "complete",
                "publicScore": "0.43156",
                "privateScore": "",
            },
            {
                "fileName": "v383_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_no_v185keep_assocdiff.csv",
                "date": "2026-07-06 00:22:25",
                "description": "v383",
                "status": "complete",
                "publicScore": "0.43136",
                "privateScore": "",
            },
        ]
        with (
            tempfile.NamedTemporaryFile("w", newline="", suffix=".csv") as fh,
            patch.object(post_july4, "read_submissions", return_value=rows),
        ):
            writer = csv.DictWriter(fh, fieldnames=["file", "message", "notes"], lineterminator="\n")
            writer.writeheader()
            writer.writerow({
                "file": "submissions/v382_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_med_keep_no_v185keep_assocdiff.csv",
                "message": "v382",
                "notes": "",
            })
            writer.writerow({
                "file": "submissions/v383_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assoc_no_med_add_no_v185keep_assocdiff.csv",
                "message": "v383",
                "notes": "",
            })
            fh.flush()

            scored = post_july4.scored_items(Path(fh.name))

        self.assertAlmostEqual(scored[0].delta, 0.0)
        self.assertAlmostEqual(scored[1].delta, -0.00020)

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

    def test_preflight_surfaces_next_reset_plan_when_current_quota_is_done(self) -> None:
        rows = [
            {
                "fileName": f"v{301 + idx}.csv",
                "date": f"2026-07-04 00:{idx:02d}:00",
                "description": "used",
                "status": "complete",
                "publicScore": "0.43156",
                "privateScore": "",
            }
            for idx in range(20)
        ]
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 4, 1, 30, 0, tzinfo=timezone.utc)):
            report = ops.render_preflight(
                "2026-07-04",
                ops.ROOT / "plans" / "2026-07-04.csv",
                ops.ROOT / "plans" / "_missing_reserve.csv",
                allow_reserve=False,
                rows=rows,
            )

        self.assertIn("recommended_action=primary_already_submitted", report)
        self.assertIn("next_reset_date=2026-07-05", report)
        self.assertIn("next_reset_plan=plans/2026-07-05.csv", report)
        self.assertIn("next_reset_valid_items=20", report)
        self.assertIn("next_reset_unsubmitted_items=20", report)
        self.assertIn("next_reset_duplicate_content_items=0", report)
        self.assertIn("next_reset_selected_plan=plans/2026-07-05.csv", report)
        self.assertIn("next_reset_recommended_action=submit_primary_after_reset", report)
        self.assertIn("next_reset_manifest=ready", report)
        self.assertIn("next_reset_manifest_report=reports/2026-07-05-manifest.md", report)
        self.assertIn("next_reset_manifest_hashes=20", report)
        self.assertIn("next_reset_decision_matrix=ready", report)
        self.assertIn("next_reset_decision_matrix_report=reports/2026-07-05-decision.md", report)
        self.assertIn("next_reset_decision_comparisons=20", report)
        self.assertIn("next_reset_auto_next_plan=plans/2026-07-06.csv", report)
        self.assertIn("next_reset_auto_next_script=src/v341_360_post_july4_followups.py", report)
        self.assertIn("next_reset_auto_next_start_version=421", report)
        self.assertIn("next_reset_auto_next_contingency=plans/2026-07-06-public-contingency.csv", report)
        self.assertIn("next_reset_auto_next_contingency_exists=true", report)
        self.assertIn("next_reset_auto_next_readiness=ready", report)
        self.assertIn("next_reset_readiness=ready", report)

    def test_preflight_flags_next_reset_manifest_hash_drift(self) -> None:
        rows = [
            {
                "fileName": f"v{301 + idx}.csv",
                "date": f"2026-07-04 00:{idx:02d}:00",
                "description": "used",
                "status": "complete",
                "publicScore": "0.43156",
                "privateScore": "",
            }
            for idx in range(20)
        ]
        plan = ops.ROOT / "plans" / "2026-07-05.csv"
        first_item = ops.read_plan(plan)[0]
        first_hash = ops.file_sha256(first_item.file)
        with tempfile.TemporaryDirectory() as tmpdir:
            reports = Path(tmpdir)
            (reports / "2026-07-05-manifest.md").write_text(
                (ops.ROOT / "reports" / "2026-07-05-manifest.md").read_text().replace(
                    f"`{first_hash}`",
                    f"`{'0' * 64}`",
                    1,
                )
            )
            (reports / "2026-07-05-decision.md").write_text(
                (ops.ROOT / "reports" / "2026-07-05-decision.md").read_text()
            )
            with (
                patch.object(ops, "REPORTS", reports),
                patch.object(ops, "utc_now", return_value=datetime(2026, 7, 4, 1, 30, 0, tzinfo=timezone.utc)),
            ):
                report = ops.render_preflight(
                    "2026-07-04",
                    ops.ROOT / "plans" / "2026-07-04.csv",
                    ops.ROOT / "plans" / "_missing_reserve.csv",
                    allow_reserve=False,
                    rows=rows,
                )

        self.assertIn("next_reset_manifest=drift", report)
        self.assertIn("next_reset_manifest_drift=1", report)
        self.assertIn("next_reset_decision_matrix=ready", report)
        self.assertIn("next_reset_readiness=needs_attention", report)

    def test_preflight_flags_next_reset_missing_decision_matrix(self) -> None:
        rows = [
            {
                "fileName": f"v{301 + idx}.csv",
                "date": f"2026-07-04 00:{idx:02d}:00",
                "description": "used",
                "status": "complete",
                "publicScore": "0.43156",
                "privateScore": "",
            }
            for idx in range(20)
        ]
        with (
            patch.object(ops, "REPORTS", ops.ROOT / "reports" / "_unit_missing"),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 4, 1, 30, 0, tzinfo=timezone.utc)),
        ):
            report = ops.render_preflight(
                "2026-07-04",
                ops.ROOT / "plans" / "2026-07-04.csv",
                ops.ROOT / "plans" / "_missing_reserve.csv",
                allow_reserve=False,
                rows=rows,
            )

        self.assertIn("next_reset_selected_plan=plans/2026-07-05.csv", report)
        self.assertIn("next_reset_manifest=missing", report)
        self.assertIn("next_reset_manifest_report=reports/_unit_missing/2026-07-05-manifest.md", report)
        self.assertIn("next_reset_decision_matrix=missing", report)
        self.assertIn("next_reset_decision_matrix_report=reports/_unit_missing/2026-07-05-decision.md", report)
        self.assertIn("next_reset_auto_next_readiness=ready", report)
        self.assertIn("next_reset_readiness=needs_attention", report)

    def test_next_reset_readiness_handles_missing_selected_plan(self) -> None:
        report = "\n".join(ops.next_reset_readiness_lines("2026-07-05", None))

        self.assertIn("next_reset_decision_matrix=missing_plan", report)
        self.assertIn("next_reset_decision_matrix_report=none", report)
        self.assertIn("next_reset_manifest=missing_plan", report)
        self.assertIn("next_reset_manifest_report=none", report)
        self.assertIn("next_reset_auto_next_readiness=missing_plan", report)
        self.assertIn("next_reset_readiness=needs_attention", report)

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

    def final_selection_rows(self) -> list[dict[str, str]]:
        scored = [
            ("v296_copd_no_j20_j45_j81_j82_j93_j95.csv", "0.42995"),
            ("v293_copd_no_j20_j45_j31_j98.csv", "0.42874"),
            ("v295_copd_no_j20_j45_j93_j95.csv", "0.42835"),
            ("v294_copd_no_j20_j45_j81_j82.csv", "0.42835"),
            ("v286_assocdiff_broad_assoc.csv", "0.42828"),
            ("v283_assocdiff_highconf_assoc.csv", "0.42828"),
            ("v300_med_add_thymus_nodes.csv", "0.42707"),
            ("v288_assocdiff_cardiorenal.csv", "0.42687"),
            ("v287_assocdiff_pulmonary.csv", "0.42687"),
            ("v209_copd_no_acute_bronch_asthma.csv", "0.42687"),
            ("v205_copd_no_j93_j95.csv", "0.42583"),
            ("v204_copd_no_j81_j82.csv", "0.42583"),
            ("v203_copd_no_j45.csv", "0.42583"),
            ("v207_copd_no_j98.csv", "0.42550"),
            ("v201_copd_no_j20.csv", "0.42550"),
            ("v299_med_add_c852.csv", "0.42528"),
            ("v202_copd_no_j31.csv", "0.42517"),
            ("v200_add_npc_kw.csv", "0.42453"),
            ("v198_add_derm_kw.csv", "0.42453"),
            ("v197_add_ild_kw.csv", "0.42453"),
        ]
        return [
            {
                "fileName": filename,
                "date": f"2026-07-03 00:{idx:02d}:00",
                "description": filename,
                "status": "complete",
                "publicScore": score,
                "privateScore": "",
            }
            for idx, (filename, score) in enumerate(scored, start=1)
        ]

    def test_render_reset_readiness_summarizes_pre_reset_gates(self) -> None:
        rows = self.final_selection_rows()
        kernels = [{
            "ref": "known/notebook",
            "title": "Known",
            "author": "Author",
            "lastRunTime": "2026-07-01 00:00:00",
            "totalVotes": "1",
        }]
        with (
            patch.object(ops, "REPORTS", ops.ROOT / "reports" / "_unit_missing"),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 5, 0, tzinfo=timezone.utc)),
        ):
            report = ops.render_reset_readiness(
                "2026-07-04",
                rows,
                kernels,
                {"known/notebook"},
                {"known/notebook": "2026-07-01 00:00:00"},
            )

        self.assertIn("# CohortX Reset Readiness — 2026-07-04", report)
        self.assertIn("- Recommended action: `wait_for_target_date`", report)
        self.assertIn("- Selected plan: `plans/2026-07-04.csv`", report)
        self.assertIn("- Final selection: 20/20", report)
        self.assertIn("- Manifest: `reports/_unit_missing/2026-07-04-manifest.md` with NA unique SHA-256 files", report)
        self.assertIn("- Decision matrix: `reports/_unit_missing/2026-07-04-decision.md` with NA matched comparisons", report)
        self.assertIn("- Auto next plan: `plans/2026-07-05.csv` via `src/v341_360_post_july4_followups.py` start_version=421; contingency_exists=true", report)
        self.assertIn("| quota | ready_at_reset |", report)
        self.assertIn("| selected_plan | ready |", report)
        self.assertIn("| manifest | missing |", report)
        self.assertIn("| decision_matrix | missing |", report)
        self.assertIn("| auto_next_plan | ready_existing |", report)
        self.assertIn("public_notebooks_new=0", report)
        self.assertIn(".venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan", report)
        self.assertIn("Do not pass `--date` during the live reset run", report)
        self.assertIn("```text\npreflight_date=2026-07-04", report)
        self.assertNotIn("seconds_until_deadline=", report)
        self.assertNotIn("seconds_until_reset=", report)

    def test_render_reset_readiness_marks_existing_decision_matrix_ready(self) -> None:
        rows = self.final_selection_rows()
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 4, 5, 0, tzinfo=timezone.utc)):
            report = ops.render_reset_readiness(
                "2026-07-05",
                rows,
                [],
                set(),
                {},
            )

        self.assertIn("- Manifest: `reports/2026-07-05-manifest.md` with 20 unique SHA-256 files; drift=0", report)
        self.assertIn("| manifest | ready | report=`reports/2026-07-05-manifest.md`; hashes=20/20; drift=0 |", report)
        self.assertIn("- Decision matrix: `reports/2026-07-05-decision.md` with 20 matched comparisons", report)
        self.assertIn("| decision_matrix | ready | report=`reports/2026-07-05-decision.md`; matched=20 |", report)
        self.assertIn("- Auto next plan: `plans/2026-07-06.csv` via `src/v341_360_post_july4_followups.py` start_version=421; contingency_exists=true", report)
        self.assertIn("| auto_next_plan | ready_existing | next=`plans/2026-07-06.csv`; script=`src/v341_360_post_july4_followups.py`; start=421; contingency=`plans/2026-07-06-public-contingency.csv`; contingency_exists=true |", report)

    def test_render_reset_readiness_blocks_on_new_public_notebook(self) -> None:
        with patch.object(ops, "utc_now", return_value=datetime(2026, 7, 3, 5, 0, tzinfo=timezone.utc)):
            report = ops.render_reset_readiness(
                "2026-07-04",
                self.final_selection_rows(),
                [{
                    "ref": "author/new-notebook",
                    "title": "New",
                    "author": "Author",
                    "lastRunTime": "2026-07-03 00:00:00",
                    "totalVotes": "1",
                }],
                set(),
                {},
            )

        self.assertIn("- Public notebooks: new=1, updated=0", report)
        self.assertIn("| notebook_guard | blocked | public_notebooks_new=1; public_notebooks_updated=0 |", report)

    def test_render_deadline_readiness_calendar_summarizes_remaining_coverage(self) -> None:
        report = ops.render_deadline_readiness_calendar(
            rows=[],
            start_date="2026-07-05",
            end_date="2026-07-07",
            now=datetime(2026, 7, 4, 5, 0, tzinfo=timezone.utc),
        )

        self.assertIn("# CohortX Deadline Readiness Calendar", report)
        self.assertIn("- Audit current UTC date: 2026-07-04", report)
        self.assertIn("- Dates audited: 3", report)
        self.assertIn("- Coverage ready/spent: 3/3", report)
        self.assertIn("- Public contingency fallback days: 1", report)
        self.assertIn("- Future unsubmitted slots protected: 60", report)
        self.assertIn("| 2026-07-05 | future | `plans/2026-07-05.csv` (primary) | ready | 20 | 20 | 0 | ready (20; `reports/2026-07-05-decision.md`) | ready_existing (`plans/2026-07-06.csv`) | ok |", report)
        self.assertIn("| 2026-07-06 | future | `plans/2026-07-06.csv` (primary) | ready | 20 | 20 | 0 | ready (15; `reports/2026-07-06-decision.md`) | ready (`plans/2026-07-07.csv`) | ok |", report)
        self.assertIn("| 2026-07-07 | future | `plans/2026-07-07-public-contingency.csv` (public_contingency) | fallback_ready | 20 | 20 | 0 | ready (18; `reports/2026-07-07-public-contingency-decision.md`) | ready (`plans/2026-07-08.csv`) | primary_missing_using_public_contingency |", report)
        self.assertIn("- No hard coverage gaps in the audited window.", report)

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

    def test_render_final_candidates_supplements_truncated_history_and_near_best_hedges(self) -> None:
        rows = [
            {
                "fileName": "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
                "date": "2026-07-03 00:22:54",
                "description": "best public",
                "status": "complete",
                "publicScore": "0.42995",
                "privateScore": "",
            },
            {
                "fileName": "v283_assocdiff_highconf_assoc.csv",
                "date": "2026-07-03 00:21:50",
                "description": "near-best assoc",
                "status": "complete",
                "publicScore": "0.42828",
                "privateScore": "",
            },
            {
                "fileName": "v287_assocdiff_pulmonary.csv",
                "date": "2026-07-03 00:22:10",
                "description": "near-best pulmonary hedge",
                "status": "complete",
                "publicScore": "0.42687",
                "privateScore": "",
            },
            {
                "fileName": "v293_copd_no_j20_j45_j31_j98.csv",
                "date": "2026-07-03 00:22:39",
                "description": "near-best public hedge",
                "status": "complete",
                "publicScore": "0.42874",
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
        recommended = report.split("## Recommended Final Selection")[1]
        recommended = recommended.split("## Neutral Hedge Watchlist")[0].split("## Top Public Submissions")[0]

        self.assertIn("Near-best submissions within 0.00325: 4", report)
        self.assertIn("Public anchor", recommended)
        self.assertIn("v178_FINAL.csv", recommended)
        self.assertIn("Private hedge", recommended)
        self.assertIn("v185_private_kw.csv", recommended)
        self.assertIn("Best public/tied", recommended)
        self.assertIn("v296_copd_no_j20_j45_j81_j82_j93_j95.csv", recommended)
        self.assertIn("Strategic ASSOC/DIFF hedge", recommended)
        self.assertIn("v283_assocdiff_highconf_assoc.csv", recommended)
        self.assertIn("v287_assocdiff_pulmonary.csv", recommended)
        self.assertIn("Near-best public hedge", recommended)
        self.assertIn("v293_copd_no_j20_j45_j31_j98.csv", recommended)
        self.assertNotIn("v186_zero_copd.csv", recommended)

    def test_render_final_candidates_fills_controlled_public_reserves_to_limit(self) -> None:
        rows = self.final_selection_rows()

        report = ops.render_final_candidates(rows, ops.DEFAULT_ANCHOR)
        csv_text = ops.render_final_selection_csv(rows, ops.DEFAULT_ANCHOR)

        self.assertIn("Recommended final selection: 20/20", report)
        self.assertIn("Controlled public reserve", report)
        self.assertIn("v205_copd_no_j93_j95.csv", report)
        self.assertIn("controlled public reserves down to 0.00600 below best", report)
        self.assertEqual(len(csv_text.strip().splitlines()), 21)
        self.assertIn("slot,role,file,public,change_volume,changed_conditions", csv_text.splitlines()[0])
        self.assertIn("Controlled public reserve", csv_text)

    def test_render_final_selection_audit_flags_copd_concentration(self) -> None:
        audit = ops.render_final_selection_audit(self.final_selection_rows(), ops.DEFAULT_ANCHOR)

        self.assertIn("# CohortX Final Selection Audit", audit)
        self.assertIn("- Slots: 20/20", audit)
        self.assertIn("- ASSOC/DIFF hedge slots: 4", audit)
        self.assertIn("- Dominant changed condition: Chronic Obstructive Pulmonary Disease (17/20)", audit)
        self.assertIn("| condition_concentration | crowded |", audit)
        self.assertIn("| assoc_diff_hedges | ready | slots=4; minimum=4 |", audit)
        self.assertIn("Replacement priority: swap lowest-value COPD-only controlled reserves", audit)

    def test_render_final_diversity_watchlist_finds_concentration_breakers(self) -> None:
        report = ops.render_final_diversity_watchlist(self.final_selection_rows(), ops.DEFAULT_ANCHOR)

        self.assertIn("# CohortX Final Diversity Watchlist", report)
        self.assertIn("| selection_concentration | crowded |", report)
        self.assertIn("| diversity_alternatives | ready |", report)
        self.assertIn("## Concentration Breakers", report)
        self.assertIn("Crowded hits", report)
        self.assertIn("Prefer the lowest `Crowded hits` candidates", report)
        self.assertIn("v198_add_derm_kw.csv", report)

    def test_write_final_candidates_also_writes_diversity_watchlist(self) -> None:
        with tempfile.TemporaryDirectory(dir=ops.REPORTS) as tmpdir:
            target = Path(tmpdir) / "final-candidates.md"
            rows = self.final_selection_rows()
            with patch.object(ops, "read_submissions", return_value=rows):
                ops.write_final_candidates(ops.DEFAULT_ANCHOR, target)

            self.assertTrue(target.exists())
            self.assertTrue((Path(tmpdir) / "final-selection.csv").exists())
            self.assertTrue((Path(tmpdir) / "final-selection-audit.md").exists())
            diversity = Path(tmpdir) / "final-diversity.md"
            self.assertTrue(diversity.exists())
            self.assertIn("# CohortX Final Diversity Watchlist", diversity.read_text())

    def test_render_final_selection_audit_excludes_protected_slots_from_public_floor(self) -> None:
        rows = [
            {
                "fileName": "v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv",
                "date": "2026-07-04 00:21:09",
                "description": "new best public",
                "status": "complete",
                "publicScore": "0.43156",
                "privateScore": "",
            },
            {
                "fileName": "v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv",
                "date": "2026-07-04 00:21:04",
                "description": "new best public tied",
                "status": "complete",
                "publicScore": "0.43156",
                "privateScore": "",
            },
            {
                "fileName": "v296_copd_no_j20_j45_j81_j82_j93_j95.csv",
                "date": "2026-07-03 00:22:54",
                "description": "prior best public",
                "status": "complete",
                "publicScore": "0.42995",
                "privateScore": "",
            },
        ]

        audit = ops.render_final_selection_audit(rows, ops.DEFAULT_ANCHOR)

        self.assertIn("- Max public drop in selection: 0.00703", audit)
        self.assertIn("- Max replaceable public drop: 0.00161", audit)
        self.assertIn("- Max protected anchor/hedge drop: 0.00703", audit)
        self.assertIn("| public_floor | ready | replaceable_max_drop=0.00161; tolerance=0.00600; protected_slots=2 |", audit)

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

    def test_generate_next_plan_uses_next_available_start_version(self) -> None:
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
        self.assertEqual(args[args.index("--start-version") + 1], "421")
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
        self.assertEqual(args[args.index("--start-version") + 1], "421")
        self.assertFalse(target.exists())

    def test_generate_next_plan_skips_reserved_existing_version_range(self) -> None:
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
                ops.ROOT / "plans" / "2026-07-04.csv",
                target,
                None,
            )

        args = run.call_args.args[0]
        self.assertIn("v341_360_post_july4_followups.py", args[1])
        self.assertEqual(args[args.index("--start-version") + 1], "421")
        self.assertFalse(target.exists())

    def test_generate_next_plan_writes_decision_matrix_after_success(self) -> None:
        target = ops.ROOT / "plans" / "_unit_next.csv"
        if target.exists():
            target.unlink()

        completed = subprocess.CompletedProcess(
            args=["fake"],
            returncode=0,
            stdout="generated",
            stderr=None,
        )
        with (
            patch.object(ops.subprocess, "run", return_value=completed),
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(target, "message")]) as validate_plan,
            patch.object(ops, "write_plan_report") as write_plan_report,
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
        ):
            ops.generate_next_plan(
                ops.ROOT / "plans" / "2026-07-04.csv",
                target,
                None,
            )

        validate_plan.assert_called_once_with(target)
        write_plan_report.assert_called_once_with(target, ops.DEFAULT_ANCHOR, None)
        write_plan_strategy_audit.assert_called_once_with(target, ops.DEFAULT_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(target, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(target, ops.DEFAULT_ANCHOR, None)

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
        self.assertTrue(result.plan_scored)
        self.assertEqual(result.unsubmitted_before, 0)
        self.assertEqual(result.scored_after, 1)
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

    def test_submit_plan_result_requires_scores_when_present(self) -> None:
        legacy = ops.SubmitPlanResult(1, 1, 1, 1)
        pending_scores = ops.SubmitPlanResult(1, 1, 1, 1, 0)
        scored = ops.SubmitPlanResult(1, 1, 1, 1, 1)

        self.assertTrue(legacy.plan_complete)
        self.assertTrue(legacy.plan_scored)
        self.assertTrue(pending_scores.plan_complete)
        self.assertFalse(pending_scores.plan_scored)
        self.assertTrue(scored.plan_scored)

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
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(1, 1, 1, 1)) as submit_plan,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_decision_outcome") as write_plan_decision_outcome,
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
        write_plan_strategy_audit.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
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
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_decision_outcome") as write_plan_decision_outcome,
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
        write_plan_strategy_audit.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
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
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
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
        write_plan_strategy_audit.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
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
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
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
        write_plan_strategy_audit.assert_not_called()
        write_plan_manifest.assert_not_called()
        write_plan_decision_matrix.assert_not_called()
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
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(1, 1, 1, 1)) as submit_plan,
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_decision_outcome") as write_plan_decision_outcome,
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
        write_plan_strategy_audit.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
        write_plan_delta_report.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR)
        submit_plan.assert_called_once_with(reserve_plan, dry_run=False, wait=True)
        write_intel.assert_called_once_with("2026-07-03", None)
        write_review.assert_called_once_with("2026-07-03", None)
        write_signals.assert_called_once_with("2026-07-03", ops.DEFAULT_ANCHOR, None)
        write_plan_scorecard.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
        write_plan_decision_outcome.assert_called_once_with(reserve_plan, ops.PRIVATE_ANCHOR, None)
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
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(1, 1, 1, 1)) as submit_plan,
            patch.object(ops, "write_intel") as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_decision_outcome") as write_plan_decision_outcome,
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
        write_plan_strategy_audit.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR, None)
        write_plan_delta_report.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR)
        submit_plan.assert_called_once_with(contingency_plan, dry_run=False, wait=True)
        write_intel.assert_called_once_with("2026-07-03", None)
        write_review.assert_called_once_with("2026-07-03", None)
        write_signals.assert_called_once_with("2026-07-03", ops.DEFAULT_ANCHOR, None)
        write_plan_scorecard.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_outcome.assert_called_once_with(contingency_plan, ops.DEFAULT_ANCHOR, None)
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
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
            patch.object(ops, "write_plan_delta_report") as write_plan_delta_report,
            patch.object(ops, "submit_plan", side_effect=record_submit),
            patch.object(ops, "write_intel", side_effect=record_intel) as write_intel,
            patch.object(ops, "write_review") as write_review,
            patch.object(ops, "write_signals") as write_signals,
            patch.object(ops, "write_plan_scorecard") as write_plan_scorecard,
            patch.object(ops, "write_plan_decision_outcome") as write_plan_decision_outcome,
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
        write_plan_strategy_audit.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        write_review.assert_called_once_with("2026-07-02", None)
        write_signals.assert_called_once_with("2026-07-02", ops.DEFAULT_ANCHOR, None)
        write_plan_scorecard.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_outcome.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_impact_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        write_final_candidates.assert_called_once_with(ops.DEFAULT_ANCHOR, None)
        generate_next_plan.assert_called_once_with(plan, next_plan, 221)

    def test_daily_run_waits_for_scores_before_post_reports_and_next_plan(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-03.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status"),
            patch.object(ops, "print_preflight"),
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "write_plan_strategy_audit"),
            patch.object(ops, "write_plan_manifest"),
            patch.object(ops, "write_plan_decision_matrix"),
            patch.object(ops, "write_plan_delta_report"),
            patch.object(ops, "submit_plan", return_value=ops.SubmitPlanResult(1, 1, 1, 1, 0)),
            patch.object(ops, "write_intel"),
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
        self.assertIn("score_guard=waiting_for_scores", output)
        self.assertIn("post_reports_guard=no_current_plan_activity", output)
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_plan_impact_report.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_does_not_generate_next_plan_when_plan_incomplete(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        next_plan = ops.ROOT / "plans" / "2026-07-03.csv"
        with (
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status"),
            patch.object(ops, "print_preflight") as print_preflight,
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
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
        write_plan_strategy_audit.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        write_plan_impact_report.assert_not_called()
        generate_next_plan.assert_not_called()

    def test_daily_run_respects_preflight_wait_for_quota_guard(self) -> None:
        plan = ops.ROOT / "plans" / "2026-07-02.csv"
        buf = io.StringIO()
        with (
            contextlib.redirect_stdout(buf),
            patch.object(ops, "utc_now", return_value=datetime(2026, 7, 2, 0, 20, tzinfo=timezone.utc)),
            patch.object(ops, "print_status"),
            patch.object(
                ops,
                "print_preflight",
                return_value=(
                    "preflight_date=2026-07-02\n"
                    "target_date_relation=current\n"
                    "recommended_action=wait_for_quota\n"
                    "selected_plan=plans/2026-07-02.csv"
                ),
            ),
            patch.object(ops, "validate_plan", return_value=[ops.PlanItem(plan, "message")]),
            patch.object(ops, "write_plan_report"),
            patch.object(ops, "write_plan_strategy_audit"),
            patch.object(ops, "write_plan_manifest"),
            patch.object(ops, "write_plan_decision_matrix"),
            patch.object(ops, "write_plan_delta_report"),
            patch.object(ops, "submit_plan") as submit_plan,
            patch.object(ops, "write_intel"),
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
        self.assertIn("preflight_guard=wait_for_quota", output)
        self.assertIn("post_reports_guard=no_current_plan_activity", output)
        submit_plan.assert_not_called()
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_plan_impact_report.assert_not_called()
        write_final_candidates.assert_not_called()
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
            patch.object(ops, "write_plan_strategy_audit") as write_plan_strategy_audit,
            patch.object(ops, "write_plan_manifest") as write_plan_manifest,
            patch.object(ops, "write_plan_decision_matrix") as write_plan_decision_matrix,
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
        write_plan_strategy_audit.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_manifest.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_decision_matrix.assert_called_once_with(plan, ops.DEFAULT_ANCHOR, None)
        write_plan_delta_report.assert_called_once_with(plan, ops.DEFAULT_ANCHOR)
        write_review.assert_not_called()
        write_signals.assert_not_called()
        write_plan_scorecard.assert_not_called()
        write_plan_impact_report.assert_not_called()
        write_final_candidates.assert_not_called()
        generate_next_plan.assert_not_called()


if __name__ == "__main__":
    unittest.main()
