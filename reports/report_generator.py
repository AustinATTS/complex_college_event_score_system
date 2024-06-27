from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from db.database import create_connection

def generate_report(filename):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores")
    scores = cursor.fetchall()

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    y = height - 40
    c.drawString(30, y, "Event Scores Report")
    y -= 40

    for score in scores:
        c.drawString(30, y, f"Event ID: {score[1]}, Participant ID: {score[2]}, Score: {score[3]}")
        y -= 20

    c.save()

if __name__ == "__main__":
    generate_report("event_scores_report.pdf")
