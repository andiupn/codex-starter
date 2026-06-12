# Lưu trữ nghiên cứu

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <strong>Tiếng Việt</strong> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>


Thư mục ini menyimpan hasil Riset yang bisa dipakai ulang pada task berikutnya.

## Đồ Quyên

- menyimpan hasil Riset ke satu tempat yang konsisten
- đại lý memudahkan mencari ulang Riset lama
- memisahkan Riset Berbasis Sumber Dari Memory yang Sifatnya Lebih Ringkas và Tahan Lama

## Cấu trúc

- `index.json`: katalog ringkas semua Riset
- `entries/<id>/report.md`: ringkasan Riset yang siap dibaca ulang
- `entries/<id>/sources.json`: từ đầu đến cuối tăng lên

## Quy trình làm việc bị loại bỏ

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari Riset Lama Dengan `./scripts/research-find.py <query>`
3. Cần cập nhật một chút về vấn đề này, đơn giản là có `./scripts/research-upsert.py`
4. Cấu trúc kiểm toán với `python3 scripts/research-health.py`
5. Jika ada cái nhìn sâu sắc yang sangat ổn định, thúc đẩy ringkasannya ke `.codex-memory/`

## Nghiên cứu Beda so với trí nhớ

- `research/`: untuk hasil Riset yang masih butuh sumber, konteks, dan bisa dipakai ulang nanti
- `.codex-memory/`: cho một người dùng thích hợp hơn, dự án phù hợp, môi trường hạn chế

## Contoh chim cánh cụt

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