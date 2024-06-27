import customtkinter as ctk
from templates.participant_management import ParticipantManagementPage
from templates.event_management import EventManagementPage
from templates.settings import SettingsPage
from templates.report_generation import ReportGenerationPage

class AdminDashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.button_participants = ctk.CTkButton(self, text="Manage Participants", command=self.show_participants)
        self.button_participants.pack(pady=10)

        self.button_events = ctk.CTkButton(self, text="Manage Events", command=self.show_events)
        self.button_events.pack(pady=10)

        self.button_reports = ctk.CTkButton(self, text="Generate Reports", command=self.show_reports)
        self.button_reports.pack(pady=10)

        self.button_settings = ctk.CTkButton(self, text="Settings", command=self.show_settings)
        self.button_settings.pack(pady=10)

        self.participant_management_page = ParticipantManagementPage(self)
        self.event_management_page = EventManagementPage(self)
        self.settings_page = SettingsPage(self)
        self.report_generation_page = ReportGenerationPage(self)

    def show_participants(self):
        self.participant_management_page.pack(fill="both", expand=True)
        self.event_management_page.pack_forget()
        self.settings_page.pack_forget()
        self.report_generation_page.pack_forget()

    def show_events(self):
        self.participant_management_page.pack_forget()
        self.event_management_page.pack(fill="both", expand=True)
        self.settings_page.pack_forget()
        self.report_generation_page.pack_forget()

    def show_reports(self):
        self.participant_management_page.pack_forget()
        self.event_management_page.pack_forget()
        self.settings_page.pack_forget()
        self.report_generation_page.pack(fill="both", expand=True)

    def show_settings(self):
        self.participant_management_page.pack_forget()
        self.event_management_page.pack_forget()
        self.settings_page.pack(fill="both", expand=True)
        self.report_generation_page.pack_forget()
