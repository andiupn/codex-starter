# Araştırma Arşivi

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <strong>Türkçe</strong> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>


Klasör, bir görevin yerine getirilmesi için gerekenleri içerir.

## Tujuan

- uygun bir tempoda yükselmek için zaman ayırın
- memudahkan ajan mencari ulang Riset Lama
- yaz aylarında anıların ve hatıraların silinmesi ve tahan lama ile ilgili bilgiler

## Yapı

- `index.json`: katalog ringkas yükselişi
- `entries/<id>/report.md`: ringkasan yükselişi yang siap dibaca ulang
- `entries/<id>/sources.json`: kısa bir süre için yaz tatili

## İş Akışı

1. Jalankan `./scripts/project-health.sh --auto`
2. Cari yükselişi `./scripts/research-find.py <query>`
3. Güncellemeyle ilgili bir güncelleme yapıldı ve `./scripts/research-upsert.py` eklendi
4. `python3 scripts/research-health.py` denetim yapısı
5. İstikrarlı bir içgörü elde edin, `.codex-memory/` ile ringkasannya'yı tanıtın

## Beda araştırması hafızaya karşı

- `research/`: yaz aylarında yükselişe geçti, konteks ve bir kaç gün içinde bir araya geldi
- `.codex-memory/`: kullanıcıyı, projeyi ve kısıtlama ortamını tercih etmek için farklı seçenekler

## Devamını Oku

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