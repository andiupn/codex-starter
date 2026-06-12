# Codex Starter 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <strong>Português (BR)</strong> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>Uma IA sem memória é apenas um consultor temporário.</strong></h3>
  <p><strong>Um modelo inicial leve e altamente organizado para criar espaços de trabalho guiados por agentes com OpenAI/Codex, com memória inicial integrada e arquivamento de pesquisa estruturado.</strong></p>

  <p>Pare de permitir que a IA esqueça suas decisões de engenharia, estilos de código e erros passados em sessões de bate-papo. Construa um espaço de trabalho que acumule sabedoria.</p>
</div>

> 📦 Modelo gratuito de **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licenciado sob [Licença MIT](LICENSE)  
> ☕ Se for útil, [me compre um café](https://ko-fi.com/andiupn) · 🚀 Precisa de monorepos profissionais? Experimente a [versão PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
__EMBAIXO_1__
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
__EMBAIXO_3__
__EMBAIXO_4__
__EMBLEMA_5__

---

## 💡 O problema: a "amnésia da IA"
Os modelos de IA são extremamente capazes, mas sofrem de amnésia completa durante as sessões de chat. Eles esquecem as dicas personalizadas do seu projeto, repetindo os mesmos erros de codificação continuamente, desperdiçando seu orçamento de API e seu valioso tempo.

---

## ⚡ A solução: o espaço de trabalho que acumula sabedoria

### 1. 🧠 Sistema de memória de sementes integrado
Equipado com `.codex-memory/` que contém índices de conhecimento localizados. O agente de IA lê, grava e atualiza sua memória diretamente durante suas tarefas de codificação. Se resolver um bug uma vez, ele armazena a solução e nunca mais repete o erro.

### 📜 2. Arquivo de pesquisa reutilizável
Um diretório de arquivamento `research/` estruturado com scripts de utilitário de pesquisa (`scripts/research-find.py`). Crie um repositório de APIs e estruturas verificadas que os agentes podem consultar em milissegundos.

### 🛰️ 3. Scripts de saúde e manutenção Otonom
Pré-requisitos verificados e verificados automaticamente via `./scripts/project-health.sh --auto`. Mantenha as regras do seu espaço de trabalho, a sintaxe da memória e as diretrizes de código 100% compatíveis.

---

## 📊 LITE vs PRO: a atualização premium

`codex-starter` foi projetado para ser extremamente leve. Para orquestrar monorepos profissionais e em escala de agência:

| LITE (grátis) | PRÓ (US$ 1-5) |
|---|---|
| Padrão gpt-5.5 | gpt-5.5 e gpt-5.4-mini |
| Sem agentes personalizados | 3 Agentes Aduaneiros (governança, benchmark, etc.) |
| Sem habilidades de fluxo de trabalho | 5 habilidades premium (curador, extrator, git-sync, etc.) |
| Estrutura simples | Monorepo com status primeiro (`active/`, `staging/`, etc.) |
| Nenhuma configuração DevOps | Modelo de pilha local reutilizável do Docker Compose |

👉 **[Obtenha a edição PRO nos patrocinadores do GitHub](https://github.com/sponsors/andiupn?frequency=monthly)** · Detalhes completos: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Início rápido

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

## 🔒 Segurança e espaços reservados

- **SUBSTITUA todos os valores de espaço reservado** antes de publicar ou usar este repositório.
- `.env.example` contém variáveis ​​de ambiente de amostra. **Copie para `.env`** e preencha seu e-mail (`andi.upn@gmail.com`) e credenciais reais.
- NÃO envie `.env`, dumps de banco de dados, backups ou dados privados de clientes para o Git.

---

## 💖 Apoie este projeto (doações)

Este modelo inicial é gratuito e de código aberto. Considere doar para apoiar sua manutenção:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licença e Distribuição

- **Licença:** Licença MIT (consulte [LICENSE](LICENSE) - Copyright Andi UPN)
- **Guia de contribuição:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Guia de doações:** [DONATE.md](DONATE.md)