"""Operational helpers for the CohortX Task 3 submission loop."""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


COMPETITION = "cohort-x-task-3"
EXPECTED_COLUMNS = ["Condition", "KEEP", "ASSOCIATION", "DIFF"]
DAILY_LIMIT = 20
FINAL_SELECTION_LIMIT = 20
MAX_RECOMMENDED_CHANGE_VOLUME = 1000
COMPETITION_DEADLINE_UTC = datetime(2026, 7, 16, 11, 59, tzinfo=timezone.utc)
ROOT = Path(__file__).resolve().parents[1]
KAGGLE = ROOT / ".venv" / "bin" / "kaggle"
REPORTS = ROOT / "reports"
DEFAULT_ANCHOR = ROOT / "submissions" / "v178_FINAL.csv"
PRIVATE_ANCHOR = ROOT / "submissions" / "v185_private_kw.csv"
csv.field_size_limit(10_000_000)
BRT = timezone(timedelta(hours=-3))


@dataclass(frozen=True)
class PlanItem:
    file: Path
    message: str
    notes: str = ""


@dataclass(frozen=True)
class SubmitPlanResult:
    plan_items: int
    unsubmitted_before: int
    submitted_now: int
    submitted_after: int

    @property
    def plan_complete(self) -> bool:
        return self.submitted_after >= self.plan_items


def kaggle_cmd() -> str:
    return str(KAGGLE) if KAGGLE.exists() else "kaggle"


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [kaggle_cmd(), *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def clean_kaggle_csv(text: str, header: str) -> str:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if line.startswith(header):
            return "\n".join(lines[idx:]) + "\n"
    raise RuntimeError(f"Kaggle CSV header not found: {header}\n{text[:1000]}")


def read_submissions() -> list[dict[str, str]]:
    proc = run(["competitions", "submissions", "-c", COMPETITION, "-v"])
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    payload = clean_kaggle_csv(proc.stdout, "fileName,date,description,status,publicScore,privateScore")
    return list(csv.DictReader(payload.splitlines()))


def read_kernels() -> list[dict[str, str]]:
    proc = run([
        "kernels",
        "list",
        "--competition",
        COMPETITION,
        "--sort-by",
        "dateRun",
        "--page-size",
        "20",
        "-v",
    ])
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    payload = clean_kaggle_csv(proc.stdout, "ref,title,author,lastRunTime,totalVotes")
    return list(csv.DictReader(payload.splitlines()))


def read_leaderboard_top() -> list[dict[str, str]]:
    proc = run(["competitions", "leaderboard", COMPETITION, "--show", "-v"])
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    payload = clean_kaggle_csv(proc.stdout, "teamId,teamName,submissionDate,score")
    return list(csv.DictReader(payload.splitlines()))


def discussion_status(timeout_s: int = 20) -> dict[str, str]:
    url = f"https://www.kaggle.com/competitions/{COMPETITION}/discussion"
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(request, timeout=timeout_s) as response:
            html = response.read().decode("utf-8", "ignore")
    except (OSError, URLError) as exc:
        return {"url": url, "status": "error", "detail": str(exc)}
    lower = html.lower()
    markers = [
        marker
        for marker in ("discussion", "no discussions", "new prize", "cohortx")
        if marker in lower
    ]
    status = "static_markers_found" if any(marker != "cohortx" for marker in markers) else "js_shell_only"
    return {
        "url": url,
        "status": status,
        "chars": str(len(html)),
        "markers": ", ".join(markers) if markers else "none",
    }


def known_notebook_refs() -> set[str]:
    refs: set[str] = set()
    for path in (ROOT / "external_notebooks").glob("*/kernel-metadata.json"):
        try:
            payload = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        ref = payload.get("id")
        if isinstance(ref, str) and ref:
            refs.add(ref)
    return refs


def parse_kaggle_date(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def format_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def format_brt(value: datetime) -> str:
    return value.astimezone(BRT).strftime("%Y-%m-%d %H:%M:%S BRT")


def next_quota_reset(now: datetime | None = None) -> datetime:
    current = now.astimezone(timezone.utc) if now else utc_now()
    tomorrow = current.date() + timedelta(days=1)
    return datetime(tomorrow.year, tomorrow.month, tomorrow.day, tzinfo=timezone.utc)


def seconds_until_reset(now: datetime | None = None) -> int:
    current = now.astimezone(timezone.utc) if now else utc_now()
    return max(0, int((next_quota_reset(current) - current).total_seconds()))


def seconds_until_deadline(now: datetime | None = None) -> int:
    current = now.astimezone(timezone.utc) if now else utc_now()
    return max(0, int((COMPETITION_DEADLINE_UTC - current).total_seconds()))


def competition_is_open(now: datetime | None = None) -> bool:
    current = now.astimezone(timezone.utc) if now else utc_now()
    return current <= COMPETITION_DEADLINE_UTC


def target_after_deadline(date_value: str) -> bool:
    target = datetime.strptime(date_value, "%Y-%m-%d").date()
    return target > COMPETITION_DEADLINE_UTC.date()


def submissions_today(rows: list[dict[str, str]], now: datetime | None = None) -> list[dict[str, str]]:
    current = now.astimezone(timezone.utc) if now else utc_now()
    today = current.date()
    return [row for row in rows if parse_kaggle_date(row["date"]).date() == today]


def submissions_on_date(rows: list[dict[str, str]], date_value: str) -> list[dict[str, str]]:
    target = datetime.strptime(date_value, "%Y-%m-%d").date()
    return [row for row in rows if parse_kaggle_date(row["date"]).date() == target]


def target_date_relation(date_value: str, now: datetime | None = None) -> str:
    target = datetime.strptime(date_value, "%Y-%m-%d").date()
    current = (now.astimezone(timezone.utc) if now else utc_now()).date()
    if target < current:
        return "past"
    if target > current:
        return "future"
    return "current"


def remote_filenames(rows: list[dict[str, str]]) -> set[str]:
    return {row["fileName"] for row in rows}


def submission_content_key(path: Path) -> tuple[tuple[str, ...], ...]:
    validate_submission(path)
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        return tuple(tuple(row[column] for column in EXPECTED_COLUMNS) for row in reader)


def submitted_content_keys(rows: list[dict[str, str]]) -> dict[tuple[tuple[str, ...], ...], str]:
    keys: dict[tuple[tuple[str, ...], ...], str] = {}
    for row in rows:
        path = local_submission_path(row["fileName"])
        if not path.exists():
            continue
        keys.setdefault(submission_content_key(path), row["fileName"])
    return keys


def plan_accounted_count(
    items: list[PlanItem],
    submitted_names: set[str],
    submitted_content: dict[tuple[tuple[str, ...], ...], str],
) -> int:
    count = 0
    for item in items:
        if item.file.name in submitted_names or submission_content_key(item.file) in submitted_content:
            count += 1
    return count


def public_score(row: dict[str, str]) -> float | None:
    value = row.get("publicScore", "")
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def best_public(rows: list[dict[str, str]]) -> float | None:
    scores = [score for row in rows if (score := public_score(row)) is not None]
    return max(scores) if scores else None


def validate_submission(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"{path}: bad columns {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 23:
        raise ValueError(f"{path}: expected 23 rows, found {len(rows)}")
    for idx, row in enumerate(rows, start=2):
        if not row["Condition"].strip():
            raise ValueError(f"{path}: empty Condition on CSV line {idx}")
        for col in EXPECTED_COLUMNS[1:]:
            if row[col] is None or not str(row[col]).strip():
                raise ValueError(f"{path}: empty {col} on CSV line {idx}")


def read_submission_file(path: Path) -> dict[str, dict[str, str]]:
    validate_submission(path)
    with path.open(newline="") as fh:
        return {row["Condition"]: row for row in csv.DictReader(fh)}


def parse_codes(value: str) -> set[str]:
    if not value or value == "Not Applicable":
        return set()
    return {code.strip() for code in value.split(";") if code.strip()}


def submission_changes(anchor: Path, candidate: Path) -> list[tuple[str, str]]:
    base_rows = read_submission_file(anchor)
    candidate_rows = read_submission_file(candidate)
    changes: list[tuple[str, str]] = []
    for condition in base_rows:
        summaries = []
        for column in EXPECTED_COLUMNS[1:]:
            before = parse_codes(base_rows[condition][column])
            after = parse_codes(candidate_rows[condition][column])
            if before == after:
                continue
            added = len(after - before)
            removed = len(before - after)
            summaries.append(f"{column} +{added}/-{removed}")
        if summaries:
            changes.append((condition, ", ".join(summaries)))
    return changes


def read_plan(path: Path) -> list[PlanItem]:
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        required = {"file", "message"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"{path}: required columns are file,message")
        items = []
        for row in reader:
            rel = Path(row["file"])
            if rel.is_absolute() or ".." in rel.parts:
                raise ValueError(f"{path}: unsafe file path {rel}")
            items.append(PlanItem(ROOT / rel, row["message"], row.get("notes", "")))
    return items


def duplicate_plan_content(items: list[PlanItem]) -> list[tuple[PlanItem, PlanItem]]:
    seen: dict[tuple[tuple[str, ...], ...], PlanItem] = {}
    duplicates: list[tuple[PlanItem, PlanItem]] = []
    for item in items:
        key = submission_content_key(item.file)
        original = seen.get(key)
        if original is not None:
            duplicates.append((item, original))
            continue
        seen[key] = item
    return duplicates


def validate_plan(path: Path) -> list[PlanItem]:
    items = read_plan(path)
    for item in items:
        validate_submission(item.file)
    duplicates = duplicate_plan_content(items)
    if duplicates:
        examples = ", ".join(
            f"{duplicate.file.relative_to(ROOT)} matches {original.file.relative_to(ROOT)}"
            for duplicate, original in duplicates[:5]
        )
        raise ValueError(f"{path}: duplicate submission content within plan: {examples}")
    return items


def plan_notes_for_date(date_value: str) -> dict[str, PlanItem]:
    plan_path = ROOT / "plans" / f"{date_value}.csv"
    if not plan_path.exists():
        return {}
    return {item.file.name: item for item in read_plan(plan_path)}


def print_status() -> None:
    comp = run(["competitions", "list", "-s", COMPETITION])
    print(comp.stdout.strip())
    now = utc_now()
    rows = read_submissions()
    today = submissions_today(rows, now)
    best = best_public(rows)
    reset = next_quota_reset(now)
    print(f"submissions_today_utc={len(today)}/{DAILY_LIMIT}")
    print(f"next_quota_reset_utc={format_utc(reset)}")
    print(f"next_quota_reset_brt={format_brt(reset)}")
    print(f"seconds_until_reset={seconds_until_reset(now)}")
    print(f"competition_deadline_utc={format_utc(COMPETITION_DEADLINE_UTC)}")
    print(f"competition_deadline_brt={format_brt(COMPETITION_DEADLINE_UTC)}")
    print(f"seconds_until_deadline={seconds_until_deadline(now)}")
    print(f"competition_open={str(competition_is_open(now)).lower()}")
    print(f"best_public={best:.5f}" if best is not None else "best_public=NA")
    print("latest:")
    for row in rows[: min(25, len(rows))]:
        print(f"{row['date']} {row['fileName']} {row['status']} {row.get('publicScore', '')}")


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def resolve_path(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def inspect_plan(
    path: Path,
    submitted: set[str],
    submitted_content: dict[tuple[tuple[str, ...], ...], str] | None = None,
) -> tuple[list[PlanItem], list[PlanItem], list[PlanItem]]:
    items = validate_plan(path)
    content = submitted_content or {}
    unsubmitted: list[PlanItem] = []
    duplicate_content: list[PlanItem] = []
    for item in items:
        if item.file.name in submitted:
            continue
        if submission_content_key(item.file) in content:
            duplicate_content.append(item)
            continue
        unsubmitted.append(item)
    return items, unsubmitted, duplicate_content


def render_preflight(
    date_value: str,
    plan_path: Path | None,
    reserve_path: Path | None,
    allow_reserve: bool,
    rows: list[dict[str, str]],
    contingency_path: Path | None = None,
) -> str:
    primary = resolve_path(plan_path or (ROOT / "plans" / f"{date_value}.csv"))
    contingency = resolve_path(contingency_path or (ROOT / "plans" / f"{date_value}-public-contingency.csv"))
    reserve = resolve_path(reserve_path or (ROOT / "plans" / f"{date_value}-reserve.csv"))
    now = utc_now()
    today = submissions_today(rows, now)
    remaining = max(0, DAILY_LIMIT - len(today))
    submitted = remote_filenames(rows)
    submitted_content = submitted_content_keys(rows)
    reset = next_quota_reset(now)
    relation = target_date_relation(date_value, now)
    open_for_submissions = competition_is_open(now)
    target_expired = target_after_deadline(date_value)

    lines = [
        f"preflight_date={date_value}",
        f"current_utc_date={now.date().isoformat()}",
        f"target_date_relation={relation}",
        f"competition_deadline_utc={format_utc(COMPETITION_DEADLINE_UTC)}",
        f"competition_deadline_brt={format_brt(COMPETITION_DEADLINE_UTC)}",
        f"seconds_until_deadline={seconds_until_deadline(now)}",
        f"competition_open={str(open_for_submissions).lower()}",
        f"target_after_deadline={str(target_expired).lower()}",
        f"quota_used_utc={len(today)}/{DAILY_LIMIT}",
        f"quota_remaining={remaining}",
        f"next_quota_reset_utc={format_utc(reset)}",
        f"next_quota_reset_brt={format_brt(reset)}",
        f"seconds_until_reset={seconds_until_reset(now)}",
        f"best_public={best_public(rows):.5f}" if best_public(rows) is not None else "best_public=NA",
        f"primary_plan={display_path(primary)}",
        f"primary_exists={str(primary.exists()).lower()}",
    ]

    primary_items: list[PlanItem] = []
    primary_unsubmitted: list[PlanItem] = []
    if primary.exists():
        primary_items, primary_unsubmitted, primary_duplicates = inspect_plan(primary, submitted, submitted_content)
        lines.extend([
            f"primary_valid_items={len(primary_items)}",
            f"primary_unsubmitted_items={len(primary_unsubmitted)}",
            f"primary_duplicate_content_items={len(primary_duplicates)}",
        ])

    lines.extend([
        f"contingency_plan={display_path(contingency)}",
        f"contingency_exists={str(contingency.exists()).lower()}",
    ])

    contingency_items: list[PlanItem] = []
    contingency_unsubmitted: list[PlanItem] = []
    if contingency.exists():
        contingency_items, contingency_unsubmitted, contingency_duplicates = inspect_plan(contingency, submitted, submitted_content)
        lines.extend([
            f"contingency_valid_items={len(contingency_items)}",
            f"contingency_unsubmitted_items={len(contingency_unsubmitted)}",
            f"contingency_duplicate_content_items={len(contingency_duplicates)}",
        ])

    lines.extend([
        f"reserve_plan={display_path(reserve)}",
        f"reserve_exists={str(reserve.exists()).lower()}",
        f"reserve_allowed={str(allow_reserve).lower()}",
    ])

    reserve_items: list[PlanItem] = []
    reserve_unsubmitted: list[PlanItem] = []
    if reserve.exists():
        reserve_items, reserve_unsubmitted, reserve_duplicates = inspect_plan(reserve, submitted, submitted_content)
        lines.extend([
            f"reserve_valid_items={len(reserve_items)}",
            f"reserve_unsubmitted_items={len(reserve_unsubmitted)}",
            f"reserve_duplicate_content_items={len(reserve_duplicates)}",
        ])

    selected: Path | None = None
    if not open_for_submissions:
        action = "competition_closed"
    elif target_expired:
        action = "target_after_deadline"
    elif relation == "future":
        selected = primary if primary.exists() else contingency if contingency.exists() else None
        action = "wait_for_target_date"
    elif relation == "past":
        selected = primary if primary.exists() else contingency if contingency.exists() else None
        action = "stale_plan_date"
    elif primary.exists():
        selected = primary
        if not primary_unsubmitted:
            action = "primary_already_submitted"
        elif remaining <= 0:
            action = "wait_for_quota"
        else:
            action = "submit_primary"
    elif contingency.exists():
        selected = contingency
        if not contingency_unsubmitted:
            action = "contingency_already_submitted"
        elif remaining <= 0:
            action = "wait_for_quota"
        else:
            action = "submit_public_contingency"
    elif reserve.exists() and allow_reserve:
        selected = reserve
        if not reserve_unsubmitted:
            action = "reserve_already_submitted"
        elif remaining <= 0:
            action = "wait_for_quota"
        else:
            action = "submit_reserve"
    elif reserve.exists():
        action = "hold_for_primary_or_rerun_adaptive"
    elif remaining <= 0:
        action = "wait_for_quota"
    else:
        action = "create_primary_plan"

    lines.append(f"recommended_action={action}")
    if selected is not None:
        lines.append(f"selected_plan={display_path(selected)}")
    return "\n".join(lines)


def print_preflight(
    date_value: str,
    plan_path: Path | None,
    reserve_path: Path | None,
    allow_reserve: bool,
    contingency_path: Path | None = None,
) -> None:
    rows = read_submissions()
    print(render_preflight(date_value, plan_path, reserve_path, allow_reserve, rows, contingency_path))


def submit_plan(path: Path, dry_run: bool, wait: bool) -> SubmitPlanResult:
    items = validate_plan(path)
    rows = read_submissions()
    now = utc_now()
    open_for_submissions = competition_is_open(now)
    used = len(submissions_today(rows, now))
    remaining = max(0, DAILY_LIMIT - used)
    submitted = remote_filenames(rows)
    submitted_content = submitted_content_keys(rows)
    candidates: list[PlanItem] = []
    duplicate_content: list[tuple[PlanItem, str]] = []
    for item in items:
        if item.file.name in submitted:
            continue
        duplicate_filename = submitted_content.get(submission_content_key(item.file))
        if duplicate_filename:
            duplicate_content.append((item, duplicate_filename))
            continue
        candidates.append(item)

    print(f"quota_used_utc={used}/{DAILY_LIMIT}")
    print(f"competition_deadline_utc={format_utc(COMPETITION_DEADLINE_UTC)}")
    print(f"seconds_until_deadline={seconds_until_deadline(now)}")
    print(f"competition_open={str(open_for_submissions).lower()}")
    print(f"plan_items={len(items)} unsubmitted_plan_items={len(candidates)}")
    if duplicate_content:
        print(f"duplicate_content_plan_items={len(duplicate_content)}")
        for item, duplicate_filename in duplicate_content[:5]:
            rel = item.file.relative_to(ROOT)
            print(f"duplicate_content_skip={rel} matches={duplicate_filename}")
    if not open_for_submissions:
        print("competition_closed; no submissions sent")
        submitted_count = plan_accounted_count(items, submitted, submitted_content)
        print(f"submitted_plan_items_after={submitted_count}/{len(items)}")
        return SubmitPlanResult(len(items), len(candidates), 0, submitted_count)
    if remaining <= 0:
        print("quota_remaining=0; no submissions sent")
        submitted_count = plan_accounted_count(items, submitted, submitted_content)
        print(f"submitted_plan_items_after={submitted_count}/{len(items)}")
        return SubmitPlanResult(len(items), len(candidates), 0, submitted_count)

    submitted_now = 0
    for item in candidates[:remaining]:
        rel = item.file.relative_to(ROOT)
        print(f"submit {rel}: {item.message}")
        if dry_run:
            continue
        proc = run(["competitions", "submit", "-c", COMPETITION, "-f", str(rel), "-m", item.message])
        print(proc.stdout.strip())
        if proc.returncode != 0:
            raise RuntimeError(f"submit failed for {rel}")
        submitted_now += 1
        time.sleep(2)

    if wait and not dry_run:
        wait_until_complete()

    if dry_run:
        submitted_count = len(items) - len(candidates)
    else:
        rows_after = read_submissions()
        submitted_after = remote_filenames(rows_after)
        submitted_content_after = submitted_content_keys(rows_after)
        submitted_count = plan_accounted_count(items, submitted_after, submitted_content_after)
    print(f"submitted_plan_items_after={submitted_count}/{len(items)}")
    return SubmitPlanResult(len(items), len(candidates), submitted_now, submitted_count)


def wait_until_complete(timeout_s: int = 240) -> None:
    deadline = time.time() + timeout_s
    while True:
        rows = read_submissions()
        latest = rows[:DAILY_LIMIT]
        pending = [row for row in latest if row["status"] != "complete"]
        for row in latest:
            print(f"{row['date']} {row['fileName']} {row['status']} {row.get('publicScore', '')}")
        if not pending:
            return
        if time.time() > deadline:
            raise TimeoutError("submissions still pending")
        time.sleep(10)


def render_review(date_value: str, rows: list[dict[str, str]]) -> str:
    target_rows = submissions_on_date(rows, date_value)
    target_rows = sorted(target_rows, key=lambda row: parse_kaggle_date(row["date"]))
    target_date = datetime.strptime(date_value, "%Y-%m-%d").date()
    before_rows = [row for row in rows if parse_kaggle_date(row["date"]).date() < target_date]
    previous_best = best_public(before_rows)
    current_best = best_public(rows)
    plan_items = plan_notes_for_date(date_value)
    has_plan_notes = bool(plan_items)

    lines = [
        f"# CohortX Daily Review — {date_value}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Submissions in day: {len(target_rows)}/{DAILY_LIMIT}",
        f"- Best public before day: {previous_best:.5f}" if previous_best is not None else "- Best public before day: NA",
        f"- Best public after day: {current_best:.5f}" if current_best is not None else "- Best public after day: NA",
        "",
        "## Scores",
        "",
    ]
    if has_plan_notes:
        lines.extend([
            "| File | Status | Public | Delta vs previous best | Message | Notes |",
            "|---|---|---:|---:|---|---|",
        ])
    else:
        lines.extend([
            "| File | Status | Public | Delta vs previous best | Message |",
            "|---|---|---:|---:|---|",
        ])

    for row in target_rows:
        score = public_score(row)
        score_text = f"{score:.5f}" if score is not None else ""
        if score is None or previous_best is None:
            delta_text = ""
        else:
            delta_text = f"{score - previous_best:+.5f}"
        message = row.get("description", "").replace("|", "/")
        if has_plan_notes:
            plan = plan_items.get(row["fileName"])
            notes = plan.notes.replace("|", "/") if plan else ""
            lines.append(f"| `{row['fileName']}` | {row['status']} | {score_text} | {delta_text} | {message} | {notes} |")
        else:
            lines.append(f"| `{row['fileName']}` | {row['status']} | {score_text} | {delta_text} | {message} |")

    scored = [row for row in target_rows if public_score(row) is not None]
    improved = [row for row in scored if previous_best is not None and public_score(row) > previous_best]
    neutral = [row for row in scored if previous_best is not None and public_score(row) == previous_best]
    worse = [row for row in scored if previous_best is not None and public_score(row) < previous_best]

    lines.extend([
        "",
        "## Readout",
        "",
        f"- Improved: {', '.join(row['fileName'] for row in improved) if improved else 'none'}",
        f"- Tied best: {', '.join(row['fileName'] for row in neutral) if neutral else 'none'}",
        f"- Worse: {len(worse)} submissions",
    ])

    if worse and previous_best is not None:
        lines.extend([
            "",
            "## Largest Drops",
            "",
        ])
        if has_plan_notes:
            lines.extend([
                "| File | Public | Drop | Message | Notes |",
                "|---|---:|---:|---|---|",
            ])
        else:
            lines.extend([
                "| File | Public | Drop | Message |",
                "|---|---:|---:|---|",
            ])
        ranked = sorted(worse, key=lambda row: public_score(row) or 0.0)
        for row in ranked[:8]:
            score = public_score(row)
            drop = score - previous_best if score is not None else 0.0
            message = row.get("description", "").replace("|", "/")
            if has_plan_notes:
                plan = plan_items.get(row["fileName"])
                notes = plan.notes.replace("|", "/") if plan else ""
                lines.append(f"| `{row['fileName']}` | {score:.5f} | {drop:+.5f} | {message} | {notes} |")
            else:
                lines.append(f"| `{row['fileName']}` | {score:.5f} | {drop:+.5f} | {message} |")

    lines.extend([
        "",
        "## Next Action",
        "",
        "- If nothing improved, keep the previous best as public anchor.",
        "- Preserve neutral public variants as possible private hedges only when they change hidden/private conditions.",
        "- Use the largest score drops to identify public split movers for the next probe set.",
        "",
    ])
    return "\n".join(lines)


def render_signals(date_value: str, rows: list[dict[str, str]], anchor: Path) -> str:
    target_rows = submissions_on_date(rows, date_value)
    target_rows = sorted(target_rows, key=lambda row: parse_kaggle_date(row["date"]))
    target_date = datetime.strptime(date_value, "%Y-%m-%d").date()
    before_rows = [row for row in rows if parse_kaggle_date(row["date"]).date() < target_date]
    previous_best = best_public(before_rows)

    lines = [
        f"# CohortX Public Signals — {date_value}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Anchor: `{anchor.relative_to(ROOT)}`",
        f"- Submissions in day: {len(target_rows)}/{DAILY_LIMIT}",
        f"- Previous best public: {previous_best:.5f}" if previous_best is not None else "- Previous best public: NA",
        "",
        "## File-Level Changes",
        "",
        "| File | Public | Delta | Changed conditions | Message |",
        "|---|---:|---:|---|---|",
    ]

    metric_scale = len(read_submission_file(anchor)) if anchor.exists() else 1
    single_condition_rows: list[tuple[str, str, float, float, float, str]] = []
    for row in target_rows:
        score = public_score(row)
        if score is None:
            continue
        delta = score - previous_best if previous_best is not None else 0.0
        candidate = ROOT / "submissions" / row["fileName"]
        if not candidate.exists():
            changed_text = "local file missing"
            changes: list[tuple[str, str]] = []
        else:
            changes = submission_changes(anchor, candidate)
            if changes:
                changed = [f"{condition} ({summary})" for condition, summary in changes[:4]]
                if len(changes) > 4:
                    changed.append(f"+{len(changes) - 4} more")
                changed_text = "; ".join(changed)
            else:
                changed_text = "identical to anchor"
        message = row.get("description", "").replace("|", "/")
        lines.append(f"| `{row['fileName']}` | {score:.5f} | {delta:+.5f} | {changed_text} | {message} |")
        if len(changes) == 1:
            single_condition_rows.append((changes[0][0], row["fileName"], score, delta, delta * metric_scale, changes[0][1]))

    if single_condition_rows:
        lines.extend([
            "",
            "## Single-Condition Probes",
            "",
            f"- `scaled_x{metric_scale}` is a heuristic condition-level delta: public delta multiplied by the {metric_scale} submitted conditions.",
            "",
            "| Condition | File | Public | Delta | Scaled | Change |",
            "|---|---|---:|---:|---:|---|",
        ])
        ranked = sorted(single_condition_rows, key=lambda item: item[3])
        for condition, filename, score, delta, scaled, change in ranked:
            lines.append(f"| {condition} | `{filename}` | {score:.5f} | {delta:+.5f} | {scaled:+.5f} | {change} |")

        strongest_by_condition: dict[str, tuple[str, float, float]] = {}
        for condition, filename, _score, delta, scaled, _change in single_condition_rows:
            current = strongest_by_condition.get(condition)
            if current is None or delta < current[1]:
                strongest_by_condition[condition] = (filename, delta, scaled)

        lines.extend([
            "",
            "## Public Sensitivity Ranking",
            "",
            "| Condition | Strongest probe | Delta | Scaled | Interpretation |",
            "|---|---|---:|---:|---|",
        ])
        for condition, (filename, delta, scaled) in sorted(strongest_by_condition.items(), key=lambda item: item[1][1]):
            interpretation = "public-sensitive" if delta < 0 else "public-neutral so far"
            lines.append(f"| {condition} | `{filename}` | {delta:+.5f} | {scaled:+.5f} | {interpretation} |")

    lines.extend([
        "",
        "## Use",
        "",
        "- Large negative single-condition probes identify public split movers.",
        f"- `scaled_x{metric_scale}` helps compare single-condition movement as an approximate condition-level contribution, not as a private-score guarantee.",
        "- Neutral single-condition probes are public-invisible and should mainly be private hedges.",
        "- Multi-condition probes should be decomposed before trusting them as improvements.",
        "",
    ])
    return "\n".join(lines)


def render_plan_report(plan_path: Path, items: list[PlanItem], anchor: Path) -> str:
    rel_plan = plan_path.relative_to(ROOT)
    lines = [
        f"# CohortX Plan Report — {plan_path.stem}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Plan: `{rel_plan}`",
        f"- Anchor: `{anchor.relative_to(ROOT)}`",
        f"- Items: {len(items)}",
        "",
        "## Planned Changes",
        "",
        "| Order | File | Changed conditions | Message | Notes |",
        "|---:|---|---|---|---|",
    ]
    for idx, item in enumerate(items, start=1):
        changes = submission_changes(anchor, item.file)
        if changes:
            changed = [f"{condition} ({summary})" for condition, summary in changes[:4]]
            if len(changes) > 4:
                changed.append(f"+{len(changes) - 4} more")
            changed_text = "; ".join(changed)
        else:
            changed_text = "identical to anchor"
        rel = item.file.relative_to(ROOT)
        message = item.message.replace("|", "/")
        notes = item.notes.replace("|", "/")
        lines.append(f"| {idx} | `{rel}` | {changed_text} | {message} | {notes} |")

    lines.extend([
        "",
        "## Pre-Submit Checklist",
        "",
        "- The report should show one controlled condition change for each public probe.",
        "- Any accidental multi-condition change should be regenerated before submission.",
        "- Run `validate-plan` immediately before `submit-plan`.",
        "",
    ])
    return "\n".join(lines)


def local_submission_path(filename: str) -> Path:
    return ROOT / "submissions" / filename


def changed_conditions_text(anchor: Path, candidate: Path) -> str:
    if not candidate.exists():
        return "local file missing"
    changes = submission_changes(anchor, candidate)
    if not changes:
        return "identical to anchor"
    changed = [f"{condition} ({summary})" for condition, summary in changes[:4]]
    if len(changes) > 4:
        changed.append(f"+{len(changes) - 4} more")
    return "; ".join(changed)


def change_volume(anchor: Path, candidate: Path) -> int:
    if not candidate.exists():
        return sys.maxsize
    total = 0
    for _condition, summary in submission_changes(anchor, candidate):
        for added, removed in re.findall(r"\+(\d+)/-(\d+)", summary):
            total += int(added) + int(removed)
    return total


def unique_complete_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    complete = [
        row for row in rows
        if row.get("status") == "complete" and public_score(row) is not None
    ]
    complete = sorted(
        complete,
        key=lambda row: (public_score(row) or 0.0, parse_kaggle_date(row["date"])),
        reverse=True,
    )
    seen: set[str] = set()
    unique: list[dict[str, str]] = []
    for row in complete:
        filename = row["fileName"]
        if filename in seen:
            continue
        seen.add(filename)
        unique.append(row)
    return unique


def latest_rows_by_file(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    latest: dict[str, dict[str, str]] = {}
    for row in sorted(rows, key=lambda row: parse_kaggle_date(row["date"]), reverse=True):
        latest.setdefault(row["fileName"], row)
    return latest


def anchor_public_score(rows: list[dict[str, str]], anchor: Path) -> float | None:
    scores = [
        score
        for row in rows
        if row["fileName"] == anchor.name
        if (score := public_score(row)) is not None
    ]
    return max(scores) if scores else best_public(rows)


def plan_score_signal(score: float | None, baseline: float | None) -> str:
    if score is None:
        return "missing_score"
    if baseline is None:
        return "scored"
    if score > baseline:
        return "improved"
    if score == baseline:
        return "tied"
    return "worse"


def recommended_final_rows(
    rows: list[dict[str, str]],
    anchor: Path,
    limit: int = FINAL_SELECTION_LIMIT,
) -> list[tuple[str, dict[str, str]]]:
    complete = unique_complete_rows(rows)
    if not complete:
        return []
    best = public_score(complete[0])
    selected: list[tuple[str, dict[str, str]]] = []
    seen: set[str] = set()

    def add(role: str, row: dict[str, str] | None) -> None:
        if row is None or len(selected) >= limit:
            return
        filename = row["fileName"]
        if filename in seen:
            return
        seen.add(filename)
        selected.append((role, row))

    def is_identical(row: dict[str, str]) -> bool:
        return changed_conditions_text(anchor, local_submission_path(row["fileName"])) == "identical to anchor"

    public_anchor = next(
        (row for row in complete if row["fileName"] == anchor.name or is_identical(row)),
        None,
    )
    private_hedge = next((row for row in complete if row["fileName"] == "v185_private_kw.csv"), None)

    add("Public anchor", public_anchor)
    add("Private hedge", private_hedge)
    add("Best public/tied", complete[0])

    for row in complete:
        score = public_score(row)
        if best is None or score != best:
            continue
        candidate = local_submission_path(row["fileName"])
        if is_identical(row):
            continue
        if change_volume(anchor, candidate) > MAX_RECOMMENDED_CHANGE_VOLUME:
            continue
        add("Neutral hedge", row)

    for row in complete:
        score = public_score(row)
        if best is None or score != best:
            continue
        candidate = local_submission_path(row["fileName"])
        if not is_identical(row) and change_volume(anchor, candidate) > MAX_RECOMMENDED_CHANGE_VOLUME:
            continue
        add("Best-score reserve", row)

    return selected


def render_final_candidates(rows: list[dict[str, str]], anchor: Path) -> str:
    complete = unique_complete_rows(rows)
    best = public_score(complete[0]) if complete else None
    tied_best = [row for row in complete if best is not None and public_score(row) == best]
    changed_tied = [
        row for row in tied_best
        if local_submission_path(row["fileName"]).exists()
        and changed_conditions_text(anchor, local_submission_path(row["fileName"])) != "identical to anchor"
    ]
    private_hedge = next((row for row in changed_tied if row["fileName"] == "v185_private_kw.csv"), None)
    selection = recommended_final_rows(rows, anchor)
    latest_changed_date = parse_kaggle_date(changed_tied[0]["date"]).date() if changed_tied else None
    neutral_watchlist = [
        row for row in changed_tied
        if not private_hedge or row["fileName"] != private_hedge["fileName"]
        if latest_changed_date is not None and parse_kaggle_date(row["date"]).date() == latest_changed_date
    ][:12]

    lines = [
        "# CohortX Final Candidate Watchlist",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Best public score: {best:.5f}" if best is not None else "- Best public score: NA",
        f"- Best-score submissions: {len(tied_best)}",
        f"- Local changed hedges tied at best: {len(changed_tied)}",
        f"- Recommended final selection: {len(selection)}/{FINAL_SELECTION_LIMIT}",
        "",
        "## Recommended Final Selection",
        "",
        "| Slot | Role | File | Public | Change volume | Changed conditions |",
        "|---:|---|---|---:|---:|---|",
    ]
    for idx, (role, row) in enumerate(selection, start=1):
        path = local_submission_path(row["fileName"])
        volume = change_volume(anchor, path)
        volume_text = "" if volume == sys.maxsize else str(volume)
        lines.append(
            f"| {idx} | {role} | `{row['fileName']}` | {public_score(row):.5f} | {volume_text} | {changed_conditions_text(anchor, path)} |"
        )

    if neutral_watchlist:
        lines.extend([
            "",
            "## Neutral Hedge Watchlist",
            "",
            "| File | Date UTC | Public | Changed conditions |",
            "|---|---|---:|---|",
        ])
    for row in neutral_watchlist:
        path = local_submission_path(row["fileName"])
        lines.append(
            f"| `{row['fileName']}` | {row['date']} | {public_score(row):.5f} | {changed_conditions_text(anchor, path)} |"
        )

    lines.extend([
        "",
        "## Top Public Submissions",
        "",
        "| Rank | File | Date UTC | Public | Message | Changed conditions |",
        "|---:|---|---|---:|---|---|",
    ])
    for rank, row in enumerate(complete[:20], start=1):
        path = local_submission_path(row["fileName"])
        message = row.get("description", "").replace("|", "/")
        lines.append(
            f"| {rank} | `{row['fileName']}` | {row['date']} | {public_score(row):.5f} | {message} | {changed_conditions_text(anchor, path)} |"
        )

    lines.extend([
        "",
        "## Selection Notes",
        "",
        "- Keep at least one unchanged/public-anchor submission in the final set.",
        f"- Fill remaining final slots with public-neutral hedges under change volume {MAX_RECOMMENDED_CHANGE_VOLUME}.",
        "- Do not promote probes that lose public score unless later private/hidden evidence justifies them.",
        "- Very large public-neutral mutations stay visible in Top Public only, not in the recommended selection.",
        "",
    ])
    return "\n".join(lines)


def render_plan_scorecard(plan_path: Path, rows: list[dict[str, str]], anchor: Path) -> str:
    if not plan_path.is_absolute():
        plan_path = ROOT / plan_path
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    items = validate_plan(plan_path)
    latest = latest_rows_by_file(rows)
    baseline = anchor_public_score(rows, anchor)

    scored_rows: list[tuple[PlanItem, dict[str, str], float, float | None, str]] = []
    lines = [
        f"# CohortX Plan Scorecard — {plan_path.stem}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Plan: `{plan_path.relative_to(ROOT)}`",
        f"- Anchor: `{anchor.relative_to(ROOT)}`",
        f"- Anchor public: {baseline:.5f}" if baseline is not None else "- Anchor public: NA",
        f"- Items: {len(items)}",
        "",
        "## Plan Items",
        "",
        "| Order | File | Status | Public | Delta vs anchor | Signal | Changed conditions | Message | Notes |",
        "|---:|---|---|---:|---:|---|---|---|---|",
    ]

    for idx, item in enumerate(items, start=1):
        row = latest.get(item.file.name)
        score = public_score(row) if row else None
        delta = score - baseline if score is not None and baseline is not None else None
        signal = plan_score_signal(score, baseline)
        status = row.get("status", "missing") if row else "missing"
        score_text = f"{score:.5f}" if score is not None else ""
        delta_text = f"{delta:+.5f}" if delta is not None else ""
        changed = changed_conditions_text(anchor, item.file).replace("|", "/")
        message = item.message.replace("|", "/")
        notes = item.notes.replace("|", "/")
        lines.append(
            f"| {idx} | `{item.file.relative_to(ROOT)}` | {status} | {score_text} | {delta_text} | {signal} | {changed} | {message} | {notes} |"
        )
        if row is not None and score is not None:
            scored_rows.append((item, row, score, delta, signal))

    lines.extend([
        "",
        "## Ranked Complete Signals",
        "",
    ])
    if scored_rows:
        lines.extend([
            "| Rank | File | Public | Delta vs anchor | Signal | Changed conditions |",
            "|---:|---|---:|---:|---|---|",
        ])
        ranked = sorted(scored_rows, key=lambda item: (item[3] if item[3] is not None else item[2]), reverse=True)
        for rank, (item, _row, score, delta, signal) in enumerate(ranked, start=1):
            delta_text = f"{delta:+.5f}" if delta is not None else ""
            changed = changed_conditions_text(anchor, item.file).replace("|", "/")
            lines.append(f"| {rank} | `{item.file.name}` | {score:.5f} | {delta_text} | {signal} | {changed} |")
    else:
        lines.append("No completed plan items yet.")

    lines.extend([
        "",
        "## Strategy Use",
        "",
        "- Improved rows are immediate candidates for promotion or cross-condition combinations.",
        "- Tied rows are public-neutral and mainly useful as private hedges.",
        "- Worse rows identify public-sensitive code families; use the direction of the edit before deciding whether to add back or remove codes.",
        "- Missing rows mean the adaptive generator should wait rather than fill the next plan with weak guesses.",
        "",
    ])
    return "\n".join(lines)


def render_intel(
    date_value: str,
    kernels: list[dict[str, str]],
    leaderboard: list[dict[str, str]],
    discussion: dict[str, str],
    submissions: list[dict[str, str]],
    known_refs: set[str],
) -> str:
    today = submissions_on_date(submissions, date_value)
    jv_row = next((row for row in leaderboard if "João Victor" in row.get("teamName", "")), None)
    best = best_public(submissions)
    new_kernels = [row for row in kernels if row.get("ref", "") not in known_refs]
    lines = [
        f"# CohortX Intel — {date_value}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Competition: `{COMPETITION}`",
        f"- Best public observed: {best:.5f}" if best is not None else "- Best public observed: NA",
        f"- JV leaderboard: #{leaderboard.index(jv_row) + 1} with {jv_row['score']}" if jv_row else "- JV leaderboard: not found in top page",
        f"- Submissions on date: {len(today)}/{DAILY_LIMIT}",
        f"- Public notebooks listed: {len(kernels)}",
        f"- Downloaded notebook refs: {len(known_refs)}",
        f"- New public notebooks: {len(new_kernels)}",
        f"- Discussion page: {discussion.get('status', 'unknown')} ({discussion.get('url', '')})",
        f"- Discussion static HTML chars: {discussion.get('chars', '')}",
        f"- Discussion markers: {discussion.get('markers', discussion.get('detail', ''))}",
        "",
        "## Recent Public Notebooks",
        "",
        "| Ref | Title | Author | Last run UTC | Votes |",
        "|---|---|---|---|---:|",
    ]
    for row in kernels[:10]:
        lines.append(
            f"| `{row.get('ref', '')}` | {row.get('title', '').replace('|', '/')} | "
            f"{row.get('author', '').replace('|', '/')} | {row.get('lastRunTime', '')} | {row.get('totalVotes', '')} |"
        )

    lines.extend([
        "",
        "## New Public Notebooks",
        "",
    ])
    if new_kernels:
        lines.extend([
            "| Ref | Title | Author | Last run UTC | Votes |",
            "|---|---|---|---|---:|",
        ])
        for row in new_kernels:
            lines.append(
                f"| `{row.get('ref', '')}` | {row.get('title', '').replace('|', '/')} | "
                f"{row.get('author', '').replace('|', '/')} | {row.get('lastRunTime', '')} | {row.get('totalVotes', '')} |"
            )
    else:
        lines.append("No new public notebooks beyond `external_notebooks/`.")

    lines.extend([
        "",
        "## Leaderboard Top",
        "",
        "| Rank | Team | Last submission UTC | Public |",
        "|---:|---|---|---:|",
    ])
    for rank, row in enumerate(leaderboard[:12], start=1):
        lines.append(
            f"| {rank} | {row.get('teamName', '').replace('|', '/')} | "
            f"{row.get('submissionDate', '')} | {row.get('score', '')} |"
        )

    lines.extend([
        "",
        "## Latest JV Submissions",
        "",
        "| File | Date UTC | Status | Public |",
        "|---|---|---|---:|",
    ])
    for row in submissions[:10]:
        lines.append(
            f"| `{row.get('fileName', '')}` | {row.get('date', '')} | "
            f"{row.get('status', '')} | {row.get('publicScore', '')} |"
        )

    lines.extend([
        "",
        "## Use",
        "",
        "- If a new public notebook appears, download and diff it against `external_notebooks/` before generating the next plan.",
        "- If leaderboard movement appears without new notebooks, keep probing public movers rather than copying weak public examples.",
        "- If discussion remains `js_shell_only`, use browser/API inspection when a specific new discussion is suspected.",
    ])
    return "\n".join(lines)


def write_intel(date_value: str, out_path: Path | None) -> Path:
    content = render_intel(
        date_value,
        read_kernels(),
        read_leaderboard_top(),
        discussion_status(),
        read_submissions(),
        known_notebook_refs(),
    )
    path = out_path or (REPORTS / f"{date_value}-intel.md")
    if path.is_absolute():
        target = path
    else:
        target = ROOT / path
    if ".." in target.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content + "\n")
    print(target.relative_to(ROOT))
    return target


def write_review(date_value: str, out_path: Path | None) -> Path:
    rows = read_submissions()
    content = render_review(date_value, rows)
    path = out_path or (REPORTS / f"{date_value}.md")
    if path.is_absolute():
        target = path
    else:
        target = ROOT / path
    if ".." in target.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content + "\n")
    print(target.relative_to(ROOT))
    return target


def write_plan_scorecard(plan_path: Path, anchor: Path, out_path: Path | None) -> Path:
    rows = read_submissions()
    if not plan_path.is_absolute():
        plan_path = ROOT / plan_path
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    content = render_plan_scorecard(plan_path, rows, anchor)
    path = out_path or (REPORTS / f"{plan_path.stem}-scorecard.md")
    if path.is_absolute():
        target = path
    else:
        target = ROOT / path
    if ".." in target.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content + "\n")
    print(target.relative_to(ROOT))
    return target


def write_final_candidates(anchor: Path, out_path: Path | None) -> Path:
    rows = read_submissions()
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    content = render_final_candidates(rows, anchor)
    path = out_path or (REPORTS / "final-candidates.md")
    if path.is_absolute():
        target = path
    else:
        target = ROOT / path
    if ".." in target.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content + "\n")
    print(target.relative_to(ROOT))
    return target


def write_plan_report(plan_path: Path, anchor: Path, out_path: Path | None) -> Path:
    if not plan_path.is_absolute():
        plan_path = ROOT / plan_path
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    items = validate_plan(plan_path)
    content = render_plan_report(plan_path, items, anchor)
    path = out_path or (REPORTS / f"{plan_path.stem}-plan.md")
    if path.is_absolute():
        target = path
    else:
        target = ROOT / path
    if ".." in target.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content + "\n")
    print(target.relative_to(ROOT))
    return target


def write_signals(date_value: str, anchor: Path, out_path: Path | None) -> Path:
    rows = read_submissions()
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    content = render_signals(date_value, rows, anchor)
    path = out_path or (REPORTS / f"{date_value}-signals.md")
    if path.is_absolute():
        target = path
    else:
        target = ROOT / path
    if ".." in target.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content + "\n")
    print(target.relative_to(ROOT))
    return target


def default_next_plan_path(date_value: str) -> Path:
    target = datetime.strptime(date_value, "%Y-%m-%d").date() + timedelta(days=1)
    return ROOT / "plans" / f"{target.isoformat()}.csv"


def generate_next_plan(prior_plan: Path, next_plan: Path, start_version: int | None) -> None:
    script = ROOT / "src" / "v221_240_adaptive_followups.py"
    if not script.exists():
        print(f"next_plan_script_missing={script.relative_to(ROOT)}")
        return
    if next_plan.exists():
        print(f"next_plan_exists={next_plan.relative_to(ROOT)}")
        return
    args = [sys.executable, str(script), "--prior-plan", str(prior_plan), "--out-plan", str(next_plan)]
    if start_version is not None:
        args.extend(["--start-version", str(start_version)])
    proc = subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    print(proc.stdout.strip())
    if proc.returncode != 0:
        print(f"next_plan_not_ready={next_plan.relative_to(ROOT)}")
        return
    validate_plan(next_plan)
    write_plan_report(next_plan, DEFAULT_ANCHOR, None)


def run_report_script(script_name: str, args: list[str]) -> None:
    script = ROOT / "src" / script_name
    if not script.exists():
        raise FileNotFoundError(script)
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    print(proc.stdout.strip())
    if proc.returncode != 0:
        raise RuntimeError(f"{script_name} failed")


def write_plan_delta_report(plan_path: Path, anchor: Path) -> None:
    out = REPORTS / f"{plan_path.stem}-code-deltas.md"
    run_report_script(
        "audit_plan_deltas.py",
        ["--plan", str(plan_path), "--anchor", str(anchor), "--out", str(out)],
    )


def write_plan_impact_report(plan_path: Path, anchor: Path) -> None:
    out = REPORTS / f"{plan_path.stem}-impact.md"
    run_report_script(
        "interpret_plan_scores.py",
        ["--plan", str(plan_path), "--anchor", str(anchor), "--out", str(out)],
    )


def daily_run(
    date_value: str,
    plan_path: Path | None,
    dry_run: bool,
    wait: bool,
    skip_reports: bool,
    next_plan_path: Path | None,
    start_version: int | None,
    reserve_plan_path: Path | None = None,
    allow_reserve: bool = False,
    contingency_plan_path: Path | None = None,
) -> None:
    primary_plan = resolve_path(plan_path or (ROOT / "plans" / f"{date_value}.csv"))
    contingency_plan = resolve_path(contingency_plan_path or (ROOT / "plans" / f"{date_value}-public-contingency.csv"))
    reserve_plan = resolve_path(reserve_plan_path or (ROOT / "plans" / f"{date_value}-reserve.csv"))
    next_plan = next_plan_path
    if next_plan is not None and not next_plan.is_absolute():
        next_plan = ROOT / next_plan

    now = utc_now()
    relation = target_date_relation(date_value, now)
    open_for_submissions = competition_is_open(now)
    print_status()
    print(f"competition_deadline_utc={format_utc(COMPETITION_DEADLINE_UTC)}")
    print(f"seconds_until_deadline={seconds_until_deadline(now)}")
    print(f"competition_open={str(open_for_submissions).lower()}")
    if not skip_reports:
        write_intel(date_value, None)
    if contingency_plan_path is None:
        print_preflight(date_value, primary_plan, reserve_plan, allow_reserve)
    else:
        print_preflight(date_value, primary_plan, reserve_plan, allow_reserve, contingency_plan)

    plan: Path | None = None
    plan_kind: str | None = None
    plan_anchor = DEFAULT_ANCHOR
    if primary_plan.exists():
        plan = primary_plan
        plan_kind = "primary"
    elif contingency_plan.exists():
        print(f"primary_plan_missing={display_path(primary_plan)}")
        print(f"contingency_plan_available={display_path(contingency_plan)}")
        plan = contingency_plan
        plan_kind = "public_contingency"
    elif reserve_plan.exists():
        print(f"primary_plan_missing={display_path(primary_plan)}")
        print(f"contingency_plan_missing={display_path(contingency_plan)}")
        print(f"reserve_plan_available={display_path(reserve_plan)}")
        if allow_reserve:
            plan = reserve_plan
            plan_kind = "reserve"
            plan_anchor = PRIVATE_ANCHOR if PRIVATE_ANCHOR.exists() else DEFAULT_ANCHOR
        else:
            print("reserve_guard=requires_allow_reserve")
    else:
        print(f"plan_missing={display_path(primary_plan)}")

    plan_ready = False
    post_reports_ready = False
    if plan is not None:
        print(f"selected_plan_kind={plan_kind}")
        print(f"selected_plan={display_path(plan)}")
        items = validate_plan(plan)
        print(f"validated_plan_items={len(items)}")
        write_plan_report(plan, plan_anchor, None)
        write_plan_delta_report(plan, plan_anchor)
        print(f"target_date_relation={relation}")
        if not open_for_submissions:
            print("deadline_guard=skip_submit")
        elif target_after_deadline(date_value):
            print("deadline_guard=target_after_deadline")
        elif relation == "current":
            result = submit_plan(plan, dry_run=dry_run, wait=wait)
            plan_ready = result.plan_complete
            post_reports_ready = result.submitted_now > 0 or result.plan_complete
            if not plan_ready:
                print("next_plan_guard=prior_plan_incomplete")
        else:
            print("date_guard=skip_submit")

    if skip_reports:
        print("skip_reports=true")
        return

    if not post_reports_ready:
        print("post_reports_guard=no_current_plan_activity")
        return

    write_review(date_value, None)
    write_signals(date_value, DEFAULT_ANCHOR, None)
    if plan is not None:
        write_plan_scorecard(plan, plan_anchor, None)
        write_plan_impact_report(plan, plan_anchor)
    write_final_candidates(DEFAULT_ANCHOR, None)
    if next_plan is not None and plan_ready and plan_kind in {"primary", "public_contingency"}:
        generate_next_plan(plan, next_plan, start_version)
    elif next_plan is not None and plan_ready and plan_kind == "reserve":
        print("next_plan_guard=reserve_plan")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    preflight = sub.add_parser("preflight")
    preflight.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    preflight.add_argument("--plan", type=Path)
    preflight.add_argument("--contingency-plan", type=Path)
    preflight.add_argument("--reserve-plan", type=Path)
    preflight.add_argument("--allow-reserve", action="store_true")
    validate = sub.add_parser("validate-plan")
    validate.add_argument("plan", type=Path)
    submit = sub.add_parser("submit-plan")
    submit.add_argument("plan", type=Path)
    submit.add_argument("--dry-run", action="store_true")
    submit.add_argument("--no-wait", action="store_true")
    review = sub.add_parser("review")
    review.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    review.add_argument("--out", type=Path)
    intel = sub.add_parser("intel")
    intel.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    intel.add_argument("--out", type=Path)
    plan_report = sub.add_parser("plan-report")
    plan_report.add_argument("plan", type=Path)
    plan_report.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    plan_report.add_argument("--out", type=Path)
    plan_scorecard = sub.add_parser("plan-scorecard")
    plan_scorecard.add_argument("plan", type=Path)
    plan_scorecard.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    plan_scorecard.add_argument("--out", type=Path)
    final = sub.add_parser("final-candidates")
    final.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    final.add_argument("--out", type=Path)
    signals = sub.add_parser("signals")
    signals.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    signals.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    signals.add_argument("--out", type=Path)
    daily = sub.add_parser("daily-run")
    daily.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    daily.add_argument("--plan", type=Path)
    daily.add_argument("--dry-run", action="store_true")
    daily.add_argument("--no-wait", action="store_true")
    daily.add_argument("--skip-reports", action="store_true")
    daily.add_argument("--next-plan", type=Path)
    daily.add_argument("--auto-next-plan", action="store_true")
    daily.add_argument("--start-version", type=int)
    daily.add_argument("--contingency-plan", type=Path)
    daily.add_argument("--reserve-plan", type=Path)
    daily.add_argument("--allow-reserve", action="store_true")
    args = parser.parse_args(argv)

    if args.cmd == "status":
        print_status()
    elif args.cmd == "preflight":
        print_preflight(args.date, args.plan, args.reserve_plan, args.allow_reserve, args.contingency_plan)
    elif args.cmd == "validate-plan":
        items = validate_plan(args.plan)
        print(f"validated_plan_items={len(items)}")
    elif args.cmd == "submit-plan":
        submit_plan(args.plan, dry_run=args.dry_run, wait=not args.no_wait)
    elif args.cmd == "review":
        write_review(args.date, args.out)
    elif args.cmd == "intel":
        write_intel(args.date, args.out)
    elif args.cmd == "plan-report":
        write_plan_report(args.plan, args.anchor, args.out)
    elif args.cmd == "plan-scorecard":
        write_plan_scorecard(args.plan, args.anchor, args.out)
    elif args.cmd == "final-candidates":
        write_final_candidates(args.anchor, args.out)
    elif args.cmd == "signals":
        write_signals(args.date, args.anchor, args.out)
    elif args.cmd == "daily-run":
        next_plan_path = args.next_plan
        if args.auto_next_plan and next_plan_path is None:
            next_plan_path = default_next_plan_path(args.date)
        daily_run(
            args.date,
            args.plan,
            dry_run=args.dry_run,
            wait=not args.no_wait,
            skip_reports=args.skip_reports,
            next_plan_path=next_plan_path,
            start_version=args.start_version,
            reserve_plan_path=args.reserve_plan,
            allow_reserve=args.allow_reserve,
            contingency_plan_path=args.contingency_plan,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
