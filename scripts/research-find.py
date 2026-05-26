#!/usr/bin/env python3

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "research" / "index.json"


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def score_entry(entry: dict, query_tokens: list[str]) -> int:
    haystacks = {
        "title": tokenize(entry.get("title", "")),
        "question": tokenize(entry.get("question", "")),
        "tags": tokenize(" ".join(entry.get("tags", []))),
        "keywords": tokenize(" ".join(entry.get("keywords", []))),
        "summary": tokenize(entry.get("summary", "")),
    }

    weights = {
        "title": 6,
        "question": 5,
        "tags": 4,
        "keywords": 4,
        "summary": 2,
    }

    score = 0
    for token in query_tokens:
        for field, tokens in haystacks.items():
            if token in tokens:
                score += weights[field]
    return score


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Find relevant research entries from the local research archive."
    )
    parser.add_argument("query", nargs="*", help="Query terms used to search research.")
    parser.add_argument("--limit", type=int, default=3, help="Maximum number of results to return.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not INDEX_PATH.exists():
        print(f"Research index not found: {INDEX_PATH}")
        return 1

    with INDEX_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries", [])
    query = " ".join(args.query).strip()
    query_tokens = tokenize(query)

    if not query_tokens:
        ranked = sorted(entries, key=lambda item: item.get("updated_at", ""), reverse=True)
    else:
        ranked = sorted(entries, key=lambda item: score_entry(item, query_tokens), reverse=True)
        ranked = [item for item in ranked if score_entry(item, query_tokens) > 0]

    if not ranked:
        print("No relevant research entries found.")
        return 0

    print(f"Research index: {INDEX_PATH}")
    if query:
        print(f"Query: {query}")
    print("")

    for idx, entry in enumerate(ranked[: max(1, args.limit)], start=1):
        print(f"{idx}. {entry.get('id', 'unknown')}")
        print(f"   title: {entry.get('title', '')}")
        print(f"   question: {entry.get('question', '')}")
        print(f"   path: {entry.get('path', '')}")
        print(f"   summary: {entry.get('summary', '')}")
        print("")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
