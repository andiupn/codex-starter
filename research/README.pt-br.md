# Arquivo de Pesquisa

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <strong>Português (BR)</strong> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>


A pasta ini menyimpan hasil riset yang bisa dipakai ulang pada task berikutnya.

##Tujuan

- menyimpan hasil riset ke satu tempat yang konsisten
- memudahkan agente mencari ulang riset lama
- memisahkan riset berbasis sumber dari memory yang sifatnya lebih ringkas dan tahan lama

## Estrutura

- `index.json`: catálogo ringkas semua riset
- `entries/<id>/report.md`: ringkasan riset yang siap dibaca ulang
- `entries/<id>/sources.json`: daftar sumber untuk riset tersebut

## Fluxo de trabalho que está sendo resolvido

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari riset lama com `./scripts/research-find.py <query>`
3. Se for uma atualização ou uma atualização, simpan hasil com `./scripts/research-upsert.py`
4. Estrutura de auditoria com `python3 scripts/research-health.py`
5. Jika ada insight yang sangat stabil, promova ringkasannya ke `.codex-memory/`

## Pesquisa Beda vs memória

- `research/`: para hasil riset yang masih butuh sumber, konteks, dan bisa dipakai ulang nanti
- `.codex-memory/`: para que você possa escolher o que deseja usar como usuário preferido, projeto de implementação ou ambiente de restrição

## Contoh penggunaan

```bash
./scripts/research-find.py openai skills memory

./scripts/research-upsert.py \
  --title "Codex skills versus memory" \
  --question "Apakah sistem skill perlu dipakai selain memory?" \
  --summary "Skills cocok untuk workflow yang berulang, memory cocok untuk context tahan lama." \
  --tag openai,codex,skills,memory \
  --keyword "skills,memory,research workflow" \
  --finding "Skills menambahkan capability dan workflow khusus." \
  --finding "Memory lebih cocok untuk context ringkas yang akumulatif." \
  --reuse-note "Gunakan skill untuk workflow riset atau task berulang." \
  --source "OpenAI Docs | https://developers.openai.com/codex/skills | Dokumentasi resmi skills Codex"

python3 scripts/research-health.py
```