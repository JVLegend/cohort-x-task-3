"""Download newly listed public Kaggle notebooks for local audit."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

try:
    from cohortx_ops import ROOT, kaggle_cmd, known_notebook_refs, read_kernels
    import audit_public_notebooks
except ModuleNotFoundError:
    from src.cohortx_ops import ROOT, kaggle_cmd, known_notebook_refs, read_kernels
    from src import audit_public_notebooks


EXTERNAL = ROOT / "external_notebooks"
MANIFEST = EXTERNAL / "public_notebook_manifest.json"


@dataclass(frozen=True)
class SyncResult:
    ref: str
    path: Path
    status: str


def read_manifest(path: Path = MANIFEST) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text())
    if not isinstance(payload, dict):
        return {}
    notebooks = payload.get("notebooks", {})
    if not isinstance(notebooks, dict):
        return {}
    return {
        str(ref): {str(key): str(value) for key, value in details.items()}
        for ref, details in notebooks.items()
        if isinstance(details, dict)
    }


def manifest_entry(row: dict[str, str]) -> dict[str, str]:
    return {
        "ref": row.get("ref", ""),
        "title": row.get("title", ""),
        "author": row.get("author", ""),
        "lastRunTime": row.get("lastRunTime", ""),
        "totalVotes": row.get("totalVotes", ""),
    }


def write_manifest(rows: list[dict[str, str]], path: Path = MANIFEST) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "notebooks": {
            row["ref"]: manifest_entry(row)
            for row in rows
            if row.get("ref")
        },
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return path


def safe_dirname(ref: str) -> str:
    value = ref.lower().replace("/", "-")
    value = re.sub(r"[^a-z0-9-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    if not value:
        raise ValueError(f"invalid notebook ref: {ref!r}")
    return value[:96]


def pending_kernel_rows(rows: list[dict[str, str]] | None = None) -> list[tuple[str, dict[str, str]]]:
    if rows is None:
        rows = read_kernels()
    known = known_notebook_refs()
    manifest = read_manifest()
    pending: list[tuple[str, dict[str, str]]] = []
    for row in rows:
        ref = row.get("ref", "")
        if not ref:
            continue
        if ref not in known:
            pending.append(("new", row))
            continue
        manifest_last_run = manifest.get(ref, {}).get("lastRunTime")
        if manifest_last_run is not None and manifest_last_run != row.get("lastRunTime", ""):
            pending.append(("updated", row))
    return pending


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
    rows = read_kernels()
    pending = pending_kernel_rows(rows)
    results: list[SyncResult] = []
    for reason, row in pending:
        ref = row["ref"]
        target = EXTERNAL / safe_dirname(ref)
        if dry_run:
            results.append(SyncResult(ref=ref, path=target, status=f"dry_run_{reason}"))
            continue
        result = pull_kernel(ref, target)
        results.append(SyncResult(ref=result.ref, path=result.path, status=reason))
    if not dry_run:
        write_manifest(rows)
    if audit and not dry_run:
        audit_public_notebooks.write_report()
    return results


def result_counts(results: list[SyncResult]) -> tuple[int, int]:
    new_count = sum(1 for result in results if result.status.endswith("new"))
    updated_count = sum(1 for result in results if result.status.endswith("updated"))
    return new_count, updated_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-audit", action="store_true")
    parser.add_argument("--refresh-manifest", action="store_true")
    args = parser.parse_args()

    if args.refresh_manifest:
        path = write_manifest(read_kernels())
        print(f"manifest={path.relative_to(ROOT)}")
        return

    results = sync_public_notebooks(dry_run=args.dry_run, audit=not args.no_audit)
    new_count, updated_count = result_counts(results)
    print(f"pending_public_notebooks={len(results)}")
    print(f"new_public_notebooks={new_count}")
    print(f"updated_public_notebooks={updated_count}")
    for result in results:
        print(f"{result.status} {result.ref} -> {result.path.relative_to(ROOT)}")
    if not args.dry_run and not args.no_audit:
        print("audit_report=reports/public-notebook-audit.md")


if __name__ == "__main__":
    main()
