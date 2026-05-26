#!/usr/bin/env python3

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MEMORY_DIR = ROOT / ".codex-memory"
INDEX_PATH = MEMORY_DIR / "index.json"
ENTRIES_DIR = MEMORY_DIR / "entries"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_markdown(path: Path) -> dict:
    parsed = {
        "title": "",
        "sections": set(),
        "summary": "",
        "stable_notes_count": 0,
        "practical_impact_count": 0,
    }

    lines = path.read_text(encoding="utf-8").splitlines()
    current_section = None
    summary_lines: list[str] = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# ") and not parsed["title"]:
            parsed["title"] = stripped[2:].strip()
            continue

        if stripped.startswith("## "):
            current_section = stripped[3:].strip()
            parsed["sections"].add(current_section)
            continue

        if not current_section:
            continue

        if current_section == "Summary" and stripped:
            summary_lines.append(stripped)
        elif current_section == "Stable Notes" and (
            stripped.startswith("- ") or re.match(r"^\d+\.\s+", stripped)
        ):
            parsed["stable_notes_count"] += 1
        elif current_section == "Practical Impact" and (
            stripped.startswith("- ") or re.match(r"^\d+\.\s+", stripped)
        ):
            parsed["practical_impact_count"] += 1

    parsed["summary"] = " ".join(summary_lines).strip()
    return parsed


def validate_index_entry(entry: dict, ids: set[str], paths: set[str], errors: list[str], warnings: list[str]) -> None:
    required_fields = ["id", "kind", "title", "summary", "path", "priority", "updated_at"]
    for field in required_fields:
        if field not in entry or entry[field] in ("", None):
            errors.append(f"Index entry missing required field '{field}': {entry}")

    entry_id = entry.get("id", "")
    if entry_id:
        if entry_id in ids:
            errors.append(f"Duplicate memory id in index: {entry_id}")
        ids.add(entry_id)

    rel_path = entry.get("path", "")
    if rel_path:
        if rel_path in paths:
            errors.append(f"Duplicate memory path in index: {rel_path}")
        paths.add(rel_path)

        full_path = ROOT / rel_path
        if not full_path.exists():
            errors.append(f"Indexed memory file does not exist: {rel_path}")
        elif ENTRIES_DIR not in full_path.parents:
            warnings.append(f"Indexed memory path is outside .codex-memory/entries: {rel_path}")

    updated_at = entry.get("updated_at", "")
    if updated_at and not DATE_RE.match(str(updated_at)):
        warnings.append(f"Index updated_at is not YYYY-MM-DD for {entry_id}: {updated_at}")

    summary = str(entry.get("summary", "")).strip()
    if len(summary) > 260:
        warnings.append(f"Summary is long for {entry_id} ({len(summary)} chars). Consider compacting it.")

    for field in ("tags", "keywords"):
        values = entry.get(field, [])
        if not isinstance(values, list):
            errors.append(f"Index field '{field}' must be a list for {entry_id}")
            continue

        normalized = [str(item).strip().lower() for item in values if str(item).strip()]
        if len(normalized) != len(set(normalized)):
            warnings.append(f"Index field '{field}' contains duplicates for {entry_id}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Codex memory index and entry files.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero if warnings are found.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    if not INDEX_PATH.exists():
        print(f"ERROR: Missing memory index: {INDEX_PATH}")
        return 1

    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON in {INDEX_PATH}: {exc}")
        return 1

    if not isinstance(data.get("entries"), list):
        print("ERROR: .codex-memory/index.json must contain an 'entries' list.")
        return 1

    index_updated_at = str(data.get("updated_at", "")).strip()
    if index_updated_at and not DATE_RE.match(index_updated_at):
        warnings.append(f"Index updated_at is not YYYY-MM-DD: {index_updated_at}")

    ids: set[str] = set()
    paths: set[str] = set()
    indexed_files: set[Path] = set()

    for entry in data["entries"]:
        validate_index_entry(entry, ids, paths, errors, warnings)

        rel_path = entry.get("path")
        if rel_path:
            indexed_files.add((ROOT / rel_path).resolve())
            full_path = ROOT / rel_path
            if full_path.exists():
                parsed = parse_markdown(full_path)
                if not parsed["title"]:
                    errors.append(f"Memory entry missing H1 title: {rel_path}")

                required_sections = {"Summary", "Stable Notes", "Practical Impact"}
                missing_sections = sorted(required_sections - parsed["sections"])
                if missing_sections:
                    errors.append(
                        f"Memory entry missing required sections {missing_sections}: {rel_path}"
                    )

                if not parsed["summary"]:
                    errors.append(f"Memory entry summary is empty: {rel_path}")

                if parsed["stable_notes_count"] == 0:
                    warnings.append(f"Memory entry has no bullet items in Stable Notes: {rel_path}")

                if parsed["practical_impact_count"] == 0:
                    warnings.append(
                        f"Memory entry has no bullet items in Practical Impact: {rel_path}"
                    )

                index_title = str(entry.get("title", "")).strip()
                if index_title and parsed["title"] and index_title != parsed["title"]:
                    warnings.append(
                        f"Index title differs from entry H1 for {entry.get('id')}: "
                        f"index='{index_title}' entry='{parsed['title']}'"
                    )

    if ENTRIES_DIR.exists():
        for file_path in sorted(ENTRIES_DIR.glob("*.md")):
            if file_path.resolve() not in indexed_files:
                warnings.append(f"Memory entry file is not indexed: {file_path.relative_to(ROOT)}")
    else:
        errors.append(f"Missing entries directory: {ENTRIES_DIR}")

    print("Memory health report")
    print(f"- Index file: {INDEX_PATH.relative_to(ROOT)}")
    print(f"- Indexed entries: {len(data['entries'])}")
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

    if warnings and args.strict:
        return 2

    if not warnings:
        print("")
        print("Memory system looks healthy.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
