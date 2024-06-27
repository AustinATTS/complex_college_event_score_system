import customtkinter as ctk
from templates.login import LoginPage
from db.database import initialize_db

initialize_db()

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tournament Management System")
        self.geometry("800x600")

        self.login_page = LoginPage(self)
        self.login_page.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
