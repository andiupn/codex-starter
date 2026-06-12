# 法典入门🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <strong>简体中文</strong> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>没有记忆的人工智能只是一个临时顾问。</strong></h3>
  <p><strong>轻量级、高度组织化的入门模板，用于使用 OpenAI/Codex 构建代理引导的工作区，具有集成种子内存和结构化研究归档功能。</strong></p>

  <p>不要让人工智能忘记您的工程决策、代码风格和聊天会话中过去的错误。打造一个积累智慧的工作空间.</p>
</div>

> 📦 **andiupn** 提供的免费模板 ([kuncimu.com](https://kuncimu.com)) · 根据 [MIT 许可证](LICENSE) 获得许可  
> ☕ 如果有用，[请我喝杯咖啡](https://ko-fi.com/andiupn) · 🚀 需要专业的 monorepos？尝试[专业版](https://github.com/sponsors/andiupn?frequency=monthly)

__徽章_0__
__徽章_1__
__徽章_2__
__徽章_3__
__徽章_4__
__徽章_5__

---

## 💡 问题：“人工智能失忆症”
人工智能模型非常有能力，但它们在聊天过程中完全失忆。他们忘记了您项目的自定义陷阱，一遍又一遍地重复相同的编码错误，浪费了您的 API 预算和宝贵的时间。

---

## ⚡ 解决方案：积累智慧的工作空间

### 1. 🧠 内置种子记忆系统
配备保存本地化知识索引的`.codex-memory/`。 AI 代理在您的编码任务期间直接读取、写入和更新其内存。如果它解决了一次错误，它就会存储解决方案并且永远不会重复该错误。

### 📜 2.可重复使用的研究档案
带有搜索实用程序脚本 (`scripts/research-find.py`) 的结构化 `research/` 归档目录。构建经过验证的 API 和结构的存储库，代理可以在几毫秒内查询。

### 🛰️ 3. Otonom 健康和维护脚本
通过 `./scripts/project-health.sh --auto` 自动检查和验证先决条件。确保您的工作区规则、内存语法和代码指南 100% 合规。

---

## 📊 LITE 与 PRO：高级升级

`codex-starter` 被设计得极其轻量。对于编排专业和机构规模的单一存储库：

|精简版（免费）|专业版 ($1-5) |
|---|---|
|标准gpt-5.5 | gpt-5.5 和 gpt-5.4-mini |
|无定制代理| 3 个自定义代理（治理、基准等）|
|没有工作流程技能 | 5 项高级技能（curator、extractor、git-sync 等）|
|结构简单|状态优先 Monorepo（`active/`、`staging/` 等）|
|没有 DevOps 配置 |可重用的 Docker Compose 本地堆栈模板 |

👉 **[在 GitHub 赞助商上获取专业版](https://github.com/sponsors/andiupn?frequency=monthly)** · 完整详细信息：[COMPARISON.md](COMPARISON.md)

---

## 🚀 快速入门

__代码_块_0__

---

## 🔒 安全性和占位符

- **在发布或使用此存储库之前替换所有占位符值**。
- `.env.example` 包含示例环境变量。 **将其复制到 `.env`** 并填写您的电子邮件 (`andi.upn@gmail.com`) 和实际凭据。
- 不要将 `.env`、数据库转储、备份或私人客户数据提交到 Git。

---

## 💖 支持这个项目（捐款）

该入门模板是免费且开源的。考虑捐赠以支持其维护：
- **Ko-fi：** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon：** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer：** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria：** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 许可和分发

- **许可证：** MIT 许可证（请参阅 [许可证](LICENSE) - 版权所有 Andi UPN）
- **贡献指南：** [CONTRIBUTING.md](CONTRIBUTING.md)
- **捐赠指南：** [DONATE.md](DONATE.md)