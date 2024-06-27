import customtkinter as ctk
from templates.scoreboard import ScoreboardPage

class UserDashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.button_scoreboard = ctk.CTkButton(self, text="View Scoreboard", command=self.show_scoreboard)
        self.button_scoreboard.pack(pady=10)

        self.scoreboard_page = ScoreboardPage(self)

    def show_scoreboard(self):
        self.scoreboard_page.pack(fill="both", expand=True)
