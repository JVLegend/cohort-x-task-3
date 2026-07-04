"""Operational helpers for the CohortX Task 3 submission loop."""
from __future__ import annotations

import argparse
import base64
import csv
import errno
import io
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
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
FINAL_HEDGE_PUBLIC_DROP_TOLERANCE = 0.00325
FINAL_RESERVE_PUBLIC_DROP_TOLERANCE = 0.00600
COMPETITION_DEADLINE_UTC = datetime(2026, 7, 16, 11, 59, tzinfo=timezone.utc)
ROOT = Path(__file__).resolve().parents[1]
KAGGLE = ROOT / ".venv" / "bin" / "kaggle"
REPORTS = ROOT / "reports"
NOTEBOOK_MANIFEST = ROOT / "external_notebooks" / "public_notebook_manifest.json"
DEFAULT_ANCHOR = ROOT / "submissions" / "v178_FINAL.csv"
PRIVATE_ANCHOR = ROOT / "submissions" / "v185_private_kw.csv"
LOCK_STALE_AFTER_SECONDS = 2 * 60 * 60
csv.field_size_limit(10_000_000)
BRT = timezone(timedelta(hours=-3))
KNOWN_FINAL_SUBMISSIONS = [
    {
        "fileName": "v178_FINAL.csv",
        "date": "2026-06-10 13:41:36",
        "description": "known public anchor",
        "status": "complete",
        "publicScore": "0.42453",
        "privateScore": "",
    },
    {
        "fileName": "v185_private_kw.csv",
        "date": "2026-07-01 02:34:58",
        "description": "known private KEEP hedge",
        "status": "complete",
        "publicScore": "0.42453",
        "privateScore": "",
    },
]


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


class SubmissionLock:
    """Atomic local lock to prevent overlapping Kaggle submission loops."""

    def __init__(self, name: str = "submission") -> None:
        self.name = name
        self.path = ROOT / ".cohortx_locks" / f"{name}.lock"
        self.acquired = False

    def acquire(self) -> bool:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        while True:
            try:
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            except FileExistsError:
                if self._is_stale():
                    try:
                        self.path.unlink()
                    except FileNotFoundError:
                        pass
                    continue
                return False
            payload = {
                "pid": os.getpid(),
                "created_utc": utc_now().isoformat(),
                "name": self.name,
            }
            with os.fdopen(fd, "w") as fh:
                json.dump(payload, fh)
                fh.write("\n")
            self.acquired = True
            return True

    def release(self) -> None:
        if not self.acquired:
            return
        try:
            self.path.unlink()
        except FileNotFoundError:
            pass
        self.acquired = False

    def _is_stale(self) -> bool:
        try:
            payload = json.loads(self.path.read_text())
        except (OSError, json.JSONDecodeError):
            payload = {}
        pid = payload.get("pid")
        if isinstance(pid, int):
            return not process_is_alive(pid)
        try:
            age = time.time() - self.path.stat().st_mtime
        except OSError:
            return True
        return age > LOCK_STALE_AFTER_SECONDS


def process_is_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except OSError as exc:
        if exc.errno in {errno.ESRCH, errno.EINVAL}:
            return False
        return True
    return True


def print_lock_held(lock: SubmissionLock) -> None:
    print("submission_lock_held=true")
    print(f"submission_lock_path={display_path(lock.path)}")
    try:
        print(f"submission_lock_payload={lock.path.read_text().strip()}")
    except OSError:
        pass
    print("submission_lock_action=skip_submit")


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


def kaggle_api_credentials() -> tuple[str, str] | None:
    username = os.environ.get("KAGGLE_USERNAME")
    key = os.environ.get("KAGGLE_KEY")
    if username and key:
        return username, key

    config_dir = Path(os.environ.get("KAGGLE_CONFIG_DIR", Path.home() / ".kaggle"))
    path = config_dir / "kaggle.json"
    try:
        payload = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    username = payload.get("username")
    key = payload.get("key")
    if isinstance(username, str) and isinstance(key, str) and username and key:
        return username, key
    return None


def kaggle_api_post(service: str, method: str, payload: dict[str, object], timeout_s: int = 20) -> dict[str, object]:
    url = f"https://api.kaggle.com/v1/{service}/{method}"
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "cohortx-task3-ops",
    }
    credentials = kaggle_api_credentials()
    if credentials is not None:
        token = base64.b64encode(f"{credentials[0]}:{credentials[1]}".encode("utf-8")).decode("ascii")
        headers["Authorization"] = f"Basic {token}"
    request = Request(url, data=body, headers=headers, method="POST")
    with urlopen(request, timeout=timeout_s) as response:
        text = response.read().decode("utf-8", "ignore")
    data = json.loads(text or "{}")
    if not isinstance(data, dict):
        raise RuntimeError(f"Kaggle API returned non-object payload for {service}/{method}")
    return data


def discussion_note_summary(messages: list[dict[str, object]]) -> list[str]:
    text = " ".join(
        str(message.get("rawMarkdown") or message.get("content") or "")
        for message in messages
    ).lower()
    notes: list[str] = []
    if "online api" in text or "online service" in text:
        notes.append("Processing must stay offline; online APIs/services are not allowed.")
    if "proprietary data" in text:
        notes.append("Proprietary data is not allowed for processing.")
    if "hugging face" in text:
        notes.append("Open pretrained models from Hugging Face are allowed if downloaded and loaded locally.")
    if "creative commons" in text or "public domain" in text:
        notes.append("Creative Commons/Public Domain data is allowed.")
    if "15 gb ram" in text:
        notes.append("Final approach should load on a server with 15 GB RAM and run quickly.")
    if "top 10" in text and "source code" in text:
        notes.append("Top-10 finishers may need source code, a 5-minute video, and paper contribution after the challenge.")
    return notes


def discussion_status(timeout_s: int = 20) -> dict[str, object]:
    url = f"https://www.kaggle.com/competitions/{COMPETITION}/discussion"
    try:
        payload = kaggle_api_post(
            "competitions.CompetitionApiService",
            "ListCompetitionTopics",
            {"competitionName": COMPETITION, "sortBy": 4, "page": 1},
            timeout_s=timeout_s,
        )
        topics = payload.get("topics", [])
        if not isinstance(topics, list):
            topics = []
        clean_topics: list[dict[str, object]] = []
        notes: list[str] = []
        for topic in topics:
            if not isinstance(topic, dict):
                continue
            topic_id = topic.get("id")
            messages: list[dict[str, object]] = []
            if isinstance(topic_id, int):
                message_payload = kaggle_api_post(
                    "competitions.CompetitionApiService",
                    "ListTopicMessages",
                    {
                        "competitionName": COMPETITION,
                        "topicId": topic_id,
                        "sortBy": 3,
                        "pageSize": -1,
                    },
                    timeout_s=timeout_s,
                )
                raw_messages = message_payload.get("messages", [])
                if isinstance(raw_messages, list):
                    messages = [message for message in raw_messages if isinstance(message, dict)]
                    notes.extend(discussion_note_summary(messages))
            clean_topics.append({**topic, "messages": messages})
        latest = ""
        for topic in clean_topics:
            value = topic.get("lastCommentPostDate") or topic.get("postDate") or ""
            if isinstance(value, str) and value > latest:
                latest = value
        return {
            "url": url,
            "status": "api_ok",
            "topic_count": str(payload.get("totalCount", len(clean_topics))),
            "latest_topic_date": latest,
            "topics": clean_topics,
            "notes": list(dict.fromkeys(notes)),
        }
    except (OSError, URLError, json.JSONDecodeError, RuntimeError, ValueError) as api_exc:
        api_detail = str(api_exc)

    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(request, timeout=timeout_s) as response:
            html = response.read().decode("utf-8", "ignore")
    except (OSError, URLError) as exc:
        return {"url": url, "status": "error", "detail": f"api={api_detail}; html={exc}"}
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
        "api_detail": api_detail,
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


def known_notebook_versions() -> dict[str, str]:
    if not NOTEBOOK_MANIFEST.exists():
        return {}
    try:
        payload = json.loads(NOTEBOOK_MANIFEST.read_text())
    except (OSError, json.JSONDecodeError):
        return {}
    notebooks = payload.get("notebooks", {})
    if not isinstance(notebooks, dict):
        return {}
    versions: dict[str, str] = {}
    for ref, details in notebooks.items():
        if not isinstance(ref, str) or not isinstance(details, dict):
            continue
        last_run = details.get("lastRunTime")
        if isinstance(last_run, str):
            versions[ref] = last_run
    return versions


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


def submission_event_key(row: dict[str, str]) -> tuple[str, str, str]:
    return (row.get("fileName", ""), row.get("date", ""), row.get("description", ""))


def unique_submission_events(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[tuple[str, str, str]] = set()
    unique: list[dict[str, str]] = []
    for row in rows:
        key = submission_event_key(row)
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)
    return unique


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


def submission_ledger_path(now: datetime | None = None) -> Path:
    current = now.astimezone(timezone.utc) if now else utc_now()
    return ROOT / ".cohortx_locks" / f"submission-ledger-{current.date().isoformat()}.json"


def read_submission_ledger(now: datetime | None = None) -> list[dict[str, str]]:
    path = submission_ledger_path(now)
    try:
        payload = json.loads(path.read_text())
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    if not isinstance(payload, list):
        return []
    return [row for row in payload if isinstance(row, dict)]


def local_ledger_filenames(now: datetime | None = None) -> set[str]:
    return {
        str(row.get("fileName", ""))
        for row in read_submission_ledger(now)
        if row.get("fileName")
    }


def record_submission_ledger(item: PlanItem, message: str, now: datetime | None = None) -> None:
    current = now.astimezone(timezone.utc) if now else utc_now()
    path = submission_ledger_path(current)
    rows = read_submission_ledger(current)
    file_name = item.file.name
    if any(row.get("fileName") == file_name for row in rows):
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    rows.append({
        "fileName": file_name,
        "path": str(item.file.relative_to(ROOT)),
        "message": message,
        "recordedUtc": current.strftime("%Y-%m-%d %H:%M:%S"),
    })
    path.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")


def kaggle_quota_error(text: str) -> bool:
    lowered = text.lower()
    return "daily submission allowance" in lowered or "used its daily submission allowance" in lowered


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
    unique_today = unique_submission_events(today)
    best = best_public(rows)
    reset = next_quota_reset(now)
    print(f"submissions_today_utc={len(today)}/{DAILY_LIMIT}")
    print(f"unique_submission_events_today={len(unique_today)}")
    print(f"duplicate_submission_rows_today={max(0, len(today) - len(unique_today))}")
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
    local_submitted: set[str] | None = None,
) -> tuple[list[PlanItem], list[PlanItem], list[PlanItem]]:
    items = validate_plan(path)
    content = submitted_content or {}
    local = local_submitted or set()
    unsubmitted: list[PlanItem] = []
    duplicate_content: list[PlanItem] = []
    for item in items:
        if item.file.name in submitted or item.file.name in local:
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
    unique_today = unique_submission_events(today)
    remaining = max(0, DAILY_LIMIT - len(today))
    submitted = remote_filenames(rows)
    submitted_content = submitted_content_keys(rows)
    local_submitted = local_ledger_filenames(now)
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
        f"unique_submission_events_today={len(unique_today)}",
        f"duplicate_submission_rows_today={max(0, len(today) - len(unique_today))}",
        f"local_ledger_submissions_today={len(local_submitted)}",
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
        primary_items, primary_unsubmitted, primary_duplicates = inspect_plan(primary, submitted, submitted_content, local_submitted)
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
        contingency_items, contingency_unsubmitted, contingency_duplicates = inspect_plan(contingency, submitted, submitted_content, local_submitted)
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
        reserve_items, reserve_unsubmitted, reserve_duplicates = inspect_plan(reserve, submitted, submitted_content, local_submitted)
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
    if relation == "current" and remaining <= 0:
        next_date = reset.date().isoformat()
        next_plan = resolve_path(ROOT / "plans" / f"{next_date}.csv")
        next_contingency = resolve_path(ROOT / "plans" / f"{next_date}-public-contingency.csv")
        next_selected = next_plan if next_plan.exists() else next_contingency if next_contingency.exists() else None
        lines.extend([
            f"next_reset_date={next_date}",
            f"next_reset_plan={display_path(next_plan)}",
            f"next_reset_plan_exists={str(next_plan.exists()).lower()}",
        ])
        if next_plan.exists():
            next_items, next_unsubmitted, next_duplicates = inspect_plan(next_plan, submitted, submitted_content, local_submitted)
            lines.extend([
                f"next_reset_valid_items={len(next_items)}",
                f"next_reset_unsubmitted_items={len(next_unsubmitted)}",
                f"next_reset_duplicate_content_items={len(next_duplicates)}",
            ])
        lines.extend([
            f"next_reset_contingency_plan={display_path(next_contingency)}",
            f"next_reset_contingency_exists={str(next_contingency.exists()).lower()}",
        ])
        if next_selected is not None:
            lines.append(f"next_reset_selected_plan={display_path(next_selected)}")
            if next_selected == next_plan and next_plan.exists():
                next_action = "submit_primary_after_reset"
            else:
                next_action = "submit_public_contingency_after_reset"
        else:
            next_action = "create_primary_plan_before_reset"
        lines.append(f"next_reset_recommended_action={next_action}")
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
    local_submitted = local_ledger_filenames(now)
    candidates: list[PlanItem] = []
    duplicate_content: list[tuple[PlanItem, str]] = []
    for item in items:
        if item.file.name in submitted:
            continue
        if item.file.name in local_submitted:
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
    if local_submitted:
        print(f"local_ledger_submissions_today={len(local_submitted)}")
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
        refreshed_rows = read_submissions()
        refreshed_used = len(submissions_today(refreshed_rows, utc_now()))
        refreshed_submitted = remote_filenames(refreshed_rows)
        refreshed_submitted_content = submitted_content_keys(refreshed_rows)
        refreshed_local_submitted = local_ledger_filenames(utc_now())
        if refreshed_used >= DAILY_LIMIT:
            print(f"quota_used_utc={refreshed_used}/{DAILY_LIMIT}")
            print("quota_remaining=0; stopping before next submit")
            break
        rel = item.file.relative_to(ROOT)
        if item.file.name in refreshed_submitted:
            print(f"already_submitted_skip={rel}")
            continue
        if item.file.name in refreshed_local_submitted:
            print(f"local_ledger_skip={rel}")
            continue
        duplicate_filename = refreshed_submitted_content.get(submission_content_key(item.file))
        if duplicate_filename:
            print(f"duplicate_content_skip={rel} matches={duplicate_filename}")
            continue
        print(f"submit {rel}: {item.message}")
        if dry_run:
            continue
        proc = run(["competitions", "submit", "-c", COMPETITION, "-f", str(rel), "-m", item.message])
        print(proc.stdout.strip())
        if proc.returncode != 0:
            if kaggle_quota_error(proc.stdout):
                print("kaggle_quota_error=true")
                print("quota_remaining=0; stopping after Kaggle quota rejection")
                break
            raise RuntimeError(f"submit failed for {rel}")
        record_submission_ledger(item, item.message, utc_now())
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
        latest = unique_submission_events(rows)[:DAILY_LIMIT]
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


def parse_plan_strategy_axes(notes: str) -> dict[str, str]:
    axes: dict[str, str] = {
        "source": "",
        "source_public": "",
        "source_delta": "",
        "source_anchor": "",
        "med": "",
        "private_keep": "",
        "assoc": "",
    }
    source_match = re.search(r"source\s+(\S+)\s+\(([0-9.]+),\s+([+-][0-9.]+)\s+vs\s+([^)]+)\)", notes)
    if source_match:
        axes["source"] = source_match.group(1)
        axes["source_public"] = source_match.group(2)
        axes["source_delta"] = source_match.group(3)
        axes["source_anchor"] = source_match.group(4)
    for match in re.finditer(r"\b(med|private_keep|assoc)=([^,;]+)", notes):
        axes[match.group(1)] = match.group(2).strip()
    return axes


def render_plan_strategy_audit(plan_path: Path, items: list[PlanItem], anchor: Path) -> str:
    rel_plan = plan_path.relative_to(ROOT)
    rows = []
    for idx, item in enumerate(items, start=1):
        axes = parse_plan_strategy_axes(item.notes)
        changes = submission_changes(anchor, item.file)
        columns = sorted({
            column
            for _condition, summary in changes
            for column in EXPECTED_COLUMNS[1:]
            if column in summary
        })
        source_score = public_score({"publicScore": axes["source_public"]})
        rows.append({
            "order": idx,
            "item": item,
            "axes": axes,
            "source_score": source_score,
            "volume": change_volume(anchor, item.file),
            "columns": ",".join(columns) if columns else "none",
            "conditions": len(changes),
        })

    med_counts = Counter(row["axes"]["med"] or "unknown" for row in rows)
    private_counts = Counter(row["axes"]["private_keep"] or "unknown" for row in rows)
    assoc_counts = Counter(row["axes"]["assoc"] or "unknown" for row in rows)
    source_counts = Counter(row["axes"]["source"] or "unknown" for row in rows)
    source_scores = [score for row in rows if (score := row["source_score"]) is not None]
    best_source = max(source_scores) if source_scores else None
    first_source = rows[0]["source_score"] if rows else None

    def gate_status(name: str) -> str:
        if name == "item_count":
            return "ready" if len(items) == DAILY_LIMIT else "incomplete"
        if name == "ordering":
            return "ready" if best_source is not None and first_source == best_source else "review"
        if name == "mediastinum_toggle":
            return "ready" if med_counts.get("keep", 0) and med_counts.get("drop", 0) else "thin"
        if name == "private_keep_mix":
            return "ready" if len(private_counts) >= 4 and private_counts.get("none", 0) else "thin"
        if name == "assoc_mix":
            return "ready" if len(assoc_counts) >= 4 else "thin"
        raise KeyError(name)

    lines = [
        f"# CohortX Plan Strategy Audit — {plan_path.stem}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Plan: `{rel_plan}`",
        f"- Anchor: `{anchor.relative_to(ROOT)}`",
        f"- Items: {len(items)}",
        f"- Best source public: {best_source:.5f}" if best_source is not None else "- Best source public: NA",
        f"- Distinct source submissions: {len(source_counts)}",
        f"- Mediastinum axis: keep={med_counts.get('keep', 0)}, drop={med_counts.get('drop', 0)}",
        f"- Private KEEP buckets: {len(private_counts)}",
        f"- ASSOC/DIFF buckets: {len(assoc_counts)}",
        "",
        "## Gates",
        "",
        "| Gate | Status | Detail |",
        "|---|---|---|",
        f"| item_count | {gate_status('item_count')} | items={len(items)}/{DAILY_LIMIT} |",
        f"| ordering | {gate_status('ordering')} | first_source={first_source:.5f}; best_source={best_source:.5f} |" if first_source is not None and best_source is not None else "| ordering | unknown | missing source scores |",
        f"| mediastinum_toggle | {gate_status('mediastinum_toggle')} | med=keep {med_counts.get('keep', 0)}; med=drop {med_counts.get('drop', 0)} |",
        f"| private_keep_mix | {gate_status('private_keep_mix')} | buckets={len(private_counts)}; none={private_counts.get('none', 0)} |",
        f"| assoc_mix | {gate_status('assoc_mix')} | buckets={len(assoc_counts)} |",
        "",
        "## Axis Coverage",
        "",
        "### Source Submissions",
        "",
        "| Source | Slots |",
        "|---|---:|",
    ]
    for source, count in source_counts.most_common():
        lines.append(f"| `{source}` | {count} |")

    lines.extend(["", "### Mediastinum", "", "| Axis | Slots |", "|---|---:|"])
    for med, count in med_counts.most_common():
        lines.append(f"| med={med} | {count} |")

    lines.extend(["", "### Private KEEP", "", "| Bucket | Slots |", "|---|---:|"])
    for bucket, count in private_counts.most_common():
        lines.append(f"| {bucket} | {count} |")

    lines.extend(["", "### ASSOC/DIFF", "", "| Bucket | Slots |", "|---|---:|"])
    for bucket, count in assoc_counts.most_common():
        lines.append(f"| {bucket} | {count} |")

    lines.extend([
        "",
        "## First-Wave Order",
        "",
        "| Order | File | Source public | Source delta | med | private_keep | assoc | Volume | Columns | Conditions |",
        "|---:|---|---:|---:|---|---|---|---:|---|---:|",
    ])
    for row in rows[:8]:
        item = row["item"]
        axes = row["axes"]
        rel = item.file.relative_to(ROOT)
        score_text = f"{row['source_score']:.5f}" if row["source_score"] is not None else ""
        volume_text = "" if row["volume"] == sys.maxsize else str(row["volume"])
        lines.append(
            f"| {row['order']} | `{rel}` | {score_text} | {axes['source_delta']} | {axes['med']} | {axes['private_keep']} | {axes['assoc']} | {volume_text} | {row['columns']} | {row['conditions']} |"
        )

    lines.extend([
        "",
        "## Use",
        "",
        "- Submit all 20 after the UTC reset if `preflight` still selects this primary plan.",
        "- If a network/Kaggle interruption allows only a partial send, preserve plan order: the first slots use the best public source and cover the main private KEEP splits.",
        "- Interpret public movement by comparing this audit with the scorecard: `med=drop` isolates whether the mediastinum add is carrying real signal; `private_keep=none` isolates ASSOC/DIFF without the v185 KEEP hedge.",
        "- Treat public-neutral results as private-hedge evidence, not proof of private improvement.",
        "",
    ])
    return "\n".join(lines)


def decision_axis_rule(axis: str) -> str:
    if axis == "med":
        return "If `drop` beats `keep`, demote thymus/nodes; if `keep` wins or ties, keep mediastinum add in composites."
    if axis == "private_keep":
        return "If `none` ties/wins, ASSOC/DIFF carries signal without private KEEP; if v185 buckets win, keep them as private hedges."
    if axis == "assoc":
        return "Promote winning ASSOC bucket; avoid losing buckets unless public-neutral and useful for private hedge diversity."
    if axis == "source":
        return "Promote the source family that wins after matching axes; demote weaker COPD/source variant in next composites."
    return "Compare matched variants and promote the public winner."


def render_plan_decision_matrix(plan_path: Path, items: list[PlanItem], anchor: Path) -> str:
    plan_display = plan_path.relative_to(ROOT)
    impact_display = REPORTS / f"{plan_path.stem}-impact.md"
    impact_display = impact_display.relative_to(ROOT)
    rows = []
    for idx, item in enumerate(items, start=1):
        rows.append({
            "order": idx,
            "item": item,
            "axes": parse_plan_strategy_axes(item.notes),
        })

    def short_source(source: str) -> str:
        return source.removesuffix(".csv") if source else "unknown"

    def matched_groups(axis: str, fixed_axes: list[str]) -> list[tuple[str, dict[str, list[dict[str, object]]]]]:
        groups: dict[tuple[str, ...], dict[str, list[dict[str, object]]]] = defaultdict(lambda: defaultdict(list))
        for row in rows:
            axes = row["axes"]
            key = tuple(str(axes.get(name, "")) for name in fixed_axes)
            value = str(axes.get(axis, "") or "unknown")
            groups[key][value].append(row)

        out = []
        for key, values in groups.items():
            if len(values) < 2:
                continue
            held = "; ".join(
                f"{name}={short_source(value) if name == 'source' else value}"
                for name, value in zip(fixed_axes, key, strict=True)
            )
            out.append((held, dict(values)))
        return out

    comparison_specs = [
        ("med", ["source", "private_keep", "assoc"]),
        ("private_keep", ["source", "med", "assoc"]),
        ("assoc", ["source", "med", "private_keep"]),
        ("source", ["med", "private_keep", "assoc"]),
    ]
    comparisons = [
        (axis, held, values)
        for axis, fixed_axes in comparison_specs
        for held, values in matched_groups(axis, fixed_axes)
    ]

    lines = [
        f"# CohortX Plan Decision Matrix — {plan_path.stem}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Plan: `{plan_display}`",
        f"- Anchor: `{anchor.relative_to(ROOT)}`",
        f"- Items: {len(items)}",
        f"- Matched decision comparisons: {len(comparisons)}",
        "",
        "## Gates",
        "",
        "| Gate | Status | Detail |",
        "|---|---|---|",
        f"| item_count | {'ready' if len(items) == DAILY_LIMIT else 'incomplete'} | items={len(items)}/{DAILY_LIMIT} |",
        f"| matched_comparisons | {'ready' if comparisons else 'thin'} | comparisons={len(comparisons)} |",
        "",
        "## Decision Comparisons",
        "",
        "| Axis | Held constant | Variants | Files | Rule |",
        "|---|---|---|---|---|",
    ]
    for axis, held, values in comparisons[:16]:
        variants = []
        files = []
        for value, variant_rows in sorted(values.items()):
            variants.append(f"`{axis}={value}` ({len(variant_rows)})")
            files.append(
                f"`{value}`: "
                + ", ".join(f"`{row['item'].file.name}`" for row in variant_rows[:3])
            )
        lines.append(
            f"| {axis} | {held} | {'; '.join(variants)} | {'; '.join(files)} | {decision_axis_rule(axis)} |"
        )

    lines.extend([
        "",
        "## Post-Score Checklist",
        "",
        f"1. Run `.venv/bin/python src/cohortx_ops.py plan-scorecard {plan_display}` after all 20 scores are complete.",
        f"2. Run `.venv/bin/python src/interpret_plan_scores.py --plan {plan_display} --out {impact_display}`.",
        "3. For each matched comparison above, prefer the variant with the higher public score; if tied, keep the lower-volume or more diverse private hedge.",
        "4. Regenerate `reports/final-candidates.md` and `reports/final-diversity.md` before choosing final slots.",
        "",
        "## Use",
        "",
        "- This matrix is a pre-commitment device: use it to interpret scores before being distracted by single-file leaderboard noise.",
        "- Do not override the Kaggle notebook guard; new public notebooks still require sync/audit before submission or next-plan generation.",
    ])
    return "\n".join(lines)


def local_submission_path(filename: str) -> Path:
    return ROOT / "submissions" / filename


def existing_submission_versions() -> set[int]:
    versions: set[int] = set()
    for path in (ROOT / "submissions").glob("v*.csv"):
        match = re.match(r"v(\d+)_", path.name)
        if match:
            versions.add(int(match.group(1)))
    return versions


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


def touches_assoc_diff(anchor: Path, candidate: Path) -> bool:
    if not candidate.exists():
        return False
    return any(
        "ASSOCIATION" in summary or "DIFF" in summary
        for _condition, summary in submission_changes(anchor, candidate)
    )


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


def supplement_known_final_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    present = {row.get("fileName", "") for row in rows}
    out = list(rows)
    for row in KNOWN_FINAL_SUBMISSIONS:
        if row["fileName"] in present:
            continue
        if not local_submission_path(row["fileName"]).exists():
            continue
        out.append(dict(row))
    return out


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
    complete = unique_complete_rows(supplement_known_final_rows(rows))
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

    def near_best(row: dict[str, str]) -> bool:
        score = public_score(row)
        return best is not None and score is not None and score >= best - FINAL_HEDGE_PUBLIC_DROP_TOLERANCE

    public_anchor = next(
        (row for row in complete if row["fileName"] == anchor.name or is_identical(row)),
        None,
    )
    private_hedge = next((row for row in complete if row["fileName"] == "v185_private_kw.csv"), None)

    add("Public anchor", public_anchor)
    add("Private hedge", private_hedge)
    add("Best public/tied", complete[0])

    for row in complete:
        if not near_best(row):
            continue
        candidate = local_submission_path(row["fileName"])
        if is_identical(row):
            continue
        if not touches_assoc_diff(anchor, candidate):
            continue
        add("Strategic ASSOC/DIFF hedge", row)

    for row in complete:
        if not near_best(row):
            continue
        candidate = local_submission_path(row["fileName"])
        if is_identical(row):
            continue
        if touches_assoc_diff(anchor, candidate):
            continue
        if change_volume(anchor, candidate) > MAX_RECOMMENDED_CHANGE_VOLUME:
            continue
        add("Near-best public hedge", row)

    for row in complete:
        score = public_score(row)
        if best is None or score != best:
            continue
        candidate = local_submission_path(row["fileName"])
        if not is_identical(row) and change_volume(anchor, candidate) > MAX_RECOMMENDED_CHANGE_VOLUME:
            continue
        add("Best-score reserve", row)

    for row in complete:
        score = public_score(row)
        candidate = local_submission_path(row["fileName"])
        if best is None or score is None:
            continue
        if score < best - FINAL_RESERVE_PUBLIC_DROP_TOLERANCE:
            continue
        if is_identical(row):
            continue
        if change_volume(anchor, candidate) > MAX_RECOMMENDED_CHANGE_VOLUME:
            continue
        add("Controlled public reserve", row)

    return selected


def render_final_selection_csv(rows: list[dict[str, str]], anchor: Path) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["slot", "role", "file", "public", "change_volume", "changed_conditions"],
        lineterminator="\n",
    )
    writer.writeheader()
    for idx, (role, row) in enumerate(recommended_final_rows(rows, anchor), start=1):
        path = local_submission_path(row["fileName"])
        volume = change_volume(anchor, path)
        writer.writerow({
            "slot": idx,
            "role": role,
            "file": row["fileName"],
            "public": f"{public_score(row):.5f}" if public_score(row) is not None else "",
            "change_volume": "" if volume == sys.maxsize else str(volume),
            "changed_conditions": changed_conditions_text(anchor, path),
        })
    return output.getvalue()


def render_final_selection_audit(rows: list[dict[str, str]], anchor: Path) -> str:
    selection = recommended_final_rows(rows, anchor)
    protected_roles = {"Public anchor", "Private hedge"}
    scores = [score for _role, row in selection if (score := public_score(row)) is not None]
    replaceable_scores = [
        score
        for role, row in selection
        if role not in protected_roles
        if (score := public_score(row)) is not None
    ]
    protected_scores = [
        score
        for role, row in selection
        if role in protected_roles
        if (score := public_score(row)) is not None
    ]
    best = max(scores) if scores else None
    floor = min(scores) if scores else None
    max_drop = (best - floor) if best is not None and floor is not None else None
    replaceable_floor = min(replaceable_scores) if replaceable_scores else None
    replaceable_max_drop = (
        best - replaceable_floor
        if best is not None and replaceable_floor is not None
        else None
    )
    protected_floor = min(protected_scores) if protected_scores else None
    protected_max_drop = (
        best - protected_floor
        if best is not None and protected_floor is not None
        else None
    )
    role_counts = Counter(role for role, _row in selection)
    condition_counts: Counter[str] = Counter()
    column_counts: Counter[str] = Counter()
    assoc_diff_slots = 0
    non_copd_changed_slots = 0
    copd_only_slots = 0
    identical_slots = 0
    slot_rows: list[tuple[int, str, dict[str, str], float | None, int, str, str]] = []

    for idx, (role, row) in enumerate(selection, start=1):
        path = local_submission_path(row["fileName"])
        score = public_score(row)
        volume = change_volume(anchor, path)
        changes = submission_changes(anchor, path) if path.exists() else []
        columns = sorted({
            column
            for _condition, summary in changes
            for column in EXPECTED_COLUMNS[1:]
            if column in summary
        })
        changed_conditions = [condition for condition, _summary in changes]
        condition_counts.update(changed_conditions)
        column_counts.update(columns)
        if not changes:
            identical_slots += 1
        elif all(condition == "Chronic Obstructive Pulmonary Disease" for condition in changed_conditions):
            copd_only_slots += 1
        if any(condition != "Chronic Obstructive Pulmonary Disease" for condition in changed_conditions):
            non_copd_changed_slots += 1
        if {"ASSOCIATION", "DIFF"} & set(columns):
            assoc_diff_slots += 1
        slot_rows.append((
            idx,
            role,
            row,
            score,
            volume,
            ",".join(columns) if columns else "none",
            changed_conditions_text(anchor, path),
        ))

    dominant_condition, dominant_count = condition_counts.most_common(1)[0] if condition_counts else ("none", 0)
    concentration_limit = max(8, FINAL_SELECTION_LIMIT // 2)

    def gate_status(name: str) -> str:
        if name == "slots":
            return "ready" if len(selection) == FINAL_SELECTION_LIMIT else "incomplete"
        if name == "public_floor":
            if replaceable_max_drop is None:
                return "unknown"
            return "ready" if replaceable_max_drop <= FINAL_RESERVE_PUBLIC_DROP_TOLERANCE else "wide_drop"
        if name == "assoc_diff_hedges":
            return "ready" if assoc_diff_slots >= 4 else "thin"
        if name == "condition_concentration":
            return "crowded" if dominant_count > concentration_limit else "balanced"
        if name == "non_copd_hedges":
            return "ready" if non_copd_changed_slots >= 5 else "needs_more"
        raise KeyError(name)

    lines = [
        "# CohortX Final Selection Audit",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Slots: {len(selection)}/{FINAL_SELECTION_LIMIT}",
        f"- Public score floor: {floor:.5f}" if floor is not None else "- Public score floor: NA",
        f"- Best public in selection: {best:.5f}" if best is not None else "- Best public in selection: NA",
        f"- Max public drop in selection: {max_drop:.5f}" if max_drop is not None else "- Max public drop in selection: NA",
        f"- Replaceable public floor: {replaceable_floor:.5f}" if replaceable_floor is not None else "- Replaceable public floor: NA",
        f"- Max replaceable public drop: {replaceable_max_drop:.5f}" if replaceable_max_drop is not None else "- Max replaceable public drop: NA",
        f"- Max protected anchor/hedge drop: {protected_max_drop:.5f}" if protected_max_drop is not None else "- Max protected anchor/hedge drop: NA",
        f"- ASSOC/DIFF hedge slots: {assoc_diff_slots}",
        f"- Non-COPD changed slots: {non_copd_changed_slots}",
        f"- COPD-only changed slots: {copd_only_slots}",
        f"- Identical/public-anchor slots: {identical_slots}",
        f"- Dominant changed condition: {dominant_condition} ({dominant_count}/{len(selection)})",
        "",
        "## Gates",
        "",
        "| Gate | Status | Detail |",
        "|---|---|---|",
        f"| slots | {gate_status('slots')} | selected={len(selection)}/{FINAL_SELECTION_LIMIT} |",
        f"| public_floor | {gate_status('public_floor')} | replaceable_max_drop={replaceable_max_drop:.5f}; tolerance={FINAL_RESERVE_PUBLIC_DROP_TOLERANCE:.5f}; protected_slots={sum(role_counts[role] for role in protected_roles)} |" if replaceable_max_drop is not None else "| public_floor | unknown | no replaceable scored rows |",
        f"| assoc_diff_hedges | {gate_status('assoc_diff_hedges')} | slots={assoc_diff_slots}; minimum=4 |",
        f"| condition_concentration | {gate_status('condition_concentration')} | dominant=`{dominant_condition}`; slots={dominant_count}; warning_above={concentration_limit} |",
        f"| non_copd_hedges | {gate_status('non_copd_hedges')} | slots={non_copd_changed_slots}; minimum=5 |",
        "",
        "## Role Mix",
        "",
        "| Role | Slots |",
        "|---|---:|",
    ]
    for role, count in role_counts.most_common():
        lines.append(f"| {role} | {count} |")

    lines.extend([
        "",
        "## Changed Columns",
        "",
        "| Column | Slots |",
        "|---|---:|",
    ])
    for column in EXPECTED_COLUMNS[1:]:
        lines.append(f"| {column} | {column_counts.get(column, 0)} |")

    lines.extend([
        "",
        "## Changed Condition Concentration",
        "",
        "| Condition | Slots |",
        "|---|---:|",
    ])
    for condition, count in condition_counts.most_common(12):
        lines.append(f"| {condition} | {count} |")

    lines.extend([
        "",
        "## Slot Diagnostics",
        "",
        "| Slot | Role | File | Public | Drop vs best | Volume | Changed columns | Changed conditions |",
        "|---:|---|---|---:|---:|---:|---|---|",
    ])
    for idx, role, row, score, volume, columns, changed in slot_rows:
        drop = (best - score) if best is not None and score is not None else None
        score_text = f"{score:.5f}" if score is not None else ""
        drop_text = f"{drop:.5f}" if drop is not None else ""
        volume_text = "" if volume == sys.maxsize else str(volume)
        lines.append(
            f"| {idx} | {role} | `{row['fileName']}` | {score_text} | {drop_text} | {volume_text} | {columns} | {changed} |"
        )

    lines.extend([
        "",
        "## Actions",
        "",
        "- Treat `condition_concentration=crowded` as a warning, not a blocker: the current public leaderboard is driven by COPD, but final slots should diversify when new public-neutral private hedges appear.",
        "- Replacement priority: swap lowest-value COPD-only controlled reserves before dropping public anchor, private hedge, best public, or ASSOC/DIFF hedges.",
        "- Keep at least four ASSOC/DIFF hedge slots unless a later public or private signal proves those buckets harmful.",
        "- Keep the replaceable public floor within the controlled reserve tolerance; protected anchor/hedge slots may sit below that floor by design.",
    ])
    return "\n".join(lines)


def render_final_diversity_watchlist(rows: list[dict[str, str]], anchor: Path) -> str:
    rows = supplement_known_final_rows(rows)
    complete = unique_complete_rows(rows)
    selection = recommended_final_rows(rows, anchor)
    selected_names = {row["fileName"] for _role, row in selection}
    best = public_score(complete[0]) if complete else None
    floor = (best - FINAL_RESERVE_PUBLIC_DROP_TOLERANCE) if best is not None else None
    concentration_limit = max(8, FINAL_SELECTION_LIMIT // 2)
    selected_condition_counts: Counter[str] = Counter()

    for _role, row in selection:
        path = local_submission_path(row["fileName"])
        if path.exists():
            selected_condition_counts.update(condition for condition, _summary in submission_changes(anchor, path))

    crowded_conditions = {
        condition
        for condition, count in selected_condition_counts.items()
        if count > concentration_limit
    }
    candidate_rows = []
    for row in complete:
        filename = row["fileName"]
        score = public_score(row)
        if filename in selected_names or score is None or floor is None or score < floor:
            continue
        path = local_submission_path(filename)
        if not path.exists():
            continue
        changes = submission_changes(anchor, path)
        if not changes:
            continue
        changed_conditions = [condition for condition, _summary in changes]
        columns = sorted({
            column
            for _condition, summary in changes
            for column in EXPECTED_COLUMNS[1:]
            if column in summary
        })
        crowded_hits = sum(1 for condition in changed_conditions if condition in crowded_conditions)
        fresh_conditions = sum(1 for condition in changed_conditions if condition not in crowded_conditions)
        volume = change_volume(anchor, path)
        candidate_rows.append((
            crowded_hits,
            -fresh_conditions,
            best - score,
            volume,
            row,
            ",".join(columns) if columns else "none",
            changed_conditions_text(anchor, path),
        ))
    candidate_rows.sort(key=lambda item: (item[0], item[2], item[3]))

    def gate_status(name: str) -> str:
        if name == "selection_concentration":
            return "crowded" if crowded_conditions else "balanced"
        if name == "diversity_alternatives":
            return "ready" if candidate_rows else "thin"
        if name == "public_floor":
            return "ready" if floor is not None else "unknown"
        raise KeyError(name)

    crowded_text = ", ".join(f"`{condition}`" for condition in sorted(crowded_conditions)) if crowded_conditions else "none"
    lines = [
        "# CohortX Final Diversity Watchlist",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Recommended final selection: {len(selection)}/{FINAL_SELECTION_LIMIT}",
        f"- Best public score: {best:.5f}" if best is not None else "- Best public score: NA",
        f"- Diversity candidate floor: {floor:.5f}" if floor is not None else "- Diversity candidate floor: NA",
        f"- Crowded conditions: {crowded_text}",
        f"- Eligible concentration breakers: {len(candidate_rows)}",
        "",
        "## Gates",
        "",
        "| Gate | Status | Detail |",
        "|---|---|---|",
        f"| selection_concentration | {gate_status('selection_concentration')} | crowded_conditions={len(crowded_conditions)}; warning_above={concentration_limit} |",
        f"| diversity_alternatives | {gate_status('diversity_alternatives')} | candidates={len(candidate_rows)} |",
        f"| public_floor | {gate_status('public_floor')} | floor={floor:.5f}; tolerance={FINAL_RESERVE_PUBLIC_DROP_TOLERANCE:.5f} |" if floor is not None else "| public_floor | unknown | missing best public |",
        "",
        "## Current Crowding",
        "",
        "| Condition | Selected slots |",
        "|---|---:|",
    ]
    for condition, count in selected_condition_counts.most_common(12):
        lines.append(f"| {condition} | {count} |")

    lines.extend([
        "",
        "## Concentration Breakers",
        "",
        "| File | Public | Drop vs best | Crowded hits | Volume | Columns | Changed conditions |",
        "|---|---:|---:|---:|---:|---|---|",
    ])
    if not candidate_rows:
        lines.append("| none |  |  |  |  |  |  |")
    for crowded_hits, _fresh, drop, volume, row, columns, changed in candidate_rows[:12]:
        volume_text = "" if volume == sys.maxsize else str(volume)
        lines.append(
            f"| `{row['fileName']}` | {public_score(row):.5f} | {drop:.5f} | {crowded_hits} | {volume_text} | {columns} | {changed} |"
        )

    lines.extend([
        "",
        "## Use",
        "",
        "- Use this watchlist only as a swap guide; do not drop public anchor, private hedge, best-public slots, or strong ASSOC/DIFF hedges just to reduce concentration.",
        "- Prefer the lowest `Crowded hits` candidates, especially zero-hit candidates when they appear after the next scored batch.",
        "- Keep every replacement within the controlled public reserve floor unless later private evidence justifies a larger public drop.",
    ])
    return "\n".join(lines)


def render_final_candidates(rows: list[dict[str, str]], anchor: Path) -> str:
    rows = supplement_known_final_rows(rows)
    complete = unique_complete_rows(rows)
    best = public_score(complete[0]) if complete else None
    tied_best = [row for row in complete if best is not None and public_score(row) == best]
    near_best = [
        row for row in complete
        if best is not None
        and public_score(row) is not None
        and (public_score(row) or 0.0) >= best - FINAL_HEDGE_PUBLIC_DROP_TOLERANCE
    ]
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
        f"- Near-best submissions within {FINAL_HEDGE_PUBLIC_DROP_TOLERANCE:.5f}: {len(near_best)}",
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
        "- Add the known historical anchor/hedge rows when the Kaggle CLI truncates older submissions from the recent listing.",
        "- Promote public-neutral ASSOC/DIFF variants as strategic private hedges even when their code volume is large.",
        f"- Fill remaining final slots with near-best public hedges under change volume {MAX_RECOMMENDED_CHANGE_VOLUME}.",
        f"- Near-best means public score no more than {FINAL_HEDGE_PUBLIC_DROP_TOLERANCE:.5f} below the current best.",
        f"- If fewer than {FINAL_SELECTION_LIMIT} slots are filled, use controlled public reserves down to {FINAL_RESERVE_PUBLIC_DROP_TOLERANCE:.5f} below best, still under change volume {MAX_RECOMMENDED_CHANGE_VOLUME}.",
        "- Do not promote larger public-score losses unless later private/hidden evidence justifies them.",
        "- Very large public-neutral KEEP-only mutations stay visible in Top Public only, not in the recommended selection.",
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
    discussion: dict[str, object],
    submissions: list[dict[str, str]],
    known_refs: set[str],
    known_versions: dict[str, str] | None = None,
) -> str:
    today = submissions_on_date(submissions, date_value)
    jv_row = next((row for row in leaderboard if "João Victor" in row.get("teamName", "")), None)
    jv_rank = leaderboard.index(jv_row) + 1 if jv_row else None
    jv_score_text = jv_row.get("score", "") if jv_row else ""
    jv_leaderboard_score = public_score({"publicScore": jv_score_text}) if jv_row else None
    next_rank_row = leaderboard[jv_rank - 2] if jv_rank is not None and jv_rank > 1 else None
    next_rank_team = next_rank_row.get("teamName", "unknown") if next_rank_row else ""
    next_rank_score_text = next_rank_row.get("score", "") if next_rank_row else ""
    next_rank_score = public_score({"publicScore": next_rank_score_text}) if next_rank_row else None
    next_rank_gap = (
        next_rank_score - jv_leaderboard_score
        if next_rank_score is not None and jv_leaderboard_score is not None
        else None
    )
    best = best_public(submissions)
    new_kernels = [row for row in kernels if row.get("ref", "") not in known_refs]
    known_versions = known_versions or {}
    updated_kernels = [
        row
        for row in kernels
        if row.get("ref", "") in known_refs
        and row.get("ref", "") in known_versions
        and known_versions[row.get("ref", "")] != row.get("lastRunTime", "")
    ]
    discussion_topics = [
        topic for topic in discussion.get("topics", [])
        if isinstance(topic, dict)
    ] if isinstance(discussion.get("topics", []), list) else []
    discussion_notes = [
        note for note in discussion.get("notes", [])
        if isinstance(note, str) and note
    ] if isinstance(discussion.get("notes", []), list) else []
    lines = [
        f"# CohortX Intel — {date_value}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Competition: `{COMPETITION}`",
        f"- Best public observed: {best:.5f}" if best is not None else "- Best public observed: NA",
        f"- JV leaderboard: #{jv_rank} with {jv_score_text or 'NA'}" if jv_row else "- JV leaderboard: not found in top page",
        f"- Next rank target: #{jv_rank - 1} `{next_rank_team}` at {next_rank_score_text or 'NA'}" if next_rank_row and jv_rank is not None else "- Next rank target: none/top or not found",
        f"- Gap to next rank: {next_rank_gap:.5f}" if next_rank_gap is not None else "- Gap to next rank: NA",
        f"- Submissions on date: {len(today)}/{DAILY_LIMIT}",
        f"- Public notebooks listed: {len(kernels)}",
        f"- Downloaded notebook refs: {len(known_refs)}",
        f"- New public notebooks: {len(new_kernels)}",
        f"- Updated public notebooks: {len(updated_kernels)}",
        f"- Discussion page: {discussion.get('status', 'unknown')} ({discussion.get('url', '')})",
        f"- Competition discussion topics: {discussion.get('topic_count', len(discussion_topics))}",
        f"- Latest discussion update: {discussion.get('latest_topic_date', '')}",
    ]
    if discussion.get("chars"):
        lines.append(f"- Discussion static HTML chars: {discussion.get('chars', '')}")
    discussion_marker = discussion.get("markers", discussion.get("detail", ""))
    if discussion_marker:
        lines.append(f"- Discussion markers: {discussion_marker}")
    lines.extend([
        "",
        "## Recent Public Notebooks",
        "",
        "| Ref | Title | Author | Last run UTC | Votes |",
        "|---|---|---|---|---:|",
    ])
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
        "## Updated Public Notebooks",
        "",
    ])
    if updated_kernels:
        lines.extend([
            "| Ref | Title | Author | Local last run | Kaggle last run | Votes |",
            "|---|---|---|---|---|---:|",
        ])
        for row in updated_kernels:
            ref = row.get("ref", "")
            lines.append(
                f"| `{ref}` | {row.get('title', '').replace('|', '/')} | "
                f"{row.get('author', '').replace('|', '/')} | {known_versions.get(ref, '')} | "
                f"{row.get('lastRunTime', '')} | {row.get('totalVotes', '')} |"
            )
    else:
        lines.append("No downloaded public notebooks have newer Kaggle runs.")

    lines.extend([
        "",
        "## Competition Discussion Topics",
        "",
    ])
    if discussion_topics:
        lines.extend([
            "| Topic | Last update UTC | Comments | Votes | URL |",
            "|---|---|---:|---:|---|",
        ])
        for topic in discussion_topics:
            topic_url = str(topic.get("topicUrl") or topic.get("url") or "")
            if topic_url.startswith("/"):
                topic_url = f"https://www.kaggle.com{topic_url}"
            lines.append(
                f"| {str(topic.get('title', '')).replace('|', '/')} | "
                f"{topic.get('lastCommentPostDate') or topic.get('postDate') or ''} | "
                f"{topic.get('commentCount', '')} | {topic.get('votes', '')} | {topic_url} |"
            )
    else:
        lines.append("No competition-specific discussion topics returned by the API.")

    lines.extend([
        "",
        "## Discussion Notes",
        "",
    ])
    if discussion_notes:
        for note in discussion_notes:
            lines.append(f"- {note}")
    else:
        lines.append("No actionable discussion notes extracted.")

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
        "- If a new or updated public notebook appears, sync and diff it against `external_notebooks/` before submitting or generating the next plan.",
        "- If leaderboard movement appears without new notebooks, keep probing public movers rather than copying weak public examples.",
        "- If discussion API fails and HTML remains `js_shell_only`, use browser/API inspection before assuming the forum is empty.",
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
        known_notebook_versions(),
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


def intel_public_notebook_alerts(report_path: object) -> tuple[int, list[str]]:
    if not isinstance(report_path, Path):
        return 0, []
    path = report_path if report_path.is_absolute() else ROOT / report_path
    if not path.exists():
        return 0, []
    content = path.read_text()
    counts = [
        int(match.group(1))
        for match in re.finditer(r"^- (?:New|Updated) public notebooks: (\d+)$", content, flags=re.MULTILINE)
    ]
    count = sum(counts)
    if count == 0:
        return 0, []
    refs: list[str] = []
    for section_name in ("New Public Notebooks", "Updated Public Notebooks"):
        if f"## {section_name}" not in content:
            continue
        section = content.split(f"## {section_name}", 1)[-1].split("## ", 1)[0]
        refs.extend(re.findall(r"\| `([^`]+)` \|", section))
    return count, refs


def intel_new_public_notebooks(report_path: object) -> tuple[int, list[str]]:
    return intel_public_notebook_alerts(report_path)


def public_notebook_watch_counts(
    kernels: list[dict[str, str]],
    known_refs: set[str],
    known_versions: dict[str, str],
) -> tuple[int, int]:
    new_count = sum(1 for row in kernels if row.get("ref", "") not in known_refs)
    updated_count = sum(
        1
        for row in kernels
        if row.get("ref", "") in known_refs
        and row.get("ref", "") in known_versions
        and known_versions[row.get("ref", "")] != row.get("lastRunTime", "")
    )
    return new_count, updated_count


def parse_line_kv(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        out[key] = value
    return out


def stable_preflight_text(preflight: str) -> str:
    volatile_keys = {"seconds_until_deadline", "seconds_until_reset"}
    lines = []
    for line in preflight.splitlines():
        key = line.split("=", 1)[0]
        if key in volatile_keys:
            continue
        lines.append(line)
    return "\n".join(lines)


def decision_report_path_for_selected_plan(selected_plan: str) -> Path | None:
    if not selected_plan:
        return None
    return REPORTS / f"{Path(selected_plan).stem}-decision.md"


def decision_report_comparison_count(path: Path | None) -> int | None:
    if path is None or not path.exists():
        return None
    match = re.search(r"^- Matched decision comparisons: (\d+)$", path.read_text(), re.MULTILINE)
    return int(match.group(1)) if match else None


def render_reset_readiness(
    date_value: str,
    rows: list[dict[str, str]],
    kernels: list[dict[str, str]],
    known_refs: set[str],
    known_versions: dict[str, str],
    plan_path: Path | None = None,
    reserve_path: Path | None = None,
    allow_reserve: bool = False,
    contingency_path: Path | None = None,
    anchor: Path = DEFAULT_ANCHOR,
) -> str:
    preflight = render_preflight(date_value, plan_path, reserve_path, allow_reserve, rows, contingency_path)
    values = parse_line_kv(preflight)
    new_notebooks, updated_notebooks = public_notebook_watch_counts(kernels, known_refs, known_versions)
    selection = recommended_final_rows(rows, anchor)

    selected_plan = values.get("selected_plan", "")
    if selected_plan == values.get("primary_plan"):
        selected_prefix = "primary"
    elif selected_plan == values.get("contingency_plan"):
        selected_prefix = "contingency"
    elif selected_plan == values.get("reserve_plan"):
        selected_prefix = "reserve"
    else:
        selected_prefix = ""

    valid_items = values.get(f"{selected_prefix}_valid_items", "") if selected_prefix else ""
    unsubmitted_items = values.get(f"{selected_prefix}_unsubmitted_items", "") if selected_prefix else ""
    duplicate_items = values.get(f"{selected_prefix}_duplicate_content_items", "") if selected_prefix else ""
    decision_report = decision_report_path_for_selected_plan(selected_plan)
    decision_count = decision_report_comparison_count(decision_report)
    decision_report_display = display_path(decision_report) if decision_report is not None else "none"
    decision_count_display = str(decision_count) if decision_count is not None else "NA"

    relation = values.get("target_date_relation", "")
    quota_remaining = int(values.get("quota_remaining", "0"))
    target_after_deadline_value = values.get("target_after_deadline", "false")
    competition_open_value = values.get("competition_open", "false")

    def gate_status(name: str) -> str:
        if name == "target_date":
            if target_after_deadline_value == "true" or competition_open_value != "true":
                return "blocked"
            return "ready_now" if relation == "current" else f"wait_{relation}"
        if name == "quota":
            if relation == "future":
                return "ready_at_reset"
            return "ready_now" if quota_remaining > 0 else "wait_for_quota"
        if name == "selected_plan":
            if not selected_plan:
                return "missing"
            if valid_items != str(DAILY_LIMIT):
                return "invalid_count"
            if duplicate_items not in {"", "0"}:
                return "duplicate_content"
            return "ready"
        if name == "decision_matrix":
            if decision_report is None:
                return "missing_plan"
            if not decision_report.exists():
                return "missing"
            if decision_count is None:
                return "malformed"
            return "ready" if decision_count > 0 else "thin"
        if name == "notebook_guard":
            return "ready" if new_notebooks == 0 and updated_notebooks == 0 else "blocked"
        if name == "final_selection":
            return "ready" if len(selection) == FINAL_SELECTION_LIMIT else "incomplete"
        raise KeyError(name)

    lines = [
        f"# CohortX Reset Readiness — {date_value}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Recommended action: `{values.get('recommended_action', '')}`",
        f"- Selected plan: `{selected_plan or 'none'}`",
        f"- Selected plan items: {valid_items or 'NA'} valid, {unsubmitted_items or 'NA'} unsubmitted, {duplicate_items or 'NA'} duplicate_content",
        f"- Quota now: {values.get('quota_used_utc', 'NA')} used, {values.get('quota_remaining', 'NA')} remaining",
        f"- Next reset UTC/BRT: {values.get('next_quota_reset_utc', 'NA')} / {values.get('next_quota_reset_brt', 'NA')}",
        f"- Deadline UTC/BRT: {values.get('competition_deadline_utc', 'NA')} / {values.get('competition_deadline_brt', 'NA')}",
        f"- Best public: {values.get('best_public', 'NA')}",
        f"- Public notebooks: new={new_notebooks}, updated={updated_notebooks}",
        f"- Final selection: {len(selection)}/{FINAL_SELECTION_LIMIT}",
        f"- Decision matrix: `{decision_report_display}` with {decision_count_display} matched comparisons",
        "",
        "## Gates",
        "",
        "| Gate | Status | Detail |",
        "|---|---|---|",
        f"| target_date | {gate_status('target_date')} | relation={relation}; target_after_deadline={target_after_deadline_value}; competition_open={competition_open_value} |",
        f"| quota | {gate_status('quota')} | quota_remaining={values.get('quota_remaining', 'NA')}; reset={values.get('next_quota_reset_utc', 'NA')} |",
        f"| selected_plan | {gate_status('selected_plan')} | plan=`{selected_plan or 'none'}`; valid={valid_items or 'NA'}; duplicates={duplicate_items or 'NA'} |",
        f"| decision_matrix | {gate_status('decision_matrix')} | report=`{decision_report_display}`; matched={decision_count_display} |",
        f"| notebook_guard | {gate_status('notebook_guard')} | public_notebooks_new={new_notebooks}; public_notebooks_updated={updated_notebooks} |",
        f"| final_selection | {gate_status('final_selection')} | selected={len(selection)}/{FINAL_SELECTION_LIMIT}; report=`reports/final-candidates.md`; csv=`reports/final-selection.csv` |",
        "",
        "## Reset Command",
        "",
        "```bash",
        ".venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan",
        "```",
        "",
        "## Submit Rules",
        "",
        "- Run the reset command only when `preflight` returns `recommended_action=submit_primary` for the current UTC date.",
        "- Do not pass `--date` during the live reset run; let the CLI resolve the current UTC day.",
        f"- Use the selected plan `{selected_plan or 'none'}` unless the preflight switches to a newer primary plan.",
        "- Stop before submission if any new or updated public notebook appears, then sync/audit it first.",
        "",
        "## Raw Preflight",
        "",
        "Volatile countdown fields are omitted so this report stays stable between readiness checks.",
        "",
        "```text",
        stable_preflight_text(preflight),
        "```",
    ]
    return "\n".join(lines)


def write_reset_readiness(
    date_value: str,
    out_path: Path | None,
    plan_path: Path | None = None,
    reserve_path: Path | None = None,
    allow_reserve: bool = False,
    contingency_path: Path | None = None,
    anchor: Path = DEFAULT_ANCHOR,
) -> Path:
    rows = read_submissions()
    content = render_reset_readiness(
        date_value,
        rows,
        read_kernels(),
        known_notebook_refs(),
        known_notebook_versions(),
        plan_path,
        reserve_path,
        allow_reserve,
        contingency_path,
        anchor,
    )
    path = out_path or (REPORTS / f"{date_value}-readiness.md")
    target = path if path.is_absolute() else ROOT / path
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
    csv_target = target.with_name("final-selection.csv")
    csv_target.write_text(render_final_selection_csv(rows, anchor))
    print(csv_target.relative_to(ROOT))
    audit_target = target.with_name("final-selection-audit.md")
    audit_target.write_text(render_final_selection_audit(rows, anchor) + "\n")
    print(audit_target.relative_to(ROOT))
    diversity_target = target.with_name("final-diversity.md")
    diversity_target.write_text(render_final_diversity_watchlist(rows, anchor) + "\n")
    print(diversity_target.relative_to(ROOT))
    return target


def write_final_selection_audit(anchor: Path, out_path: Path | None) -> Path:
    rows = read_submissions()
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    content = render_final_selection_audit(rows, anchor)
    path = out_path or (REPORTS / "final-selection-audit.md")
    target = path if path.is_absolute() else ROOT / path
    if ".." in target.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content + "\n")
    print(target.relative_to(ROOT))
    return target


def write_final_diversity_watchlist(anchor: Path, out_path: Path | None) -> Path:
    rows = read_submissions()
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    content = render_final_diversity_watchlist(rows, anchor)
    path = out_path or (REPORTS / "final-diversity.md")
    target = path if path.is_absolute() else ROOT / path
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


def write_plan_strategy_audit(plan_path: Path, anchor: Path, out_path: Path | None) -> Path:
    if not plan_path.is_absolute():
        plan_path = ROOT / plan_path
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    items = validate_plan(plan_path)
    content = render_plan_strategy_audit(plan_path, items, anchor)
    path = out_path or (REPORTS / f"{plan_path.stem}-strategy.md")
    target = path if path.is_absolute() else ROOT / path
    if ".." in target.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {path}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content + "\n")
    print(target.relative_to(ROOT))
    return target


def write_plan_decision_matrix(plan_path: Path, anchor: Path, out_path: Path | None) -> Path:
    if not plan_path.is_absolute():
        plan_path = ROOT / plan_path
    if not anchor.is_absolute():
        anchor = ROOT / anchor
    items = validate_plan(plan_path)
    content = render_plan_decision_matrix(plan_path, items, anchor)
    path = out_path or (REPORTS / f"{plan_path.stem}-decision.md")
    target = path if path.is_absolute() else ROOT / path
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


def inferred_next_start_version(prior_plan: Path) -> int | None:
    versions: list[int] = []
    for item in read_plan(prior_plan):
        match = re.match(r"v(\d+)_", item.file.name)
        if match:
            versions.append(int(match.group(1)))
    return max(versions) + 1 if versions else None


def next_available_start_version(prior_plan: Path) -> int | None:
    start = inferred_next_start_version(prior_plan)
    if start is None:
        return None
    used = existing_submission_versions()
    while start in used:
        start += 1
    return start


def plan_versions(items: list[PlanItem]) -> list[int]:
    versions: list[int] = []
    for item in items:
        match = re.match(r"v(\d+)_", item.file.name)
        if match:
            versions.append(int(match.group(1)))
    return versions


def is_modern_post_july4_plan(versions: list[int]) -> bool:
    return bool(versions) and min(versions) >= 341


def next_plan_script_for(prior_plan: Path) -> Path:
    try:
        items = read_plan(prior_plan)
    except OSError:
        items = []
    names = [item.file.name.lower() for item in items]
    versions = plan_versions(items)
    if versions and min(versions) >= 301 and max(versions) <= 320:
        return ROOT / "src" / "v341_360_post_july4_followups.py"
    if is_modern_post_july4_plan(versions):
        return ROOT / "src" / "v341_360_post_july4_followups.py"
    if any("assocdiff" in name for name in names):
        return ROOT / "src" / "v301_320_post_assocdiff_followups.py"
    return ROOT / "src" / "v221_240_adaptive_followups.py"


def next_plan_report_anchor(prior_plan: Path) -> Path:
    try:
        items = read_plan(prior_plan)
    except OSError:
        items = []
    names = [item.file.name.lower() for item in items]
    versions = plan_versions(items)
    if versions and min(versions) >= 301 and max(versions) <= 320:
        return ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
    if is_modern_post_july4_plan(versions):
        return ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
    if any("assocdiff" in name for name in names):
        return ROOT / "submissions" / "v209_copd_no_acute_bronch_asthma.csv"
    return DEFAULT_ANCHOR


def plan_report_anchor_for(plan_path: Path) -> Path:
    try:
        items = read_plan(plan_path)
    except OSError:
        items = []
    names = [item.file.name.lower() for item in items]
    versions = plan_versions(items)
    if versions and min(versions) >= 301 and max(versions) <= 320:
        return ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
    if is_modern_post_july4_plan(versions):
        return ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
    if any("copd_no_j20_j45" in name and "med_add_thymus_nodes" in name for name in names):
        return ROOT / "submissions" / "v296_copd_no_j20_j45_j81_j82_j93_j95.csv"
    if any("assocdiff" in name for name in names):
        return ROOT / "submissions" / "v209_copd_no_acute_bronch_asthma.csv"
    return DEFAULT_ANCHOR


def generate_next_plan(prior_plan: Path, next_plan: Path, start_version: int | None) -> None:
    script = next_plan_script_for(prior_plan)
    if not script.exists():
        print(f"next_plan_script_missing={script.relative_to(ROOT)}")
        return
    if next_plan.exists():
        print(f"next_plan_exists={next_plan.relative_to(ROOT)}")
        return
    args = [sys.executable, str(script), "--prior-plan", str(prior_plan), "--out-plan", str(next_plan)]
    if start_version is None:
        start_version = next_available_start_version(prior_plan)
    if start_version is not None:
        args.extend(["--start-version", str(start_version)])
    proc = subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    print(proc.stdout.strip())
    if proc.returncode != 0:
        print(f"next_plan_not_ready={next_plan.relative_to(ROOT)}")
        return
    validate_plan(next_plan)
    anchor = plan_report_anchor_for(next_plan)
    write_plan_report(next_plan, anchor, None)
    write_plan_strategy_audit(next_plan, anchor, None)
    write_plan_decision_matrix(next_plan, anchor, None)


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
    allow_new_notebooks: bool = False,
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
        intel_path = write_intel(date_value, None)
        new_notebook_count, new_notebook_refs = intel_public_notebook_alerts(intel_path)
        if new_notebook_count and not allow_new_notebooks:
            print(f"new_public_notebooks_guard={new_notebook_count}")
            for ref in new_notebook_refs[:10]:
                print(f"new_public_notebook={ref}")
            print("new_public_notebooks_action=download_diff_audit_before_submit")
            print("new_public_notebooks_command=.venv/bin/python src/sync_public_notebooks.py")
            return
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
        if plan_kind in {"primary", "public_contingency"}:
            plan_anchor = plan_report_anchor_for(plan)
        items = validate_plan(plan)
        print(f"validated_plan_items={len(items)}")
        write_plan_report(plan, plan_anchor, None)
        write_plan_strategy_audit(plan, plan_anchor, None)
        write_plan_decision_matrix(plan, plan_anchor, None)
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
    readiness = sub.add_parser("readiness")
    readiness.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    readiness.add_argument("--plan", type=Path)
    readiness.add_argument("--contingency-plan", type=Path)
    readiness.add_argument("--reserve-plan", type=Path)
    readiness.add_argument("--allow-reserve", action="store_true")
    readiness.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    readiness.add_argument("--out", type=Path)
    plan_report = sub.add_parser("plan-report")
    plan_report.add_argument("plan", type=Path)
    plan_report.add_argument("--anchor", type=Path)
    plan_report.add_argument("--out", type=Path)
    plan_strategy = sub.add_parser("plan-strategy")
    plan_strategy.add_argument("plan", type=Path)
    plan_strategy.add_argument("--anchor", type=Path)
    plan_strategy.add_argument("--out", type=Path)
    plan_decision = sub.add_parser("plan-decision")
    plan_decision.add_argument("plan", type=Path)
    plan_decision.add_argument("--anchor", type=Path)
    plan_decision.add_argument("--out", type=Path)
    plan_scorecard = sub.add_parser("plan-scorecard")
    plan_scorecard.add_argument("plan", type=Path)
    plan_scorecard.add_argument("--anchor", type=Path)
    plan_scorecard.add_argument("--out", type=Path)
    final = sub.add_parser("final-candidates")
    final.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    final.add_argument("--out", type=Path)
    final_audit = sub.add_parser("final-audit")
    final_audit.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    final_audit.add_argument("--out", type=Path)
    final_diversity = sub.add_parser("final-diversity")
    final_diversity.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    final_diversity.add_argument("--out", type=Path)
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
    daily.add_argument("--allow-new-notebooks", action="store_true")
    args = parser.parse_args(argv)

    if args.cmd == "status":
        print_status()
    elif args.cmd == "preflight":
        print_preflight(args.date, args.plan, args.reserve_plan, args.allow_reserve, args.contingency_plan)
    elif args.cmd == "validate-plan":
        items = validate_plan(args.plan)
        print(f"validated_plan_items={len(items)}")
    elif args.cmd == "submit-plan":
        if args.dry_run:
            submit_plan(args.plan, dry_run=args.dry_run, wait=not args.no_wait)
        else:
            lock = SubmissionLock()
            if not lock.acquire():
                print_lock_held(lock)
                return 0
            try:
                submit_plan(args.plan, dry_run=args.dry_run, wait=not args.no_wait)
            finally:
                lock.release()
    elif args.cmd == "review":
        write_review(args.date, args.out)
    elif args.cmd == "intel":
        write_intel(args.date, args.out)
    elif args.cmd == "readiness":
        write_reset_readiness(
            args.date,
            args.out,
            args.plan,
            args.reserve_plan,
            args.allow_reserve,
            args.contingency_plan,
            args.anchor,
        )
    elif args.cmd == "plan-report":
        anchor = args.anchor if args.anchor is not None else plan_report_anchor_for(args.plan)
        write_plan_report(args.plan, anchor, args.out)
    elif args.cmd == "plan-strategy":
        anchor = args.anchor if args.anchor is not None else plan_report_anchor_for(args.plan)
        write_plan_strategy_audit(args.plan, anchor, args.out)
    elif args.cmd == "plan-decision":
        anchor = args.anchor if args.anchor is not None else plan_report_anchor_for(args.plan)
        write_plan_decision_matrix(args.plan, anchor, args.out)
    elif args.cmd == "plan-scorecard":
        anchor = args.anchor if args.anchor is not None else plan_report_anchor_for(args.plan)
        write_plan_scorecard(args.plan, anchor, args.out)
    elif args.cmd == "final-candidates":
        write_final_candidates(args.anchor, args.out)
    elif args.cmd == "final-audit":
        write_final_selection_audit(args.anchor, args.out)
    elif args.cmd == "final-diversity":
        write_final_diversity_watchlist(args.anchor, args.out)
    elif args.cmd == "signals":
        write_signals(args.date, args.anchor, args.out)
    elif args.cmd == "daily-run":
        next_plan_path = args.next_plan
        if args.auto_next_plan and next_plan_path is None:
            next_plan_path = default_next_plan_path(args.date)
        if args.dry_run:
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
                allow_new_notebooks=args.allow_new_notebooks,
            )
        else:
            lock = SubmissionLock()
            if not lock.acquire():
                print_lock_held(lock)
                return 0
            try:
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
                    allow_new_notebooks=args.allow_new_notebooks,
                )
            finally:
                lock.release()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
