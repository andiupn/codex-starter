# Onderzoeksarchief

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <strong>Nederlands</strong> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>


Folder ini menyimpan hasil riset yang bisa dipakai ulang pada task berikutnya.

## Tujuan

- Menyimpan heeft de temperatuur constant gehouden
- memudahkan-agent mencari ulang riset lama
- memisahkan worden gebaseerd op het geheugen van mijn leven en de lama

## Structuur

- `index.json`: catalogus ringkas semua gestegen
- `entries/<id>/report.md`: ringkasan stijgt yang siap dibaca ulang
- `entries/<id>/sources.json`: het wordt kort gezegd

## Workflow is niet mogelijk

1. Jalankan `./scripts/project-health.sh --auto`
2. Ik kom op met `./scripts/research-find.py <query>`
3. Als je een update wilt, kun je eenvoudigweg `./scripts/research-upsert.py`
4. Auditstructuur met `python3 scripts/research-health.py`
5. Jika ada inzicht yang sangat stabil, promoot ringkasannya ke `.codex-memory/`

## Beda-onderzoek versus geheugen

- `research/`: voor het grootste deel van de tijd, konteks, dan is dit het geval
- `.codex-memory/`: voor het kiezen van een andere voorkeursgebruiker, een project, een beperkingsomgeving

## Contoh penggunaan

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