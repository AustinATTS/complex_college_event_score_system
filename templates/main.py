import customtkinter as ctk
from templates.login import LoginPage
from templates.admin_dashboard import AdminDashboard
from templates.user_dashboard import UserDashboard
from templates.judge_dashboard import JudgeDashboard
from utils.auth import get_logged_in_user

class MainWindow(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.login_page = LoginPage(self)
        self.admin_dashboard = AdminDashboard(self)
        self.user_dashboard = UserDashboard(self)
        self.judge_dashboard = JudgeDashboard(self)

        self.show_login_page()

    def show_login_page(self):
        self.login_page.pack(fill="both", expand=True)
        self.admin_dashboard.pack_forget()
        self.user_dashboard.pack_forget()
        self.judge_dashboard.pack_forget()

    def show_dashboard(self):
        user = get_logged_in_user()
        if user:
            if user['role'] == 'admin':
                self.admin_dashboard.pack(fill="both", expand=True)
            elif user['role'] == 'judge':
                self.judge_dashboard.pack(fill="both", expand=True)
            else:
                self.user_dashboard.pack(fill="both", expand=True)
            self.login_page.pack_forget()
        else:
            print("No user logged in")
            self.show_login_page()
