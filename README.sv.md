# Codex Starter 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <strong>Svenska</strong> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>En AI utan minne är bara en tillfällig konsult.</strong></h3>
  <p><strong>En lätt, välorganiserad startmall för att bygga agentstyrda arbetsytor med OpenAI/Codex, med integrerat fröminne och strukturerad forskningsarkivering.</strong></p>

  <p>Sluta låta AI glömma dina tekniska beslut, kodstilar och tidigare fel i chattsessioner. Bygg en arbetsyta som ackumulerar visdom.</p>
</div>

> 📦 Gratis mall av **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licensierad under [MIT License](LICENSE)  
> ☕ Om det är användbart, [köp mig en kaffe](https://ko-fi.com/andiupn) · 🚀 Behöver du professionella monorepos? Prova [PRO-versionen](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Problemet: "AI Amnesia"
AI-modeller är extremt kapabla, men de lider av fullständig minnesförlust över chattsessioner. De glömmer ditt projekts anpassade gotchas, upprepar samma kodningsfel om och om igen, slösar bort din API-budget och din värdefulla tid.

---

## ⚡ Lösningen: The Wisdom Accumulating Workspace

### 1. 🧠 Inbyggt fröminnessystem
Utrustad med `.codex-memory/` som innehåller lokaliserade kunskapsindex. AI-agenten läser, skriver och uppdaterar sitt minne direkt under dina kodningsuppgifter. Om den löser en bugg en gång lagrar den lösningen och upprepar aldrig felet.

### 📜 2. Återanvändbart forskningsarkiv
En strukturerad `research/` arkiveringskatalog med sökverktygsskript (`scripts/research-find.py`). Bygg ett arkiv med verifierade API:er och strukturer som agenter kan fråga efter på millisekunder.

### 🛰️ 3. Otonom Health & Maintenance Scripts
Förutsättningar kontrolleras och verifieras automatiskt via `./scripts/project-health.sh --auto`. Håll dina arbetsytaregler, minnessyntax och kodriktlinjer 100 % kompatibla.

---

## 📊 LITE vs PRO: Premium-uppgraderingen

`codex-starter` är designad för att vara extremt lätt. För orkestrering av professionella monorepos och byråskala:

| LITE (gratis) | PRO ($1-5) |
|---|---|
| Standard gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| Inga anpassade agenter | 3 Custom Agents (styrning, benchmark, etc.) |
| Inga arbetsflödesfärdigheter | 5 premiumfärdigheter (kurator, extraherare, git-sync, etc.) |
| Enkel struktur | Status-first Monorepo (`active/`, `staging/`, etc.) |
| Ingen DevOps-konfiguration | Återanvändbar Docker Compose lokal stackmall |

👉 **[Hämta PRO-versionen på GitHub-sponsorer](https://github.com/sponsors/andiupn?frequency=monthly)** · Fullständig information: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Snabbstart

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

## 🔒 Säkerhet och platshållare

- **BYT UT alla platshållarvärden** innan du publicerar eller använder det här arkivet.
- `.env.example` innehåller exempel på miljövariabler. **Kopiera den till `.env`** och fyll i din e-post (`andi.upn@gmail.com`) och faktiska referenser.
- Begå INTE `.env`, DB-dumpar, säkerhetskopior eller privat kunddata till Git.

---

## 💖 Stöd detta projekt (donationer)

Denna startmallen är gratis och öppen källkod. Överväg att donera för att stödja dess underhåll:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licens och distribution

- **Licens:** MIT-licens (se [LICENS](LICENSE) - Copyright Andi UPN)
- **Bidragsguide:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Donationsguide:** [DONATE.md](DONATE.md)