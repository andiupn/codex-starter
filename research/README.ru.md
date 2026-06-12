# Архив исследований

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <strong>Русский</strong> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>


Папка ini menyimpan hasilriset yang bisa dipakai ulang Pada Task berikutnya.

## Туджуань

- меньимпан хасил рисет ке сату темпат ян консистен
- агент мемудакан менкари уланг рисет лама
- мемисахкан рисет бербасис самбер дари память ян сифатня лебих рингкас дан тахан лама

## Структура

- `index.json`: каталог звонков по разным ценам
- `entries/<id>/report.md`: рингкасан рисет ян сиап дибака уланг
- `entries/<id>/sources.json`: дафтар сумбер до конца

## Рабочий процесс ян дисаранкан

1. Джаланкан `./scripts/project-health.sh --auto`
2. Кари рисет лама денган `./scripts/research-find.py <query>`
3. Обновление Jika belum ada atau perlu, просто хасил деньган `./scripts/research-upsert.py`
4. Структура аудита с `python3 scripts/research-health.py`
5. Jika Ada Insight Yang Sangat Stabil, продвигайте Ringkasannya ke `.codex-memory/`

## Исследование Беда против памяти

- `research/`: untuk hasilriset yang masihbutuh sumber, konteks, dan bisa dipakai ulang nanti
- `.codex-memory/`: для отдельных предпочтений пользователя, проекта keputusan, среды ограничений atau

## Конто пенггунаан

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