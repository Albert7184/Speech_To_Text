import streamlit as st
import whisper
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# --- 1. LOAD MODEL (CACHE) ---
@st.cache_resource(show_spinner=False)
def load_model(model_size):
    try:
        return whisper.load_model(model_size)
    except Exception as e:
        st.error(f"Lỗi load model: {e}")
        return None

# --- 2. XỬ LÝ TRANSCRIPT ---
def transcribe_audio(model, file_path, language_setting=None):
    """
    Hàm xử lý STT có hỗ trợ chọn ngôn ngữ
    language_setting: 'vi', 'en', hoặc None (Auto)
    """
    # Cấu hình tham số decode
    options = dict(fp16=False)
    
    # Nếu người dùng chọn ngôn ngữ cụ thể (không phải Auto)
    if language_setting:
        options["language"] = language_setting

    # Transcribe
    result = model.transcribe(file_path, **options)
    return result

# --- 3. FORMAT THỜI GIAN ---
def format_time(seconds):
    """Chuyển giây thành phút:giây (VD: 70 -> 01:10)"""
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"

# --- 4. VẼ BIỂU ĐỒ SÓNG ÂM (HÀM BỊ THIẾU) ---
def plot_waveform(file_path):
    """
    Vẽ biểu đồ sóng âm (Waveform)
    Trả về: (figure, duration)
    """
    # Load file âm thanh
    y, sr = librosa.load(file_path, sr=None)
    duration = len(y) / sr
    
    # Vẽ biểu đồ
    fig, ax = plt.subplots(figsize=(10, 2))
    librosa.display.waveshow(y, sr=sr, ax=ax, color='#1f77b4', alpha=0.8)
    
    # Ẩn trục toạ độ cho đẹp
    ax.set_title("")
    ax.set_xlabel("")
    ax.set_ylabel("")
    plt.tight_layout()
    
    return fig, duration