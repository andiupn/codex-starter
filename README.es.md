#Iniciador del Códice 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <strong>Español</strong> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>Una IA sin memoria es sólo un consultor temporal.</strong></h3>
  <p><strong>Una plantilla inicial liviana y altamente organizada para crear espacios de trabajo guiados por agentes con OpenAI/Codex, que presenta memoria inicial integrada y archivo de investigación estructurado.</strong></p>

  <p>Deje de permitir que la IA olvide sus decisiones de ingeniería, estilos de código y errores pasados en las sesiones de chat. Construye un espacio de trabajo que acumule sabiduría.</p>
</div>

> 📦 Plantilla gratuita de **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licenciado bajo [Licencia MIT](LICENSE)  
> ☕ Si es útil, [cómprame un café](https://ko-fi.com/andiupn) · 🚀 ¿Necesitas monorepos profesionales? Pruebe la [versión PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 El Problema: La "Amnesia de la IA"
Los modelos de IA son extremadamente capaces, pero sufren de amnesia total durante las sesiones de chat. Se olvidan de los errores personalizados de su proyecto, repitiendo los mismos errores de codificación una y otra vez, desperdiciando su presupuesto de API y su valioso tiempo.

---

## ⚡ La solución: el espacio de trabajo para acumular sabiduría

### 1. 🧠 Sistema de memoria de semillas incorporado
Equipado con `.codex-memory/` que contiene índices de conocimiento localizados. El agente de IA lee, escribe y actualiza su memoria directamente durante sus tareas de codificación. Si resuelve un error una vez, almacena la solución y nunca repite el error.

### 📜 2. Archivo de investigación reutilizable
Un directorio de archivo estructurado `research/` con scripts de utilidad de búsqueda (`scripts/research-find.py`). Cree un repositorio de estructuras y API verificadas que los agentes puedan consultar en milisegundos.

### 🛰️ 3. Guiones de salud y mantenimiento de Otonom
Requisitos previos verificados y verificados automáticamente a través de `./scripts/project-health.sh --auto`. Mantenga las reglas de su espacio de trabajo, la sintaxis de la memoria y las pautas de código 100 % compatibles.

---

## 📊 LITE vs PRO: La actualización Premium

`codex-starter` está diseñado para ser extremadamente liviano. Para orquestar monorepos a escala profesional y de agencia:

| LITE (Gratis) | PRO ($1-5) |
|---|---|
| Estándar gpt-5.5 | gpt-5.5 y gpt-5.4-mini |
| Sin agentes personalizados | 3 Agentes Aduaneros (gobernanza, benchmark, etc.) |
| Sin habilidades de flujo de trabajo | 5 habilidades premium (curador, extractor, git-sync, etc.) |
| Estructura sencilla | Monorepo de estado primero (`active/`, `staging/`, etc.) |
| Sin configuración de DevOps | Plantilla de pila local Docker Compose reutilizable |

👉 **[Obtenga la edición PRO con patrocinadores de GitHub](https://github.com/sponsors/andiupn?frequency=monthly)** · Detalles completos: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Inicio rápido

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

## 🔒 Seguridad y marcadores de posición

- **REEMPLAZAR todos los valores de los marcadores de posición** antes de publicar o usar este repositorio.
- `.env.example` contiene variables de entorno de muestra. **Cópielo a `.env`** y complete su correo electrónico (`andi.upn@gmail.com`) y sus credenciales reales.
- NO envíe `.env`, volcados de bases de datos, copias de seguridad ni datos privados de clientes en Git.

---

## 💖 Apoye este proyecto (Donaciones)

Esta plantilla inicial es gratuita y de código abierto. Considere donar para apoyar su mantenimiento:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licencia y distribución

- **Licencia:** Licencia MIT (ver [LICENCIA](LICENSE) - Copyright Andi UPN)
- **Guía contribuyente:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Guía de donación:** [DONAR.md](DONATE.md)