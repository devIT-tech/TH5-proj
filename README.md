# ICU Forecast using Kalman Filter

## 📝 Giới thiệu  
Dự án này nhằm dự đoán số lượng giường ICU còn trống tại bệnh viện bằng cách áp dụng các mô hình Kalman Filter. Dữ liệu được sử dụng đến từ Kaggle Playground Series - Season 5 Episode 4. Mục tiêu là phân tích chuỗi thời gian, triển khai và đánh giá hiệu suất của nhiều biến thể Kalman Filter.

## 📁 Cấu trúc thư mục  
kalman_icu_forecast/  
├── data/              # Chứa file train.csv, test.csv  
├── notebooks/         # Notebook hoặc script chính để phân tích  
├── src/               # Các mô-đun, hàm, class hỗ trợ  
├── requirements.txt   # Danh sách các thư viện cần thiết  
└── README.md          # Tài liệu mô tả project  

## 🔧 Thiết lập môi trường  
Yêu cầu Python >= 3.7. Cài đặt các thư viện cần thiết bằng:  
pip install -r requirements.txt  

## 🚀 Cách chạy project  
1. Clone repository:  
git clone https://github.com/username/kalman_icu_forecast.git  
cd kalman_icu_forecast  

2. (Tuỳ chọn) Tải dữ liệu từ Kaggle và đặt vào thư mục data/  

3. Mở và chạy notebook phân tích:  
jupyter notebook notebooks/icu_kalman_analysis.ipynb  

## 🔄 Quy trình xử lý  
- Đọc và tiền xử lý dữ liệu (chuyển đổi ngày, xử lý thiếu, tạo đặc trưng)  
- Tách dữ liệu theo yêu cầu bài toán (chỉ giữ ngày Thứ Năm hoặc dùng toàn bộ)  
- Chia tập huấn luyện và kiểm tra  
- Khởi tạo và huấn luyện các mô hình Kalman  
- Dự đoán và đánh giá kết quả (RMSE, MAE)  
- Trực quan hóa kết quả: dữ liệu gốc, trạng thái lọc, và dự đoán  

## 📊 Công cụ và thư viện  
- Python  
- pandas  
- numpy  
- matplotlib  
- scikit-learn  
- statsmodels  
- pykalman (tùy chọn)  

## 📈 Kết quả mong đợi  
- Mô hình Kalman lọc và dự đoán dữ liệu ICU theo thời gian  
- Đánh giá chính xác bằng RMSE, MAE  
- So sánh hiệu suất giữa các biến thể mô hình  

## 📎 Tham khảo  
- Kaggle Playground S5E4  
- Tài liệu Kalman Filter: https://en.wikipedia.org/wiki/Kalman_filter  
- Thư viện pykalman: https://github.com/pykalman/pykalman  

## 📬 Liên hệ  
Mọi thắc mắc hoặc đóng góp xin gửi về email: yourname@example.com hoặc mở issue trên GitHub repo.
