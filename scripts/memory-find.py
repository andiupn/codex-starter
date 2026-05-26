#!/usr/bin/env python3

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / ".codex-memory" / "index.json"


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def score_entry(entry: dict, query_tokens: list[str]) -> int:
    haystacks = {
        "title": tokenize(entry.get("title", "")),
        "tags": tokenize(" ".join(entry.get("tags", []))),
        "keywords": tokenize(" ".join(entry.get("keywords", []))),
        "summary": tokenize(entry.get("summary", "")),
        "kind": tokenize(entry.get("kind", "")),
    }

    weights = {
        "title": 6,
        "tags": 5,
        "keywords": 4,
        "summary": 2,
        "kind": 1,
    }

    score = 0
    for token in query_tokens:
        for field, tokens in haystacks.items():
            if token in tokens:
                score += weights[field]

    score += int(entry.get("priority", 0))
    return score


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Find the most relevant Codex memory entries for a given query."
    )
    parser.add_argument("query", nargs="*", help="Query terms used to score memory entries.")
    parser.add_argument(
        "--limit",
        type=int,
        default=3,
        help="Maximum number of results to return. Defaults to 3.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not INDEX_PATH.exists():
        print(f"Index not found: {INDEX_PATH}")
        return 1

    with INDEX_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries", [])
    query = " ".join(args.query).strip()
    query_tokens = tokenize(query)

    if not query_tokens:
        ranked = sorted(entries, key=lambda item: int(item.get("priority", 0)), reverse=True)
    else:
        ranked = sorted(entries, key=lambda item: score_entry(item, query_tokens), reverse=True)
        ranked = [item for item in ranked if score_entry(item, query_tokens) > int(item.get("priority", 0))]

    if not ranked:
        print("No relevant memory entries found.")
        return 0

    print(f"Memory index: {INDEX_PATH}")
    if query:
        print(f"Query: {query}")
    print("")

    limit = max(1, args.limit)
    for idx, entry in enumerate(ranked[:limit], start=1):
        entry_path = entry.get("path", "")
        print(f"{idx}. {entry.get('id', 'unknown')}")
        print(f"   title: {entry.get('title', '')}")
        print(f"   kind: {entry.get('kind', '')}")
        print(f"   priority: {entry.get('priority', 0)}")
        print(f"   path: {entry_path}")
        print(f"   summary: {entry.get('summary', '')}")
        print("")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
