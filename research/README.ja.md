# 研究アーカイブ

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <strong>日本語</strong> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>


フォルダーは、ヤン ビサ ディパカイ ウラン パダ タスク ベリクトニャを開始します。

## トゥジュアン

- メニュインパン・ハシル・リセット・ケ・サトゥ・テンパット・ヤン・コンシステン
- メムダカン エージェント メンカリ ウラン リセット ラマ
- メミサカン・リセット・ベルバシス・サンバー・ダリ・メモリー・ヤン・シファトニャ・レビ・リンカス・ダン・タハン・ラマ

## ストラクトゥール

- `index.json`: カタログリングカスセムアライズト
- `entries/<id>/report.md`: リングカサン リセット ヤン シアップ ディバカ ウラン
- `entries/<id>/sources.json`: 夏のことは忘れないでください

## ワークフロー ヤン ディサランカン

1.じゃらんかん `./scripts/project-health.sh --auto`
2. カリ・リゼット・ラマ・デンガン `./scripts/research-find.py <query>`
3. ジカ・ベラム・アダ・アタウ・ペルル更新、シンパン・ハシル・デンガン `./scripts/research-upsert.py`
4. 監査ストラクトゥルデンガン `python3 scripts/research-health.py`
5. ジカ・アダ・インサイト・ヤン・サンガット・スタビル、リングカサンニャ・ケ `.codex-memory/` を促進する

## Beda の研究と記憶

- `research/`: ウントゥク・ハシル・リセット・ヤン・マシ・ブトゥ・スンバー、コンテクス、ダン・ビサ・ディパカイ・ウラン・ナンティ
- `.codex-memory/`: ユーザー、ケプトゥサン プロジェクト、アタウ制約環境を優先するペンゲタフアン リングカス ヤン タハン ラマ セペルティを選択してください

## コントー・ペングナーン

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