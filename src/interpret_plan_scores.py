"""Interpret scored plan probes using exact ICD code deltas."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

try:
    from audit_plan_deltas import CodeDelta, code_block, plan_deltas, read_titles
    from cohortx_ops import (
        DEFAULT_ANCHOR,
        ROOT,
        PlanItem,
        anchor_public_score,
        latest_rows_by_file,
        plan_score_signal,
        public_score,
        read_plan,
        read_submissions,
        validate_plan,
    )
except ModuleNotFoundError:
    from src.audit_plan_deltas import CodeDelta, code_block, plan_deltas, read_titles
    from src.cohortx_ops import (
        DEFAULT_ANCHOR,
        ROOT,
        PlanItem,
        anchor_public_score,
        latest_rows_by_file,
        plan_score_signal,
        public_score,
        read_plan,
        read_submissions,
        validate_plan,
    )


DEFAULT_PLAN = ROOT / "plans" / "2026-07-02.csv"
DEFAULT_OUT = ROOT / "reports" / "2026-07-02-impact.md"


@dataclass(frozen=True)
class InterpretedProbe:
    order: int
    item: PlanItem
    status: str
    score: float | None
    delta: float | None
    signal: str
    code_delta: CodeDelta | None
    interpretation: str


def resolve(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def delta_kind(delta: CodeDelta | None) -> str:
    if delta is None:
        return "no local delta"
    if delta.added and delta.removed:
        return f"+{len(delta.added)}/-{len(delta.removed)}"
    if delta.added:
        return f"added {len(delta.added)}"
    if delta.removed:
        return f"removed {len(delta.removed)}"
    return "no code change"


def action_for(signal: str, delta: CodeDelta | None) -> str:
    if signal == "missing_score":
        return "wait for Kaggle score before changing strategy"
    if delta is None:
        return "inspect manually; local delta not found"
    if signal == "improved":
        if delta.removed and not delta.added:
            return "removal improved public score; consider pruning these codes or combining this removal"
        if delta.added and not delta.removed:
            return "addition improved public score; consider promoting these codes or combining this addition"
        return "mixed edit improved public score; decompose before promoting"
    if signal == "worse":
        if delta.removed and not delta.added:
            return "removal hurt public score; keep/restore these codes in public-facing candidates"
        if delta.added and not delta.removed:
            return "addition hurt public score; treat these codes as public false positives"
        return "mixed edit hurt public score; avoid as-is and decompose"
    if signal == "tied":
        if delta.added:
            return "public-neutral addition; useful mainly as private hedge or low-priority combo"
        if delta.removed:
            return "public-neutral removal; possible private hedge, but do not prune public anchor yet"
        return "public-neutral/no-op"
    return "scored; inspect alongside final-candidates"


def delta_by_file(deltas: list[CodeDelta]) -> dict[str, CodeDelta]:
    by_file: dict[str, CodeDelta] = {}
    for delta in deltas:
        by_file.setdefault(delta.item.file.name, delta)
    return by_file


def interpret_plan(plan_path: Path, anchor: Path) -> tuple[float | None, list[InterpretedProbe]]:
    plan = resolve(plan_path)
    anchor_path = resolve(anchor)
    validate_plan(plan)
    rows = read_submissions()
    latest = latest_rows_by_file(rows)
    baseline = anchor_public_score(rows, anchor_path)
    deltas = delta_by_file(plan_deltas(plan, anchor_path))
    interpreted: list[InterpretedProbe] = []
    for order, item in enumerate(read_plan(plan), start=1):
        row = latest.get(item.file.name)
        score = public_score(row) if row else None
        delta = score - baseline if score is not None and baseline is not None else None
        signal = plan_score_signal(score, baseline)
        code_delta = deltas.get(item.file.name)
        interpreted.append(InterpretedProbe(
            order=order,
            item=item,
            status=row.get("status", "missing") if row else "missing",
            score=score,
            delta=delta,
            signal=signal,
            code_delta=code_delta,
            interpretation=action_for(signal, code_delta),
        ))
    return baseline, interpreted


def render_report(plan_path: Path, anchor: Path, baseline: float | None, probes: list[InterpretedProbe]) -> str:
    titles = read_titles()
    scored = [probe for probe in probes if probe.score is not None]
    improved = [probe for probe in scored if probe.signal == "improved"]
    tied = [probe for probe in scored if probe.signal == "tied"]
    worse = [probe for probe in scored if probe.signal == "worse"]
    missing = [probe for probe in probes if probe.signal == "missing_score"]

    lines = [
        f"# CohortX Plan Impact Readout - {resolve(plan_path).stem}",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Plan: `{display_path(resolve(plan_path))}`",
        f"- Anchor: `{display_path(resolve(anchor))}`",
        f"- Anchor public: {baseline:.5f}" if baseline is not None else "- Anchor public: NA",
        f"- Scored items: {len(scored)}/{len(probes)}",
        f"- Improved/tied/worse/missing: {len(improved)}/{len(tied)}/{len(worse)}/{len(missing)}",
        "",
        "## Decision Table",
        "",
        "| Order | File | Status | Public | Delta | Signal | Edit | Interpretation |",
        "|---:|---|---|---:|---:|---|---|---|",
    ]
    for probe in probes:
        score = f"{probe.score:.5f}" if probe.score is not None else ""
        delta = f"{probe.delta:+.5f}" if probe.delta is not None else ""
        lines.append(
            f"| {probe.order} | `{probe.item.file.name}` | {probe.status} | {score} | {delta} | "
            f"{probe.signal} | {delta_kind(probe.code_delta)} | {probe.interpretation} |"
        )

    ranked = sorted(
        [probe for probe in scored if probe.delta is not None],
        key=lambda probe: probe.delta or 0.0,
        reverse=True,
    )
    if ranked:
        lines.extend([
            "",
            "## Ranked Scored Probes",
            "",
            "| Rank | File | Delta | ICD change | Exact codes |",
            "|---:|---|---:|---|---|",
        ])
        for rank, probe in enumerate(ranked, start=1):
            code_delta = probe.code_delta
            exact = "none"
            if code_delta is not None:
                codes = code_delta.added or code_delta.removed
                exact = code_block(codes, titles, 8)
            lines.append(
                f"| {rank} | `{probe.item.file.name}` | {probe.delta:+.5f} | "
                f"{delta_kind(code_delta)} | {exact} |"
            )
    else:
        lines.extend([
            "",
            "## Ranked Scored Probes",
            "",
            "No completed plan scores yet. Run this again after the batch is submitted and complete.",
        ])

    lines.extend([
        "",
        "## Use",
        "",
        "- Improved removals are pruning candidates for public-facing combos.",
        "- Improved additions are promotion candidates for public-facing combos.",
        "- Tied edits are mainly private hedges unless later combo evidence says otherwise.",
        "- Worse removals indicate codes that likely belong in the public gold slice; worse additions are public false positives.",
        "",
    ])
    return "\n".join(lines)


def write_report(plan_path: Path = DEFAULT_PLAN, anchor: Path = DEFAULT_ANCHOR, out_path: Path = DEFAULT_OUT) -> Path:
    plan = resolve(plan_path)
    anchor_path = resolve(anchor)
    out = resolve(out_path)
    if ".." in out.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {out_path}")
    baseline, probes = interpret_plan(plan, anchor_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_report(plan, anchor_path, baseline, probes).rstrip() + "\n")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    parser.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    path = write_report(args.plan, args.anchor, args.out)
    print(display_path(path))


if __name__ == "__main__":
    main()
