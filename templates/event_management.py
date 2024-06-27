import customtkinter as ctk
from db.database import create_connection
from logging.logger import get_logger

logger = get_logger(__name__)

class EventManagementPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_name = ctk.CTkLabel(self, text="Event Name")
        self.label_name.pack(pady=10)
        self.entry_name = ctk.CTkEntry(self)
        self.entry_name.pack(pady=10)

        self.label_type = ctk.CTkLabel(self, text="Event Type")
        self.label_type.pack(pady=10)
        self.entry_type = ctk.CTkEntry(self)
        self.entry_type.pack(pady=10)

        self.label_date = ctk.CTkLabel(self, text="Event Date")
        self.label_date.pack(pady=10)
        self.entry_date = ctk.CTkEntry(self)
        self.entry_date.pack(pady=10)

        self.label_time = ctk.CTkLabel(self, text="Event Time")
        self.label_time.pack(pady=10)
        self.entry_time = ctk.CTkEntry(self)
        self.entry_time.pack(pady=10)

        self.label_location = ctk.CTkLabel(self, text="Event Location")
        self.label_location.pack(pady=10)
        self.entry_location = ctk.CTkEntry(self)
        self.entry_location.pack(pady=10)

        self.button_save = ctk.CTkButton(self, text="Save", command=self.save_event)
        self.button_save.pack(pady=10)

    def save_event(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        date = self.entry_date.get()
        time = self.entry_time.get()
        location = self.entry_location.get()

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO events (name, type, date, time, location) VALUES (?, ?, ?, ?, ?)", (name, type, date, time, location))
        conn.commit()
        conn.close()

        logger.info(f"Event {name} added successfully")
        ctk.CTkMessageBox.show_info("Success", "Event added successfully")
