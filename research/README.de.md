# Forschungsarchiv

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <strong>Deutsch</strong> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>


Der Ordner wird mit der Zeit gefüllt, bis die Aufgabe erledigt ist.

## Tujuan

- Sie müssen sich darauf verlassen, dass Ihre Zeit konsistent bleibt
- Memudahkan Agent Mencari Ulang Riset Lama
- Sie können Ihre Erinnerungen an Ihre Kinder und Ihr Leben aufwerten

##Struktur

- `index.json`: Der Katalog wird immer wieder angezeigt
- `entries/<id>/report.md`: Der erste Schritt besteht darin, einen Kommentar abzugeben
- `entries/<id>/sources.json`: Daftar Sumber bis zum nächsten Anstieg

## Der Workflow wird angezeigt

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari Riset Lama mit `./scripts/research-find.py <query>`
3. Ich habe ein neues Update erhalten und es mit `./scripts/research-upsert.py` geteilt.
4. Audit-Struktur mit `python3 scripts/research-health.py`
5. Jika ada Insight Yang Sangat Stabil, promote ringkasannya ke `.codex-memory/`

## Beda-Forschung vs. Gedächtnis

- `research/`: Bis ich mehr als nur ein paar Leute gesehen habe, die ich gelesen habe, und bis jetzt nichts mehr gesagt hat
- `.codex-memory/`: Für den Fall, dass Sie den Benutzer bevorzugen, ein Projekt verwenden oder eine Umgebung mit Einschränkungen verwenden

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