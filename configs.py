import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=".google_sheet.env")

SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")

# Configuration for Google Sheets URLs and required columns
SHEET_CONFIG = {
    "results": {
        "required_columns": {"Student ID", "Grade Level", "Term"},
        "output_file": "results.csv",
        "url": os.getenv("GOOGLE_SHEET_URL_RESULTS")
    },
    "students": {
        "required_columns": {"Student ID"},
        "output_file": "students.csv",
        "url": os.getenv("GOOGLE_SHEET_URL_STUDENTS")
    },
    "parents": {
        "required_columns": {"Parent ID"},
        "output_file": "parents.csv",
        "url": os.getenv("GOOGLE_SHEET_URL_PARENTS")
    },
    "teachers": {
        "required_columns": {"Teacher ID"},
        "output_file": "teachers.csv",
        "url": os.getenv("GOOGLE_SHEET_URL_TEACHERS")
    },
}
