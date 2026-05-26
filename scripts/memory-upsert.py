#!/usr/bin/env python3

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MEMORY_DIR = ROOT / ".codex-memory"
INDEX_PATH = MEMORY_DIR / "index.json"
def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def slugify(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "memory-entry"


def split_csv(values: list[str] | None) -> list[str]:
    if not values:
        return []

    parts: list[str] = []
    for value in values:
        for item in value.split(","):
            cleaned = item.strip()
            if cleaned:
                parts.append(cleaned)
    return parts


def unique_keep_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        cleaned = item.strip()
        normalized = cleaned.strip("`").strip().lower()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(cleaned)
    return result


def parse_markdown_entry(path: Path) -> dict:
    parsed = {
        "title": "",
        "summary": "",
        "stable_notes": [],
        "practical_impact": [],
        "references": [],
    }

    if not path.exists():
        return parsed

    lines = path.read_text(encoding="utf-8").splitlines()
    current_section = None
    buckets = {
        "summary": [],
        "stable_notes": [],
        "practical_impact": [],
        "references": [],
    }

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()

        if stripped.startswith("# ") and not parsed["title"]:
            parsed["title"] = stripped[2:].strip()
            continue

        if stripped == "## Summary":
            current_section = "summary"
            continue
        if stripped == "## Stable Notes":
            current_section = "stable_notes"
            continue
        if stripped == "## Practical Impact":
            current_section = "practical_impact"
            continue
        if stripped == "## References":
            current_section = "references"
            continue
        if stripped.startswith("## "):
            current_section = None
            continue

        if current_section is None:
            continue

        if current_section == "summary":
            if stripped:
                buckets["summary"].append(stripped)
            continue

        if stripped.startswith("- "):
            buckets[current_section].append(stripped[2:].strip())
        elif re.match(r"^\d+\.\s+", stripped):
            buckets[current_section].append(re.sub(r"^\d+\.\s+", "", stripped).strip())
        elif stripped:
            buckets[current_section].append(stripped)

    parsed["summary"] = " ".join(buckets["summary"]).strip()
    parsed["stable_notes"] = unique_keep_order(buckets["stable_notes"])
    parsed["practical_impact"] = unique_keep_order(buckets["practical_impact"])
    parsed["references"] = unique_keep_order(buckets["references"])
    return parsed


def load_index() -> dict:
    if not INDEX_PATH.exists():
        return {"version": 1, "updated_at": today(), "entries": []}
    with INDEX_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_index(data: dict) -> None:
    data["updated_at"] = today()
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def render_markdown(title: str, summary: str, stable_notes: list[str], practical_impact: list[str], references: list[str]) -> str:
    lines = [f"# {title}", "", "## Summary", "", summary.strip() or "TBD", ""]

    lines.extend(["## Stable Notes", ""])
    if stable_notes:
        lines.extend([f"- {item}" for item in stable_notes])
    else:
        lines.append("- TBD")
    lines.append("")

    lines.extend(["## Practical Impact", ""])
    if practical_impact:
        lines.extend([f"- {item}" for item in practical_impact])
    else:
        lines.append("- TBD")
    lines.append("")

    if references:
        lines.extend(["## References", ""])
        lines.extend([f"- `{item}`" if not item.startswith("`") else f"- {item}" for item in references])
        lines.append("")

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create or update a Codex memory entry and sync the memory index."
    )
    parser.add_argument("--id", dest="entry_id", help="Stable memory entry id. If omitted, derived from title.")
    parser.add_argument("--title", help="Human-readable title for the memory entry.")
    parser.add_argument("--kind", help="Entry kind, for example preference, environment, project, bug, workflow.")
    parser.add_argument("--summary", help="Compact summary used in the memory entry and index.")
    parser.add_argument("--tags", action="append", help="Comma-separated tags. Can be passed multiple times.")
    parser.add_argument("--keywords", action="append", help="Comma-separated keywords. Can be passed multiple times.")
    parser.add_argument("--stable-note", action="append", help="Bullet to add under Stable Notes. Can be passed multiple times.")
    parser.add_argument("--impact", action="append", help="Bullet to add under Practical Impact. Can be passed multiple times.")
    parser.add_argument("--reference", action="append", help="Reference path or note. Can be passed multiple times.")
    parser.add_argument("--priority", type=int, help="Entry priority used by memory lookup.")
    parser.add_argument("--path", help="Optional custom relative path for the markdown entry.")
    parser.add_argument("--dry-run", action="store_true", help="Show the resulting entry and index metadata without writing files.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.entry_id and not args.title:
        parser.error("either --id or --title is required")

    index_data = load_index()
    entries = index_data.setdefault("entries", [])

    entry_id = args.entry_id or slugify(args.title or "")
    index_entry = next((item for item in entries if item.get("id") == entry_id), None)

    default_path = f".codex-memory/entries/{entry_id}.md"
    entry_rel_path = args.path or (index_entry.get("path") if index_entry else default_path)
    entry_path = ROOT / entry_rel_path

    existing_doc = parse_markdown_entry(entry_path)

    title = (
        args.title
        or (index_entry.get("title") if index_entry else "")
        or existing_doc.get("title")
        or entry_id.replace("-", " ").title()
    )
    summary = (
        args.summary
        or (index_entry.get("summary") if index_entry else "")
        or existing_doc.get("summary")
        or f"Memory entry for {title}."
    ).strip()

    tags = unique_keep_order(
        (index_entry.get("tags", []) if index_entry else []) + split_csv(args.tags)
    )
    keywords = unique_keep_order(
        (index_entry.get("keywords", []) if index_entry else []) + split_csv(args.keywords)
    )
    stable_notes = unique_keep_order(existing_doc.get("stable_notes", []) + (args.stable_note or []))
    practical_impact = unique_keep_order(existing_doc.get("practical_impact", []) + (args.impact or []))
    references = unique_keep_order(existing_doc.get("references", []) + (args.reference or []))

    priority = (
        args.priority
        if args.priority is not None
        else int(index_entry.get("priority", 5)) if index_entry
        else 5
    )

    markdown = render_markdown(title, summary, stable_notes, practical_impact, references)

    updated_index_entry = {
        "id": entry_id,
        "kind": args.kind or (index_entry.get("kind", "note") if index_entry else "note"),
        "title": title,
        "tags": tags,
        "keywords": keywords,
        "summary": summary,
        "path": entry_rel_path,
        "priority": priority,
        "updated_at": today(),
    }

    if args.dry_run:
        print(json.dumps(updated_index_entry, indent=2, ensure_ascii=False))
        print("")
        print(markdown)
        return 0

    entry_path.parent.mkdir(parents=True, exist_ok=True)
    entry_path.write_text(markdown + "\n", encoding="utf-8")

    if index_entry is None:
        entries.append(updated_index_entry)
    else:
        index_entry.update(updated_index_entry)

    entries.sort(key=lambda item: (-int(item.get("priority", 0)), item.get("id", "")))
    write_index(index_data)

    print(f"Updated memory entry: {entry_id}")
    print(f"Entry file: {entry_rel_path}")
    print(f"Index file: {INDEX_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
