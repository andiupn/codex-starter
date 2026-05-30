# LITE vs PRO Comparison — Codex/OpenAI Edition

> Bingung memilih versi mana? Berikut perbandingan fitur lengkap antara edisi LITE (Starter) dan PRO (Premium).

## TL;DR

- **LITE / Starter (Gratis):** Cocok untuk single-project sederhana. Menyertakan 3 core scripts, index memory dasar, lisensi open-source MIT, dan struktur proyek standar.
- **PRO / Premium (Berbayar $1–$5):** Ditujukan untuk pengembang serius, freelancer, dan agensi. Menyertakan 5 specialized agents, 17 universal skills, docker/caddy devops, memory curation tools, dan research archive otomatis.

---

## Feature Matrix

| Fitur | 🆓 LITE (Starter) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Model Routing Defaults** | standard `gpt-5.5` | standard `gpt-5.5` & `gpt-5.4-mini` |
| **Specialized Custom Agents** | ❌ | 3 (`governance-auditor`, `benchmark-verifier`, `repo-researcher`) |
| **Workflow Skills** | ❌ | 5 (`research-archive`, `maintenance-operator`, `memory-curator`, `knowledge-extract`, `git-sync-operator`) |
| **Workspace Structure** | Simple (`src/`, `docs/`) | Status-first Monorepo (`active/`, `staging/`, `archive/`, `shared/`, `devops/`, `artifacts/`) |
| **Devops & Docker (`devops/`)** | ❌ | ✅ (`devops/docker/` local stack template) |
| **Memory Tooling Scripts** | standard | advanced (Memory Curation & Auto-Extract) |
| **Experiments Scaffold** | ❌ | ✅ (`experiments/` benchmark & scaffold) |
| **Lisensi & Dukungan** | MIT License | Proprietary Commercial |
| Redistribution allowed | ✅ | ❌ |
| Komersial (proyek klien & internal) | ✅ | ✅ |
| Dukungan Email | Best-effort (Komunitas) | Best-effort (No SLA - Prioritas Tinggi) |
| Pembaruan Berkelanjutan | Via GitHub | Via kuncimu.com |

---

## When to Choose Which?

### Pilih **LITE (Starter)** jika:
- ✅ Anda baru mulai mempelajari orkestrasi AI Agent menggunakan OpenAI/Codex.
- ✅ Proyek Anda adalah single-project sederhana (1 aplikasi saja).
- ✅ Anda ingin membuat fork komunitas gratis dan open-source.
- ✅ Anda ingin menggunakan memory system dasar secara gratis terlebih dahulu.

### Pilih **PRO (Premium)** jika:
- ✅ Anda mengelola banyak proyek aktif untuk klien atau internal (Agensi / Freelancer).
- ✅ Anda membutuhkan stack ops Docker & Caddy siap pakai.
- ✅ Anda membutuhkan state-management pengetahuan (Riset, Rencana, Memory) yang terintegrasi.
- ✅ Anda ingin meningkatkan kecepatan pengerjaan dengan 17 skills otomasi yang super lengkap.
- ✅ Anda ingin mendukung pemeliharaan berkelanjutan dari proyek ini.

---

## Upgrade Path

Jika Anda sudah menggunakan versi LITE dan ingin beralih ke PRO:

1. Dapatkan lisensi resmi versi PRO di **[kuncimu.com](https://kuncimu.com)**.
2. Unduh berkas repositori `codex-pro`.
3. Pindahkan berkas kode proyek Anda yang sudah ada dari `src/` versi Starter ke direktori `active/web/<nama-proyek>` di versi PRO.
4. Sesuaikan konfigurasi file `AGENTS.md` Anda.

Tidak ada lock-in — Anda dapat kembali ke versi LITE kapan saja secara bebas.

---

## Hubungi Kami

- **Pertanyaan Umum / Masalah:** Silakan buat Issue di GitHub [github.com/andiupn](https://github.com/andiupn).
- **Pertanyaan Pra-Penjualan PRO:** Hubungi kami melalui email di **andi.upn@gmail.com**.

👉 **[Dapatkan Edisi PRO di kuncimu.com](https://kuncimu.com)**
