import customtkinter as ctk
from utils.auth import login_user
from templates.main import MainWindow

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("College Event Score System")
        self.geometry("800x600")

        # Initialize the main window
        self.main_window = MainWindow(self)
        self.main_window.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
