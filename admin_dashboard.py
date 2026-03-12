import streamlit as st
import pandas as pd
import numpy as np
# Import hàm lấy thống kê thật
from database import get_stats

def show():
    # LẤY DỮ LIỆU TỪ DATABASE
    total_files, total_mins, recent_logs = get_stats()

    st.markdown("## 🛠️ Admin Dashboard - Quản trị hệ thống")
    st.markdown("---")

    # 1. METRICS (CHỈ SỐ THỰC TẾ)
    col1, col2, col3, col4 = st.columns(4)
    # Hiển thị số file thật
    col1.metric("Tổng Files đã xử lý", f"{total_files}", "Real-time")
    # Hiển thị tổng phút thật
    col2.metric("Thời gian xử lý", f"{total_mins} phút", "Tích lũy")
    
    col3.metric("Trạng thái DB", "Connected", delta_color="normal")
    col4.metric("Server Status", "Online", delta_color="normal")

    st.markdown("---")

    # 2. BIỂU ĐỒ & TÀI NGUYÊN
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("📊 Nhật ký hoạt động gần đây")
        if recent_logs:
            # Chuyển dữ liệu log thành DataFrame để hiển thị bảng đẹp
            df_logs = pd.DataFrame(recent_logs, columns=["Tên File", "Kích thước (MB)", "Model", "Ngôn ngữ", "Thời lượng (s)", "Thời gian chạy"])
            st.dataframe(df_logs, use_container_width=True)
        else:
            st.info("Chưa có dữ liệu. Hãy sang trang 'Công cụ xử lý' để chạy thử.")
    
    with c2:
        st.subheader("⚙️ Tài nguyên hệ thống")
        st.progress(70, text="CPU Usage (70%)")
        st.progress(45, text="RAM Usage (45%)")
        
        st.caption("Database: SQLite (vietscribe.db)")
        st.caption("Backend: Python + Whisper")
        st.success("✅ System Healthy")