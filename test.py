# import snowflake.connector
# from airflow.hooks.base import BaseHook

# try:
#     # Establish the connection
#     conn = snowflake.connector.connect(
#         user='UCHE',
#         password='datathon',
#         account='qa11672.eu-central-2.aws',
#         warehouse='SMARTED',
#         database='ROSHE_SCHOOLS_DB',
#         schema='ADMIN',
#         role='DATA_ENGINEER',
#         insecure_mode=True
#     )

#     # Create a cursor object
#     cursor = conn.cursor()
    
#     # Execute a simple SQL command
#     cursor.execute("SELECT CURRENT_VERSION();")

#     # Fetch the results
#     result = cursor.fetchone()

#     # Print the result
#     print(f"Snowflake connection successful! Current version: {result[0]}")

# except Exception as e:
#     print(f"Connection failed: {e}")

# finally:
#     # Close the connection
#     cursor.close()
#     conn.close()

# conn = BaseHook.get_connection("snowflake_default")
# print(conn.get_uri())



import os
import pandas as pd
import gspread
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=".google_sheet.env")

# Retrieve variables from the .env file
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")

# Define file path for local CSV
_FILE_PATH = "/tmp/local_sheet_data.csv"

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def extract_and_save_csv_from_gsheets():
    """Extract data from Google Sheets and save as a CSV file."""
    logger.info("Extracting data from Google Sheets...")
    gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    sh = gc.open_by_url(GOOGLE_SHEET_URL)
    spreadsheet_title = sh.title

    # Extract data from each worksheet/tab and merge into a single DataFrame
    all_data = []
    for worksheet in sh.worksheets():
        records = worksheet.get_all_records()
        if records:
            df = pd.DataFrame(records)
            all_data.append(df)

    # Merge all data into a single DataFrame
    if all_data:
        consolidated_df = pd.concat(all_data, ignore_index=True)
        consolidated_df.to_csv(_FILE_PATH, index=False)
        logger.info(f"Data extracted and saved to {_FILE_PATH}")
    else:
        logger.warning(f"No data found in the sheets. Please check {spreadsheet_title}.")

def process_saved_csv(file_path):
    """Load and process the saved CSV file."""
    try:
        logger.info(f"Loading data from local CSV file: {file_path}")
        df = pd.read_csv(file_path)

        # Drop the first row if necessary (assuming it could be the header)
        df.columns = range(df.shape[1])

        # Print the first few rows for verification
        logger.info("Processed DataFrame:")
        print(df.head())
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}. Please run `extract_and_save_csv_from_gsheets()` first.")
    except Exception as e:
        logger.error(f"An error occurred while processing the file: {e}")

# Use these two functions separately as needed:

# Step 1: Run this only once to download and save data from Google Sheets to a local CSV file.
# extract_and_save_csv_from_gsheets()

# Step 2: Use this function to process the saved CSV file.
process_saved_csv(_FILE_PATH)

