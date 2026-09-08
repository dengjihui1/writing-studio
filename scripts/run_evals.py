#!/usr/bin/env python3
"""Validate Writing Studio eval fixtures and optionally run cold-start traces."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Iterable


SKILL_ROOT = Path(__file__).resolve().parent.parent
CASES_PATH = SKILL_ROOT / "evals" / "core-cases.jsonl"
SCHEMA_PATHS = (
    SKILL_ROOT / "evals" / "rubric.schema.json",
    SKILL_ROOT / "evals" / "pairwise.schema.json",
)
RUNTIME_PARTS = ("SKILL.md", "agents", "references", "scripts", "evals", "docs")
ZERO_WIDTH = re.compile(r"[\u200b\u200c\u200d\u2060\ufeff]")
PRIVATE_PATTERNS = (
    re.compile(r"[A-Za-z]:[\\/](?:Users|CodexWork)[\\/]", re.IGNORECASE),
    re.compile(r"wxid_[A-Za-z0-9_]+", re.IGNORECASE),
    re.compile(r"codex://threads/", re.IGNORECASE),
)


class EvalError(RuntimeError):
    pass


def read_cases(path: Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            case = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise EvalError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
        if not isinstance(case, dict):
            raise EvalError(f"{path}:{line_number}: each line must be an object")
        case["_line"] = line_number
        cases.append(case)
    return cases


def validate_cases(cases: list[dict[str, Any]]) -> dict[str, Any]:
    errors: list[str] = []
    ids: set[str] = set()
    required = {"id", "split", "trigger", "language", "genre", "intent", "prompt", "expected", "protected_literals", "rationale"}
    allowed_splits = {"dev", "holdout"}
    allowed_triggers = {"explicit", "implicit", "contextual", "negative"}
    allowed_routes = {"writing-studio", "specialist", "direct"}
    allowed_modes = {"A", "B", "none"}
    coverage = {"splits": set(), "triggers": set(), "routes": set(), "modes": set(), "languages": set(), "intents": set()}

    for case in cases:
        label = f"line {case.get('_line', '?')}"
        missing = sorted(required - case.keys())
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(missing)}")
            continue
        case_id = case["id"]
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9-]+", case_id):
            errors.append(f"{label}: id must use lowercase letters, digits, and hyphens")
        elif case_id in ids:
            errors.append(f"{label}: duplicate id {case_id}")
        ids.add(case_id)
        if case["split"] not in allowed_splits:
            errors.append(f"{case_id}: invalid split {case['split']!r}")
        if case["trigger"] not in allowed_triggers:
            errors.append(f"{case_id}: invalid trigger {case['trigger']!r}")
        expected = case["expected"]
        if not isinstance(expected, dict):
            errors.append(f"{case_id}: expected must be an object")
            continue
        for key in ("route", "mode", "action", "must", "must_not"):
            if key not in expected:
                errors.append(f"{case_id}: expected.{key} is required")
        if expected.get("route") not in allowed_routes:
            errors.append(f"{case_id}: invalid route {expected.get('route')!r}")
        if expected.get("mode") not in allowed_modes:
            errors.append(f"{case_id}: invalid mode {expected.get('mode')!r}")
        if not isinstance(expected.get("must"), list) or not isinstance(expected.get("must_not"), list):
            errors.append(f"{case_id}: expected.must and expected.must_not must be arrays")
        if not isinstance(case["protected_literals"], list) or not all(isinstance(value, str) and value for value in case["protected_literals"]):
            errors.append(f"{case_id}: protected_literals must contain non-empty strings")
        serialized = json.dumps(case, ensure_ascii=False)
        for pattern in PRIVATE_PATTERNS:
            if pattern.search(serialized):
                errors.append(f"{case_id}: fixture contains a private path or identifier")
        coverage["splits"].add(case["split"])
        coverage["triggers"].add(case["trigger"])
        coverage["routes"].add(expected.get("route"))
        coverage["modes"].add(expected.get("mode"))
        coverage["languages"].add(case["language"])
        coverage["intents"].add(case["intent"])

    requirements = {
        "splits": allowed_splits,
        "triggers": allowed_triggers,
        "routes": allowed_routes,
        "modes": allowed_modes,
    }
    for dimension, required_values in requirements.items():
        missing_values = sorted(required_values - coverage[dimension])
        if missing_values:
            errors.append(f"coverage.{dimension}: missing {', '.join(missing_values)}")
    if len(cases) < 10:
        errors.append("core suite must contain at least 10 cases")
    if sum(case.get("split") == "holdout" for case in cases) < 4:
        errors.append("core suite must contain at least four holdout cases")
    if errors:
        raise EvalError("\n".join(errors))
    return {key: sorted(value) for key, value in coverage.items()}


def validate_schemas() -> list[str]:
    titles: list[str] = []
    for path in SCHEMA_PATHS:
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise EvalError(f"cannot read schema {path}: {exc}") from exc
        if schema.get("type") != "object" or not schema.get("required") or not schema.get("properties"):
            raise EvalError(f"{path}: expected an object schema with required and properties")
        titles.append(schema.get("title", path.name))
    return titles


def iter_runtime_files(root: Path) -> Iterable[Path]:
    for part in RUNTIME_PARTS:
        path = root / part
        if path.is_file():
            yield path
        elif path.is_dir():
            for child in sorted(path.rglob("*")):
                if child.is_file() and "__pycache__" not in child.parts and child.suffix not in {".pyc", ".log", ".tmp"}:
                    yield child


def runtime_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in iter_runtime_files(root):
        relative = path.relative_to(root).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def installed_skill_path() -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    return codex_home / "skills" / "writing-studio"


def recursive_text(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(recursive_text(item) for item in value.values())
    if isinstance(value, list):
        return " ".join(recursive_text(item) for item in value)
    return str(value)


def extract_trace_metrics(events: list[dict[str, Any]]) -> tuple[str, int, dict[str, int], bool]:
    final_chunks: list[str] = []
    command_ids: set[str] = set()
    token_usage: dict[str, int] = {}
    trace_text = recursive_text(events).replace("\\", "/").lower()
    trace_text = re.sub(r"/+", "/", trace_text)
    for event in events:
        item = event.get("item") if isinstance(event, dict) else None
        if isinstance(item, dict):
            item_type = str(item.get("type", ""))
            if item_type in {"command_execution", "command", "tool_call"}:
                command_ids.add(str(item.get("id", f"anonymous-{len(command_ids)}")))
            if item_type in {"agent_message", "message"} and isinstance(item.get("text"), str):
                final_chunks.append(item["text"])
        usage = event.get("usage") if isinstance(event, dict) else None
        if isinstance(usage, dict):
            for key, value in usage.items():
                if isinstance(value, int):
                    token_usage[key] = max(token_usage.get(key, 0), value)
    # Explicitly invoked skills may have SKILL.md injected into context and then
    # read only routed references. Accept either the entrypoint or any file read
    # under the installed skill root as observable invocation evidence.
    skill_observed = (
        "writing-studio/skill.md" in trace_text
        or ".codex/skills/writing-studio/" in trace_text
    )
    return "\n".join(final_chunks).strip(), len(command_ids), token_usage, skill_observed


def run_live_case(case: dict[str, Any], timeout: int) -> dict[str, Any]:
    command = ["codex", "exec", "--ephemeral", "--json", "--sandbox", "read-only", case["prompt"]]
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, check=False)
    events: list[dict[str, Any]] = []
    parse_errors = 0
    for raw in completed.stdout.splitlines():
        try:
            event = json.loads(raw)
        except json.JSONDecodeError:
            parse_errors += 1
            continue
        if isinstance(event, dict):
            events.append(event)
    final_text, command_count, token_usage, skill_observed = extract_trace_metrics(events)
    expected_route = case["expected"]["route"]
    route_pass = skill_observed if expected_route == "writing-studio" else not skill_observed
    missing_literals = [literal for literal in case["protected_literals"] if literal not in final_text]
    checks = {
        "process_exit_zero": completed.returncode == 0,
        "json_trace_readable": bool(events) and parse_errors == 0,
        "route_observed": route_pass,
        "no_zero_width_characters": ZERO_WIDTH.search(final_text) is None,
        "protected_literals_preserved": not missing_literals,
    }
    return {
        "id": case["id"],
        "checks": checks,
        "pass": all(checks.values()),
        "observed": {
            "skill_read": skill_observed,
            "command_count": command_count,
            "token_usage": token_usage,
            "final_characters": len(final_text),
            "missing_protected_literals": missing_literals,
            "parse_errors": parse_errors,
        },
        "stderr_tail": completed.stderr[-1200:] if completed.returncode else "",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", action="store_true", help="run deterministic fixture and schema validation (default)")
    parser.add_argument("--live", action="store_true", help="run selected cases through cold-start codex exec traces")
    parser.add_argument("--ids", help="comma-separated case IDs for --live")
    parser.add_argument("--split", choices=("dev", "holdout"), help="filter cases by split")
    parser.add_argument("--all-live", action="store_true", help="explicitly allow all selected cases to run live")
    parser.add_argument("--allow-skill-mismatch", action="store_true", help="run even if candidate and installed runtime hashes differ")
    parser.add_argument("--timeout", type=int, default=180, help="timeout in seconds for each live case")
    parser.add_argument("--output", type=Path, help="optional JSON summary path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        cases = read_cases(CASES_PATH)
        coverage = validate_cases(cases)
        schemas = validate_schemas()
        summary: dict[str, Any] = {
            "validation": "pass",
            "case_count": len(cases),
            "coverage": coverage,
            "schemas": schemas,
        }
        if args.live:
            requested = {value.strip() for value in (args.ids or "").split(",") if value.strip()}
            selected = [case for case in cases if (not requested or case["id"] in requested) and (not args.split or case["split"] == args.split)]
            unknown = sorted(requested - {case["id"] for case in cases})
            if unknown:
                raise EvalError(f"unknown case IDs: {', '.join(unknown)}")
            if not selected:
                raise EvalError("no cases selected")
            if not requested and not args.all_live:
                raise EvalError("--live requires --ids or explicit --all-live")
            installed = installed_skill_path()
            if not installed.is_dir():
                raise EvalError(f"installed skill not found: {installed}")
            candidate_hash = runtime_hash(SKILL_ROOT)
            installed_hash = runtime_hash(installed)
            if candidate_hash != installed_hash and not args.allow_skill_mismatch:
                raise EvalError("candidate and installed skill hashes differ; install the candidate before live evaluation")
            summary["runtime_hash"] = candidate_hash
            summary["live"] = [run_live_case(case, args.timeout) for case in selected]
            summary["live_pass"] = all(result["pass"] for result in summary["live"])
        rendered = json.dumps(summary, ensure_ascii=False, indent=2)
        print(rendered)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered + "\n", encoding="utf-8")
        return 0 if summary.get("live_pass", True) else 1
    except (EvalError, OSError, subprocess.SubprocessError) as exc:
        print(f"evaluation failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
