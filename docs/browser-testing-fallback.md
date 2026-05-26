# Browser Testing Fallback

Dokumen ini menjelaskan fallback workflow untuk browser atau UI testing ketika browser tool utama, MCP browser path, atau localhost inspection tidak tersedia.

## Goal

Sediakan pola yang portable, deterministik, dan mudah dibuang setelah tidak dipakai.

## Prefer This Order

1. browser tool atau Playwright yang sudah tersedia di session interaktif
2. browser tooling yang memang menjadi bagian dari app atau eksperimen terkait
3. script Playwright lokal kecil di folder app atau eksperimen yang relevan

## When To Use This Fallback

Gunakan fallback ini jika:

- browser tool interaktif tidak tersedia
- localhost UI perlu verifikasi yang tidak cukup dengan fetch biasa
- dibutuhkan screenshot dan assertion deterministik untuk satu flow spesifik

## Workflow

1. Pastikan target app sudah berjalan dan URL-nya jelas.
2. Simpan runner script di folder app atau eksperimen terkait, bukan di root repo.
3. Install Playwright hanya di area yang memang membutuhkannya.
4. Tulis script kecil untuk satu flow yang jelas.
5. Gunakan cleanup yang andal seperti `try/finally` dan `browser.close()`.
6. Simpan screenshot atau output ke folder artifact eksperimen.
7. Rangkum hasil pass/fail per langkah.

## Minimal Script Expectations

- satu flow yang jelas
- selector yang eksplisit
- assertion untuk state penting
- screenshot saat langkah penting atau saat gagal
- cleanup yang andal

## Safety Rules

- Jangan gunakan credential production.
- Jangan jadikan fallback ini default global jika tool utama sehat.
- Jangan install Playwright di root repo hanya demi satu eksperimen kecil.
