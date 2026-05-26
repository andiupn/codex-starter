# Rules Architecture

Dokumen ini menjelaskan di mana rules agent hidup di repo ini agar perilaku agent tetap kuat tanpa membuat template menjadi berat.

## Goal

Arsitektur rules repo ini mengikuti prinsip:

- source of truth jelas
- perubahan kecil lebih baik dari framework besar yang prematur
- governance kaya, scaffold tetap ringan

## Layer Map

| Area | Source of truth | Isi utama |
|---|---|---|
| Project-wide behavior | `AGENTS.md` | default workflow, guardrails, model routing ringkas |
| Supporting rule docs | `docs/*.md` | penjelasan detail per domain |
| Primitive executors | `scripts/*` | helper CLI yang deterministik |
| Durable compact context | `.codex-memory/` | preferensi, keputusan, constraint, recurring fix |
| Source-backed research | `research/` | hasil riset reusable |
| Experiment artifacts | `experiments/` | benchmark dan workflow test |

## Change Policy

1. Tentukan rumah yang tepat untuk perubahan.
2. Update source of truth paling dekat.
3. Tambah docs pendukung hanya jika detailnya memang terlalu berat untuk `AGENTS.md`.
4. Jika workflow baru benar-benar berulang, pertimbangkan helper script atau skill khusus secara sadar.
5. Jika perubahan menghasilkan insight durable, promote ringkas ke `.codex-memory/`.

## Research And Memory Boundary

- simpan evidence lengkap di `research/`
- simpan hanya meta-insight yang padat ke `.codex-memory/`
- jangan salin hasil riset lengkap ke memory

## Verification

Jika project-level rules, docs rules, repo skills, atau custom agents berubah, verifikasi minimalnya:

```bash
python3 scripts/rules-health.py
./scripts/project-health.sh --auto
```

Tambahkan `python3 scripts/memory-health.py --strict` atau `python3 scripts/research-health.py` jika area itu ikut berubah.
