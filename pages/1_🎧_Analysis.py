import streamlit as st
import os
import tempfile
import time
# Import các hàm từ file utils của chúng ta
from utils import load_model, transcribe_audio, plot_waveform, format_time

st.set_page_config(page_title="Analysis", page_icon="🎧", layout="wide")

# --- HEADER ---
st.markdown("## 🎧 Analysis – Phân tích audio & Speech to Text")
st.markdown("---")

# --- 1. UPLOAD AUDIO ---
st.subheader("☁️ Upload audio")
uploaded_file = st.file_uploader(
    "Drag and drop file here", 
    type=["mp3", "wav", "flac", "m4a"],
    help="Limit 200MB per file • WAV, MP3, FLAC"
)

if uploaded_file:
    # Lưu file tạm thời để xử lý
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    # Hiển thị thông tin file nhỏ bên dưới
    file_size_mb = uploaded_file.size / (1024 * 1024)
    st.caption(f"📄 File: {uploaded_file.name} | Size: {file_size_mb:.2f} MB")

    # --- 2. TUỲ CHỌN (OPTIONS) ---
    st.markdown("### ⚙️ Tuỳ chọn")
    col_opt1, col_opt2 = st.columns(2)
    with col_opt1:
        lang = st.selectbox("Ngôn ngữ", ["Auto-detect", "Vietnamese", "English"])
    with col_opt2:
        # Đây chỉ là UI option (Whisper tự cắt segment, nhưng ta để đây cho giống ảnh)
        seg_len = st.selectbox("Độ dài mỗi đoạn (giây)", [30, 60, 15, "Full"])

    # --- 3. CHUẨN HOÁ AUDIO & WAVEFORM ---
    st.markdown("### 🧼 Chuẩn hoá audio")
    
    # Hiển thị Waveform và tính duration
    with st.spinner("Đang phân tích tín hiệu âm thanh..."):
        fig, duration = plot_waveform(tmp_path)
    
    # Thanh thông báo xanh lá giống ảnh
    st.success(f"✅ Chuẩn hoá xong | Duration: {duration:.2f}s")
    
    # Audio Player
    st.audio(uploaded_file, format="audio/mp3")
    
    # Vẽ biểu đồ Waveform
    st.markdown("#### 📈 Waveform")
    st.pyplot(fig)

    st.markdown("---")

    # --- 4. SPEECH TO TEXT ---
    st.markdown("### 🧠 Speech-to-Text")
    st.markdown(f"🔹 **Số đoạn dự kiến:** ~{int(duration // 30) + 1} đoạn")

    if st.button("▶️ Thực hiện Speech-to-Text", type="primary"):
        
        # Container trạng thái
        status_container = st.container()
        
        with st.status("Đang xử lý AI...", expanded=True) as status:
            st.write("📥 Đang nạp model Whisper (Base)...")
            model = load_model("base") 
            
            st.write("✍️ Đang chuyển đổi giọng nói thành văn bản...")
            # Gọi hàm xử lý từ utils
            result = transcribe_audio(model, tmp_path)
            
            status.update(label="Xử lý hoàn tất!", state="complete", expanded=False)

        # Hiển thị kết quả sau khi chạy xong
        st.info(f"🌍 Ngôn ngữ phát hiện: **{result.get('language', 'N/A')}**")
        st.success("✅ Hoàn thành Speech-to-Text")

        st.markdown("### 📝 Transcript")
        
        # Xử lý hiển thị format: [00:00 - 00:30] Nội dung
        final_text = ""
        for segment in result['segments']:
            start_t = format_time(segment['start'])
            end_t = format_time(segment['end'])
            text = segment['text']
            
            # Format dòng text
            line = f"[{start_t} - {end_t}] {text}\n"
            final_text += line
        
        # Hiển thị Text Area
        st.text_area("Nội dung chi tiết:", value=final_text, height=350)
        
        # Nút Download
        st.download_button(
            label="📥 Tải kết quả (.txt)",
            data=final_text,
            file_name=f"transcript_{uploaded_file.name}.txt",
            mime="text/plain"
        )
        
    # (Optional) Xóa file tạm sau khi dùng xong để dọn rác
    # os.unlink(tmp_path)

else:
    # Nếu chưa upload file
    st.info("👆 Vui lòng tải file âm thanh lên để bắt đầu phân tích.")