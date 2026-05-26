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

## Distribusi

- lisensi default: lihat `LICENSE`
- panduan kontribusi: lihat `CONTRIBUTING.md`
- monetisasi donasi: lihat `DONATE.md` dan `.github/FUNDING.yml`

## Keamanan & Placeholder

- **GANTI semua nilai placeholder** sebelum menggunakan repo ini.
- File `.env.example` berisi contoh variabel lingkungan. **Salin ke `.env`** dan isi dengan nilai asli sebelum menjalankan aplikasi.
- Jangan commit `.env`, dump database, backup, atau data pelanggan ke git.
- Selalu gunakan dummy data dan fixture lokal untuk pengembangan.

## Catatan

- `codex-starter` sengaja ringan. Jika nanti butuh workflow yang lebih kaya, tambahkan repo skills, custom agents, atau stack devops secara bertahap.
- Aturan model dan workflow OpenAI/Codex ada di `AGENTS.md` dan `docs/codex-model-strategy.md`.
