import streamlit as st

def show():
    # --- CSS CHO TRANG HOME ---
    st.markdown("""
    <style>
        .hero-title {
            font-size: 42px;
            font-weight: 700;
            color: #202124;
            margin-bottom: 10px;
        }
        .hero-subtitle {
            font-size: 20px;
            color: #5f6368;
            margin-bottom: 30px;
        }
        .feature-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            text-align: center;
            height: 100%;
            border: 1px solid #f1f3f4;
        }
        .feature-icon {
            font-size: 30px;
            margin-bottom: 15px;
            color: #1a73e8;
        }
    </style>
    """, unsafe_allow_html=True)

    # --- HERO SECTION (BANNER) ---
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True) # Spacer
        st.markdown('<div class="hero-title">Biến giọng nói thành văn bản<br>trong tích tắc.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">Hệ thống AI nhận dạng giọng nói tiếng Việt chuyên sâu, hỗ trợ bóc tách biên bản cuộc họp tự động với độ chính xác cao.</div>', unsafe_allow_html=True)
        
        # Nút Call to Action giả lập (Chỉ dẫn người dùng)
        st.info("👈 Chọn **'Công cụ xử lý'** ở menu bên trái để bắt đầu ngay!")

    with col2:
        # Bạn có thể để ảnh minh họa project ở đây
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <img src="https://cdn-icons-png.flaticon.com/512/3029/3029337.png" width="200" style="opacity: 0.8;">
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # --- FEATURES SECTION (TÍNH NĂNG) ---
    st.markdown("### 🚀 Tại sao chọn VietScribe?")
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <h4>Tốc độ xử lý cao</h4>
            <p style="color: #5f6368;">Sử dụng mô hình Whisper tối ưu hóa, xử lý file âm thanh dài chỉ trong vài giây.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h4>Độ chính xác 98%</h4>
            <p style="color: #5f6368;">Nhận diện tốt tiếng Việt đa vùng miền, tự động thêm dấu câu và ngắt đoạn.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <h4>Bảo mật tuyệt đối</h4>
            <p style="color: #5f6368;">Dữ liệu được xử lý cục bộ và mã hóa, đảm bảo an toàn thông tin cuộc họp.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # --- TEAM SECTION ---
    st.markdown("### 👥 Đội ngũ phát triển")
    st.markdown("""
    **Giảng viên hướng dẫn:** Bùi Tiến Đức (ORCID: 0000-0001-5174-3558)
    
    **Sinh viên thực hiện:**
    * Cao Minh Phu
    """)