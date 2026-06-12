#Codexstarter🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <strong>Nederlands</strong> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>Een AI zonder geheugen is slechts een tijdelijke adviseur.</strong></h3>
  <p><strong>Een lichtgewicht, goed georganiseerde startersjabloon voor het bouwen van door agenten geleide werkruimten met OpenAI/Codex, met geïntegreerd startgeheugen en gestructureerde onderzoeksarchivering.</strong></p>

  <p>Laat AI uw technische beslissingen, codestijlen en fouten uit het verleden tijdens chatsessies niet langer vergeten. Bouw een werkruimte waarin wijsheid wordt verzameld.</p>
</div>

> 📦 Gratis sjabloon van **andiupn** ([kuncimu.com](https://kuncimu.com)) · Gelicentieerd onder [MIT-licentie](LICENSE)  
> ☕ Indien nuttig, [koop een koffie voor me](https://ko-fi.com/andiupn) · 🚀 Professionele monorepo's nodig? Probeer de [PRO-versie](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Het probleem: de "AI-geheugenverlies"
AI-modellen zijn buitengewoon capabel, maar lijden tijdens chatsessies aan volledig geheugenverlies. Ze vergeten de aangepaste valkuilen van uw project, herhalen dezelfde codeerfouten keer op keer, waardoor uw API-budget en uw kostbare tijd worden verspild.

---

## ⚡ De oplossing: de wijsheid accumulerende werkruimte

### 1. 🧠 Ingebouwd zaadgeheugensysteem
Uitgerust met `.codex-memory/` met gelokaliseerde kennisindexen. De AI-agent leest, schrijft en werkt zijn geheugen rechtstreeks bij tijdens uw codeertaken. Als het een bug één keer oplost, slaat het de oplossing op en herhaalt de fout nooit meer.

### 📜 2. Herbruikbaar onderzoeksarchief
Een gestructureerde `research/` archiveringsmap met scripts voor zoekhulpprogramma's (`scripts/research-find.py`). Bouw een opslagplaats van geverifieerde API's en structuren die agenten in milliseconden kunnen opvragen.

### 🛰️ 3. Otonom Gezondheids- en onderhoudsscripts
Vereisten worden automatisch gecontroleerd en geverifieerd via `./scripts/project-health.sh --auto`. Houd uw werkruimteregels, geheugensyntaxis en coderichtlijnen 100% compatibel.

---

## 📊 LITE versus PRO: de premium-upgrade

`codex-starter` is ontworpen om extreem licht te zijn. Voor het orkestreren van monorepos op professionele en bureauschaal:

| LITE (gratis) | PRO ($1-5) |
|---|---|
| Standaard gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| Geen aangepaste agenten | 3 Douaneagenten (governance, benchmark, etc.) |
| Geen workflowvaardigheden | 5 premiumvaardigheden (curator, extractor, git-sync, enz.) |
| Eenvoudige structuur | Status-eerste Monorepo (`active/`, `staging/`, enz.) |
| Geen DevOps-configuratie | Herbruikbare Docker Componeer lokale stapelsjabloon |

👉 **[Krijg de PRO-editie op GitHub-sponsors](https://github.com/sponsors/andiupn?frequency=monthly)** · Volledige details: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Snelle start

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

## 🔒 Beveiliging en tijdelijke aanduidingen

- **VERVANG alle placeholder-waarden** voordat u deze repository publiceert of gebruikt.
- `.env.example` bevat voorbeeldomgevingsvariabelen. **Kopieer het naar `.env`** en vul uw e-mailadres (`andi.upn@gmail.com`) en daadwerkelijke inloggegevens in.
- Leg GEEN `.env`, DB-dumps, back-ups of privé-klantgegevens vast in Git.

---

## 💖 Steun dit project (donaties)

Dit startersjabloon is gratis en open source. Overweeg een donatie te doen om het onderhoud ervan te ondersteunen:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licentie en distributie

- **Licentie:** MIT-licentie (zie [LICENSE](LICENSE) - Copyright Andi UPN)
- **Bijdragengids:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Donatiegids:** [DONATE.md](DONATE.md)