#コーデックススターター 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <strong>日本語</strong> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>記憶を持たない AI は一時的なコンサルタントにすぎません。</strong></h3>
  <p><strong>OpenAI/Codex を使用してエージェント主導のワークスペースを構築するための、軽量で高度に組織化されたスターター テンプレート。統合されたシード メモリと構造化された研究アーカイブが特徴です。</strong></p>

  <p>チャット セッション全体でエンジニアリング上の決定、コード スタイル、過去のエラーを AI に忘れさせないでください。知恵を蓄積するワークスペースを構築します。</p>
</div>

> 📦 **andiupn** による無料テンプレート ([kuncimu.com](https://kuncimu.com)) · [MIT ライセンス](LICENSE) に基づいてライセンスされています  
> ☕ 役に立ったら、[コーヒーを買ってきてください](https://ko-fi.com/andiupn) · 🚀 専門的なモノリポジトリが必要ですか? [PRO バージョン](https://github.com/sponsors/andiupn?frequency=monthly) をお試しください

__バッジ_0__
__バッジ_1__
__バッジ_2__
__バッジ_3__
__バッジ_4__
__バッジ_5__

---

## 💡 問題: 「AI 健忘症」
AI モデルは非常に有能ですが、チャット セッション中に完全な記憶喪失に悩まされます。彼らはプロジェクトのカスタム注意点を忘れ、同じコーディングエラーを何度も繰り返し、API 予算と貴重な時間を無駄にします。

---

## ⚡ 解決策: 知恵を蓄積するワークスペース

### 1. 🧠 内蔵シードメモリーシステム
ローカライズされたナレッジインデックスを保持する`.codex-memory/`を搭載。 AI エージェントは、コーディング タスク中にメモリを直接読み取り、書き込み、更新します。バグを一度解決すると、その解決策が保存され、エラーが繰り返されることはありません。

### 📜 2. 再利用可能な研究アーカイブ
検索ユーティリティ スクリプト (`scripts/research-find.py`) を含む構造化された `research/` アーカイブ ディレクトリ。エージェントがミリ秒単位でクエリできる、検証済みの API と構造のリポジトリを構築します。

### 🛰️ 3.otonom ヘルス & メンテナンス スクリプト
前提条件は `./scripts/project-health.sh --auto` 経由で自動的にチェックおよび検証されます。ワークスペースのルール、メモリ構文、コード ガイドラインに 100% 準拠した状態を保ちます。

---

## 📊 LITE vs PRO: プレミアムアップグレード

`codex-starter` は非常に軽量になるように設計されています。プロフェッショナルおよび代理店規模のモノリポジトリをオーケストレーションする場合:

|ライト（無料） |プロ (1 ～ 5 ドル) |
|---|---|
|標準 gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
|カスタムエージェントなし | 3 カスタム エージェント (ガバナンス、ベンチマークなど) |
|ワークフロースキルなし | 5 つのプレミアム スキル (キュレーター、エクストラクター、git-sync など) |
|シンプルな構造 |ステータス優先のモノリポジトリ (`active/`、`staging/` など) |
| DevOps 構成がありません |再利用可能な Docker Compose ローカル スタック テンプレート |

👉 **[GitHub スポンサーで PRO エディションを入手](https://github.com/sponsors/andiupn?frequency=monthly)** · 詳細: [COMPARISON.md](COMPARISON.md)

---

## 🚀 クイックスタート

```bash
# Run local repository and environment health checks
./scripts/project-health.sh --auto

# Validate rules and configuration syntax
python3 scripts/rules-health.py
python3 scripts/memory-health.py
python3 scripts/research-health.py

# Search inside local memory and research index
./scripts/memory-find.py workflow
./scripts/research-find.py model
```

---

## 🔒 セキュリティとプレースホルダー

- このリポジトリを公開または使用する前に、**すべてのプレースホルダー値を置き換えてください**。
- `.env.example` にはサンプル環境変数が含まれています。 **これを `.env`** にコピーし、電子メール (`andi.upn@gmail.com`) と実際の資格情報を入力します。
- `.env`、DB ダンプ、バックアップ、またはプライベート顧客データを Git にコミットしないでください。

---

## 💖 このプロジェクトをサポートする (寄付)

このスターター テンプレートは無料でオープンソースです。メンテナンスをサポートするために寄付を検討してください。
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **サウェリア:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 ライセンスと配布

- **ライセンス:** MIT ライセンス ([ライセンス](LICENSE) を参照 - 著作権 Andi UPN)
- **貢献ガイド:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **寄付ガイド:** [DONATE.md](DONATE.md)