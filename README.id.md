# Codex Starter 🧠

<div align="center">
  <a href="README.md">English</a> | <strong>Bahasa Indonesia</strong> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a>
</div>

<br />

<div align="center">
  <h3><strong>AI tanpa memori hanyalah konsultan sementara.</strong></h3>
  <p><strong>Starter template yang ringan dan sangat terorganisir untuk membangun workspace terpandu AI bersama OpenAI/Codex, dilengkapi dengan memori lokal dan pengarsipan riset yang terstruktur.</strong></p>

  <p>Hentikan kebiasaan AI melupakan keputusan arsitektur, gaya kode, dan kesalahan masa lalu Anda di setiap sesi obrolan baru. Bangun workspace yang mengumpulkan kebijaksanaan.</p>
</div>

> 📦 Free template by **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licensed under [MIT License](LICENSE)  
> ☕ Jika bermanfaat, [beli saya kopi](https://ko-fi.com/andiupn) · 🚀 Butuh monorepo skala profesional? Coba [versi PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Masalahnya: "Amnesia AI" yang Pemboros
Model AI sangat cerdas, namun mereka menderita amnesia total di setiap pergantian sesi obrolan baru. Mereka melupakan gotchas khusus proyek Anda, mengulangi kesalahan pengodean yang sama terus-menerus, membuang-buang kuota API Anda, dan menghabiskan waktu berharga Anda.

---

## ⚡ Solusinya: Workspace yang Mengumpulkan Kebijaksanaan

### 1. 🧠 Sistem Memori Lokal Siap Pakai
Dilengkapi dengan folder `.codex-memory/` yang menyimpan indeks pengetahuan lokal proyek Anda. AI agent membaca, menulis, dan memperbarui memori ini secara mandiri selama pengerjaan kode. Begitu bug teratasi sekali, AI tidak akan mengulangi kesalahan tersebut.

### 📜 2. Arsip Riset yang Reusable
Direktori pengarsipan `research/` terstruktur dengan skrip pencarian pembantu (`scripts/research-find.py`). Bangun pustaka API dan modul terverifikasi yang dapat dipetakan oleh agen AI dalam hitungan milidetik.

### 🛰️ 3. Skrip Perawatan Otonom
Prasyarat dan kesehatan repositori diperiksa secara otomatis melalui `./scripts/project-health.sh --auto`. Pastikan aturan workspace, sintaks memori, dan panduan kode Anda 100% patuh sebelum pengembangan dimulai.

---

## 📊 LITE vs PRO: Upgrade Premium

`codex-starter` dirancang agar sangat ringan. Untuk orkestrasi monorepo skala profesional dan tingkat agensi:

| LITE (Gratis) | PRO ($1-5) |
|---|---|
| Standard gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| Tanpa Custom Agent | 3 Custom Agent (tata kelola, benchmark, dll.) |
| Tanpa Workflow Skills | 5 Premium Skills (kurator, ekstraktor, sinkronisasi git, dll.) |
| Struktur sederhana | Monorepo status-first (`active/`, `staging/`, dll.) |
| Tanpa Konfigurasi DevOps | Templat Docker Compose lokal siap pakai |

👉 **[Dapatkan Edisi PRO di GitHub Sponsors](https://github.com/sponsors/andiupn?frequency=monthly)** · Detail lengkap: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Memulai Cepat

```bash
# Jalankan pemeriksaan kesehatan repositori dan lingkungan lokal
./scripts/project-health.sh --auto

# Validasi aturan dan sintaks konfigurasi
python3 scripts/rules-health.py
python3 scripts/memory-health.py
python3 scripts/research-health.py

# Cari di dalam memori lokal dan indeks riset
./scripts/memory-find.py workflow
./scripts/research-find.py model
```

---

## 🔒 Keamanan & Placeholder

- **GANTI semua nilai placeholder** sebelum mempublikasikan atau menggunakan repositori ini.
- Berkas `.env.example` berisi contoh variabel lingkungan. **Salin ke `.env`** dan isi dengan email Anda (`andi.upn@gmail.com`) dan kredensial riil sebelum digunakan.
- Jangan commit `.env`, dump database, backup, atau data pelanggan ke git.

---

## 💖 Dukung Proyek Ini (Donasi)

Template starter ini gratis dan open-source. Pertimbangkan untuk memberikan dukungan:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer (Indonesia):** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria (Indonesia):** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Lisensi & Distribusi

- **Lisensi:** MIT License (lihat [LICENSE](LICENSE) - Copyright Andi UPN)
- **Panduan Kontribusi:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Panduan Donasi:** [DONATE.md](DONATE.md)
