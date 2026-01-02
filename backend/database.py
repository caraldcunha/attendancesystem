import sqlite3

def get_db():
    return sqlite3.connect("data/students.db")

def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

