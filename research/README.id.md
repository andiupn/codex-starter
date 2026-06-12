# Arsip Penelitian

<div align="center">
  <a href="README.md">English</a> | <strong>Bahasa Indonesia</strong> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>


Folder ini menyimpan hasil penelitian yang bisa dipakai ulang pada tugas berikutnya.

## Tujuan

- menyimpan hasil penelitian ke satu tempat yang konsisten
- Memudahkan agen mencari ulang penelitian lama
- Membedakan penelitian berdasarkan sumber dari memori yang sifatnya lebih ringkas dan tahan lama

## Struktur

- `index.json`: katalog semua riset
- `entries/<id>/report.md`: ringkasan penelitian yang siap dibaca ulang
- `entries/<id>/sources.json`: daftar sumber untuk penelitian tersebut

## Alur kerja yang disarankan

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari riset lama dengan `./scripts/research-find.py <query>`
3. Jika belum ada atau perlu update, simpan hasil dengan `./scripts/research-upsert.py`
4. Struktur Audit dengan `python3 scripts/research-health.py`
5. Jika ada wawasan yang sangat stabil, promosikan ringkasannya ke `.codex-memory/`

## Beda penelitian vs memori

- `research/`: untuk hasil penelitian yang masih membutuhkan sumber, konteks, dan bisa dipakai ulang nanti
- `.codex-memory/`: untuk pengetahuan ringkas yang tahan lama seperti preferensi pengguna, keputusan proyek, atau lingkungan kendala

## Contoh penggunaan

__KODE_BLOK_0__