# Codex Starter 🧠

<div align="center">
  <strong>English</strong> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a>
</div>

<br />

<div align="center">
  <h3><strong>An AI without a memory is just a temporary consultant.</strong></h3>
  <p><strong>A lightweight, highly organized starter template for building agent-guided workspaces with OpenAI/Codex, featuring integrated seed memory and structured research archiving.</strong></p>

  <p>Stop letting AI forget your engineering decisions, code styles, and past errors across chat sessions. Build a workspace that accumulates wisdom.</p>
</div>

> 📦 Free template by **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licensed under [MIT License](LICENSE)  
> ☕ If useful, [buy me a coffee](https://ko-fi.com/andiupn) · 🚀 Need professional monorepos? Try the [PRO version](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 The Problem: The "AI Amnesia"
AI models are extremely capable, but they suffer from complete amnesia across chat sessions. They forget your project's custom gotchas, repeating the same coding errors over and over, wasting your API budget and your valuable time.

---

## ⚡ The Solution: The Wisdom Accumulating Workspace

### 1. 🧠 Built-In Seed Memory System
Equipped with `.codex-memory/` that holds localized knowledge indexes. The AI agent reads, writes, and updates its memory directly during your coding tasks. If it solves a bug once, it stores the solution and never repeats the error.

### 📜 2. Reusable Research Archive
A structured `research/` archiving directory with search utility scripts (`scripts/research-find.py`). Build a repository of verified APIs and structures that agents can query in milliseconds.

### 🛰️ 3. Otonom Health & Maintenance Scripts
Prerequisites checked and verified automatically via `./scripts/project-health.sh --auto`. Keep your workspace rules, memory syntax, and code guidelines 100% compliant.

---

## 📊 LITE vs PRO: The Premium Upgrade

`codex-starter` is designed to be extremely lightweight. For orchestrating professional and agency-scale monorepos:

| LITE (Free) | PRO ($1-5) |
|---|---|
| Standard gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| No Custom Agents | 3 Custom Agents (governance, benchmark, etc.) |
| No Workflow Skills | 5 Premium Skills (curator, extractor, git-sync, etc.) |
| Simple structure | Status-first Monorepo (`active/`, `staging/`, etc.) |
| No DevOps Configuration | Reusable Docker Compose local stack template |

👉 **[Get the PRO Edition on GitHub Sponsors](https://github.com/sponsors/andiupn?frequency=monthly)** · Full details: [COMPARISON.md](COMPARISON.md)

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

## 🔒 Security & Placeholders

- **REPLACE all placeholder values** before publishing or using this repository.
- `.env.example` contains sample environment variables. **Copy it to `.env`** and fill in your email (`andi.upn@gmail.com`) and actual credentials.
- Do NOT commit `.env`, DB dumps, backups, or private customer data to Git.

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
