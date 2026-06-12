# Codex Starter 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <strong>Română</strong>
</div>
<br>

<div align="center">
  <h3><strong>O IA fără memorie este doar un consultant temporar.</strong></h3>
  <p><strong>Un șablon de pornire ușor și foarte organizat pentru construirea de spații de lucru ghidate de agenți cu OpenAI/Codex, cu memorie semințe integrată și arhivare structurată de cercetare.</strong></p>

  <p>Nu mai lăsați AI să uite deciziile de inginerie, stilurile de cod și erorile anterioare în sesiunile de chat. Construiește un spațiu de lucru care acumulează înțelepciune.</p>
</div>

> 📦 Șablon gratuit de la **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licențiat sub [Licență MIT](LICENSE)  
> ☕ Dacă este util, [cumpără-mi o cafea](https://ko-fi.com/andiupn) · 🚀 Ai nevoie de monorepo profesionale? Încercați [versiunea PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Problema: „Amnezia AI”
Modelele AI sunt extrem de capabile, dar suferă de amnezie completă în timpul sesiunilor de chat. Ei uită problemele personalizate ale proiectului dvs., repetând aceleași erori de codare mereu, irosindu-vă bugetul API și timpul prețios.

---

## ⚡ Soluția: spațiul de lucru care acumulează înțelepciune

### 1. 🧠 Sistem de memorie de semințe încorporat
Echipat cu `.codex-memory/` care conține indici de cunoștințe localizați. Agentul AI citește, scrie și își actualizează memoria direct în timpul sarcinilor de codare. Dacă rezolvă o eroare o dată, stochează soluția și nu repetă niciodată eroarea.

### 📜 2. Arhiva de cercetare reutilizabilă
Un director de arhivare `research/` structurat cu scripturi utilitare de căutare (`scripts/research-find.py`). Creați un depozit de API-uri și structuri verificate pe care agenții le pot interoga în milisecunde.

### 🛰️ 3. Scripturi Otonom Health & Maintenance
Cerințe preliminare verificate și verificate automat prin `./scripts/project-health.sh --auto`. Păstrați regulile spațiului de lucru, sintaxa memoriei și regulile de cod 100% conforme.

---

## 📊 LITE vs PRO: Upgrade Premium

`codex-starter` este conceput pentru a fi extrem de ușor. Pentru orchestrarea monorepourilor profesionale și la scară de agenție:

| LITE (gratuit) | PRO ($1-5) |
|---|---|
| Standard gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| Fără agenți personalizați | 3 agenți personalizați (guvernare, benchmark etc.) |
| Fără abilități de flux de lucru | 5 abilități premium (curator, extractor, git-sync etc.) |
| Structură simplă | Status-primul Monorepo (`active/`, `staging/` etc.) |
| Fără configurație DevOps | Șablon de stivă locală Docker Compose reutilizabil |

👉 **[Obțineți ediția PRO pe sponsorii GitHub](https://github.com/sponsors/andiupn?frequency=monthly)** · Detalii complete: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Început rapid

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

## 🔒 Securitate și substituenți

- **ÎNLOCUIȚI toate valorile substituenților** înainte de a publica sau de a utiliza acest depozit.
- `.env.example` conține exemple de variabile de mediu. **Copiați-l în `.env`** și completați adresa dvs. de e-mail (`andi.upn@gmail.com`) și acreditările reale.
- NU trimiteți `.env`, depozitări DB, copii de siguranță sau date private ale clienților în Git.

---

## 💖 Sprijină acest proiect (donații)

Acest șablon de pornire este gratuit și open-source. Luați în considerare donarea pentru a sprijini întreținerea acestuia:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licență și distribuție

- **Licență:** MIT Licență (consultați [LICENSE](LICENSE) - Copyright Andi UPN)
- **Ghid pentru contribuții:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Ghid pentru donații:** [DONATE.md](DONATE.md)