# RSS STORE APTAC - Máy Tính Tài Nguyên

**[Español](README_es.md) | [English](README_en.md) | [Português](README_pt.md) | Tiếng Việt | [Bahasa Indonesia](README_id.md) | [Français](README_fr.md)**

---

## 📱 RSS STORE APTAC là gì?

Ứng dụng máy tính để tự động trích xuất tài nguyên vương quốc từ ảnh chụp màn hình bằng công nghệ OCR với quản lý tài khoản thông minh.

## ✨ Tính Năng

- ✅ Trích xuất tài nguyên tự động với OCR
- 🎯 Giao diện đa ngôn ngữ (6 ngôn ngữ được hỗ trợ)
- 🔄 Cập nhật tự động từ GitHub
- 📊 Xử lý hàng loạt (lên đến 100 hình ảnh)
- 💾 Xuất sang tệp TXT/CSV
- 🌍 Tất cả các tin nhắn tôn trọng ngôn ngữ bạn chọn

## 🚀 Cài Đặt Nhanh

1. Tải `RSS_STORE_APTAC_Installer.exe` từ [Releases](https://github.com/Aptac0/Resource-Calculator/releases)
2. Chạy trình cài đặt
3. Xong! Ứng dụng sẽ tự động cập nhật khi có phiên bản mới

## 📖 Hướng Dẫn Người Dùng

### Quy Trình Nhanh

1. **Mở ứng dụng:** Chạy `RSS STORE APTAC.exe`
2. **Thêm hình ảnh:** Nhấp vào "Thêm Hình Ảnh" và chọn ảnh chụp màn hình của bạn
3. **Chọn vương quốc:** Chọn vương quốc thích hợp từ thực đơn thả xuống
4. **Cấu hình số:**
   - `Số bắt đầu`: Số tài khoản đầu tiên (ví dụ: 1)
   - `Số kết thúc`: Số tài khoản cuối cùng (ví dụ: 30)
   - `Số bị chặn`: (tùy chọn) Số cần bỏ qua (ví dụ: 3,5,7)
5. **Đặt cấp độ:** Chọn "Cấp Thành Phố" và "Cấp Kho" (1-25)
6. **Xử lý:** Nhấp vào nút tài nguyên bạn cần

### Cách Chụp Ảnh Màn Hình

#### Từ PC (Khuyên dùng)
- Mở trò chơi ở chế độ cửa sổ
- Chụp ảnh màn hình rõ ràng của cửa sổ Tài Nguyên
- Đảm bảo số và nhãn có thể đọc được

![Ảnh chụp từ PC](../Ejemplos/Foto-desde-PC.png)

#### Từ Điện Thoại Di Động
- Chuyển hình ảnh sang PC (USB, Google Drive, v.v.)
- Tránh ảnh bị nghiêng hoặc mờ
- Đảm bảo hình ảnh sắc nét

![Ảnh chụp từ Điện Thoại](../Ejemplos/Foto-desde-Movil.png)

### Định Dạng Đầu Vào

#### Số Bắt Đầu và Kết Thúc
- Chỉ những con số (ví dụ: `1` và `30`)
- Phải là số nguyên dương hợp lệ

#### Số Bị Chặn (Tùy chọn)
Hai định dạng có sẵn:
- **Phạm vi:** `1-10` (tất cả các số từ 1 đến 10)
- **Danh sách:** `1,3,5,7` (những con số cụ thể)
- **Hỗn hợp:** `1-5,8,10-15`

**Ví dụ:**
- `bắt đầu=1`, `kết thúc=10`, `bị chặn=3,5` → xử lý: 1,2,4,6,7,8,9,10
- Ứng dụng xác thực bạn có đủ hình ảnh

#### Cấp Độ
- `Cấp Thành Phố` (Thị Trường): 1-25
- `Cấp Kho` (Lưu Trữ): 1-25

![Cấp Thị Trường](../Ejemplos/Niveles-Puesto-de-Venta.png)
![Cấp Kho](../Ejemplos/Niveles-de-Almacen.png)

## 🔄 Hệ Thống Cập Nhật

### Tự Động
Ứng dụng kiểm tra phiên bản mới khi khởi động. Nếu được tìm thấy:
- Bạn sẽ nhận được thông báo
- Tải xuống trực tiếp từ ứng dụng
- Cài đặt tự động

### Thủ Công
Chạy `actualizar.bat` từ thư mục cài đặt

## 💾 Kết Quả và Tệp Đã Lưu

### Vị Trí Tệp

```
GUARDADOS/
├── REINO_results_20260602_143022.txt
├── REINO_results_20260602_145015.txt
└── REINO_results_20260603_101530.txt
```

### Định Dạng Tệp

```
Nickname: Account_1
Cấp Thành Phố: 15
Cấp Kho: 18
Thức phẩm: 45.0K
Gỗ: 32.5K
Đá: 28.7K
Vàng: 5.6K
---
Nickname: Account_2
Cấp Thành Phố: 15
Cấp Kho: 18
Thức phẩm: 41.2K
Gỗ: 35.1K
Đá: 26.8K
Vàng: 6.1K
---
```

### Cách Sử Dụng Kết Quả

1. Mở tệp `.txt` trong trình chỉnh sửa
2. Sao chép dữ liệu bạn cần
3. Dán vào công cụ quản lý của bạn
4. Tên gợi ý được tạo tự động

---
