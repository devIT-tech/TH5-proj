
## Giới thiệu

Dự án này phân tích ảnh hưởng của một **sự thay đổi cấu trúc (structural break)** trong chuỗi thời gian đến mô hình ARIMA, thông qua trường hợp tỷ lệ thất nghiệp hàng tháng tại Hoa Kỳ từ năm 1978 đến 2023.  
Một biến giả mô phỏng sự kiện COVID-19 được đưa vào để kiểm tra xem mô hình mở rộng ARIMAX có phản ánh tốt hơn sự thay đổi cấu trúc này so với ARIMA truyền thống không.

---


## Các bước chính

### 1. Xử lý dữ liệu
- Nguồn: Kaggle - Unemployment Rates by Demographics & Race (1978–2023)
- Làm sạch, chuẩn hóa thời gian, xử lý giá trị thiếu (nội suy tuyến tính).
- Tạo biến `policy_change = 1` từ 03/2020 để mô phỏng ảnh hưởng chính sách sau COVID-19.

### 2. Kiểm định và mô hình hóa
- Sử dụng kiểm định ADF → chuỗi không dừng → lấy sai phân bậc 1.
- Xây dựng:
  - **ARIMA(1,1,1)** trên chuỗi sai phân.
  - **ARIMAX(1,1,1)** với biến `policy_change` làm ngoại sinh.
- So sánh dự báo và các chỉ số AIC, BIC, Log-Likelihood giữa hai mô hình.

### 3. Kết quả

| Chỉ số          | ARIMA       | ARIMAX         |
|-----------------|-------------|----------------|
| Log Likelihood  | 585.729     | **593.422**    |
| AIC             | -1165.419   | **-1178.824**  |
| BIC             | -1152.577   | **-1161.723**  |
| HQIC            | -1160.394   | **-1172.145**  |
| σ² (Phương sai) | 0.0641      | **0.0452**     |

→ ARIMAX cho kết quả tốt hơn rõ rệt khi xét đến sự thay đổi cấu trúc.

---

## Thảo luận & Định hướng mở rộng

### Hạn chế:
- Chưa áp dụng kỹ thuật phát hiện điểm gãy tự động (ruptures, Chow test,...).
- Chỉ dùng một biến giả duy nhất → chưa phản ánh đầy đủ các yếu tố kinh tế khác (GDP, CPI,...).
- Mô hình tuyến tính có thể không mô phỏng tốt các phi tuyến phức tạp trong dữ liệu.

### Hướng phát triển:
- Sử dụng thư viện `ruptures` để xác định điểm gãy chính xác hơn.
- Kết hợp thêm nhiều biến vĩ mô khác.
- So sánh với các mô hình hiện đại như: Facebook Prophet, LSTM, Transformer...

---

##  Hướng dẫn sử dụng
```bash

git clone https://github.com/devIT-tech/TH5-proj.git
cd TH5-proj
