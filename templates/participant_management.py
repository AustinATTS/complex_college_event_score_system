import customtkinter as ctk
from utils.validation import validate_email, validate_phone
from logging_function.logger_function import get_logger
from db.database import create_connection
from utils.ctk_custom import show_error, show_info

logger = get_logger(__name__)

class ParticipantManagementPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_name = ctk.CTkLabel(self, text="Name")
        self.label_name.pack(pady=10)
        self.entry_name = ctk.CTkEntry(self)
        self.entry_name.pack(pady=10)

        self.label_email = ctk.CTkLabel(self, text="Email")
        self.label_email.pack(pady=10)
        self.entry_email = ctk.CTkEntry(self)
        self.entry_email.pack(pady=10)

        self.label_phone = ctk.CTkLabel(self, text="Phone")
        self.label_phone.pack(pady=10)
        self.entry_phone = ctk.CTkEntry(self)
        self.entry_phone.pack(pady=10)

        self.button_save = ctk.CTkButton(self, text="Save", command=self.save_participant)
        self.button_save.pack(pady=10)

    def save_participant(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        if not validate_email(email):
            logger.error("Invalid email format")
            show_error("Error", "Invalid email format")
            return

        if not validate_phone(phone):
            logger.error("Invalid phone format")
            show_error("Error", "Invalid phone format")
            return

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO participants (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        conn.commit()
        conn.close()

        logger.info(f"Participant {name} added successfully")
        show_info("Success", "Participant added successfully")
