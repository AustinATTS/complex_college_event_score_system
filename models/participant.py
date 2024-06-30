import sqlite3
from db.database import create_connection

def add_participant():
    pass

def save_participant():
    pass

def delete_participant(participant_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM participants WHERE ID = ?", (participant_id))
    cursor.commit()
    conn.close()()

def get_participant():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM participants")
    participants = cursor.fetchall()
    conn.close()
    return participants
