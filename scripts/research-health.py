#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "research" / "index.json"
ENTRIES_DIR = ROOT / "research" / "entries"


def parse_report(path: Path) -> dict:
    parsed = {
        "title": "",
        "sections": set(),
    }

    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and not parsed["title"]:
            parsed["title"] = stripped[2:].strip()
        elif stripped.startswith("## "):
            parsed["sections"].add(stripped[3:].strip())
    return parsed


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not INDEX_PATH.exists():
        print(f"ERROR: Missing research index: {INDEX_PATH}")
        return 1

    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON in research index: {exc}")
        return 1

    entries = data.get("entries")
    if not isinstance(entries, list):
        print("ERROR: research/index.json must contain an 'entries' list.")
        return 1

    indexed_reports: set[Path] = set()

    for entry in entries:
        entry_id = entry.get("id", "")
        report_rel = entry.get("path", "")
        sources_rel = entry.get("sources_path", "")

        for field in ("id", "title", "question", "summary", "path", "sources_path", "updated_at", "created_at"):
            if not entry.get(field):
                errors.append(f"Research entry missing required field '{field}': {entry}")

        report_path = ROOT / report_rel
        sources_path = ROOT / sources_rel
        indexed_reports.add(report_path.resolve())

        if not report_path.exists():
            errors.append(f"Missing research report for {entry_id}: {report_rel}")
        else:
            parsed = parse_report(report_path)
            required_sections = {"Research Question", "Summary", "Key Findings", "Reuse Guidance", "Sources"}
            missing_sections = sorted(required_sections - parsed["sections"])
            if missing_sections:
                errors.append(f"Research report missing sections {missing_sections}: {report_rel}")
            if not parsed["title"]:
                errors.append(f"Research report missing title: {report_rel}")

        if not sources_path.exists():
            errors.append(f"Missing research sources for {entry_id}: {sources_rel}")
        else:
            try:
                sources = json.loads(sources_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"Invalid JSON in sources file {sources_rel}: {exc}")
            else:
                if not isinstance(sources, list):
                    errors.append(f"Sources file must contain a list: {sources_rel}")
                elif len(sources) == 0:
                    warnings.append(f"Research entry has no sources yet: {sources_rel}")

    if ENTRIES_DIR.exists():
        for report_path in sorted(ENTRIES_DIR.glob("*/report.md")):
            if report_path.resolve() not in indexed_reports:
                warnings.append(f"Research report is not indexed: {report_path.relative_to(ROOT)}")

    print("Research health report")
    print(f"- Index file: {INDEX_PATH.relative_to(ROOT)}")
    print(f"- Indexed entries: {len(entries)}")
    print(f"- Errors: {len(errors)}")
    print(f"- Warnings: {len(warnings)}")

    if warnings:
        print("")
        print("Warnings:")
        for item in warnings:
            print(f"- {item}")

    if errors:
        print("")
        print("Errors:")
        for item in errors:
            print(f"- {item}")
        return 1

    if not warnings:
        print("")
        print("Research archive looks healthy.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
