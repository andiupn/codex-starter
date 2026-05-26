#!/usr/bin/env python3

import argparse
import re
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
SKILLS_DIR = ROOT / ".agents" / "skills"
CUSTOM_AGENTS_DIR = ROOT / ".codex" / "agents"
AGENTS_PATH = ROOT / "AGENTS.md"
README_PATH = ROOT / "README.md"

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "active/README.md",
    "active/web/README.md",
    "active/mobile/README.md",
    "staging/README.md",
    "templates/README.md",
    "templates/web/README.md",
    "templates/mobile/README.md",
    "shared/README.md",
    "artifacts/README.md",
    "archive/README.md",
    "docs/codex-memory-system.md",
    "docs/codex-model-strategy.md",
    "docs/project-folder-system.md",
    "docs/research-system.md",
    "docs/rules-architecture.md",
    "docs/vendor-pattern-translation.md",
    "docs/browser-testing-fallback.md",
    "scripts/project-health.sh",
    "scripts/rules-health.py",
]

REQUIRED_DIRS = [
    "active",
    "active/web",
    "active/mobile",
    "staging",
    "templates",
    "templates/web",
    "templates/mobile",
    "shared",
    "artifacts",
    "archive",
]

ACTIVE_MODELS = {"gpt-5.5", "gpt-5.4-mini", "gpt-5.3-codex"}
ALLOWED_MODEL_IDS = ACTIVE_MODELS | {"gpt-5-codex", "gpt-5.5-2026-04-23"}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MODEL_RE = re.compile(r"\bgpt-[a-z0-9.\-]+\b")
SKILL_PATH_RE = re.compile(r"`(\.agents/skills/[^`]+)`")
AGENT_PATH_RE = re.compile(r"`(\.codex/agents/[^`]+)`")

LEGACY_MARKERS = {
    ".claude/": "Legacy Claude path",
    ".gemini/": "Legacy Gemini path",
    "CLAUDE.md": "Claude workspace file name",
    "GEMINI.md": "Gemini workspace file name",
    "invoke_agent": "Vendor-specific sub-agent invocation name",
    "enter_plan_mode": "Vendor-specific planning tool name",
    "ask_user": "Vendor-specific user prompt tool name",
}


def parse_frontmatter(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return data

    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            break
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def normalize_skill_root(raw_path: str) -> str:
    normalized = raw_path.strip().rstrip("/")
    if normalized.endswith("/SKILL.md"):
        normalized = normalized[: -len("/SKILL.md")]
    return normalized


def extract_repo_skill_paths(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return {normalize_skill_root(match) for match in SKILL_PATH_RE.findall(text)}


def extract_repo_agent_paths(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return {match.strip().rstrip("/") for match in AGENT_PATH_RE.findall(text)}


def resolve_local_link(base_file: Path, target: str) -> Path | None:
    target = target.strip()
    if not target or target.startswith("#"):
        return None
    if target.startswith(("http://", "https://", "mailto:", "file://")):
        return None

    target = target.split("#", 1)[0].split("?", 1)[0].strip()
    if not target:
        return None
    if target.startswith("/"):
        return ROOT / target.lstrip("/")
    return (base_file.parent / target).resolve()


def collect_markdown_files() -> list[Path]:
    files = [AGENTS_PATH, README_PATH]
    if DOCS_DIR.exists():
        files.extend(sorted(DOCS_DIR.glob("**/*.md")))
    return files


def check_required_files(errors: list[str]) -> None:
    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"Missing required rules file: {rel_path}")


def check_required_dirs(errors: list[str]) -> None:
    for rel_path in REQUIRED_DIRS:
        full_path = ROOT / rel_path
        if not full_path.exists() or not full_path.is_dir():
            errors.append(f"Missing required project directory: {rel_path}")


def check_markdown_links(markdown_files: list[Path], errors: list[str]) -> int:
    checked_links = 0
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.findall(text):
            resolved = resolve_local_link(path, match)
            if resolved is None:
                continue
            checked_links += 1
            if not resolved.exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT)}: {match.strip()}")
    return checked_links


def check_skill_inventory(errors: list[str], warnings: list[str]) -> int:
    if not SKILLS_DIR.exists():
        return 0

    actual_skill_roots: set[str] = set()
    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        root = f".agents/skills/{skill_file.parent.name}"
        actual_skill_roots.add(root)

        frontmatter = parse_frontmatter(skill_file)
        skill_name = frontmatter.get("name", "")
        if not skill_name:
            errors.append(f"Skill frontmatter missing name: {skill_file.relative_to(ROOT)}")
        elif skill_name != skill_file.parent.name:
            warnings.append(
                f"Skill frontmatter name differs from directory name: {skill_file.relative_to(ROOT)}"
            )

    documented_in_agents = extract_repo_skill_paths(AGENTS_PATH)
    documented_in_readme = extract_repo_skill_paths(README_PATH)
    documented_roots = documented_in_agents | documented_in_readme

    for documented_root in sorted(documented_roots):
        if not (ROOT / documented_root / "SKILL.md").exists():
            errors.append(f"Documented repo skill does not exist: {documented_root}")

    for missing_root in sorted(actual_skill_roots - documented_in_agents):
        warnings.append(f"Repo skill is not referenced in AGENTS.md: {missing_root}")
    for missing_root in sorted(actual_skill_roots - documented_in_readme):
        warnings.append(f"Repo skill is not referenced in README.md: {missing_root}")

    return len(actual_skill_roots)


def check_custom_agent_inventory(errors: list[str], warnings: list[str]) -> int:
    if not CUSTOM_AGENTS_DIR.exists():
        return 0

    actual_agent_paths: set[str] = set()
    for agent_file in sorted(CUSTOM_AGENTS_DIR.glob("*.toml")):
        rel_path = f".codex/agents/{agent_file.name}"
        actual_agent_paths.add(rel_path)

        try:
            data = tomllib.loads(agent_file.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"Invalid TOML in custom agent file {agent_file.relative_to(ROOT)}: {exc}")
            continue

        for field in ("name", "description", "developer_instructions"):
            if not str(data.get(field, "")).strip():
                errors.append(f"Custom agent missing required field '{field}': {agent_file.relative_to(ROOT)}")

    documented_in_agents = extract_repo_agent_paths(AGENTS_PATH)
    documented_in_readme = extract_repo_agent_paths(README_PATH)
    documented_paths = documented_in_agents | documented_in_readme

    for documented_path in sorted(documented_paths):
        if not (ROOT / documented_path).exists():
            errors.append(f"Documented custom agent does not exist: {documented_path}")

    for missing_path in sorted(actual_agent_paths - documented_in_agents):
        warnings.append(f"Custom agent is not referenced in AGENTS.md: {missing_path}")
    for missing_path in sorted(actual_agent_paths - documented_in_readme):
        warnings.append(f"Custom agent is not referenced in README.md: {missing_path}")

    return len(actual_agent_paths)


def check_model_docs(errors: list[str], warnings: list[str]) -> None:
    for rel_path in ("AGENTS.md", "docs/codex-model-strategy.md"):
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        mentions = set(MODEL_RE.findall(text))
        missing = sorted(ACTIVE_MODELS - mentions)
        if missing:
            errors.append(f"Active model ids missing from {rel_path}: {', '.join(missing)}")
        unknown = sorted(model for model in mentions if model not in ALLOWED_MODEL_IDS)
        if unknown:
            warnings.append(f"Unexpected model ids in {rel_path}: {', '.join(unknown)}")


def check_file_sizes(warnings: list[str]) -> None:
    size_limits = {
        AGENTS_PATH: (240, 18000),
        README_PATH: (120, 9000),
    }
    for path, (line_limit, byte_limit) in size_limits.items():
        lines = path.read_text(encoding="utf-8").splitlines()
        byte_count = path.stat().st_size
        if len(lines) > line_limit or byte_count > byte_limit:
            warnings.append(
                f"Rules doc is getting large: {path.relative_to(ROOT)} ({len(lines)} lines, {byte_count} bytes)"
            )


def check_legacy_vendor_markers(warnings: list[str]) -> None:
    for path in (AGENTS_PATH, README_PATH):
        text = path.read_text(encoding="utf-8")
        for marker, label in LEGACY_MARKERS.items():
            if marker in text:
                warnings.append(
                    f"Potential vendor-specific drift in {path.relative_to(ROOT)}: {label} ({marker})"
                )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate project-level rules, docs, optional repo skills, and optional custom agents."
    )
    parser.add_argument("--strict", action="store_true", help="Return non-zero if warnings are found.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    check_required_files(errors)
    check_required_dirs(errors)
    markdown_files = collect_markdown_files()
    checked_links = check_markdown_links(markdown_files, errors)
    skill_count = check_skill_inventory(errors, warnings)
    custom_agent_count = check_custom_agent_inventory(errors, warnings)
    check_model_docs(errors, warnings)
    check_file_sizes(warnings)
    check_legacy_vendor_markers(warnings)

    print("Rules health report")
    print("- Scope: project rules, docs, optional repo skills, and optional custom agents")
    print(f"- Markdown files checked: {len(markdown_files)}")
    print(f"- Local markdown links checked: {checked_links}")
    print(f"- Repo skills found: {skill_count}")
    print(f"- Custom agents found: {custom_agent_count}")
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
        print("Rules governance looks healthy.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
