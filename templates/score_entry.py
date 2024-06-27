import customtkinter as ctk
from db.database import create_connection
from logging.logger import get_logger

logger = get_logger(__name__)

class ScoreEntryPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_event_id = ctk.CTkLabel(self, text="Event ID")
        self.label_event_id.pack(pady=10)
        self.entry_event_id = ctk.CTkEntry(self)
        self.entry_event_id.pack(pady=10)

        self.label_participant_id = ctk.CTkLabel(self, text="Participant ID")
        self.label_participant_id.pack(pady=10)
        self.entry_participant_id = ctk.CTkEntry(self)
        self.entry_participant_id.pack(pady=10)

        self.label_score = ctk.CTkLabel(self, text="Score")
        self.label_score.pack(pady=10)
        self.entry_score = ctk.CTkEntry(self)
        self.entry_score.pack(pady=10)

        self.button_save = ctk.CTkButton(self, text="Save", command=self.save_score)
        self.button_save.pack(pady=10)

    def save_score(self):
        event_id = self.entry_event_id.get()
        participant_id = self.entry_participant_id.get()
        score = self.entry_score.get()

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (event_id, participant_id, score) VALUES (?, ?, ?)", (event_id, participant_id, score))
        conn.commit()
        conn.close()

        logger.info(f"Score {score} for event {event_id} and participant {participant_id} added successfully")
        ctk.CTkMessageBox.show_info("Success", "Score added successfully")
