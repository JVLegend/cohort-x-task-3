"""Operational helpers for the CohortX Task 3 submission loop."""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


COMPETITION = "cohort-x-task-3"
EXPECTED_COLUMNS = ["Condition", "KEEP", "ASSOCIATION", "DIFF"]
DAILY_LIMIT = 20
ROOT = Path(__file__).resolve().parents[1]
KAGGLE = ROOT / ".venv" / "bin" / "kaggle"
REPORTS = ROOT / "reports"


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


def submissions_today(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.now(timezone.utc).date()
    return [row for row in rows if parse_kaggle_date(row["date"]).date() == today]


def submissions_on_date(rows: list[dict[str, str]], date_value: str) -> list[dict[str, str]]:
    target = datetime.strptime(date_value, "%Y-%m-%d").date()
    return [row for row in rows if parse_kaggle_date(row["date"]).date() == target]


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
    print(f"submissions_today_utc={len(today)}/{DAILY_LIMIT}")
    print(f"best_public={best:.5f}" if best is not None else "best_public=NA")
    print("latest:")
    for row in rows[: min(25, len(rows))]:
        print(f"{row['date']} {row['fileName']} {row['status']} {row.get('publicScore', '')}")


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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    validate = sub.add_parser("validate-plan")
    validate.add_argument("plan", type=Path)
    submit = sub.add_parser("submit-plan")
    submit.add_argument("plan", type=Path)
    submit.add_argument("--dry-run", action="store_true")
    submit.add_argument("--no-wait", action="store_true")
    review = sub.add_parser("review")
    review.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    review.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    if args.cmd == "status":
        print_status()
    elif args.cmd == "validate-plan":
        items = validate_plan(args.plan)
        print(f"validated_plan_items={len(items)}")
    elif args.cmd == "submit-plan":
        submit_plan(args.plan, dry_run=args.dry_run, wait=not args.no_wait)
    elif args.cmd == "review":
        write_review(args.date, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
