from airflow.decorators import dag, task, task_group
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago
import pandas as pd
import gspread
import logging
import os
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

from configs import (
    SERVICE_ACCOUNT_FILE,
    SHEET_CONFIG,
)


logger = logging.getLogger(__name__)

# Environment-based configuration for flexibility
AIRFLOW_HOME = os.getenv("AIRFLOW_HOME", "/usr/local/airflow")
_SNOWFLAKE_CONN_ID = "snowflake_default"
_OUTPUT_DIR = "/tmp/"

# Define constants
_SCHEMA_NAME = "admin"
_STAGE_NAME = "temp_stage"
_DATABASE = "roshe_schools_db"

_TABLE_NAMES = {
    "results": "results",
    "students": "students",
    "parents": "parents",
    "teachers": "teachers",
}

DBT_PROJECT_PATH = os.path.join(AIRFLOW_HOME, "dags/dbt/roshe_schools_analytics")
DBT_EXECUTABLE_PATH = os.path.join(AIRFLOW_HOME, "dbt_venv/bin/dbt")

EXECUTION_CONFIG = ExecutionConfig(
    dbt_executable_path=DBT_EXECUTABLE_PATH,
)

PROFILE_CONFIG = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id=_SNOWFLAKE_CONN_ID,
        profile_args={"database": _DATABASE, "schema": _SCHEMA_NAME, "threads": 6},
    ),
)


def get_file_path(sheet_type):
    return os.path.join(_OUTPUT_DIR, SHEET_CONFIG[sheet_type]["output_file"])


def get_staged_file_name(sheet_type):
    return SHEET_CONFIG[sheet_type]["output_file"]


# Define the DAG
@dag(
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
    tags=["snowflake", "smartEd analytics"],
    template_searchpath=["include/sql"],
    doc_md=__doc__,
    default_args={"owner": "Uche Madu", "retries": 0},
)
def google_sheets_to_snowflake_dag():
    def extract_and_save(sheet_type, sheet_url, output_file_path):
        """Extract data from Google Sheets based on specific column requirements, validate, and save as CSV."""
        logger.info(
            f"Extracting and validating {sheet_type} data from Google Sheets..."
        )

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
                    raise ValueError(
                        f"Missing required columns in '{worksheet.title}' for {sheet_type}. Expected: {required_columns}"
                    )
                all_data.append(df)

        if all_data:
            consolidated_df = pd.concat(all_data, ignore_index=True).drop_duplicates(
                subset=list(required_columns)
            )

            # Convert object-type columns to string data type
            consolidated_df = consolidated_df.astype(
                {
                    col: str
                    for col in consolidated_df.select_dtypes(include="object").columns
                }
            )

            # Save the DataFrame to CSV
            consolidated_df.to_csv(output_file_path, index=False, header=False)
            logger.info(
                f"{sheet_type.capitalize()} data extraction complete. Saved to {output_file_path}"
            )
        else:
            raise ValueError(
                f"No valid data found for {sheet_type}. Please ensure the sheets contain the expected data."
            )

    # Define a task group for extracting and validating data for each sheet type
    @task_group(group_id="extract_sheets")
    def extract_sheet_group():
        @task
        def extract_sheet_data(sheet_type: str):
            """Generic task to extract data for each sheet type."""
            config = SHEET_CONFIG[sheet_type]
            output_file = _OUTPUT_DIR + config["output_file"]
            extract_and_save(sheet_type, config["url"], output_file)

        # Creating tasks for each sheet type with unique task_ids
        extract_result_data = extract_sheet_data.override(
            task_id="extract_results_data"
        )("results")  # noqa: F841
        extract_student_data = extract_sheet_data.override(
            task_id="extract_students_data"
        )("students")  # noqa: F841
        extract_parent_data = extract_sheet_data.override(
            task_id="extract_parents_data"
        )("parents")  # noqa: F841
        extract_teacher_data = extract_sheet_data.override(
            task_id="extract_teachers_data"
        )("teachers")  # noqa: F841

    # Create table tasks
    create_results_table_task = SQLExecuteQueryOperator(
        task_id="create_results_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_results.sql",
        params={"schema_name": _SCHEMA_NAME, "table_name": _TABLE_NAMES["results"]},
    )

    create_students_table_task = SQLExecuteQueryOperator(
        task_id="create_students_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_students.sql",
        params={"schema_name": _SCHEMA_NAME, "table_name": _TABLE_NAMES["students"]},
    )

    create_parents_table_task = SQLExecuteQueryOperator(
        task_id="create_parents_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_parents.sql",
        params={"schema_name": _SCHEMA_NAME, "table_name": _TABLE_NAMES["parents"]},
    )

    create_teachers_table_task = SQLExecuteQueryOperator(
        task_id="create_teachers_table",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="create_teachers.sql",
        params={"schema_name": _SCHEMA_NAME, "table_name": _TABLE_NAMES["teachers"]},
    )

    create_snowflake_csv_file_format_task = SQLExecuteQueryOperator(
        task_id="create_snowflake_csv_file_format",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="snowflake_csv_file_format.sql",
    )

    remove_from_stage_task = SQLExecuteQueryOperator(
        task_id="remove_from_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="remove_from_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
        },
    )

    upload_results_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_results_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_path("results"),
        },
    )

    upload_students_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_students_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_path("students"),
        },
    )

    upload_parents_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_parents_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_path("parents"),
        },
    )

    upload_teachers_to_stage_task = SQLExecuteQueryOperator(
        task_id="upload_teachers_to_stage",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="upload_to_stage.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "stage_name": _STAGE_NAME,
            "file_path": get_file_path("teachers"),
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
            "file_name": get_staged_file_name("results"),
        },
    )

    merge_students_task = SQLExecuteQueryOperator(
        task_id="merge_students",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_students.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["students"],
            "stage_name": _STAGE_NAME,
            "file_name": get_staged_file_name("students"),
        },
    )

    merge_parents_task = SQLExecuteQueryOperator(
        task_id="merge_parents",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_parents.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["parents"],
            "stage_name": _STAGE_NAME,
            "file_name": get_staged_file_name("parents"),
        },
    )

    merge_teachers_task = SQLExecuteQueryOperator(
        task_id="merge_teachers",
        conn_id=_SNOWFLAKE_CONN_ID,
        sql="merge_teachers.sql",
        params={
            "schema_name": _SCHEMA_NAME,
            "table_name": _TABLE_NAMES["teachers"],
            "stage_name": _STAGE_NAME,
            "file_name": get_staged_file_name("teachers"),
        },
    )

    data_modeling_tasks = DbtTaskGroup(
        group_id="data_modeling",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=PROFILE_CONFIG,
        execution_config=EXECUTION_CONFIG,
        operator_args={"install_deps": True},
    )

    # Define task dependencies
    extract_sheet_task_group = extract_sheet_group()

    # Dummy start task
    start = EmptyOperator(task_id="start")
    # Dummy a synchronization task
    sync_task = EmptyOperator(task_id="sync_extract_and_create")
    # Dummy wait task
    wait_for_merge_tasks = EmptyOperator(task_id="wait_for_merge_tasks")

    create_tables_start = [
        create_results_table_task,
        create_students_table_task,
        create_parents_table_task,
        create_teachers_table_task,
    ]

    # Run extraction and table creation in parallel from the start
    start >> extract_sheet_task_group
    start >> create_tables_start
    start >> create_snowflake_csv_file_format_task

    # Use sync_task to ensure that both extract and create tasks are completed
    extract_sheet_task_group >> sync_task
    create_tables_start >> remove_from_stage_task >> sync_task

    # Define upload and merge dependencies for each table
    (
        sync_task
        >> upload_results_to_stage_task
        >> merge_results_task
        >> wait_for_merge_tasks
    )
    (
        sync_task
        >> upload_students_to_stage_task
        >> merge_students_task
        >> wait_for_merge_tasks
    )
    (
        sync_task
        >> upload_parents_to_stage_task
        >> merge_parents_task
        >> wait_for_merge_tasks
    )
    (
        sync_task
        >> upload_teachers_to_stage_task
        >> merge_teachers_task
        >> wait_for_merge_tasks
    )

    wait_for_merge_tasks >> data_modeling_tasks


# Instantiate the DAG
google_sheets_to_snowflake_dag()
