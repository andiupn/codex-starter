#Bộ khởi đầu Codex 🧠

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <strong>Tiếng Việt</strong> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  __HTML_41_<strong>AI không có bộ nhớ chỉ là nhà tư vấn tạm thời.</strong></h3>
  <p><strong>Một mẫu khởi đầu gọn nhẹ, có tính tổ chức cao để xây dựng không gian làm việc được hướng dẫn bởi tác nhân với OpenAI/Codex, có bộ nhớ gốc tích hợp và lưu trữ nghiên cứu có cấu trúc.</strong></p>

  <p>Đừng để AI quên các quyết định kỹ thuật, kiểu mã và lỗi trong quá khứ của bạn trong các phiên trò chuyện. Xây dựng không gian làm việc tích lũy trí tuệ.</p>
</div>

> 📦 Mẫu miễn phí của **andiupn** ([kuncimu.com](https://kuncimu.com)) · Được cấp phép theo [Giấy phép MIT](LICENSE)  
> ☕ Nếu hữu ích, [mua cho tôi một ly cà phê](https://ko-fi.com/andiupn) · 🚀 Cần monorepos chuyên nghiệp? Hãy thử [phiên bản PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/codex-starter)](https://github.com/andiupn/codex-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Vấn đề: Chứng mất trí nhớ AI
Các mô hình AI cực kỳ có khả năng nhưng chúng bị mất trí nhớ hoàn toàn trong các phiên trò chuyện. Họ quên các vấn đề tùy chỉnh của dự án của bạn, lặp đi lặp lại các lỗi mã hóa giống nhau, lãng phí ngân sách API và thời gian quý báu của bạn.

---

## ⚡ Giải pháp: Không gian làm việc tích lũy trí tuệ

### 1. 🧠 Hệ thống bộ nhớ hạt giống tích hợp
Được trang bị `.codex-memory/` chứa các chỉ mục kiến thức đã bản địa hóa. Tác nhân AI đọc, ghi và cập nhật bộ nhớ của nó trực tiếp trong các tác vụ mã hóa của bạn. Nếu nó giải quyết được lỗi một lần, nó sẽ lưu trữ giải pháp và không bao giờ lặp lại lỗi đó.

### 📜 2. Lưu trữ nghiên cứu có thể tái sử dụng
Thư mục lưu trữ có cấu trúc `research/` với các tập lệnh tiện ích tìm kiếm (`scripts/research-find.py`). Xây dựng kho lưu trữ các cấu trúc và API đã được xác minh mà tổng đài viên có thể truy vấn trong một phần nghìn giây.

### 🛰️ 3. Tập lệnh bảo trì & sức khỏe Otonom
Các điều kiện tiên quyết được kiểm tra và xác minh tự động qua `./scripts/project-health.sh --auto`. Giữ các quy tắc không gian làm việc, cú pháp bộ nhớ và nguyên tắc mã của bạn tuân thủ 100%.

---

## 📊 LITE vs PRO: Bản nâng cấp cao cấp

`codex-starter` được thiết kế cực kỳ nhẹ. Để điều phối các monorepos chuyên nghiệp và quy mô đại lý:

| LITE (Miễn phí) | CHUYÊN NGHIỆP ($1-5) |
|---|---|
| Chuẩn gpt-5.5 | gpt-5.5 & gpt-5.4-mini |
| Không có đại lý tùy chỉnh | 3 Đại lý tùy chỉnh (quản trị, điểm chuẩn, v.v.) |
| Không có kỹ năng về quy trình làm việc | 5 Kỹ năng cao cấp (người quản lý, người trích xuất, git-sync, v.v.) |
| Cấu trúc đơn giản | Monorepo trạng thái đầu tiên (`active/`, `staging/`, v.v.) |
| Không có cấu hình DevOps | Docker có thể tái sử dụng Soạn mẫu ngăn xếp cục bộ |

👉 **[Nhận phiên bản PRO trên Nhà tài trợ GitHub](https://github.com/sponsors/andiupn?frequency=monthly)** · Chi tiết đầy đủ: [COMPARISON.md](COMPARISON.md)

---

## 🚀 Bắt đầu nhanh

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

## 🔒 Bảo mật & Trình giữ chỗ

- **THAY THẾ tất cả các giá trị giữ chỗ** trước khi xuất bản hoặc sử dụng kho lưu trữ này.
- `.env.example` chứa các biến môi trường mẫu. **Sao chép nó vào `.env`** và điền email của bạn (`andi.upn@gmail.com`) và thông tin xác thực thực tế.
- KHÔNG cam kết `.env`, kết xuất DB, sao lưu hoặc dữ liệu khách hàng riêng tư với Git.

---

## 💖 Hỗ trợ dự án này (Quyên góp)

Mẫu khởi đầu này là miễn phí và có nguồn mở. Xem xét quyên góp để hỗ trợ bảo trì:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Giấy phép & Phân phối

- **Giấy phép:** Giấy phép MIT (xem [LICENSE](LICENSE) - Copyright Andi UPN)
- **Hướng dẫn đóng góp:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Hướng dẫn quyên góp:** [DONATE.md](DONATE.md)