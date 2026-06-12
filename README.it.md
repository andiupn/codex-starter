#Codice Iniziale 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <strong>Italiano</strong> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>Un'intelligenza artificiale senza memoria è solo un consulente temporaneo.</strong></h3>
  <p><strong>Un modello iniziale leggero e altamente organizzato per la creazione di spazi di lavoro guidati da agenti con OpenAI/Codex, con memoria seed integrata e archiviazione strutturata della ricerca.</strong></p>

  <p>Smetti di lasciare che l'IA dimentichi le tue decisioni ingegneristiche, gli stili di codice e gli errori passati durante le sessioni di chat. Costruisci uno spazio di lavoro che accumuli saggezza.</p>
</div>

> 📦 Modello gratuito di **andiupn** ([kuncimu.com](https://kuncimu.com)) · Concesso in licenza con [licenza MIT](LICENSE)  
> ☕ Se utile, [offrimi un caffè](https://ko-fi.com/andiupn) · 🚀 Hai bisogno di monorepos professionali? Prova la [versione PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Il problema: l'"amnesia dell'IA"
I modelli IA sono estremamente capaci, ma soffrono di un'amnesia completa durante le sessioni di chat. Dimenticano i trucchi personalizzati del tuo progetto, ripetendo più e più volte gli stessi errori di codifica, sprecando il tuo budget API e il tuo tempo prezioso.

---

## ⚡ La soluzione: lo spazio di lavoro per l'accumulo di saggezza

### 1. 🧠 Sistema di memoria dei semi integrato
Dotato di `.codex-memory/` che contiene indici di conoscenza localizzati. L'agente AI legge, scrive e aggiorna la sua memoria direttamente durante le attività di codifica. Se risolve un bug una volta, memorizza la soluzione e non ripete mai l'errore.

### 📜 2. Archivio di ricerca riutilizzabile
Una directory di archiviazione `research/` strutturata con script dell'utilità di ricerca (`scripts/research-find.py`). Crea un repository di API e strutture verificate su cui gli agenti possono eseguire query in millisecondi.

### 🛰️ 3. Script di salute e manutenzione di Otonom
Prerequisiti controllati e verificati automaticamente tramite `./scripts/project-health.sh --auto`. Mantieni le regole dello spazio di lavoro, la sintassi della memoria e le linee guida del codice conformi al 100%.

---

## 📊 LITE vs PRO: l'aggiornamento Premium

`codex-starter` è progettato per essere estremamente leggero. Per orchestrare monorepos su scala professionale e di agenzia:

| LITE (gratuito) | PRO ($1-5) |
|---|---|
| Standard gpt-5.5 | gpt-5.5 e gpt-5.4-mini |
| Nessun agente personalizzato | 3 Agenti personalizzati (governance, benchmark, ecc.) |
| Nessuna competenza nel flusso di lavoro | 5 competenze premium (curatore, estrattore, git-sync, ecc.) |
| Struttura semplice | Monorepo con primo stato (`active/`, `staging/` e così via) |
| Nessuna configurazione DevOps | Docker riutilizzabile Componi modello stack locale |

👉 **[Ottieni l'edizione PRO sugli sponsor GitHub](https://github.com/sponsors/andiupn?frequency=monthly)** · Dettagli completi: [COMPARISON.md](COMPARISON.md)

---

## 🚀Avvio rapido

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

## 🔒 Sicurezza e segnaposto

- **SOSTITUISCI tutti i valori segnaposto** prima di pubblicare o utilizzare questo repository.
- `.env.example` contiene variabili di ambiente di esempio. **Copialo su `.env`** e inserisci il tuo indirizzo email (`andi.upn@gmail.com`) e le credenziali effettive.
- NON eseguire il commit di `.env`, dump di DB, backup o dati privati ​​dei clienti su Git.

---

## 💖 Sostieni questo progetto (donazioni)

Questo modello iniziale è gratuito e open source. Prendi in considerazione la possibilità di donare per sostenere il suo mantenimento:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licenza e distribuzione

- **Licenza:** Licenza MIT (vedi [LICENZA](LICENSE) - Copyright Andi UPN)
- **Guida per contribuire:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Guida alle donazioni:** [DONATE.md](DONATE.md)