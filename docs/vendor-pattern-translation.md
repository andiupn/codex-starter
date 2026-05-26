# Vendor Pattern Translation

Dokumen ini menjelaskan bagaimana pola dari workspace Claude, Gemini, atau vendor agent lain diterjemahkan ke workflow yang native untuk repo Codex ini.

## Goal

Ambil pola yang reusable tanpa menyalin mekanisme vendor-specific yang tidak map dengan baik ke OpenAI Codex atau ChatGPT tool workflows.

## Translation Matrix

| Vendor pattern | Terjemahan di repo ini | Catatan |
|---|---|---|
| `CLAUDE.md`, `GEMINI.md` | `AGENTS.md` + docs pendukung di `docs/` | aturan inti tetap di satu file utama; detail dipindah ke docs kecil |
| `.claude/skills/`, `.gemini/skills/` | `.agents/skills/` | hanya untuk workflow repo yang benar-benar berulang |
| `.claude/agents/*.md` atau agent manifest vendor lain | `.codex/agents/*.toml` | hanya untuk role delegasi yang eksplisit dan bounded |
| `active/`, `archive/`, `shared/`, `staging/`, `templates/` workspace sibling | sistem lifecycle app/project yang sama di repo ini | dipakai untuk app/project nyata, bukan untuk mengganti `experiments/` atau `devops/` |
| vendor memory folders | `.codex-memory/` | memory tetap ringkas, indexed, dan hemat token |
| vendor wiki atau knowledge base besar | `research/` + `.codex-memory/` | research untuk findings berbasis sumber; memory untuk meta-insight padat |
| slash command seperti `/plan-new`, `/rules-maintenance` | skill repo yang kecil atau direct tool workflow | jangan copy syntax slash command jika tidak perlu |
| `@agent`, `invoke_agent`, atau routing UI-specific | sub-agent Codex yang eksplisit dan bounded | hanya dipakai jika user memang minta delegasi atau task-nya cocok |
| MCP/tool name vendor-specific | capability-level guidance | dokumentasikan kemampuan, bukan nama tool vendor lain |
| workspace megadoc dan permission handbook | docs kecil per domain + helper scripts | jaga repo ini tetap ringan dan mudah dirawat |

## Portable Patterns Worth Adopting

Pola yang cocok untuk repo ini:

- audit parity rules dan docs
- comparative research antar repo agent
- knowledge extraction yang selective
- fallback browser/UI verification dengan script lokal
- benchmark rules-awareness lintas model

## Patterns To Avoid Copying Directly

Hal yang tidak sebaiknya disalin mentah:

- folder `.claude/` atau `.gemini/` sebagai struktur utama repo ini
- syntax slash commands vendor sebagai source of truth
- permission matrix yang hanya relevan untuk CLI vendor tertentu
- auto-memory convention yang bergantung pada runtime vendor
- registry agent/skill besar jika repo ini belum punya kebutuhan nyata

## Adoption Checklist

Sebelum mengadopsi pola dari repo lain, cek:

1. Apakah pola ini menyelesaikan masalah nyata di repo ini?
2. Apakah bisa diterjemahkan ke tool dan workflow Codex yang sudah ada?
3. Apakah bentuk paling kecilnya cukup, tanpa menyalin scaffolding besar?
4. Apakah hasilnya bisa diverifikasi dengan script atau benchmark yang jelas?

Jika jawaban untuk salah satu poin di atas tidak jelas, simpan dulu sebagai research atau roadmap, bukan langsung jadi rule permanen.
