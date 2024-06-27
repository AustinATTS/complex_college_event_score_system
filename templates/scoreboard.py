import customtkinter as ctk
from tkinter import ttk  # Import ttk module for Treeview
from db.database import create_connection

class ScoreboardPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.tree = None
        self.show_scores()

    def show_scores(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM scores ORDER BY score DESC")
        scores = cursor.fetchall()
        conn.close()

        # Create Treeview using ttk module
        self.tree = ttk.Treeview(self, columns=("Event ID", "Participant ID", "Score"), show="headings")
        self.tree.heading("Event ID", text="Event ID")
        self.tree.heading("Participant ID", text="Participant ID")
        self.tree.heading("Score", text="Score")

        for score in scores:
            self.tree.insert("", "end", values=score)

        self.tree.pack(fill="both", expand=True)