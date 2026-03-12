import streamlit as st
import os
from streamlit_option_menu import option_menu
# Import các trang con
import home
import user_dashboard
import admin_dashboard
# Import database để khởi tạo
import database

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="VietScribe AI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- KHỞI TẠO DB NGAY KHI CHẠY APP ---
database.init_db()

# --- CSS TOÀN CỤC (STYLE GOOGLE) ---
st.markdown("""
<style>
    /* 1. Nền xám nhạt đặc trưng của Google */
    .stApp {
        background-color: #F8F9FA;
        font-family: 'Google Sans', 'Roboto', Arial, sans-serif;
    }
    
    /* 2. Ẩn Header mặc định của Streamlit */
    header {visibility: hidden;}
    .st-emotion-cache-12fmjuu {top: 0px;}
    
    /* 3. Tùy chỉnh Menu bên trái cho đẹp hơn */
    .nav-link {
        font-size: 15px !important;
        text-align: left !important;
        margin: 0px !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- QUẢN LÝ SESSION ---
if 'is_admin' not in st.session_state:
    st.session_state['is_admin'] = False

# --- SIDEBAR (THANH BÊN) ---
with st.sidebar:
    # Logo & Tên dự án
    if os.path.exists("rose.png"):
        st.image("rose.png", width=50)
    st.markdown("### VietScribe AI")
    st.caption("v2.1 Enterprise Edition")
    
    st.write("") # Khoảng trống

    # MENU ĐIỀU HƯỚNG
    options = ["Trang chủ", "Công cụ xử lý"]
    icons = ["house", "cpu"]
    
    # Nếu là Admin thì hiện thêm dòng Admin
    if st.session_state['is_admin']:
        options.append("Quản trị hệ thống")
        icons.append("gear")

    selected = option_menu(
        menu_title=None,
        options=options,
        icons=icons,
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#5f6368", "font-size": "16px"}, 
            "nav-link": {"color": "#3c4043", "font-weight": "500"},
            "nav-link-selected": {"background-color": "#E8F0FE", "color": "#1967D2"}, # Xanh Google khi chọn
        }
    )

    st.write("---")
    
    # LOGIN ADMIN
    if not st.session_state['is_admin']:
        with st.expander("🔐 Admin Access"):
            user = st.text_input("User", key="u")
            pwd = st.text_input("Pass", type="password", key="p")
            if st.button("Login"):
                if user == "admin" and pwd == "123":
                    st.session_state['is_admin'] = True
                    st.rerun()
    else:
        if st.button("Đăng xuất", type="secondary"):
            st.session_state['is_admin'] = False
            st.rerun()

# --- ĐIỀU HƯỚNG NỘI DUNG ---
if selected == "Trang chủ":
    home.show()
elif selected == "Công cụ xử lý":
    user_dashboard.show()
elif selected == "Quản trị hệ thống":
    admin_dashboard.show()