# Archiwum badawcze

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <strong>Polski</strong> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>


Folder ini menyimpan hasilriset yang bisa dipakai ulang pada zadanie berikutnya.

## Tujuan

- menyimpan hasilriset ke satu tempat yang konsisten
- memudahkan agent mencari ulangriset lama
- memisahkanriset berbasis sumber dari pamięć yang sifatnya lebih ringkas dan tahan lama

## Struktura

- `index.json`: katalog ringkas semuariset
- `entries/<id>/report.md`: ringkasanriset yang siap dibaca ulang
- `entries/<id>/sources.json`: można uzyskać zwięzłe informacje

## Przepływ pracy jest inny

1. Jalankan `./scripts/project-health.sh --auto`
2. Caririset lama dengan `./scripts/research-find.py <query>`
3. Jika belum ada atau perlu update, simpan hasil dengan `./scripts/research-upsert.py`
4. Struktura audytu z `python3 scripts/research-health.py`
5. Jika ada wgląd yang sangat stabil, promuj ringkasannya ke `.codex-memory/`

## Badania Beda a pamięć

- `research/`: dla hasilriset yang masih butuh sumber, konteks, dan bisa dipakai ulang nanti
- `.codex-memory/`: dla pengetahuan ringkas yang tahan lama seperti preferensi użytkownik, projekt keputusan, środowisko z ograniczeniami atau

## Contoh penggunaan

__KOD_BLOKU_0__