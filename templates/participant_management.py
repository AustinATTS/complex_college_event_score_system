import sqlite3

import customtkinter as ctk
from utils.validation import validate_email, validate_phone
from logging_function.logger_function import get_logger
from db.database import create_connection
from utils.ctk_custom import show_error, show_info
from CTkListbox import *

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

        self.participant_listbox = CTkListbox(self)
        self.participant_listbox.pack(pady=12, padx=10, fill="both", expand=True)

        self.delete_button = ctk.CTkButton(self, text="Delete Selcted", command=self.delete_selected_participant)
        self.delete_button.pack(pady=12, padx=10)

        self.load_participants()

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

        self.load_participants()

    def get_participants(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM participants")
        participants = cursor.fetchall()
        conn.close()
        return participants

    def delete_participant(self, participant_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM participants WHERE id = ?", (participant_id))
        conn.commit()
        conn.close()

    def load_participants(self):
        participants = self.get_participants()
        self.participant_listbox.delete(0, ctk.END)
        for participant in participants:
            self.participant_listbox.insert(ctk.END, f"{participant[0]}: {participant[1]} ({participant[2]})")

    def delete_selected_participant(self):
        selected = self.participant_listbox.curselection()
        if selected:
            participant_id = self.participant_listbox.get(selected[0]).split(":")[0]
            self.delete_participant(participant_id)
            self.load_participants()