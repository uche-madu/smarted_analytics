from airflow.decorators import dag, task, task_group
from airflow.models.baseoperator import chain
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.utils.dates import days_ago
import os
import pandas as pd
import gspread
import logging
from dotenv import load_dotenv
from configs import (
    SERVICE_ACCOUNT_FILE,
    SHEET_CONFIG,

)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

_SNOWFLAKE_CONN_ID = "snowflake_default"

# Define constants for schema, stage, and file path
_SCHEMA_NAME = "admin"
_STAGE_NAME = "temp_stage"

# Define the table names for each task
_TABLE_NAMES = {
    "results": "results_table",
    "extracurricular": "extracurricular_activities",
    "health": "health_records",
    "students": "students",
    "parents": "parents",
    "teachers": "teachers"
}

OUTPUT_DIR = "../data"

# Derive the file paths from SHEET_CONFIG
def get_file_name(sheet_type):
    return SHEET_CONFIG[sheet_type]["output_file"]

# Define the DAG
@dag(
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
    tags=["snowflake", "smartEd analytics"],
    template_searchpath=["include/sql"],
    default_args={"owner": "Uche Madu"},
)
def google_sheets_to_snowflake_dag():

    # @task
    # def extract_and_save_to_csv():
    #     """Extract data from Google Sheets, validate its structure, merge into a single DataFrame, and save as CSV."""
    #     logger.info("Extracting and validating data from Google Sheets...")
    #     gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    #     sh = gc.open_by_url(GOOGLE_SHEET_URL)
    #     spreadsheet_title = sh.title

    #     # Extract and validate data from each worksheet/tab
    #     all_data = []
    #     required_columns = {"Student ID", "Grade Level", "Term"}

    #     for worksheet in sh.worksheets():
    #         records = worksheet.get_all_records()
    #         if records:
    #             df = pd.DataFrame(records)

    #             # Check if the required columns are present
    #             if not required_columns.issubset(df.columns):
    #                 raise ValueError(f"Missing required columns in worksheet '{worksheet.title}'. Required columns: {required_columns}")
                
    #             all_data.append(df)

    #     # Merge all data if validation passes
    #     if all_data:
    #         consolidated_df = pd.concat(all_data, ignore_index=True)
    #         consolidated_df.drop_duplicates(subset=["Student ID", "Grade Level", "Term"], inplace=True)
            
    #         # Save the DataFrame to CSV
    #         consolidated_df.to_csv(_FILE_PATH, index=False, header=False)
    #         logger.info(f"Data extraction complete. Saved to {_FILE_PATH}")

    #         # Log the saved CSV file content for confirmation
    #         saved_df = pd.read_csv(_FILE_PATH)
    #         logger.info(f"Data in saved CSV:\n{saved_df.head()}")

    #         return _FILE_PATH
    #     else:
    #         raise ValueError(f"No valid data found in {spreadsheet_title}. Please ensure the sheets contain student data.")



    def extract_and_save_to_csv(sheet_type, sheet_url, output_file_path):
        """Extract data from Google Sheets based on specific column requirements, validate, and save as CSV."""
        logger.info(f"Extracting and validating {sheet_type} data from Google Sheets...")

        # Open Google Sheets
        gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
        sh = gc.open_by_url(sheet_url)
        required_columns = SHEET_CONFIG[sheet_type]["required_columns"]

        all_data = []
        for worksheet in sh.worksheets():
            records = worksheet.get_all_records()
            if records:
                df = pd.DataFrame(records)

                # Check for required columns
                if not required_columns.issubset(df.columns):
                    raise ValueError(f"Missing required columns in '{worksheet.title}' for {sheet_type}. Expected: {required_columns}")

                all_data.append(df)

        if all_data:
            consolidated_df = pd.concat(all_data, ignore_index=True)
            consolidated_df.drop_duplicates(subset=list(required_columns), inplace=True)
            
            # Save the DataFrame to CSV
            consolidated_df.to_csv(output_file_path, index=False, header=True)
            logger.info(f"{sheet_type.capitalize()} data extraction complete. Saved to {output_file_path}")
            return output_file_path
        else:
            raise ValueError(f"No valid data found for {sheet_type}. Please ensure the sheets contain the expected data.")

    # Define a task group for extracting and validating data for each sheet type
    @task_group(group_id="extract_sheets")
    def extract_sheet_group():
        
        @task
        def extract_sheet_data(sheet_type: str):
            """Generic task to extract data for each sheet type."""
            config = SHEET_CONFIG[sheet_type]
            output_file = OUTPUT_DIR + config["output_file"]
            extract_and_save_to_csv(sheet_type, config["url"], output_file)

        # Creating tasks for each sheet type with unique task_ids
        extract_student_data = extract_sheet_data.override(task_id="extract_students_data")("students")
        extract_parent_data = extract_sheet_data.override(task_id="extract_parents_data")("parents")
        extract_teacher_data = extract_sheet_data.override(task_id="extract_teachers_data")("teachers")
        extract_activity_data = extract_sheet_data.override(task_id="extract_activities_data")("extracurricular_activities")
        extract_health_data = extract_sheet_data.override(task_id="extract_health_data")("health_records")


    # Create table tasks
    create_results_table_task = SQLExecuteQueryOperator(
        task_id="create_results_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_results.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["results"]
        },
    )

    create_extracurricular_table_task = SQLExecuteQueryOperator(
        task_id="create_extracurricular_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_extracurricular.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["extracurricular"]
        },
    )

    create_health_table_task = SQLExecuteQueryOperator(
        task_id="create_health_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_health.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["health"]
        },
    )

    create_students_table_task = SQLExecuteQueryOperator(
        task_id="create_students_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_students.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["students"]
        },
    )

    create_parents_table_task = SQLExecuteQueryOperator(
        task_id="create_parents_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_parents.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["parents"]
        },
    )

    create_teachers_table_task = SQLExecuteQueryOperator(
        task_id="create_teachers_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_teachers.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["teachers"]
        },
    )

    # Task to upload results CSV to Snowflake stage
    upload_results_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_results_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_name("results"),
        },
    )

    # Task to upload students CSV to Snowflake stage
    upload_students_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_students_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_name("students"),
        },
    )

    # Task to upload parents CSV to Snowflake stage
    upload_parents_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_parents_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_name("parents"),
        },
    )

    # Task to upload teachers CSV to Snowflake stage
    upload_teachers_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_teachers_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_name("teachers"),
        },
    )

    # Task to upload extracurricular activities CSV to Snowflake stage
    upload_extracurricular_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_extracurricular_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_name("extracurricular_activities"),
        },
    )

    # Task to upload health records CSV to Snowflake stage
    upload_health_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_health_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_name("health_records"),
        },
    )

    merge_results_task = SQLExecuteQueryOperator(
        task_id="merge_results",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_results.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["results"],
            "stage_name": _STAGE_NAME,
            "file_name": get_file_name("results")
        }
    )

    merge_students_task = SQLExecuteQueryOperator(
        task_id="merge_students",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_students.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["students"],
            "stage_name": _STAGE_NAME,
            "file_name": get_file_name("students")
        }
    )

    merge_parents_task = SQLExecuteQueryOperator(
        task_id="merge_parents",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_parents.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["parents"],
            "stage_name": _STAGE_NAME,
            "file_name": get_file_name("parents")
        }
    )

    merge_teachers_task = SQLExecuteQueryOperator(
        task_id="merge_teachers",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_teachers.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["teachers"],
            "stage_name": _STAGE_NAME,
            "file_name": get_file_name("teachers")
        }
    )

    merge_extracurricular_task = SQLExecuteQueryOperator(
        task_id="merge_extracurricular",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_extracurricular.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["extracurricular_activities"],
            "stage_name": _STAGE_NAME,
            "file_name": get_file_name("extracurricular_activities")
        }
    )

    merge_health_task = SQLExecuteQueryOperator(
        task_id="merge_health",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_health.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["health_records"],
            "stage_name": _STAGE_NAME,
            "file_name": get_file_name("health_records")
        }
    )


    # Define task dependencies
    extract_sheet_task_group = extract_sheet_group()

    # Set up dependencies
    chain(
        extract_sheet_task_group,
        [
            [create_results_table_task, upload_results_to_stage_task, merge_results_task],
            [create_students_table_task, upload_students_to_stage_task, merge_students_task],
            [create_parents_table_task, upload_parents_to_stage_task, merge_parents_task],
            [create_teachers_table_task, upload_teachers_to_stage_task, merge_teachers_task],
            [create_extracurricular_table_task, upload_extracurricular_to_stage_task, merge_extracurricular_task],
            [create_health_table_task, upload_health_to_stage_task, merge_health_task]
        ]
    )



# Instantiate the DAG
google_sheets_to_snowflake_dag()
