# AGENTS.md
<!--
  Scaffolded by Andi UPN (https://github.com/andiupn)
  Official Website & Support: https://kuncimu.com
  Licensed under MIT License
-->

> 📦 Free Template by **Andi UPN** ([kuncimu.com](https://kuncimu.com)) · Licensed under [MIT License](LICENSE)

## Project Purpose

- This repository is a lightweight starter for Codex/OpenAI agent workflows.
- It provides reusable governance, memory, research, and folder conventions without shipping private app data or runtime state.
- Keep the repo intentionally small. Add structure only when a real app, template, or experiment needs it.

## Default Working Mode

- Inspect the workspace first.
- Before substantial work, run `./scripts/project-health.sh --auto`.
- On Windows PowerShell, use Git Bash if `bash ./scripts/project-health.sh --auto` is unavailable.
- On Linux, prefer a native filesystem under `$HOME` such as ext4 or btrfs.
- If maintenance is overdue, let `project-health` complete before continuing.
- Prefer small, reversible changes.
- Before any git workflow, check whether `.git` exists and report if source control is unavailable.

## Experiment Rules

- Keep experiments isolated under `experiments/`.
- Use names such as `experiments/<yyyymmdd>-<short-name>/`.
- For non-trivial experiments, keep the objective, how to run, expected result, and observed result close to the code.
- Change one major variable at a time when comparing prompts, models, or tools.

## App / Project Folder System

- Use `active/` for living projects.
- Use `active/web/` for web apps and `active/mobile/` for mobile apps.
- Use `staging/` for incoming material that is not normalized yet.
- Use `templates/` for reusable starters.
- Use `shared/` for small cross-project helpers or assets.
- Use `artifacts/` for generated output.
- Use `archive/<year>/` for retired projects.
- Keep `experiments/` for agent, prompt, and benchmark work.
- Keep `devops/` for infrastructure helpers if the repo later grows into that need.

## OpenAI / Codex Defaults

- Prefer the OpenAI Responses API for new agent work.
- Model routing for this template:
  - `gpt-5.5` for most coding, architecture, review, and final synthesis.
  - `gpt-5.4-mini` for maintenance, scripted workflows, and cost-sensitive loops.
  - `gpt-5.3-codex` for benchmark or implementation work that explicitly evaluates Codex-tuned coding behavior.
- Use official model IDs exactly.
- Use floating aliases for day-to-day work and snapshots for benchmarks or reproducibility-sensitive runs.
- Start with `low` or `medium` reasoning for maintenance, `medium` for most implementation, and `high` only when justified.
- For OpenAI platform questions, prefer official OpenAI docs.
- If browser tooling is unavailable, use the fallback pattern in `docs/browser-testing-fallback.md`.

## Sub-Agent Usage

- Use sub-agents only when the user explicitly asks for delegation or parallel agent work.
- Keep the main agent on requirements, critical-path implementation, verification, and final synthesis.
- Delegate only bounded tasks with clear ownership and expected verification.
- Prefer read-heavy delegation before parallel write-heavy work.

## Project Memory System

- Use `.codex-memory/index.json` as the first-stop memory index.
- Use `.codex-memory/maintenance-log.json` as the maintenance cadence source of truth.
- Load only the few entries relevant to the current task.
- Use `scripts/memory-find.py`, `scripts/memory-upsert.py`, and `scripts/memory-health.py`.
- Store durable context only: preferences, decisions, environment constraints, recurring fixes, and verification patterns.
- Do not store secrets, raw logs, or full transcripts.

## Research Archive System

- Use `research/` for reusable source-backed findings.
- Search existing research first with `./scripts/research-find.py <query>`.
- Save reusable results with `scripts/research-upsert.py`.
- Keep evidence-heavy material in research and promote only compact durable takeaways into `.codex-memory/`.

## Project Skills And Agents

- This starter does not bundle repo-specific skills or custom agents.
- Add them later only when a workflow is clearly recurring and worth maintaining.
- Prefer simple scripts first, then add skills or custom agents only when the leverage is clear.

## Project Rules Governance

- `AGENTS.md` is the source of truth for project-wide agent behavior.
- Supporting rules docs live in `docs/`.
- Update the smallest correct source of truth instead of repeating the same rule in many files.
- Translate external vendor patterns into Codex-native workflows.
- Verify rule changes with `python3 scripts/rules-health.py` and `./scripts/project-health.sh --auto`.

## Coding Rules

- Prefer simple scripts and minimal dependencies.
- Check the standard library and existing repo tools before adding new dependencies.
- Ask before adding paid services, databases, or background infrastructure.
- Use `.env.example`, dummy data, and local fixtures.
- Do not add hidden automation or auto-start behavior unless explicitly requested.

## Verification

- Run the smallest meaningful verification after changes.
- Prefer deterministic checks that another agent can rerun.
- If full verification is not possible, state exactly what was verified and what remains unverified.

## Documentation

- Every runnable experiment should include the exact command used to run it.
- Update the nearest README or note when behavior changes.
- Keep documentation concise and continuation-friendly.

## Communication

- Be concise, direct, and explicit about assumptions and risks.
- Reply in Indonesian when the user writes in Indonesian unless asked otherwise.
- Final summaries should state what changed, how it was verified, and the next best step if there is one.
