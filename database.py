import sqlite3
import os

# Путь к папке, которая не стирается в Amvera
DATA_DIR = '/data'
DB_PATH = os.path.join(DATA_DIR, 'bot_database.db')

def get_connection():
    """Создает подключение к базе данных."""
    # Проверяем, существует ли папка /data (на всякий случай)
    if not os.path.exists(DATA_DIR):
        # Если запускаешь локально, создаст папку рядом
        os.makedirs(DATA_DIR, exist_ok=True)
        
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Создает таблицы, если их еще нет."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Таблица для транзакций (депозиты и расходы)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT, -- 'deposit' или 'expense'
            amount REAL,
            category TEXT,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Сразу инициализируем базу при импорте файла
init_db()