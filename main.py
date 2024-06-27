import customtkinter as ctk
from templates.main import MainWindow  # Import MainWindow from the appropriate location
from db.database import initialize_db

initialize_db()

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tournament Management System")
        self.geometry("800x600")

        self.main_window = MainWindow(self)  # Create MainWindow instance
        self.main_window.pack(fill="both", expand=True)  # Pack MainWindow instance

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
