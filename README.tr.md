# Kodeks Başlatıcı 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <strong>Türkçe</strong> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>Belleği olmayan bir yapay zeka yalnızca geçici bir danışmandır.</strong></h3>
  <p><strong>OpenAI/Codex ile aracı yönlendirmeli çalışma alanları oluşturmak için entegre çekirdek hafıza ve yapılandırılmış araştırma arşivleme özelliklerine sahip, hafif, üst düzeyde organize edilmiş bir başlangıç şablonu.</strong></p>

  <p>Sohbet oturumlarında yapay zekanın mühendislik kararlarınızı, kod stillerinizi ve geçmiş hatalarınızı unutmasına izin vermeyin. Bilgelik biriktiren bir çalışma alanı oluşturun.</p>
</div>

> 📦 **andiupn** ([kuncimu.com](https://kuncimu.com)) tarafından hazırlanan ücretsiz şablon · [MIT Lisansı](LICENSE) kapsamında lisanslıdır  
> ☕ Yararlıysa, [bana bir kahve al](https://ko-fi.com/andiupn) · 🚀 Profesyonel monorepolara mı ihtiyacınız var? [PRO sürümünü] deneyin(https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Sorun: "Yapay Zeka Amnezisi"
Yapay zeka modelleri son derece yeteneklidir ancak sohbet oturumlarında tamamen hafıza kaybı yaşarlar. Projenizin özel sorunlarını unutuyorlar, aynı kodlama hatalarını defalarca tekrarlıyorlar, API bütçenizi ve değerli zamanınızı boşa harcıyorlar.

---

## ⚡ Çözüm: Bilgelik Biriktiren Çalışma Alanı

### 1. 🧠 Dahili Tohum Hafıza Sistemi
Yerelleştirilmiş bilgi dizinlerini barındıran `.codex-memory/` ile donatılmıştır. AI aracısı, kodlama görevleriniz sırasında belleğini doğrudan okur, yazar ve günceller. Bir hatayı bir kez çözerse çözümü saklar ve hatayı bir daha tekrarlamaz.

### 📜 2. Yeniden Kullanılabilir Araştırma Arşivi
Arama yardımcı program komut dosyalarını (`scripts/research-find.py`) içeren yapılandırılmış bir `research/` arşivleme dizini. Aracıların milisaniyeler içinde sorgulayabileceği doğrulanmış API'lerden ve yapılardan oluşan bir depo oluşturun.

### 🛰️ 3. Otonom Sağlık ve Bakım Komut Dosyaları
Önkoşullar `./scripts/project-health.sh --auto` aracılığıyla otomatik olarak kontrol edilir ve doğrulanır. Çalışma alanı kurallarınızı, bellek sözdiziminizi ve kod yönergelerinizi %100 uyumlu tutun.

---

## 📊 LITE ve PRO: Premium Yükseltmesi

`codex-starter` son derece hafif olacak şekilde tasarlanmıştır. Profesyonel ve ajans ölçeğinde monorepoları düzenlemek için:

| LITE (Ücretsiz) | PRO (1-5$) |
|---|---|
| Standart gpt-5.5 | gpt-5.5 ve gpt-5.4-mini |
| Özel Temsilci Yok | 3 Özel Aracılar (yönetim, kıyaslama vb.) |
| İş Akışı Becerisi Yok | 5 Premium Beceri (küratör, çıkarıcı, git-sync, vb.) |
| Basit yapı | Durum-önce Monorepo (`active/`, `staging/`, vb.) |
| DevOps Yapılandırması Yok | Yeniden Kullanılabilir Docker Yerel yığın şablonu oluşturun |

👉 **[GitHub Sponsorlarından PRO Sürümünü Alın](https://github.com/sponsors/andiupn?frequency=monthly)** · Tüm ayrıntılar: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Hızlı Başlangıç

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

## 🔒 Güvenlik ve Yer Tutucular

- **Bu depoyu yayınlamadan veya kullanmadan önce tüm yer tutucu değerlerini DEĞİŞTİRİN**.
- `.env.example` örnek ortam değişkenlerini içerir. **`.env`** adresine kopyalayın ve e-postanızı (`andi.upn@gmail.com`) ve gerçek kimlik bilgilerinizi girin.
- `.env`, veritabanı dökümleri, yedeklemeler veya özel müşteri verilerini Git'e taahhüt ETMEYİN.

---

## 💖 Bu Projeyi Destekleyin (Bağışlar)

Bu başlangıç şablonu ücretsiz ve açık kaynaklıdır. Bakımını desteklemek için bağış yapmayı düşünün:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Lisans ve Dağıtım

- **Lisans:** MIT Lisansı (bkz. [LİSANS](LICENSE) - Telif Hakkı Andi UPN)
- **Katkıda Bulunma Kılavuzu:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Bağış Kılavuzu:** [DONATE.md](DONATE.md)