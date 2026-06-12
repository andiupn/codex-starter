# Codex Starter 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <strong>Українська</strong> | <a href="README.nl.md">Nederlands</a>
</div>

<br />

<div align="center">
  <h3><strong>ШІ без пам’яті — це лише тимчасовий консультант.</strong></h3>
  <p><strong>Легкий, добре організований стартовий шаблон для створення керованих агентами робочих просторів із OpenAI/Codex із вбудованою початковою пам’яттю та структурованим архівуванням досліджень.</strong></p>

  <p>Не дозволяйте штучному інтелекту забувати ваші інженерні рішення, стилі коду та минулі помилки під час сеансів чату. Створіть робочий простір, який накопичує мудрість.</p>
</div>

> 📦 Безкоштовний шаблон від **andiupn** ([kuncimu.com](https://kuncimu.com)) · Ліцензовано відповідно до [ліцензії MIT](LICENSE)  
> ☕ Якщо це корисно, [приготуйте мені кави](https://ko-fi.com/andiupn) · 🚀 Потрібні професійні монорепо? Спробуйте [PRO версію](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Проблема: «ШІ-амнезія»
Моделі штучного інтелекту надзвичайно здатні, але вони страждають від повної амнезії під час сеансів чату. Вони забувають нестандартні помилки вашого проекту, повторюючи ті самі помилки кодування знову і знову, витрачаючи ваш бюджет API і ваш дорогоцінний час.

---

## ⚡ Рішення: робочий простір для накопичення мудрості

### 1. 🧠 Вбудована система пам’яті насіння
Оснащено `.codex-memory/`, який містить локалізовані індекси знань. Агент штучного інтелекту читає, записує та оновлює свою пам’ять безпосередньо під час ваших завдань кодування. Якщо він вирішує помилку один раз, він зберігає рішення та ніколи не повторює помилку.

### 📜 2. Багаторазовий архів досліджень
Структурований `research/` каталог архівування зі скриптами пошукових утиліт (`scripts/research-find.py`). Створіть репозиторій перевірених API і структур, які агенти можуть надсилати запити за мілісекунди.

### 🛰️ 3. Скрипти здоров’я та обслуговування Otonom
Передумови перевірено та перевірено автоматично за допомогою `./scripts/project-health.sh --auto`. Дотримуйтеся правил робочої області, синтаксису пам’яті та вказівок щодо коду на 100% сумісними.

---

## 📊 LITE vs PRO: преміум-оновлення

`codex-starter` надзвичайно легкий. Для організації професійних і агенційних монорепо:

| LITE (безкоштовно) | PRO ($1-5) |
|---|---|
| Стандарт gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| Немає спеціальних агентів | 3 Спеціальні агенти (управління, порівняльний аналіз тощо) |
| Немає навичок робочого процесу | 5 преміальних навичок (куратор, екстрактор, git-sync тощо) |
| Проста структура | Монорепо статусу першого (`active/`, `staging/` тощо) |
| Немає конфігурації DevOps | Багаторазовий Docker Створення локального шаблону стека |

👉 **[Отримайте PRO Edition на GitHub Sponsors](https://github.com/sponsors/andiupn?frequency=monthly)** · Повна інформація: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Швидкий старт

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

## 🔒 Безпека та заповнювачі

- **ЗАМІНІТЬ усі значення заповнювачів** перед публікацією або використанням цього сховища.
- `.env.example` містить зразки змінних середовища. **Скопіюйте його на `.env`** та введіть свою електронну адресу (`andi.upn@gmail.com`) та фактичні облікові дані.
- НЕ передавайте `.env`, дампи БД, резервні копії або приватні дані клієнтів у Git.

---

## 💖 Підтримайте цей проект (пожертви)

Цей стартовий шаблон є безкоштовним і має відкритий код. Розгляньте пожертвування на підтримку його обслуговування:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Ліцензія та розповсюдження

- **Ліцензія:** Ліцензія MIT (див. [LICENSE](LICENSE) - Copyright Andi UPN)
- **Посібник зі створення внеску:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Посібник із пожертвувань:** [DONATE.md](DONATE.md)