import streamlit as st

st.set_page_config(page_title="Training Info", page_icon="📊")

st.title("📊 Thông tin mô hình STT")
st.markdown("---")

st.markdown("""
### Kiến trúc Whisper (OpenAI)
Hệ thống sử dụng kiến trúc **Transformer Sequence-to-Sequence** được huấn luyện trên 680,000 giờ dữ liệu đa ngôn ngữ.

### Bảng đánh giá hiệu năng
| Model Size | Parameters | Multilingual | VRAM Required | Relative Speed |
| :--- | :--- | :--- | :--- | :--- |
| **Tiny** | 39 M | Yes | ~1 GB | Fast |
| **Base** | 74 M | Yes | ~1 GB | Moderate |
| **Small** | 244 M | Yes | ~2 GB | Slow |
""")