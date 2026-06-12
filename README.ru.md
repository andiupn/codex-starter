# Стартер Кодекса 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <strong>Русский</strong> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>ИИ без памяти — всего лишь временный консультант.</strong></h3>
  <p><strong>Легкий, высокоорганизованный стартовый шаблон для создания управляемых агентами рабочих пространств с помощью OpenAI/Codex, оснащенный встроенной исходной памятью и структурированным архивированием исследований.</strong></p>

  <p>Не позволяйте искусственному интеллекту забывать ваши инженерные решения, стили кода и прошлые ошибки во время сеансов чата. Создайте рабочее пространство, в котором будет накапливаться мудрость.</p>
</div>

> 📦 Бесплатный шаблон от **andiupn** ([kuncimu.com](https://kuncimu.com)) · Лицензия [MIT License](LICENSE)  
> ☕ Если полезно, [купи мне кофе](https://ko-fi.com/andiupn) · 🚀 Нужен профессиональный монорепозиторий? Попробуйте [PRO-версию](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
__ЗНАК_3__
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Проблема: «амнезия искусственного интеллекта»
Модели искусственного интеллекта чрезвычайно эффективны, но они страдают полной амнезией во время сеансов чата. Они забывают особенности вашего проекта, повторяя одни и те же ошибки кодирования снова и снова, тратя впустую ваш бюджет API и ваше драгоценное время.

---

## ⚡ Решение: рабочее пространство для накопления мудрости

### 1. 🧠 Встроенная система памяти семян
Оснащен `.codex-memory/`, содержащим локализованные индексы знаний. Агент ИИ читает, записывает и обновляет свою память непосредственно во время ваших задач по кодированию. Если он устраняет ошибку один раз, он сохраняет решение и никогда не повторяет ошибку.

### 📜 2. Многоразовый исследовательский архив
Структурированный каталог архивирования `research/` со сценариями утилит поиска (`scripts/research-find.py`). Создайте репозиторий проверенных API и структур, к которым агенты смогут обращаться за миллисекунды.

### 🛰️ 3. Скрипты Otonom Health & Maintenance
Предварительные требования проверяются и проверяются автоматически через `./scripts/project-health.sh --auto`. Обеспечьте стопроцентное соответствие правилам вашего рабочего пространства, синтаксису памяти и рекомендациям по кодированию.

---

## 📊 LITE против PRO: Премиум-обновление

`codex-starter` спроектирован так, чтобы быть чрезвычайно легким. Для организации профессиональных и агентских монорепозиториев:

| ЛАЙТ (бесплатно) | ПРО (1–5 долларов США) |
|---|---|
| Стандартный gpt-5.5 | gpt-5.5 и gpt-5.4-мини |
| Никаких пользовательских агентов | 3 пользовательских агента (управление, контрольные показатели и т. д.) |
| Нет навыков рабочего процесса | 5 премиум-навыков (куратор, экстрактор, git-sync и т. д.) |
| Простая структура | Монорепозиторий с приоритетом по статусу (`active/`, `staging/` и т. д.) |
| Нет конфигурации DevOps | Многоразовый шаблон Docker Compose локального стека |

👉 **[Получите PRO-версию у спонсоров GitHub](https://github.com/sponsors/andiupn?frequency=monthly)** · Полная информация: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Быстрый старт

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

## 🔒 Безопасность и заполнители

- **ЗАМЕНИТЕ все значения заполнителей** перед публикацией или использованием этого репозитория.
- `.env.example` содержит примеры переменных среды. **Скопируйте его в `.env`** и укажите свой адрес электронной почты (`andi.upn@gmail.com`) и фактические учетные данные.
– НЕ передавайте `.env`, дампы БД, резервные копии или личные данные клиентов в Git.

---

## 💖 Поддержите этот проект (пожертвования)

Этот стартовый шаблон бесплатен и имеет открытый исходный код. Рассмотрите возможность пожертвования на поддержку его обслуживания:
- **Ко-фи:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Саверия:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Лицензия и распространение

- **Лицензия:** Лицензия MIT (см. [ЛИЦЕНЗИЮ](LICENSE) – авторские права Andi UPN)
- **Руководство для участников:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Руководство по пожертвованиям:** [DONATE.md](DONATE.md)