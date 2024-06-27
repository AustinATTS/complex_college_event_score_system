import customtkinter as ctk
from utils.auth import login_user
from logging_function.logger_function import get_logger
from utils.ctk_custom import show_error

logger = get_logger(__name__)

class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.label_username = ctk.CTkLabel(self, text="Username")
        self.label_username.pack(pady=10)
        self.entry_username = ctk.CTkEntry(self)
        self.entry_username.pack(pady=10)

        self.label_password = ctk.CTkLabel(self, text="Password")
        self.label_password.pack(pady=10)
        self.entry_password = ctk.CTkEntry(self, show="*")
        self.entry_password.pack(pady=10)

        self.button_login = ctk.CTkButton(self, text="Login", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        success = login_user(username, password)
        if success:
            # Check if the master object has the show_dashboard method
            if hasattr(self.master, 'show_dashboard') and callable(getattr(self.master, 'show_dashboard')):
                self.master.show_dashboard()
            else:
                logger.error("MainApp does not have show_dashboard method")
        else:
            logger.error("Login failed")
            show_error("Login failed", "Invalid username or password")
