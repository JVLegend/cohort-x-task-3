"""Operational helpers for the CohortX Task 3 submission loop."""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path


COMPETITION = "cohort-x-task-3"
EXPECTED_COLUMNS = ["Condition", "KEEP", "ASSOCIATION", "DIFF"]
DAILY_LIMIT = 20
ROOT = Path(__file__).resolve().parents[1]
KAGGLE = ROOT / ".venv" / "bin" / "kaggle"
REPORTS = ROOT / "reports"
DEFAULT_ANCHOR = ROOT / "submissions" / "v178_FINAL.csv"
csv.field_size_limit(10_000_000)
BRT = timezone(timedelta(hours=-3))


@dataclass(frozen=True)
class PlanItem:
    file: Path
    message: str
    notes: str = ""


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


def validate_plan(path: Path) -> list[PlanItem]:
    items = read_plan(path)
    for item in items:
        validate_submission(item.file)
    return items


def plan_notes_for_date(date_value: str) -> dict[str, PlanItem]:
    plan_path = ROOT / "plans" / f"{date_value}.csv"
    if not plan_path.exists():
        return {}
    return {item.file.name: item for item in read_plan(plan_path)}


def print_status() -> None:
    comp = run(["competitions", "list", "-s", COMPETITION])
    print(comp.stdout.strip())
    rows = read_submissions()
    today = submissions_today(rows)
    best = best_public(rows)
    reset = next_quota_reset()
    print(f"submissions_today_utc={len(today)}/{DAILY_LIMIT}")
    print(f"next_quota_reset_utc={format_utc(reset)}")
    print(f"next_quota_reset_brt={format_brt(reset)}")
    print(f"seconds_until_reset={seconds_until_reset()}")
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


def inspect_plan(path: Path, submitted: set[str]) -> tuple[list[PlanItem], list[PlanItem]]:
    items = validate_plan(path)
    unsubmitted = [item for item in items if item.file.name not in submitted]
    return items, unsubmitted


def render_preflight(
    date_value: str,
    plan_path: Path | None,
    reserve_path: Path | None,
    allow_reserve: bool,
    rows: list[dict[str, str]],
) -> str:
    primary = resolve_path(plan_path or (ROOT / "plans" / f"{date_value}.csv"))
    reserve = resolve_path(reserve_path or (ROOT / "plans" / f"{date_value}-reserve.csv"))
    now = utc_now()
    today = submissions_today(rows, now)
    remaining = max(0, DAILY_LIMIT - len(today))
    submitted = remote_filenames(rows)
    reset = next_quota_reset(now)
    relation = target_date_relation(date_value, now)

    lines = [
        f"preflight_date={date_value}",
        f"current_utc_date={now.date().isoformat()}",
        f"target_date_relation={relation}",
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
        primary_items, primary_unsubmitted = inspect_plan(primary, submitted)
        lines.extend([
            f"primary_valid_items={len(primary_items)}",
            f"primary_unsubmitted_items={len(primary_unsubmitted)}",
        ])

    lines.extend([
        f"reserve_plan={display_path(reserve)}",
        f"reserve_exists={str(reserve.exists()).lower()}",
        f"reserve_allowed={str(allow_reserve).lower()}",
    ])

    reserve_items: list[PlanItem] = []
    reserve_unsubmitted: list[PlanItem] = []
    if reserve.exists():
        reserve_items, reserve_unsubmitted = inspect_plan(reserve, submitted)
        lines.extend([
            f"reserve_valid_items={len(reserve_items)}",
            f"reserve_unsubmitted_items={len(reserve_unsubmitted)}",
        ])

    selected: Path | None = None
    if relation == "future":
        selected = primary if primary.exists() else None
        action = "wait_for_target_date"
    elif relation == "past":
        selected = primary if primary.exists() else None
        action = "stale_plan_date"
    elif primary.exists():
        selected = primary
        if not primary_unsubmitted:
            action = "primary_already_submitted"
        elif remaining <= 0:
            action = "wait_for_quota"
        else:
            action = "submit_primary"
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
    else:
        action = "create_primary_plan"

    lines.append(f"recommended_action={action}")
    if selected is not None:
        lines.append(f"selected_plan={display_path(selected)}")
    return "\n".join(lines)


def print_preflight(date_value: str, plan_path: Path | None, reserve_path: Path | None, allow_reserve: bool) -> None:
    rows = read_submissions()
    print(render_preflight(date_value, plan_path, reserve_path, allow_reserve, rows))


def submit_plan(path: Path, dry_run: bool, wait: bool) -> None:
    items = validate_plan(path)
    rows = read_submissions()
    used = len(submissions_today(rows))
    remaining = max(0, DAILY_LIMIT - used)
    submitted = remote_filenames(rows)
    candidates = [item for item in items if item.file.name not in submitted]

    print(f"quota_used_utc={used}/{DAILY_LIMIT}")
    print(f"plan_items={len(items)} unsubmitted_plan_items={len(candidates)}")
    if remaining <= 0:
        print("quota_remaining=0; no submissions sent")
        return

    for item in candidates[:remaining]:
        rel = item.file.relative_to(ROOT)
        print(f"submit {rel}: {item.message}")
        if dry_run:
            continue
        proc = run(["competitions", "submit", "-c", COMPETITION, "-f", str(rel), "-m", item.message])
        print(proc.stdout.strip())
        if proc.returncode != 0:
            raise RuntimeError(f"submit failed for {rel}")
        time.sleep(2)

    if wait and not dry_run:
        wait_until_complete()


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

    single_condition_rows: list[tuple[str, str, float, float, str]] = []
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
            single_condition_rows.append((changes[0][0], row["fileName"], score, delta, changes[0][1]))

    if single_condition_rows:
        lines.extend([
            "",
            "## Single-Condition Probes",
            "",
            "| Condition | File | Public | Delta | Change |",
            "|---|---|---:|---:|---|",
        ])
        ranked = sorted(single_condition_rows, key=lambda item: item[3])
        for condition, filename, score, delta, change in ranked:
            lines.append(f"| {condition} | `{filename}` | {score:.5f} | {delta:+.5f} | {change} |")

    lines.extend([
        "",
        "## Use",
        "",
        "- Large negative single-condition probes identify public split movers.",
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


def render_final_candidates(rows: list[dict[str, str]], anchor: Path) -> str:
    complete = [row for row in rows if row.get("status") == "complete" and public_score(row) is not None]
    complete = sorted(complete, key=lambda row: (public_score(row) or 0.0, parse_kaggle_date(row["date"])), reverse=True)
    best = public_score(complete[0]) if complete else None
    tied_best = [row for row in complete if best is not None and public_score(row) == best]
    changed_tied = [
        row for row in tied_best
        if local_submission_path(row["fileName"]).exists()
        and changed_conditions_text(anchor, local_submission_path(row["fileName"])) != "identical to anchor"
    ]
    anchor_rows = [
        row for row in tied_best
        if row["fileName"] == anchor.name or changed_conditions_text(anchor, local_submission_path(row["fileName"])) == "identical to anchor"
    ]
    public_anchor = anchor_rows[0] if anchor_rows else (tied_best[0] if tied_best else None)
    private_hedge = next((row for row in changed_tied if row["fileName"] == "v185_private_kw.csv"), None)
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
        "",
        "## Recommended Final Pool",
        "",
        "| Slot | File | Public | Reason | Changed conditions |",
        "|---|---|---:|---|---|",
    ]
    if public_anchor:
        path = local_submission_path(public_anchor["fileName"])
        lines.append(
            f"| Public anchor | `{public_anchor['fileName']}` | {public_score(public_anchor):.5f} | strongest public baseline | {changed_conditions_text(anchor, path)} |"
        )
    if private_hedge:
        path = local_submission_path(private_hedge["fileName"])
        lines.append(
            f"| Private hedge | `{private_hedge['fileName']}` | {public_score(private_hedge):.5f} | public-neutral hidden-condition changes | {changed_conditions_text(anchor, path)} |"
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
        "- Keep public-neutral hedges only when they change hidden/private conditions or a distinct clinical family.",
        "- Do not promote probes that lose public score unless later private/hidden evidence justifies them.",
        "",
    ])
    return "\n".join(lines)


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


def daily_run(
    date_value: str,
    plan_path: Path | None,
    dry_run: bool,
    wait: bool,
    skip_reports: bool,
    next_plan_path: Path | None,
    start_version: int | None,
) -> None:
    plan = plan_path or (ROOT / "plans" / f"{date_value}.csv")
    if not plan.is_absolute():
        plan = ROOT / plan
    next_plan = next_plan_path
    if next_plan is not None and not next_plan.is_absolute():
        next_plan = ROOT / next_plan

    relation = target_date_relation(date_value)
    print_status()
    plan_ready = False
    if plan.exists():
        items = validate_plan(plan)
        print(f"validated_plan_items={len(items)}")
        write_plan_report(plan, DEFAULT_ANCHOR, None)
        print(f"target_date_relation={relation}")
        if relation == "current":
            submit_plan(plan, dry_run=dry_run, wait=wait)
            plan_ready = True
        else:
            print("date_guard=skip_submit")
    else:
        print(f"plan_missing={plan.relative_to(ROOT)}")

    if skip_reports:
        print("skip_reports=true")
        return

    write_review(date_value, None)
    write_signals(date_value, DEFAULT_ANCHOR, None)
    write_final_candidates(DEFAULT_ANCHOR, None)
    if next_plan is not None and plan_ready:
        generate_next_plan(plan, next_plan, start_version)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    preflight = sub.add_parser("preflight")
    preflight.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    preflight.add_argument("--plan", type=Path)
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
    plan_report = sub.add_parser("plan-report")
    plan_report.add_argument("plan", type=Path)
    plan_report.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    plan_report.add_argument("--out", type=Path)
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
    args = parser.parse_args(argv)

    if args.cmd == "status":
        print_status()
    elif args.cmd == "preflight":
        print_preflight(args.date, args.plan, args.reserve_plan, args.allow_reserve)
    elif args.cmd == "validate-plan":
        items = validate_plan(args.plan)
        print(f"validated_plan_items={len(items)}")
    elif args.cmd == "submit-plan":
        submit_plan(args.plan, dry_run=args.dry_run, wait=not args.no_wait)
    elif args.cmd == "review":
        write_review(args.date, args.out)
    elif args.cmd == "plan-report":
        write_plan_report(args.plan, args.anchor, args.out)
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
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
