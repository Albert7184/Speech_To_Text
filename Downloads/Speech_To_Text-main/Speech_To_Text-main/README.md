Vietnamese Speech to Text System for Meeting Transcription

Dự án này tập trung vào việc thiết kế và phát triển hệ thống chuyển đổi giọng nói tiếng Việt thành văn bản, ứng dụng đặc biệt cho việc ghi chép biên bản cuộc họp tự động. Hệ thống sử dụng mô hình OpenAI Whisper kết hợp với giao diện Streamlit để mang lại trải nghiệm người dùng tối ưu.

📂 Cấu trúc thư mục (Project Structure)Việc tổ chức tệp tin được phân chia rõ ràng theo từng chức năng:PlaintextSpeech_To_Text-main/
├── app.py              # File chạy chính, cấu hình giao diện và điều hướng 
├── requirements.txt    # Danh sách thư viện Python cần cài đặt
├── packages.txt        # Danh sách các gói hệ thống (ffmpeg)
├── rose.png            # Logo hiển thị trên Header 
├── demo.mp3            # File âm thanh mẫu để kiểm thử [cite: 2]
├── pages/              # Thư mục chứa các trang chức năng 
│   ├── Home.py         # Trang giới thiệu đề tài 
│   ├── Analysis.py     # Trang phân tích Audio và Speech-to-Text 
│   └── Training_Info.py# Trang thông tin thông số mô hình 
└── assets/             # Chứa tài nguyên hình ảnh bổ sung

🛠️ Hướng dẫn cài đặt (Installation)Để chạy dự án này dưới máy cục bộ (Local), bạn hãy thực hiện các bước sau:
1. Yêu cầu hệ thốngPython: Phiên bản 3.8 trở lên.FFmpeg: Cần thiết để xử lý các định dạng âm thanh như .mp3.
2. Cài đặt thư việnMở Terminal tại thư mục project và chạy lệnh sau để cài đặt các "nguyên liệu" cần thiết:Bashpip install -r requirements.txt
Các thư viện chính bao gồm: streamlit, openai-whisper, torch, librosa, soundfile, matplotlib, numpy.

Cách khởi chạy ứng dụng (Usage)Sau khi cài đặt thành công, bạn thực hiện lệnh sau để mở giao diện người dùng:streamlit run app.py

Khi ứng dụng khởi động, bạn có thể:Chuyển đổi trang: Sử dụng thanh điều hướng (Sidebar) để chuyển giữa các trang Home, Analysis và Training Info. Phân tích Audio: Tại trang Analysis, bạn có thể tải lên file âm thanh hoặc dùng file demo.mp3 có sẵn để hệ thống thực hiện chuyển đổi sang văn bản.Xem kết quả: Văn bản sẽ được hiển thị ngay trên giao diện cùng với các biểu đồ phân tích âm thanh.✨ Công nghệ sử dụng (Tech Stack)Giao diện: Streamlit.Mô hình nhận diện: OpenAI Whisper.Xử lý âm thanh: Librosa, Soundfile.Tính toán & Đồ thị: Numpy, Matplotlib, Torch.

👥 Đội ngũ thực hiện
Giảng viên hướng dẫn: Bùi Tiến Đức (ORCID: 0000-0001-5174-3558).
Sinh viên thực hiện: Cao Minh Phú (phucm22@uef.edu.vn).