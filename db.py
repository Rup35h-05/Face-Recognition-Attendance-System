import sqlite3

DB_PATH = "attendance.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # Create users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            img_path TEXT NOT NULL
        )
    """)
    # Create attendance table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            date TEXT,
            time TEXT,
            status TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    conn.close()
    print("[INFO] Database initialized.")

def add_user(name, user_id, img_path):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (id, name, img_path) VALUES (?, ?, ?)",
                (user_id, name, img_path))
    conn.commit()
    conn.close()
    print(f"[INFO] Added user: {name} ({user_id})")

# Only one __main__ block
if __name__ == "__main__":
    init_db()
