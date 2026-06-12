# Forskningsarkiv

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <strong>Svenska</strong> | <a href="README.ro.md">Română</a>
</div>
<br>


Mapp ini menyimpan hasil riset yang bisa dipakai ulang pada uppgift berikutnya.

## Tujuan

- menyimpan hasil riset ke satu tempat yang konsisten
- memudahkan agent mencari ulang riset lama
- memisahkan riset berbasis sumber dari minne yang sifatnya lebih ringkas dan tahan lama

## Struktur

- `index.json`: katalog ringkas semua riset
- `entries/<id>/report.md`: ringkasan riset yang siap dibaca ulang
- `entries/<id>/sources.json`: daftar sumber untuk riset tersebut

## Arbetsflöde yang disarankan

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari riset lama dengan `./scripts/research-find.py <query>`
3. Jika belum ada atau perlu update, simpan hasil dengan `./scripts/research-upsert.py`
4. Granskningsstrukturen `python3 scripts/research-health.py`
5. Jika ada insikt yang sangat stabil, främja ringkasannya ke `.codex-memory/`

## Bedaforskning vs minne

- `research/`: untuk hasil riset yang masih butuh sumber, konteks, och bisa dipakai ulang nanti
- `.codex-memory/`: untuk pengetahuan ringkas yang tahan lama seperti preferensi användare, keputusan-projektet, atau constraint environment

## Fortfarande

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