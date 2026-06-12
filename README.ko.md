# 코덱스 스타터 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <strong>한국어</strong> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>기억이 없는 AI는 임시 컨설턴트일 뿐입니다.</strong></h3>
  <p><strong>통합 시드 메모리와 구조화된 연구 보관 기능을 갖춘 OpenAI/Codex를 사용하여 에이전트 안내 작업 공간을 구축하기 위한 가볍고 고도로 구성된 시작 템플릿입니다.</strong></p>

  <p>AI가 채팅 세션 전반에 걸쳐 엔지니어링 결정, 코드 스타일 및 과거 오류를 잊어버리지 않도록 하세요. 지혜가 쌓이는 작업공간을 만들어보세요.</p>
</div>

> 📦 **andiupn**([kuncimu.com](https://kuncimu.com))의 무료 템플릿 · [MIT 라이선스](LICENSE)에 따라 라이선스가 부여됨  
> 😄 도움이 되셨다면 [커피 사주세요](https://ko-fi.com/andiupn) · 🚀 전문적인 모노레포가 필요하신가요? [PRO 버전](https://github.com/sponsors/andiupn?frequency=monthly)을 사용해 보세요.

__배지_0__
__배지_1__
__배지_2__
__배지_3__
__배지_4__
__배지_5__

---

## 💡 문제: "AI 기억상실증"
AI 모델은 매우 유능하지만 채팅 세션 전체에서 완전한 기억 상실증에 시달립니다. 그들은 프로젝트의 사용자 정의 문제점을 잊어버리고 동일한 코딩 오류를 계속해서 반복하여 API 예산과 귀중한 시간을 낭비합니다.

---

## ⚡ 해결책: 지혜가 쌓이는 작업 공간

### 1. 🧠 내장형 시드 메모리 시스템
현지화된 지식 색인을 보유하는 `.codex-memory/`을 갖추고 있습니다. AI 에이전트는 코딩 작업 중에 메모리를 직접 읽고 쓰고 업데이트합니다. 버그를 한 번 해결하면 솔루션이 저장되고 오류가 반복되지 않습니다.

### 📜 2. 재사용 가능한 연구 아카이브
검색 유틸리티 스크립트(`scripts/research-find.py`)가 포함된 구조화된 `research/` 보관 디렉터리입니다. 에이전트가 밀리초 안에 쿼리할 수 있는 검증된 API 및 구조의 저장소를 구축하세요.

### 🛰️ 3. Otonom 상태 및 유지 관리 스크립트
필수 구성 요소는 `./scripts/project-health.sh --auto`을 통해 자동으로 확인 및 확인됩니다. 작업 공간 규칙, 메모리 구문 및 코드 지침을 100% 준수하도록 유지하세요.

---

## 📊 LITE 대 PRO: 프리미엄 업그레이드

`codex-starter`은 매우 가볍도록 설계되었습니다. 전문 및 대행사 규모의 단일 저장소를 조정하려면 다음을 수행하세요.

| 라이트(무료) | 프로($1-5) |
|---|---|
| 표준 gpt-5.5 | gpt-5.5 & gpt-5.4-미니 |
| 맞춤 에이전트 없음 | 3개의 맞춤형 에이전트(거버넌스, 벤치마크 등) |
| 워크플로 기술 없음 | 5가지 프리미엄 스킬(큐레이터, 추출기, git-sync 등) |
| 간단한 구조 | 상태 우선 모노레포(`active/`, `staging/` 등) |
| DevOps 구성 없음 | 재사용 가능한 Docker Compose 로컬 스택 템플릿 |

👉 **[GitHub 스폰서에서 PRO 버전 받기](https://github.com/sponsors/andiupn?frequency=monthly)** · 전체 세부정보: [COMPARISON.md](COMPARISON.md)

---

## 🚀 빠른 시작

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

## 🔒 보안 및 자리표시자

- 이 저장소를 게시하거나 사용하기 전에 **모든 자리 표시자 값을 바꾸세요**.
- `.env.example`에는 샘플 환경 변수가 포함되어 있습니다. **`.env`**에 복사하고 이메일(`andi.upn@gmail.com`)과 실제 자격 증명을 입력하세요.
- `.env`, DB 덤프, 백업 또는 개인 고객 데이터를 Git에 커밋하지 마세요.

---

## 💖 이 프로젝트를 후원하세요(기부)

이 시작 템플릿은 무료이며 오픈 소스입니다. 유지 관리를 지원하기 위해 기부하는 것을 고려해 보세요.
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **트랙터:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **사웨리아:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 라이선스 및 배포

- **라이센스:** MIT 라이센스([LICENSE](LICENSE) 참조 - 저작권 Andi UPN)
- **기여 가이드:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **기부 안내:** [DONATE.md](DONATE.md)