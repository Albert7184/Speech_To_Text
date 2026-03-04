import streamlit as st
import os

# ================================
# 🔧 CẤU HÌNH TRANG
# ================================
st.set_page_config(
    page_title="Vietnamese Speech to Text for Meeting Transcription",
    layout="wide"
)

# ================================
# 🎨 HEADER (GIỐNG UI Topic 3)
# ================================
with st.container():
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        
        if os.path.exists("mic.png"):
         st.image("mic.png", width=110)

    with col2:
        st.markdown(
            '''
            <h2 style="text-align:center; color:#2b6f3e;">
                🎙️ Designing and Developing a Vietnamese Speech to Text System
            </h2>
            <h4 style="text-align:center; color:#4b4b4b;">
                Automatic Meeting Transcription (Open-source + Streamlit)
            </h4>
            ''',
            unsafe_allow_html=True
        )

    with col3:
        pass  # Ô bên phải để trống như UI mẫu

st.write("---")

# ================================
# 🧭 SIDEBAR NAVIGATION
# ================================
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to:",
    [
        "Home – Giới thiệu đề tài",
        "Analysis – Phân tích audio & Speech to Text",
        "Training Info – Thông tin mô hình STT",
    ],
)

# ================================
# 📌 ROUTING ĐẾN TRANG TRONG /pages
# ================================
if page.startswith("Home"):
    from pages.Home import show
    show()

elif page.startswith("Analysis"):
    # Bạn sẽ tạo file pages/Analysis.py sau
    from pages.Analysis import show
    show()

elif page.startswith("Training Info"):
    # Bạn sẽ tạo file pages/Training_Info.py sau
    from pages.Training_Info import show
    show()

# ================================
# 📝 FOOTER (GIỐNG UI Topic 3)
# ================================
st.write("---")

st.markdown(
    '''
    <div style="
        padding:18px;
        background:#ffffdd;
        border-radius:10px;
        border:1px solid #e6d784;
        margin-bottom:10px;
    ">
        <b>Students:</b><br>
        - Student : Cao Minh Phu - phucm22@uef.edu.vn<br>
        
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div style="
        padding:18px;
        background:#fafafa;
        border-radius:12px;
        border:1px solid #ddd;
        font-size:16px;
    ">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg"
             width="22"
             style="vertical-align:middle; margin-right:6px;">
        <b>Bùi Tiến Đức</b> –
        <a href="https://orcid.org/0000-0001-5174-3558"
           target="_blank"
           style="text-decoration:none; color:#0073e6;">
           ORCID: 0000-0001-5174-3558
        </a>
    </div>
    ''',
    unsafe_allow_html=True
)
