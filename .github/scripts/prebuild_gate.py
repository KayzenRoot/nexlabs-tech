#!/usr/bin/env python3
"""Read-only prebuild checks for changed documentation and repository paths."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{50,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
)
INLINE_LINK = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+[^)]*)?\)")
HUNK = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def git(*args: str, check: bool = True) -> bytes:
    result = subprocess.run(["git", *args], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip() or "git command failed")
    return result.stdout


def changed_files() -> list[str]:
    event = os.environ.get("EVENT_NAME", "")
    base = os.environ.get("BASE_SHA", "")
    head = os.environ.get("HEAD_SHA", "")
    if not head:
        raise RuntimeError("HEAD_SHA is required")

    if event == "pull_request":
        if not base:
            raise RuntimeError("BASE_SHA is required for pull_request")
        output = git("diff", "--name-only", "--diff-filter=ACMRT", "-z", f"{base}...{head}")
    elif event == "push":
        if not base or set(base) == {"0"}:
            output = git("diff-tree", "--root", "-r", "--no-commit-id", "--name-only", "-z", head)
        else:
            output = git("diff", "--name-only", "--diff-filter=ACMRT", "-z", base, head)
    else:
        raise RuntimeError(f"Unsupported event: {event or '(missing)'}")
    return [name.decode("utf-8", "surrogateescape") for name in output.split(b"\0") if name]


def check_path_collisions() -> list[str]:
    paths = git("ls-tree", "-r", "--name-only", "-z", "HEAD").split(b"\0")
    seen: dict[str, str] = {}
    collisions: list[str] = []
    for raw_path in paths:
        if not raw_path:
            continue
        path = raw_path.decode("utf-8", "surrogateescape")
        key = path.casefold()
        if key in seen and seen[key] != path:
            collisions.append(f"{seen[key]} | {path}")
        else:
            seen[key] = path
    return collisions


def check_added_lines() -> list[str]:
    event = os.environ["EVENT_NAME"]
    base = os.environ.get("BASE_SHA", "")
    head = os.environ["HEAD_SHA"]
    if event == "pull_request":
        revision = f"{base}...{head}"
        args = ["diff", "--no-ext-diff", "--unified=0", revision, "--"]
    elif base and set(base) != {"0"}:
        args = ["diff", "--no-ext-diff", "--unified=0", base, head, "--"]
    else:
        args = ["diff", "--no-ext-diff", "--unified=0", "--root", head, "--"]
    diff = git(*args).decode("utf-8", "replace").splitlines()
    findings: list[str] = []
    current_file = "(unknown)"
    line_number = 0
    for line in diff:
        if line.startswith("+++ b/"):
            current_file = line[6:]
        elif line.startswith("+++ "):
            current_file = "(unknown)"
        elif line.startswith("@@"):
            match = HUNK.match(line)
            if match:
                line_number = int(match.group(1))
        elif line.startswith("+") and not line.startswith("+++"):
            added = line[1:]
            if any(pattern.search(added) for pattern in SECRET_PATTERNS):
                findings.append(f"Potential credential pattern at {current_file}:{line_number}")
            line_number += 1
        elif line.startswith(" "):
            line_number += 1
    return findings


def check_markdown_links(files: list[str]) -> list[str]:
    errors: list[str] = []
    for name in files:
        if Path(name).suffix.casefold() not in {".md", ".markdown"}:
            continue
        source = Path(name)
        if not source.is_file():
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for match in INLINE_LINK.finditer(line):
                raw_target = match.group(1).strip("<>")
                target = urlsplit(raw_target)
                if target.scheme or target.netloc or not target.path:
                    continue
                decoded_path = unquote(target.path)
                candidate = Path(decoded_path.lstrip("/")) if decoded_path.startswith("/") else source.parent / decoded_path
                if not candidate.exists():
                    errors.append(f"Broken relative link at {name}:{line_number}")
    return errors


def run_checks() -> int:
    files = changed_files()
    collisions = check_path_collisions()
    secret_findings = check_added_lines()
    link_errors = check_markdown_links(files)
    problems = [*(f"Case-insensitive path collision: {item}" for item in collisions), *secret_findings, *link_errors]
    if problems:
        print("Prebuild checks failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print(f"Prebuild checks passed ({len(files)} changed path(s); no credential patterns, relative-link errors, or case-fold collisions).")
    return 0


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2 or sys.argv[1] != "check":
            raise RuntimeError("Usage: prebuild_gate.py check")
        raise SystemExit(run_checks())
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Prebuild check error: {error}", file=sys.stderr)
        raise SystemExit(1)
