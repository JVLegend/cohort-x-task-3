"""Audit downloaded public Kaggle notebooks for strategic signal."""
from __future__ import annotations

import argparse
import ast
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTERNAL = ROOT / "external_notebooks"
REPORT = ROOT / "reports" / "public-notebook-audit.md"
MODEL_HINTS = (
    "SentenceTransformer",
    "BioBERT",
    "MiniLM",
    "mpnet",
    "pritamdeka",
    "all-MiniLM",
    "all-mpnet",
)


@dataclass(frozen=True)
class NotebookAudit:
    ref: str
    title: str
    path: Path
    code_lines: int
    imports: tuple[str, ...]
    models: tuple[str, ...]
    retrieval: tuple[str, ...]
    constants: tuple[str, ...]
    fills_assoc_diff: bool
    label_strategy: str
    strategic_read: str


def source_text(payload: dict) -> str:
    parts: list[str] = []
    for cell in payload.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        source = cell.get("source", "")
        if isinstance(source, list):
            parts.append("".join(source))
        elif isinstance(source, str):
            parts.append(source)
    return "\n\n".join(parts)


def quoted_strings(code: str) -> list[str]:
    out: list[str] = []
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            out.append(node.value)
    return out


def import_lines(code: str) -> tuple[str, ...]:
    lines = []
    for line in code.splitlines():
        clean = line.strip()
        if clean.startswith(("import ", "from ")):
            lines.append(clean)
    return tuple(dict.fromkeys(lines))


def model_names(code: str) -> tuple[str, ...]:
    names = []
    for value in quoted_strings(code):
        looks_like_model_id = "/" in value or value.startswith(("all-", "pritamdeka"))
        if looks_like_model_id and any(hint.lower() in value.lower() for hint in MODEL_HINTS):
            names.append(value)
    return tuple(dict.fromkeys(names))


def retrieval_components(code: str) -> tuple[str, ...]:
    checks = [
        ("embedding cosine", "cosine_similarity" in code or ".encode(" in code),
        ("TF-IDF", "TfidfVectorizer" in code),
        ("BM25", "BM25Okapi" in code),
        ("score ensemble", all(token in code for token in ("ALPHA", "BETA"))),
        ("abbreviation expansion", "ABBREVIATIONS" in code),
        ("embedding ensemble", "MODELS" in code and "np.mean" in code),
    ]
    return tuple(name for name, present in checks if present)


def constant_lines(code: str) -> tuple[str, ...]:
    constants = []
    for line in code.splitlines():
        clean = line.strip()
        if re.match(r"^(TOP_K|ALPHA|BETA|GAMMA|KEEP_THRESHOLD|ASSOCIATION_THRESHOLD)\s*=", clean):
            constants.append(clean)
    return tuple(constants)


def label_strategy(code: str) -> tuple[bool, str]:
    lower = code.lower()
    fills_assoc_diff = (
        '"association": assoc' in lower
        or '"association": association' in lower
        or "assoc = top_codes" in lower
        or "association = []" in lower
    ) and (
        '"diff": diff' in lower
        or "diff = []" in lower
        or "diff = top_codes" in lower
    )
    if "top_codes[:3]" in code and "top_codes[3:8]" in code:
        return fills_assoc_diff, "fixed top-k split: KEEP first 3, ASSOC next 5, DIFF next 7"
    if "mean_sim" in code and "std_sim" in code:
        return fills_assoc_diff, "dynamic z-style split over top candidates"
    if "KEEP_THRESHOLD" in code and "ASSOCIATION_THRESHOLD" in code:
        return fills_assoc_diff, "relative-threshold split over top candidates"
    return fills_assoc_diff, "unclassified label split"


def strategic_read(audit: NotebookAudit) -> str:
    notes = []
    if audit.fills_assoc_diff:
        notes.append("fills ASSOC/DIFF; risky because local probes show empty ASSOC/DIFF is often rewarded")
    if "BM25" in audit.retrieval:
        notes.append("BM25/TF-IDF can inspire retrieval candidates, but not direct label filling")
    if any("MiniLM" in model for model in audit.models):
        notes.append("generic MiniLM/mpnet signal is weaker than current medical-curated anchor")
    if not notes:
        notes.append("no stronger signal than current curated/public-probe strategy")
    return "; ".join(notes)


def audit_notebook(directory: Path) -> NotebookAudit:
    metadata_path = directory / "kernel-metadata.json"
    metadata = json.loads(metadata_path.read_text())
    notebook_path = directory / metadata["code_file"]
    payload = json.loads(notebook_path.read_text())
    code = source_text(payload)
    fills_assoc_diff, labels = label_strategy(code)
    audit = NotebookAudit(
        ref=metadata.get("id", directory.name),
        title=metadata.get("title", directory.name),
        path=notebook_path,
        code_lines=len([line for line in code.splitlines() if line.strip()]),
        imports=import_lines(code),
        models=model_names(code),
        retrieval=retrieval_components(code),
        constants=constant_lines(code),
        fills_assoc_diff=fills_assoc_diff,
        label_strategy=labels,
        strategic_read="",
    )
    return NotebookAudit(
        **{**audit.__dict__, "strategic_read": strategic_read(audit)}
    )


def audit_all(root: Path = EXTERNAL) -> list[NotebookAudit]:
    audits = []
    for directory in sorted(root.glob("*")):
        if (directory / "kernel-metadata.json").exists():
            audits.append(audit_notebook(directory))
    return audits


def join(values: tuple[str, ...]) -> str:
    return "<br>".join(values) if values else "none"


def render_report(audits: list[NotebookAudit]) -> str:
    lines = [
        "# Public Notebook Audit",
        "",
        "Tags: #JoaoVictor #Kaggle #Academia #Tecnologia",
        "",
        f"- Downloaded public notebooks audited: {len(audits)}",
        "- Scope: local notebooks in `external_notebooks/` linked to CohortX Task 3.",
        "- Decision: do not copy these baselines directly; use them only as weak retrieval ideas.",
        "",
        "## Notebook Signals",
        "",
        "| Ref | Title | Lines | Retrieval | Models | Label strategy | Risk/read |",
        "|---|---|---:|---|---|---|---|",
    ]
    for audit in audits:
        lines.append(
            f"| `{audit.ref}` | {audit.title.replace('|', '/')} | {audit.code_lines} | "
            f"{join(audit.retrieval)} | {join(audit.models)} | "
            f"{audit.label_strategy} | {audit.strategic_read} |"
        )

    lines.extend([
        "",
        "## Constants",
        "",
        "| Ref | Constants | Imports |",
        "|---|---|---|",
    ])
    for audit in audits:
        lines.append(f"| `{audit.ref}` | {join(audit.constants)} | {join(audit.imports)} |")

    lines.extend([
        "",
        "## Strategic Takeaways",
        "",
        "- All downloaded public notebooks are retrieval baselines, not evidence of a stronger labeling policy.",
        "- Every notebook fills ASSOCIATION/DIFF either by fixed slices or score thresholds; local Kaggle probes indicate that is usually harmful.",
        "- Useful reusable ideas are limited to abbreviation expansion, BM25/TF-IDF candidate generation, and model ensembling for candidate discovery.",
        "- The active plan should remain controlled public probes on COPD and Enlarged Mediastinum, followed by adaptive combinations only after scores are complete.",
        "",
    ])
    return "\n".join(lines)


def write_report(out_path: Path = REPORT) -> Path:
    audits = audit_all()
    out = out_path if out_path.is_absolute() else ROOT / out_path
    if ".." in out.relative_to(ROOT).parts:
        raise ValueError(f"unsafe report path: {out_path}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_report(audits).rstrip() + "\n")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=REPORT)
    args = parser.parse_args()
    path = write_report(args.out)
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
