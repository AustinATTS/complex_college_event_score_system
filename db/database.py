import sqlite3
from config import DATABASE_PATH

def create_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def initialize_db():
    conn = create_connection()
    with conn:
        with open('db/schema.sql') as f:
            conn.executescript(f.read())
    conn.close()

if __name__ == "__main__":
    initialize_db()
