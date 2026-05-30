# codex-starter

Template starter ringan untuk membangun repo kerja dengan Codex/OpenAI agents. Fokusnya sederhana: governance dasar, memory system, research archive, helper scripts, dan struktur folder yang rapi untuk repo open source atau free tier.

## Tujuan

- memberi starter yang cepat dipakai untuk project Codex baru
- menjaga workflow agent tetap terstruktur tanpa membawa data pribadi repo sumber
- menyediakan memory, research, dan rules dasar yang bisa dikembangkan nanti
- cocok untuk distribusi open source dan monetisasi berbasis donasi di luar repo

## Yang Dibawa

- `AGENTS.md` sebagai source of truth aturan kerja agent
- `docs/` untuk rules architecture, memory, research, folder system, model strategy, browser fallback, dan workspace setup
- `scripts/` untuk health check, maintenance log, memory tooling, dan research tooling
- `.codex-memory/` dengan index lokal dan seed entries generik
- `research/` sebagai archive kosong yang siap dipakai
- folder lifecycle: `active/`, `staging/`, `templates/`, `shared/`, `artifacts/`, `archive/`, `experiments/`
- dokumen distribusi dasar: `LICENSE`, `CONTRIBUTING.md`, `DONATE.md`, `.github/FUNDING.yml`

## Yang Sengaja Tidak Dibawa

- app aktif atau data runtime dari repo sumber
- repo skills dan custom agents bawaan
- dump database, backup, imports, generated artifacts, atau secret
- benchmark output lama dan report riset yang spesifik ke workspace sumber

## Quick Start

```bash
./scripts/project-health.sh --auto
python3 scripts/rules-health.py
python3 scripts/memory-health.py
python3 scripts/research-health.py
./scripts/memory-find.py workflow
./scripts/research-find.py model
```

## Distribusi & Lisensi

- **Lisensi:** MIT License (lihat [LICENSE](LICENSE) - Copyright Andi UPN)
- **Panduan Kontribusi:** Lihat [CONTRIBUTING.md](CONTRIBUTING.md)
- **Panduan Donasi:** Lihat [DONATE.md](DONATE.md)

---

## 💖 Dukung Proyek Ini (Donasi)

Template starter ini gratis dan open-source. Jika bermanfaat, pertimbangkan untuk mendukung:

| Platform | Link Dukungan | Keterangan |
|---|---|---|
| ☕ **Ko-fi** | [ko-fi.com/andiupn](https://ko-fi.com/andiupn) | Internasional (PayPal, CC) |
| 🎨 **Patreon** | [patreon.com/AndiUpn](https://patreon.com/AndiUpn) | Bulanan/Subscription |
| 🇮🇩 **Trakteer** | [trakteer.id/andi_upn](https://trakteer.id/andi_upn) | Lokal Indonesia |
| 🇮🇩 **Saweria** | [saweria.co/andiupn](https://saweria.co/andiupn) | Lokal Indonesia |

---

## 💎 Upgrade ke PRO

`codex-starter` sengaja dirancang sangat ringan. Untuk fitur orkestrasi skala profesional:

| LITE (Gratis) | PRO ($1-5) |
|---|---|
| standard gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| No Custom Agents | 3 Custom Agents (governance, benchmark, dsb.) |
| No Workflow Skills | 5 Premium Skills (curator, extractor, git-sync, dsb.) |
| Simple struktur | Status-first Monorepo (`active/`, `staging/`, dsb.) |
| No Devops Config | Docker Compose local stack template |

👉 **[Dapatkan Edisi PRO di kuncimu.com](https://kuncimu.com)** · Detail perbandingan: [COMPARISON.md](COMPARISON.md)

---

## Keamanan & Placeholder

- **GANTI semua nilai placeholder** sebelum menggunakan repo ini.
- File `.env.example` berisi contoh variabel lingkungan. **Salin ke `.env`** dan isi dengan email Anda (`andi.upn@gmail.com`) dan token autentikasi riil sebelum digunakan.
- Jangan commit `.env`, dump database, backup, atau data pelanggan ke git.
- Selalu gunakan dummy data dan fixture lokal untuk pengembangan.
- Aturan model dan workflow OpenAI/Codex ada di [AGENTS.md](AGENTS.md) dan [docs/codex-model-strategy.md](docs/codex-model-strategy.md).
