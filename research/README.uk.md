# Архів досліджень

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <strong>Українська</strong> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>


Folder ini menyimpan hasil riset yang bisa dipakai ulang pada task berikutnya.

## Тухуан

- menyimpan hasil riset ke satu tempat yang konsisten
- агент memudahkan mencari ulang riset lama
- memisahkan riset berbasis sumber dari memory yang sifatnya lebih ringkas dan tahan lama

## Структура

- `index.json`: каталог ringkas semua riset
- `entries/<id>/report.md`: ringkasan riset yang siap dibaca ulang
- `entries/<id>/sources.json`: daftar sumber untuk riset tersebut

## Workflow yang disarankan

1. Джаланкан `./scripts/project-health.sh --auto`
2. Cari riset lama dengan `./scripts/research-find.py <query>`
3. Якщо ви не оновили або оновили перлу, просто натисніть `./scripts/research-upsert.py`
4. Структура аудиту `python3 scripts/research-health.py`
5. Jika ada insight yang sangat stabil, сприяти ringkasannya ke `.codex-memory/`

## Дослідження Беда проти пам'яті

- `research/`: untuk hasil riset yang masih butuh sumber, konteks, dan bisa dipakai ulang nanti
- `.codex-memory/`: для налаштування параметрів користувача, користування проектом, або середовища обмежень

## Contoh pengguan

```bash
./scripts/research-find.py openai skills memory

./scripts/research-upsert.py \
  --title "Codex skills versus memory" \
  --question "Apakah sistem skill perlu dipakai selain memory?" \
  --summary "Skills cocok untuk workflow yang berulang, memory cocok untuk context tahan lama." \
  --tag openai,codex,skills,memory \
  --keyword "skills,memory,research workflow" \
  --finding "Skills menambahkan capability dan workflow khusus." \
  --finding "Memory lebih cocok untuk context ringkas yang akumulatif." \
  --reuse-note "Gunakan skill untuk workflow riset atau task berulang." \
  --source "OpenAI Docs | https://developers.openai.com/codex/skills | Dokumentasi resmi skills Codex"

python3 scripts/research-health.py
```