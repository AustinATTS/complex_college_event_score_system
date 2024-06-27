import customtkinter as ctk
from templates.score_entry import ScoreEntryPage

class JudgeDashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.button_score_entry = ctk.CTkButton(self, text="Enter Scores", command=self.show_score_entry)
        self.button_score_entry.pack(pady=10)

        self.score_entry_page = ScoreEntryPage(self)

    def show_score_entry(self):
        self.score_entry_page.pack(fill="both", expand=True)
