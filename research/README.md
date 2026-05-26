# Research Archive

Folder ini menyimpan hasil riset yang bisa dipakai ulang pada task berikutnya.

## Tujuan

- menyimpan hasil riset ke satu tempat yang konsisten
- memudahkan agent mencari ulang riset lama
- memisahkan riset berbasis sumber dari memory yang sifatnya lebih ringkas dan tahan lama

## Struktur

- `index.json`: katalog ringkas semua riset
- `entries/<id>/report.md`: ringkasan riset yang siap dibaca ulang
- `entries/<id>/sources.json`: daftar sumber untuk riset tersebut

## Workflow yang disarankan

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari riset lama dengan `./scripts/research-find.py <query>`
3. Jika belum ada atau perlu update, simpan hasil dengan `./scripts/research-upsert.py`
4. Audit struktur dengan `python3 scripts/research-health.py`
5. Jika ada insight yang sangat stabil, promote ringkasannya ke `.codex-memory/`

## Beda research vs memory

- `research/`: untuk hasil riset yang masih butuh sumber, konteks, dan bisa dipakai ulang nanti
- `.codex-memory/`: untuk pengetahuan ringkas yang tahan lama seperti preferensi user, keputusan project, atau constraint environment

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
