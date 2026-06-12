# Archives de recherche

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <strong>Français (CA)</strong> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>


Dossier ini menyimpan hasil Riset yang bisa dipakai ulang pada tâche berikutnya.

## Tujuan

- menyimpan hasil Riset ke satu tempat yang konsisten
- agent memudahkan mencari ulang Riset lama
- memisahkan Riset Berbasis sumber dari mémoire yang sifatnya lebih ringkas et tahan lama

## Structure

- `index.json` : catalogue ringkas semua Riset
- `entries/<id>/report.md` : ringkasan Riset yang siap dibaca ulang
- `entries/<id>/sources.json` : daftar sumber pour prendre une décision laconique

## Workflow pour mieux comprendre

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari Riset Lama dengan `./scripts/research-find.py <query>`
3. Jika belum ada atau perlu mise à jour, simpan hasil dengan `./scripts/research-upsert.py`
4. Structure d'audit avec `python3 scripts/research-health.py`
5. Jika ada insight yang sangat stabil, promouvoir ringkasannya ke `.codex-memory/`

## Recherche Beda vs mémoire

- `research/` : pour hasil Riset yang masih butuh sumber, konteks, et bisa dipakai oulang nanti
- `.codex-memory/` : pour les utilisateurs préférés de yang tahan lama, le projet Keputusan, l'environnement de contraintes atau

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