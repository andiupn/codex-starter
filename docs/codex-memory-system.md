# Codex Memory System

Dokumen ini menjelaskan desain memory internal berbasis file untuk repo template ini.

## Goal

Bangun memory yang:

- bertahan lintas sesi
- murah dalam token
- mudah dicari
- mudah dirawat
- tidak berubah menjadi dump riwayat kerja

## Recommended Design

Gunakan dua lapis:

1. `.codex-memory/index.json`
2. `.codex-memory/entries/*.md`

Index dipakai untuk lookup cepat. File entry dipakai hanya ketika detailnya memang relevan.

## Retrieval Flow

1. Jalankan `./scripts/project-health.sh --auto`
2. Baca `.codex-memory/index.json`
3. Cari entry yang relevan
4. Ambil maksimal 3 entry
5. Baru lanjut ke analisis atau implementasi

## What To Store

- preferensi user yang stabil
- keputusan arsitektur atau workflow
- constraint environment
- recurring bug/fix
- command verifikasi penting

## What Not To Store

- secret
- API key
- log mentah besar
- transcript penuh
- hasil sementara yang cepat basi

## Update Rules

- update memory hanya jika insight-nya reusable
- prefer update entry yang sudah ada daripada membuat duplikat
- jaga summary index tetap pendek
- satu entry sebaiknya mewakili satu topik stabil

## Helper Scripts

```bash
./scripts/project-health.sh --auto
python3 scripts/maintenance-check.py
./scripts/memory-find.py workflow
./scripts/memory-find.py --limit 3 memory rules
python3 scripts/memory-health.py
./scripts/memory-upsert.py --id user-preferences --stable-note "Contoh note baru" --dry-run
```

## Notes

- Jika nanti repo ini berkembang, memory bisa diperluas dengan skill atau workflow tambahan.
- Untuk template starter, memory sengaja dijaga minimal dan generik.
