# Codex Model Strategy

## Official Model Names

- `gpt-5.5`
- `gpt-5.4-mini`
- `gpt-5.3-codex`
- `gpt-5-codex`

Gunakan model ID resmi apa adanya di docs, experiment notes, dan benchmark config.

## Recommended Routing

- `gpt-5.5` untuk arsitektur, review, synthesis, dan sebagian besar coding work.
- `gpt-5.4-mini` untuk maintenance, scripted workflows, dan loop hemat biaya.
- `gpt-5.3-codex` untuk benchmark atau implementasi yang memang ingin menguji perilaku Codex-tuned coding.

## Reasoning Guidance

- `low` atau `medium` untuk maintenance
- `medium` untuk sebagian besar implementasi
- `high` untuk debugging sulit atau tradeoff besar
- `xhigh` hanya jika latency dan cost tambahan memang layak

## Reproducibility

- Gunakan alias mengambang untuk kerja harian.
- Pin snapshot untuk benchmark, eval, atau regression tracking.
- Catat model dan reasoning yang dipakai di README eksperimen atau research entry terkait.

## Tooling Notes

- Untuk pertanyaan OpenAI platform, utamakan dokumentasi resmi OpenAI.
- Untuk browser automation, utamakan tool interaktif bila tersedia.
- Jika repo tidak memiliki `.git`, laporkan bahwa verifikasi source control tidak tersedia.

## Source Of Truth

Aturan model tingkat repo hidup di `AGENTS.md` dan dokumen ini. Jika nanti Anda menambah riset atau benchmark model, simpan evidence lengkapnya ke `research/` dan promote ringkasannya hanya bila benar-benar reusable.
