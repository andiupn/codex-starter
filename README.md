# Codex Starter 🧠

<div align="center">
  <strong>English</strong> | <a href="README.id.md">Bahasa Indonesia</a>
</div>

<br />

**A lightweight, organized starter template for building agent-guided workspaces with OpenAI/Codex.**

> 📦 Free template by **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licensed under [MIT License](LICENSE)  
> ☕ If useful, [buy me a coffee](https://ko-fi.com/andiupn) · 🚀 Need more features? Try the [PRO version](https://kuncimu.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 🎯 Purpose

- Provide a fast-to-deploy starter workspace for new OpenAI/Codex projects.
- Keep agent workflows highly structured without leaking private data from source repositories.
- Offer seed memory, research, and governance rules that can be expanded easily over time.
- Highly suitable for open-source distributions and donation-based monetization models.

---

## 📦 What's Inside

- `AGENTS.md` as the master source of truth for agent behavior and directives.
- `docs/` detailing architectural rules, memory guidelines, research, folder systems, model strategies, browser fallback, and workspace setup.
- `scripts/` containing health checks, maintenance logs, memory tooling, and research search utilities.
- `.codex-memory/` equipped with a local index and generic seed memory entries.
- `research/` as an empty research archive ready to be populated.
- Lifecycle folders: `active/`, `staging/`, `templates/`, `shared/`, `artifacts/`, `archive/`, and `experiments/`.
- Distribution documents: `LICENSE`, `CONTRIBUTING.md`, `DONATE.md`, and `.github/FUNDING.yml`.

---

## ❌ What is Intentionally Excluded

- Active application code or runtime data from source repositories.
- Complex premium repository skills and custom specialized agents.
- Local database dumps, backups, sensitive assets, or credentials.
- Old benchmark outputs and highly project-specific research reports.

---

## 🚀 Quick Start

```bash
# Run local repository and environment health checks
./scripts/project-health.sh --auto

# Validate rules and configuration syntax
python3 scripts/rules-health.py
python3 scripts/memory-health.py
python3 scripts/research-health.py

# Search inside local memory and research index
./scripts/memory-find.py workflow
./scripts/research-find.py model
```

---

## 📊 LITE vs PRO Comparison

`codex-starter` is designed to be extremely lightweight. For orchestrating professional and agency-scale monorepos:

| LITE (Free) | PRO ($1-5) |
|---|---|
| Standard gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| No Custom Agents | 3 Custom Agents (governance, benchmark, etc.) |
| No Workflow Skills | 5 Premium Skills (curator, extractor, git-sync, etc.) |
| Simple structure | Status-first Monorepo (`active/`, `staging/`, etc.) |
| No DevOps Configuration | Reusable Docker Compose local stack template |

👉 **[Get the PRO Edition at kuncimu.com](https://kuncimu.com)** · Full details: [COMPARISON.md](COMPARISON.md)

---

## 🔒 Security & Placeholders

- **REPLACE all placeholder values** before publishing or using this repository.
- `.env.example` contains sample environment variables. **Copy it to `.env`** and fill in your email (`andi.upn@gmail.com`) and actual credentials.
- Do NOT commit `.env`, DB dumps, backups, or private customer data to Git.
- Always use mock data and local fixtures for offline development.
- Detailed model guidelines and rules are documented in [AGENTS.md](AGENTS.md) and [docs/codex-model-strategy.md](docs/codex-model-strategy.md).

---

## 💖 Support This Project (Donations)

This starter template is free and open-source. Consider donating to support its maintenance:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 License & Distribution

- **License:** MIT License (see [LICENSE](LICENSE) - Copyright Andi UPN)
- **Contributing Guide:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Donation Guide:** [DONATE.md](DONATE.md)
