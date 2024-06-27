import hashlib
import sqlite3
from db.database import create_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, role, password_hash FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and user[2] == hash_password(password):
        global logged_in_user
        logged_in_user = {"id": user[0], "role": user[1]}
        return True
    else:
        print("yes")
        print(hashlib.sha256(password.encode()).hexdigest())
        print(user[2])
        return False

def get_logged_in_user():
    return logged_in_user

logged_in_user = None
