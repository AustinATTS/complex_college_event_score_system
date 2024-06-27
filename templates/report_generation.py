import customtkinter as ctk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from db.database import create_connection
from logging_function.logger_function import get_logger
from utils.ctk_custom import show_info

logger = get_logger(__name__)

class ReportGenerationPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.button_generate_report = ctk.CTkButton(self, text="Generate Report", command=self.generate_report)
        self.button_generate_report.pack(pady=10)

    def generate_report(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM scores")
        scores = cursor.fetchall()
        conn.close()

        report_file = "report.pdf"
        c = canvas.Canvas(report_file, pagesize=letter)
        width, height = letter

        c.drawString(30, height - 30, "Event Scores Report")
        y = height - 50
        for score in scores:
            c.drawString(30, y, f"Event ID: {score[0]}, Participant ID: {score[1]}, Score: {score[2]}")
            y -= 20

        c.save()
        logger.info(f"Report generated at {report_file}")
        show_info("Success", f"Report generated at {report_file}")
