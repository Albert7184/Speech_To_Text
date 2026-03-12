import sqlite3
from datetime import datetime

# Tên file Database (sẽ tự tạo ra khi chạy)
DB_NAME = "vietscribe.db"

# 1. KHỞI TẠO DATABASE
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Tạo bảng logs nếu chưa có
    c.execute('''
        CREATE TABLE IF NOT EXISTS transcription_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            file_size_mb REAL,
            model_type TEXT,
            language TEXT,
            duration_seconds REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# 2. HÀM GHI NHẬT KÝ (Dùng khi User chạy xong)
def log_transcription(filename, file_size, model, lang, duration):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO transcription_logs (filename, file_size_mb, model_type, language, duration_seconds)
        VALUES (?, ?, ?, ?, ?)
    ''', (filename, file_size, model, lang, duration))
    conn.commit()
    conn.close()

# 3. HÀM LẤY THỐNG KÊ (Dùng cho Admin Dashboard)
def get_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Đếm tổng số file
    c.execute("SELECT COUNT(*) FROM transcription_logs")
    total_files = c.fetchone()[0]
    
    # Tính tổng phút
    c.execute("SELECT SUM(duration_seconds) FROM transcription_logs")
    result = c.fetchone()[0]
    total_minutes = round(result / 60, 2) if result else 0
    
    # Lấy 10 dòng log mới nhất
    c.execute("SELECT filename, file_size_mb, model_type, language, duration_seconds, timestamp FROM transcription_logs ORDER BY id DESC LIMIT 10")
    recent_logs = c.fetchall()
    
    conn.close()
    return total_files, total_minutes, recent_logs