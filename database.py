cat <<EOF > database.py
import sqlite3
from datetime import datetime

DB_PATH = "finance.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                balance REAL DEFAULT 0,
                salary_date1 INTEGER DEFAULT 25,
                salary_date2 INTEGER,
                salary_delay_until TEXT
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount REAL,
                category TEXT,
                tx_type TEXT,
                created_at TEXT
            )
        ''')
        conn.commit()

def create_user(user_id):
    with get_connection() as conn:
        conn.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
        conn.commit()

def add_transaction(user_id, amount, tx_type, category="Общее"):
    now = datetime.now().isoformat()
    change = -amount if tx_type == "expense" else amount
    with get_connection() as conn:
        conn.execute('INSERT INTO transactions (user_id, amount, category, tx_type, created_at) VALUES (?, ?, ?, ?, ?)', (user_id, amount, category, tx_type, now))
        conn.execute('UPDATE users SET balance = balance + ? WHERE user_id = ?', (change, user_id))
        conn.commit()

def get_user(user_id):
    with get_connection() as conn:
        res = conn.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()
        return dict(res) if res else None
EOF