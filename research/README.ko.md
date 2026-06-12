# 연구자료

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <strong>한국어</strong> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>


폴더 ini menyimpan hasil ridet yang bisa dipakai ulang pada task berikutnya.

## 투후안

- menyimpan hasil ridet ke satu tempat yang konsisten
- 메무다칸 요원 멘카리 울랑 리셋 라마
- memisahkan Riset berbasis sumber dari memory yang sifatnya lebih ringkas dan tahan lama

## 구조

- `index.json`: 카타로그 링카 시뮤아 라이즈
- `entries/<id>/report.md`: 링카산 리제트 양 시프 디바카 울랑
- `entries/<id>/sources.json`: tersebut의 데이터 번호입니다.

## 워크플로우 양 디사란칸

1. 잘란칸 `./scripts/project-health.sh --auto`
2. 카리 리셋 라마 덴간 `./scripts/research-find.py <query>`
3. Jika belum ada atau perlu 업데이트, simpan hasil dengan `./scripts/research-upsert.py`
4. `python3 scripts/research-health.py` 구조 감사
5. Jika ada Insight yang sangat stable, ringkasannya ke `.codex-memory/` 홍보

## 베다 연구 vs 기억

- `research/`: untuk hasil ridet yang masih butuh sumber, konteks, dan bisa dipakai ulang nanti
- `.codex-memory/`: untuk pengetahuan ringkas yang tahan lama seperti 우선 사용자, keputusan 프로젝트, atau 제약 환경

## 콘토 펭구나안

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