import streamlit as st
import tempfile
import librosa 
import numpy as np
from utils import load_model, transcribe_audio, format_time
# Import hàm ghi log
from database import log_transcription

def show():
    # --- 1. CSS GIAO DIỆN ---
    st.markdown("""
    <style>
        .google-card {
            background-color: white;
            padding: 24px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12);
            border: 1px solid #dadce0;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 16px;
            font-weight: 600;
            color: #202124;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .toolbar-container {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 6px;
            border: 1px solid #e0e0e0;
            margin-bottom: 20px;
        }
        .ts-row {
            display: flex;
            border-bottom: 1px solid #f1f3f4;
            padding: 10px 0;
        }
        .ts-time { 
            min-width: 70px; 
            color: #1967d2; 
            font-family: 'Roboto Mono', monospace; 
            font-weight: 600; font-size: 13px;
        }
        .ts-text { flex: 1; color: #3c4043; line-height: 1.5; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## 🛠️ Công cụ chuyển đổi (Speech-to-Text)")
    st.caption("Chọn cấu hình và tải file ghi âm để bắt đầu.")

    # --- 2. KHUNG INPUT & TOOLBAR ---
    st.markdown('<div class="google-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">1. Cấu hình & Dữ liệu</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="toolbar-container">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 2])
    
    with c1:
        model_option = st.selectbox(
            "🎯 Loại mô hình (Model)", 
            ["Base (Cân bằng)", "Tiny (Siêu nhanh)", "Small (Chính xác)"]
        )
        model_map = {"Base (Cân bằng)": "base", "Tiny (Siêu nhanh)": "tiny", "Small (Chính xác)": "small"}
        selected_model = model_map[model_option]

    with c2:
        lang_option = st.selectbox(
            "🌍 Ngôn ngữ nói", 
            ["Tự động nhận diện", "Tiếng Việt", "Tiếng Anh"]
        )
        lang_map = {"Tự động nhận diện": None, "Tiếng Việt": "vi", "Tiếng Anh": "en"}
        selected_lang = lang_map[lang_option]

    with c3:
        st.info("💡 **Gợi ý:** Nếu gặp lỗi, hãy thử dùng model 'Tiny' trước.")

    st.markdown('</div>', unsafe_allow_html=True) 

    col_up, col_btn = st.columns([3, 1])
    with col_up:
        uploaded_file = st.file_uploader("Chọn file ghi âm...", type=["mp3", "wav", "m4a"], label_visibility="collapsed")
    
    with col_btn:
        st.markdown("<div style='height: 5px'></div>", unsafe_allow_html=True)
        btn_process = st.button("✨ Bắt đầu xử lý", type="primary", use_container_width=True, disabled=(not uploaded_file))

    st.markdown('</div>', unsafe_allow_html=True) 

    # --- 3. XỬ LÝ LOGIC ---
    if 'result' not in st.session_state:
        st.session_state['result'] = None

    if btn_process and uploaded_file:
        with st.spinner(f"Đang chuẩn bị dữ liệu và chạy mô hình '{selected_model}'..."):
            try:
                # 1. Lưu file tạm
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                # 2. Load Audio bằng Librosa
                try:
                    # Whisper yêu cầu 16000Hz
                    audio_array, _ = librosa.load(tmp_path, sr=16000)
                except Exception as audio_err:
                    st.error(f"❌ Lỗi đọc file âm thanh: {audio_err}")
                    return 

                # 3. Gọi Model
                model = load_model(selected_model) 
                
                if model is None:
                    st.error(f"⚠️ Không thể tải model '{selected_model}'. Kiểm tra mạng Internet.")
                else:
                    # Chạy AI
                    res = transcribe_audio(model, audio_array, selected_lang)
                    
                    # --- GHI DATABASE (LƯU LỊCH SỬ) ---
                    duration_sec = len(audio_array) / 16000 # Tính thời gian file
                    file_size_mb = uploaded_file.size / (1024*1024)
                    
                    log_transcription(
                        filename=uploaded_file.name,
                        file_size=file_size_mb,
                        model=selected_model,
                        lang=selected_lang if selected_lang else "Auto",
                        duration=duration_sec
                    )
                    # ----------------------------------
                    
                    st.session_state['result'] = res
                    st.session_state['filename'] = uploaded_file.name
                    st.session_state['model_name'] = selected_model 
                    
            except Exception as e:
                st.error(f"Hệ thống gặp sự cố: {e}")

    # --- 4. HIỂN THỊ KẾT QUẢ ---
    if st.session_state['result']:
        res = st.session_state['result']
        c1, c2 = st.columns([1, 2])
        
        with c1:
            st.markdown(f"""
            <div class="google-card">
                <div class="section-title">Metadata</div>
                <p><b>File:</b> {st.session_state.get('filename')}</p>
                <p><b>Model:</b> Whisper ({st.session_state.get('model_name', 'base')})</p>
                <p><b>Language:</b> {res.get('language', 'auto').upper()}</p>
                <hr>
                <p style="color:green; font-weight:bold">✅ Hoàn thành</p>
            </div>
            """, unsafe_allow_html=True)
            st.download_button("📥 Tải (.txt)", res['text'], file_name="transcript.txt", use_container_width=True)

        with c2:
            html_content = ""
            for seg in res['segments']:
                start = format_time(seg['start'])
                text = seg['text']
                html_content += f'<div class="ts-row"><div class="ts-time">{start}</div><div class="ts-text">{text}</div></div>'
            
            st.markdown(f"""
            <div class="google-card">
                <div class="section-title">Nội dung chi tiết</div>
                <div style="max-height: 600px; overflow-y: auto; padding-right: 5px;">
                    {html_content}
                </div>
            </div>
            """, unsafe_allow_html=True)