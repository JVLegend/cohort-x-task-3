"""Download newly listed public Kaggle notebooks for local audit."""
from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

try:
    from cohortx_ops import ROOT, kaggle_cmd, known_notebook_refs, read_kernels
    import audit_public_notebooks
except ModuleNotFoundError:
    from src.cohortx_ops import ROOT, kaggle_cmd, known_notebook_refs, read_kernels
    from src import audit_public_notebooks


EXTERNAL = ROOT / "external_notebooks"


@dataclass(frozen=True)
class SyncResult:
    ref: str
    path: Path
    status: str


def safe_dirname(ref: str) -> str:
    value = ref.lower().replace("/", "-")
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    if not value:
        raise ValueError(f"invalid notebook ref: {ref!r}")
    return value[:96]


def new_kernel_refs() -> list[str]:
    known = known_notebook_refs()
    return [
        row["ref"]
        for row in read_kernels()
        if row.get("ref") and row["ref"] not in known
    ]


def pull_kernel(ref: str, target: Path) -> SyncResult:
    target.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        [kaggle_cmd(), "kernels", "pull", ref, "-p", str(target), "-m"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"failed to pull {ref}:\n{proc.stdout}")
    return SyncResult(ref=ref, path=target, status="downloaded")


def sync_public_notebooks(dry_run: bool = False, audit: bool = True) -> list[SyncResult]:
    refs = new_kernel_refs()
    results: list[SyncResult] = []
    for ref in refs:
        target = EXTERNAL / safe_dirname(ref)
        if dry_run:
            results.append(SyncResult(ref=ref, path=target, status="dry_run"))
            continue
        results.append(pull_kernel(ref, target))
    if audit and not dry_run:
        audit_public_notebooks.write_report()
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-audit", action="store_true")
    args = parser.parse_args()

    results = sync_public_notebooks(dry_run=args.dry_run, audit=not args.no_audit)
    print(f"new_public_notebooks={len(results)}")
    for result in results:
        print(f"{result.status} {result.ref} -> {result.path.relative_to(ROOT)}")
    if not args.dry_run and not args.no_audit:
        print("audit_report=reports/public-notebook-audit.md")


if __name__ == "__main__":
    main()
