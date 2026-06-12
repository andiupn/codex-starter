# Codex-Starter 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <strong>Deutsch</strong> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>Eine KI ohne Gedächtnis ist nur ein vorübergehender Berater.</strong></h3>
  <p><strong>Eine leichte, gut organisierte Einstiegsvorlage für die Erstellung agentengesteuerter Arbeitsbereiche mit OpenAI/Codex, mit integriertem Seed-Speicher und strukturierter Forschungsarchivierung.</strong></p>

  <p>Lassen Sie die KI nicht mehr Ihre technischen Entscheidungen, Codestile und vergangenen Fehler in Chat-Sitzungen vergessen. Bauen Sie einen Arbeitsbereich auf, der Weisheit sammelt.</p>
</div>

> 📦 Kostenlose Vorlage von **andiupn** ([kuncimu.com](https://kuncimu.com)) · Lizenziert unter [MIT-Lizenz](LICENSE)  
> ☕ Wenn nützlich, [kauf mir einen Kaffee](https://ko-fi.com/andiupn) · 🚀 Brauchen Sie professionelle Monorepos? Probieren Sie die [PRO-Version](https://github.com/sponsors/andiupn?frequency=monthly) aus.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Das Problem: Die „KI-Amnesie“
KI-Modelle sind äußerst leistungsfähig, leiden jedoch während der Chat-Sitzungen unter völliger Amnesie. Sie vergessen die benutzerdefinierten Fallstricke Ihres Projekts, wiederholen immer wieder dieselben Codierungsfehler und verschwenden Ihr API-Budget und Ihre wertvolle Zeit.

---

## ⚡ Die Lösung: Der Weisheit sammelnde Arbeitsbereich

### 1. 🧠 Integriertes Seed-Memory-System
Ausgestattet mit `.codex-memory/`, das lokalisierte Wissensindizes enthält. Der KI-Agent liest, schreibt und aktualisiert seinen Speicher direkt während Ihrer Codierungsaufgaben. Wenn ein Fehler einmal behoben wird, speichert es die Lösung und wiederholt den Fehler nie.

### 📜 2. Wiederverwendbares Forschungsarchiv
Ein strukturiertes `research/`-Archivierungsverzeichnis mit Suchdienstprogrammskripten (`scripts/research-find.py`). Erstellen Sie ein Repository mit verifizierten APIs und Strukturen, die Agenten in Millisekunden abfragen können.

### 🛰️ 3. Otonom-Gesundheits- und Wartungsskripte
Voraussetzungen werden automatisch über `./scripts/project-health.sh --auto` geprüft und verifiziert. Sorgen Sie dafür, dass Ihre Arbeitsbereichsregeln, Speichersyntax und Coderichtlinien zu 100 % konform sind.

---

## 📊 LITE vs. PRO: Das Premium-Upgrade

`codex-starter` ist extrem leichtgewichtig konzipiert. Für die Orchestrierung professioneller und agenturmäßiger Monorepos:

| LITE (Kostenlos) | PRO (1-5 $) |
|---|---|
| Standard gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| Keine benutzerdefinierten Agenten | 3 benutzerdefinierte Agenten (Governance, Benchmark usw.) |
| Keine Workflow-Kenntnisse | 5 Premium-Fähigkeiten (Kurator, Extraktor, Git-Sync usw.) |
| Einfache Struktur | Status-First-Monorepo (`active/`, `staging/` usw.) |
| Keine DevOps-Konfiguration | Wiederverwendbare lokale Docker Compose-Stack-Vorlage |

👉 **[Holen Sie sich die PRO Edition auf GitHub Sponsors](https://github.com/sponsors/andiupn?frequency=monthly)** · Vollständige Details: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Schnellstart

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

## 🔒 Sicherheit und Platzhalter

- **Ersetzen Sie alle Platzhalterwerte**, bevor Sie dieses Repository veröffentlichen oder verwenden.
- `.env.example` enthält Beispielumgebungsvariablen. **Kopieren Sie es nach `.env`** und geben Sie Ihre E-Mail-Adresse (`andi.upn@gmail.com`) und Ihre tatsächlichen Anmeldeinformationen ein.
- Übertragen Sie `.env`, DB-Dumps, Backups oder private Kundendaten NICHT an Git.

---

## 💖 Unterstützen Sie dieses Projekt (Spenden)

Diese Startervorlage ist kostenlos und Open Source. Erwägen Sie eine Spende, um den Unterhalt zu unterstützen:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Lizenz & Vertrieb

- **Lizenz:** MIT-Lizenz (siehe [LIZENZ](LICENSE) – Copyright Andi UPN)
- **Mitwirkender Leitfaden:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Spendenleitfaden:** [DONATE.md](DONATE.md)