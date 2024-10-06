import re
import gspread
import pandas as pd
import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv(dotenv_path=".google_sheet.env")

# Retrieve variables from the .env file
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
WAREHOUSE = os.getenv('WAREHOUSE')
DATABASE = os.getenv('DATABASE')

gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)

# Function to extract and merge all tabs in a Google Sheet into a single DataFrame
def extract_and_merge_google_sheet(spreadsheet_url):
    # Open the Google Sheet by URL
    sh = gc.open_by_url(spreadsheet_url)
    spreadsheet_title = sh.title  # e.g., "2024/2025 Graduation Set"

    # Determine the set year for table naming
    set_year = re.search(r"(\d{4})/(\d{4})", spreadsheet_title)
    if not set_year:
        raise ValueError(f"Invalid spreadsheet title format: {spreadsheet_title}")
    start_year = set_year.group(1)  # Starting year (e.g., "2024")
    end_year = set_year.group(2)    # Ending year (e.g., "2025")

    # Initialize an empty list to hold data from all tabs
    all_data = []

    # Extract data from each worksheet/tab in the Google Sheet
    for worksheet in sh.worksheets():
        records = worksheet.get_all_records()
        if records:  # Proceed only if there's data
            df = pd.DataFrame(records)
            all_data.append(df)
    
    # Merge all term data into a single DataFrame
    if all_data:
        consolidated_df = pd.concat(all_data, ignore_index=True)

        # Remove duplicates based on unique student identifiers and term
        consolidated_df.drop_duplicates(subset=["Student ID", "Grade Level", "Term"], inplace=True)

        # Output table name for insertion into the database
        table_name = f"exam_records.set_{start_year}_{end_year}_results"
        return consolidated_df, table_name
    else:
        raise ValueError(f"No valid data found in {spreadsheet_title}")

def transform_column_names(df):
    """Transform column names to be lowercase, replace spaces, and remove special characters."""
    df.columns = (
        df.columns.str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[()]", "", regex=True)
    )
    return df

def save_and_upload_to_snowflake(df, table_name, schema_name, stage_name, file_path="/tmp/bronze_data.csv"):
    """Save DataFrame to CSV and upload to Snowflake, using a dynamic MERGE INTO query."""
    # Transform column names to match Snowflake conventions
    df = transform_column_names(df)
    
    # Save DataFrame to CSV
    df.to_csv(file_path, index=False)

    # Generate a list of column names from the DataFrame
    columns = df.columns.tolist()

    # Establish Snowflake connection
    with snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=PASSWORD,
        account=ACCOUNT,
    ) as conn:
        
        cursor = conn.cursor()
        
        # Create warehouse, database, and schema if they don't exist
        cursor.execute(f"CREATE WAREHOUSE IF NOT EXISTS {WAREHOUSE}")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
        cursor.execute(f"USE DATABASE {DATABASE}")
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")

        # Upload the CSV to Snowflake stage
        cursor.execute(f"PUT file://{file_path} @{stage_name}")
        print(f"File {file_path} uploaded to stage: {stage_name}")

        # Construct the `MERGE` statement using the DataFrame columns
        # Map the columns to positional references: $1, $2, $3, etc.
        source_columns = [f"source.${i + 1}" for i in range(len(columns))]
        
        # Construct the `ON` clause based on the unique columns
        on_clause = " AND ".join([f"target.{col} = {source_columns[i]}" for i, col in enumerate(columns) if col in ["student_id", "grade_level", "term"]])

        # Construct the `UPDATE` clause for all columns
        update_clause = ",\n".join([
            f"target.{col} = CASE WHEN target.{col} != {source_columns[i]} THEN {source_columns[i]} ELSE target.{col} END"
            for i, col in enumerate(columns) if col not in ["student_id", "grade_level", "term"]
        ])

        # Construct the `INSERT` columns and values
        insert_columns = ", ".join(columns)
        insert_values = ", ".join(source_columns)

        # Complete `MERGE` query
        merge_query = f"""
        MERGE INTO {schema_name}.{table_name} AS target
        USING @{stage_name}/{os.path.basename(file_path)} AS source
        ON {on_clause}
        WHEN MATCHED THEN
          UPDATE SET
            {update_clause}
        WHEN NOT MATCHED THEN
          INSERT ({insert_columns})
          VALUES ({insert_values});
        """
        
        # Execute the MERGE query
        cursor.execute(merge_query)
        print(f"Data merged successfully into table: {schema_name}.{table_name}")

