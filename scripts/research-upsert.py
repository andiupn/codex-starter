#!/usr/bin/env python3

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = ROOT / "research"
INDEX_PATH = RESEARCH_DIR / "index.json"
ENTRIES_DIR = RESEARCH_DIR / "entries"


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def slugify(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "research-entry"


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


def normalize_source(value: str) -> dict:
    parts = [part.strip() for part in value.split("|")]
    parts += [""] * (3 - len(parts))
    return {
        "title": parts[0],
        "url": parts[1],
        "note": parts[2],
    }


def dedupe_sources(sources: list[dict]) -> list[dict]:
    seen: set[tuple[str, str, str]] = set()
    result: list[dict] = []
    for item in sources:
        normalized = (
            str(item.get("title", "")).strip().lower(),
            str(item.get("url", "")).strip().lower(),
            str(item.get("note", "")).strip().lower(),
        )
        if normalized in seen:
            continue
        seen.add(normalized)
        result.append(
            {
                "title": str(item.get("title", "")).strip(),
                "url": str(item.get("url", "")).strip(),
                "note": str(item.get("note", "")).strip(),
            }
        )
    return result


def load_index() -> dict:
    if not INDEX_PATH.exists():
        return {"version": 1, "updated_at": today(), "entries": []}
    with INDEX_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_index(data: dict) -> None:
    data["updated_at"] = today()
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_sources(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return []


def parse_report(path: Path) -> dict:
    parsed = {
        "title": "",
        "question": "",
        "summary": "",
        "findings": [],
        "reuse_notes": [],
    }

    if not path.exists():
        return parsed

    lines = path.read_text(encoding="utf-8").splitlines()
    current_section = None
    summary_lines: list[str] = []

    for raw_line in lines:
        stripped = raw_line.strip()

        if stripped.startswith("# ") and not parsed["title"]:
            parsed["title"] = stripped[2:].strip()
            continue

        if stripped == "## Research Question":
            current_section = "question"
            continue
        if stripped == "## Summary":
            current_section = "summary"
            continue
        if stripped == "## Key Findings":
            current_section = "findings"
            continue
        if stripped == "## Reuse Guidance":
            current_section = "reuse_notes"
            continue
        if stripped.startswith("## "):
            current_section = None
            continue

        if current_section == "question" and stripped:
            parsed["question"] = stripped
        elif current_section == "summary" and stripped:
            summary_lines.append(stripped)
        elif current_section == "findings" and stripped.startswith("- "):
            parsed["findings"].append(stripped[2:].strip())
        elif current_section == "reuse_notes" and stripped.startswith("- "):
            parsed["reuse_notes"].append(stripped[2:].strip())

    parsed["summary"] = " ".join(summary_lines).strip()
    parsed["findings"] = unique_keep_order(parsed["findings"])
    parsed["reuse_notes"] = unique_keep_order(parsed["reuse_notes"])
    return parsed


def render_report(title: str, question: str, summary: str, findings: list[str], reuse_notes: list[str], sources_rel_path: str) -> str:
    lines = [
        f"# {title}",
        "",
        "## Research Question",
        "",
        question.strip() or "TBD",
        "",
        "## Summary",
        "",
        summary.strip() or "TBD",
        "",
        "## Key Findings",
        "",
    ]

    if findings:
        lines.extend([f"- {item}" for item in findings])
    else:
        lines.append("- TBD")

    lines.extend(
        [
            "",
            "## Reuse Guidance",
            "",
        ]
    )

    if reuse_notes:
        lines.extend([f"- {item}" for item in reuse_notes])
    else:
        lines.append("- TBD")

    lines.extend(
        [
            "",
            "## Sources",
            "",
            f"- `./{Path(sources_rel_path).name}`",
            "",
        ]
    )

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create or update a reusable research entry and sync the research index."
    )
    parser.add_argument("--id", dest="entry_id", help="Stable research id. If omitted, derived from title.")
    parser.add_argument("--title", help="Title for the research entry.")
    parser.add_argument("--question", help="Original research question or request.")
    parser.add_argument("--summary", help="Compact summary of the research result.")
    parser.add_argument("--tag", action="append", help="Comma-separated tags. Can be passed multiple times.")
    parser.add_argument("--keyword", action="append", help="Comma-separated keywords. Can be passed multiple times.")
    parser.add_argument("--finding", action="append", help="Bullet to add under Key Findings.")
    parser.add_argument("--reuse-note", action="append", help="Bullet to add under Reuse Guidance.")
    parser.add_argument(
        "--source",
        action="append",
        help="Source in the form 'title | url | note'. Can be passed multiple times.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show output without writing files.")
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

    entry_dir = ENTRIES_DIR / entry_id
    report_path = entry_dir / "report.md"
    sources_path = entry_dir / "sources.json"

    existing_report = parse_report(report_path)
    existing_sources = load_sources(sources_path)

    title = (
        args.title
        or (index_entry.get("title") if index_entry else "")
        or existing_report.get("title")
        or entry_id.replace("-", " ").title()
    )
    question = (
        args.question
        or (index_entry.get("question") if index_entry else "")
        or existing_report.get("question")
        or "TBD"
    )
    summary = (
        args.summary
        or (index_entry.get("summary") if index_entry else "")
        or existing_report.get("summary")
        or f"Research archive entry for {title}."
    )

    tags = unique_keep_order((index_entry.get("tags", []) if index_entry else []) + split_csv(args.tag))
    keywords = unique_keep_order((index_entry.get("keywords", []) if index_entry else []) + split_csv(args.keyword))
    findings = unique_keep_order(existing_report.get("findings", []) + (args.finding or []))
    reuse_notes = unique_keep_order(existing_report.get("reuse_notes", []) + (args.reuse_note or []))

    new_sources = [normalize_source(item) for item in (args.source or [])]
    sources = dedupe_sources(existing_sources + new_sources)

    report_rel_path = str(report_path.relative_to(ROOT))
    sources_rel_path = str(sources_path.relative_to(ROOT))

    report_text = render_report(title, question, summary, findings, reuse_notes, sources_rel_path)
    updated_index_entry = {
        "id": entry_id,
        "title": title,
        "question": question,
        "tags": tags,
        "keywords": keywords,
        "summary": summary,
        "path": report_rel_path,
        "sources_path": sources_rel_path,
        "updated_at": today(),
        "created_at": index_entry.get("created_at", today()) if index_entry else today(),
    }

    if args.dry_run:
        print(json.dumps(updated_index_entry, indent=2, ensure_ascii=False))
        print("")
        print(report_text)
        print("")
        print(json.dumps(sources, indent=2, ensure_ascii=False))
        return 0

    entry_dir.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_text + "\n", encoding="utf-8")
    sources_path.write_text(json.dumps(sources, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if index_entry is None:
        entries.append(updated_index_entry)
    else:
        index_entry.update(updated_index_entry)

    entries.sort(key=lambda item: item.get("updated_at", ""), reverse=True)
    write_index(index_data)

    print(f"Updated research entry: {entry_id}")
    print(f"Report: {report_rel_path}")
    print(f"Sources: {sources_rel_path}")
    print(f"Index: {INDEX_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
