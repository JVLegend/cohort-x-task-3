"""Render exact ICD code deltas for a submission plan."""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

try:
    from cohortx_ops import DEFAULT_ANCHOR, EXPECTED_COLUMNS, ROOT, PlanItem, read_plan, validate_plan
except ModuleNotFoundError:
    from src.cohortx_ops import DEFAULT_ANCHOR, EXPECTED_COLUMNS, ROOT, PlanItem, read_plan, validate_plan


ICD_DICT = ROOT / "data" / "icd_dict.csv"
DEFAULT_PLAN = ROOT / "plans" / "2026-07-02.csv"
DEFAULT_REPORT = ROOT / "reports" / "2026-07-02-code-deltas.md"


@dataclass(frozen=True)
class CodeDelta:
    item: PlanItem
    order: int
    condition: str
    column: str
    added: tuple[str, ...]
    removed: tuple[str, ...]


def resolve(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def parse_code_list(value: str) -> list[str]:
    if not value or value == "Not Applicable":
        return []
    return [code.strip() for code in value.split(";") if code.strip()]


def read_submission(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="") as fh:
        return {row["Condition"]: row for row in csv.DictReader(fh)}


def read_titles(path: Path = ICD_DICT) -> dict[str, str]:
    with path.open(newline="") as fh:
        return {row["icd_code"]: row["long_title"] for row in csv.DictReader(fh)}


def ordered_difference(current: list[str], base: list[str]) -> tuple[str, ...]:
    base_set = set(base)
    return tuple(code for code in current if code not in base_set)


def plan_deltas(plan_path: Path, anchor: Path) -> list[CodeDelta]:
    plan = resolve(plan_path)
    base_path = resolve(anchor)
    validate_plan(plan)
    base_rows = read_submission(base_path)
    deltas: list[CodeDelta] = []
    for order, item in enumerate(read_plan(plan), start=1):
        candidate_rows = read_submission(item.file)
        for condition, base_row in base_rows.items():
            candidate_row = candidate_rows[condition]
            for column in EXPECTED_COLUMNS[1:]:
                before = parse_code_list(base_row[column])
                after = parse_code_list(candidate_row[column])
                added = ordered_difference(after, before)
                removed = ordered_difference(before, after)
                if added or removed:
                    deltas.append(CodeDelta(item, order, condition, column, added, removed))
    return deltas


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def code_label(code: str, titles: dict[str, str]) -> str:
    title = titles.get(code, "title not found")
    return f"`{code}` - {title}"


def code_block(codes: tuple[str, ...], titles: dict[str, str], limit: int) -> str:
    if not codes:
        return "none"
    shown = [code_label(code, titles) for code in codes[:limit]]
    if len(codes) > limit:
        shown.append(f"... +{len(codes) - limit} more")
    return "<br>".join(shown)


def render_report(plan_path: Path, anchor: Path, deltas: list[CodeDelta], title_limit: int = 18) -> str:
    titles = read_titles()
    lines = [
        f"# CohortX Plan Code Deltas - {resolve(plan_path).stem}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Plan: `{display_path(resolve(plan_path))}`",
        f"- Anchor: `{display_path(resolve(anchor))}`",
        f"- Changed rows: {len(deltas)}",
        "- Use: when scores arrive, map each public delta back to the exact ICD families added or removed.",
        "",
        "## Delta Summary",
        "",
        "| Order | File | Condition | Column | Added | Removed | Message | Notes |",
        "|---:|---|---|---|---:|---:|---|---|",
    ]
    for delta in deltas:
        rel = display_path(delta.item.file)
        message = delta.item.message.replace("|", "/")
        notes = delta.item.notes.replace("|", "/")
        lines.append(
            f"| {delta.order} | `{rel}` | {delta.condition} | {delta.column} | "
            f"{len(delta.added)} | {len(delta.removed)} | {message} | {notes} |"
        )

    lines.extend([
        "",
        "## Exact Code Changes",
        "",
    ])
    for delta in deltas:
        lines.extend([
            f"### {delta.order}. `{delta.item.file.name}` - {delta.condition} / {delta.column}",
            "",
            f"- Message: {delta.item.message}",
            f"- Added ({len(delta.added)}): {code_block(delta.added, titles, title_limit)}",
            f"- Removed ({len(delta.removed)}): {code_block(delta.removed, titles, title_limit)}",
            "",
        ])

    return "\n".join(lines)


def write_report(plan_path: Path = DEFAULT_PLAN, anchor: Path = DEFAULT_ANCHOR, out_path: Path = DEFAULT_REPORT) -> Path:
    plan = resolve(plan_path)
    anchor_path = resolve(anchor)
    out = resolve(out_path)
    if ".." in out.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {out_path}")
    content = render_report(plan, anchor_path, plan_deltas(plan, anchor_path))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content + "\n")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    parser.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    parser.add_argument("--out", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    path = write_report(args.plan, args.anchor, args.out)
    print(display_path(path))


if __name__ == "__main__":
    main()
