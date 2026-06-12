#Démarreur Codex 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <strong>Français (CA)</strong> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>Une IA sans mémoire n'est qu'un consultant temporaire.</strong></h3>
  <p><strong>Un modèle de démarrage léger et hautement organisé pour créer des espaces de travail guidés par des agents avec OpenAI/Codex, avec une mémoire de départ intégrée et un archivage de recherche structuré.</strong></p>

  <p>Arrêtez de laisser l'IA oublier vos décisions techniques, vos styles de code et vos erreurs passées lors des sessions de chat. Créez un espace de travail qui accumule la sagesse.</p>
</div>

> 📦 Modèle gratuit par **andiupn** ([kuncimu.com](https://kuncimu.com)) · Sous licence [Licence MIT](LICENSE)  
> ☕ Si utile, [achetez-moi un café](https://ko-fi.com/andiupn) · 🚀 Besoin de monorepos professionnels ? Essayez la [version PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Le problème : "l'amnésie de l'IA"
Les modèles d’IA sont extrêmement performants, mais ils souffrent d’une amnésie complète lors des sessions de chat. Ils oublient les pièges personnalisés de votre projet, répétant encore et encore les mêmes erreurs de codage, gaspillant votre budget API et votre temps précieux.

---

## ⚡ La solution : l'espace de travail d'accumulation de sagesse

### 1. 🧠 Système de mémoire de départ intégré
Équipé de `.codex-memory/` qui contient des index de connaissances localisés. L'agent IA lit, écrit et met à jour sa mémoire directement pendant vos tâches de codage. S'il résout un bug une fois, il stocke la solution et ne répète jamais l'erreur.

### 📜 2. Archives de recherche réutilisables
Un répertoire d'archivage `research/` structuré avec des scripts d'utilitaires de recherche (`scripts/research-find.py`). Créez un référentiel d'API et de structures vérifiées que les agents peuvent interroger en quelques millisecondes.

### 🛰️ 3. Scripts de santé et de maintenance Otonom
Prérequis vérifiés et vérifiés automatiquement via `./scripts/project-health.sh --auto`. Gardez les règles de votre espace de travail, la syntaxe de la mémoire et les directives de code 100 % conformes.

---

## 📊 LITE vs PRO : la mise à niveau Premium

`codex-starter` est conçu pour être extrêmement léger. Pour orchestrer des monorepos professionnels et à l’échelle d’une agence :

| LITE (Gratuit) | PRO (1-5 $) |
|---|---|
| Norme gpt-5.5 | gpt-5.5 et gpt-5.4-mini |
| Aucun agent personnalisé | 3 Agents personnalisés (gouvernance, benchmark, etc.) |
| Aucune compétence en matière de flux de travail | 5 compétences Premium (conservateur, extracteur, git-sync, etc.) |
| Structure simple | Monorepo avec statut premier (`active/`, `staging/`, etc.) |
| Aucune configuration DevOps | Modèle de pile locale Docker Compose réutilisable |

👉 **[Obtenez l'édition PRO sur les sponsors GitHub](https://github.com/sponsors/andiupn?frequency=monthly)** · Détails complets : [COMPARISON.md](COMPARISON.md)

---

## 🚀 Démarrage rapide

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

## 🔒 Sécurité et espaces réservés

- **REMPLACER toutes les valeurs d'espace réservé** avant de publier ou d'utiliser ce référentiel.
- `.env.example` contient des exemples de variables d'environnement. **Copiez-le sur `.env`** et remplissez votre e-mail (`andi.upn@gmail.com`) et vos informations d'identification réelles.
- Ne validez PAS `.env`, les vidages de base de données, les sauvegardes ou les données client privées sur Git.

---

## 💖 Soutenez ce projet (Dons)

Ce modèle de démarrage est gratuit et open source. Pensez à faire un don pour soutenir son entretien :
- **Ko-fi :** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon :** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer :** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria :** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licence et distribution

- **Licence :** Licence MIT (voir [LICENCE](LICENSE) - Copyright Andi UPN)
- **Guide de contribution :** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Guide de don :** [DONATE.md](DONATE.md)