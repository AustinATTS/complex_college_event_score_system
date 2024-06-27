import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(BASE_DIR, 'db', 'database.db')
LOG_FILE_PATH = os.path.join(BASE_DIR, 'logging_function', 'app.log')
