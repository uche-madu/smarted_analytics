# SmartEd Analytics: Improving Student Performance through Data-Driven Insights
## To Do: Update to README underway. Lots of code changes since the last README update.

## Introduction
SmartEd Analytics is a proof-of-concept solution developed for [DataFestAfrica Hackathon 2024](https://portfolio.diceytech.co.uk/project-opportunity/1727715039866x124628249482625020) to address the lack of data infrastructure in African secondary schools. Our project is built around Roshe Schools International [](https://roshallomschools.com/secondary-school/academics/sss-senior-secondary-school/) in Lagos, Nigeria, which manually records student results, health, and extracurricular activities. The goal is to implement a comprehensive data pipeline and warehousing solution to transform fragmented records into actionable insights and improve academic performance in key exams such as JAMB and WASSCE.

## Data Collection Methodology
To simulate the real-world data collection process, we generated synthetic data based on an [actual secondary school](https://roshallomschools.com/secondary-school/academics/sss-senior-secondary-school/), grouped into four academic streams: Basic Science and Maths, Technical and Agricultural, Commercial, and Liberal Arts and Social Science. Using a [Python script](https://github.com/uche-madu/smarted_analytics/blob/main/generate_data.py), we populated Google Sheets to mimic the entry process typically handled by form teachers and administrators. Data collected includes:

- [Academic Results](https://docs.google.com/spreadsheets/d/1FnoP8w1nzwH8z0WwLClakpvu4HK-heagXR5eQ9izdys/edit?gid=1746057588#gid=1746057588) (SS1 - SS3)
- [Student Bio Data](https://docs.google.com/spreadsheets/d/1VI3wiL3kecKAgL1Tnv6iWBFGxn6pQDYocQAYGGqG-P0/edit?gid=397552977#gid=397552977)
- [Parent Bio Data](https://docs.google.com/spreadsheets/d/10L03aVGbMIyLtVGumX58y1k4PfPe8NwtZH-K6nBXLOU/edit?gid=2000885865#gid=2000885865)
- [Teacher Bio Data](https://docs.google.com/spreadsheets/d/1P8gBY1106mxmJQZdW-emz1q5v0vkfUrEwlp2xhXbWu8/edit?gid=266312471#gid=266312471)
- [Health Records](https://docs.google.com/spreadsheets/d/1x8JAm6UYR5zSUnOXdMbKr4MvqCcmNl-urxvW03QJjEc/edit?gid=848574373#gid=848574373)
- [Extracurricular Activities](https://docs.google.com/spreadsheets/d/1ak_D4hTLtbL5Ru-7h3yrSTUGNUJPM-0hKlbD3LTuvOU/edit?gid=194248919#gid=194248919)

## Solution Overview
We designed a Medallion Architecture in Snowflake, utilizing an [automated pipeline](https://github.com/uche-madu/smarted_analytics/blob/main/dags/exam_records_dags.py) built with Airflow and [transformation models](https://github.com/uche-madu/smarted_analytics/tree/main/dags/dbt/roshe_schools_analytics) created with dbt. The architecture follows three layers:

1. **Bronze Layer**: Raw data extracted from Google Sheets.
2. **Silver Layer**: Cleaned and standardized dimension tables.
3. **Gold Layer**: Aggregated fact tables for detailed performance analysis.
The entire pipeline is automated, allowing new data to seamlessly flow from entry to visualization, ensuring up-to-date insights for stakeholders.

## Data Warehouse Schema
We designed an optimized data warehouse schema to support analytical and reporting needs. You can view the detailed schema [here](https://dbdocs.io/dreemer6/SmartEd-Data-Warehouse-Design).

## Key Insights and Analysis
With our data warehouse, the school can now answer critical questions such as:

- Which subjects show consistent underperformance for specific students?
- What is the impact of health issues or attendance on exam scores?
- How do parental and teacher backgrounds influence student performance?
- Are extracurricular activities linked to higher or lower academic outcomes?

These insights provide a foundation for predictive modeling and tailored interventions for each student.

## Screenshots
![Snowflake](images/airflow_dag_screenshot.png)
Snowflake Data Warehouse

![Airflow](images/airflow_dag_screenshot.png)
Automated Airflow DAG

## Impact and Next Steps
By implementing this data solution, we’ve created a structured framework that not only addresses immediate performance issues but also enables long-term monitoring and personalized recommendations for students. Our next steps involve building machine learning models to predict student performance trends and continuously refining the solution based on stakeholder feedback.


## How to Run the Project
### Prerequisites
- **Python 3.12** with a virtual environment.
- **Astro CLI** installed ([Installation Guide](https://www.astronomer.io/docs/astro/cli/install-cli)).
- **Google Sheets API Credentials**.

### Step 1: Clone the Repository and Navigate to Project Directory
```bash
git clone https://github.com/uche-madu/smarted_analytics.git
cd smarted_analytics
```

### Step 2: Set Up a Virtual Environment and Install Requirements
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### Step 3: Configure Google Sheets API
1. Create API credentials in Google Cloud Console and download the service account key to the root folder as `.credentials.json`.
2. Set up a `.googlesheets.env` file in the root folder with the following variables:

    ```env
    GOOGLE_SHEET_URL_RESULTS=https://_your_sheet_url
    GOOGLE_SHEET_URL_STUDENTS=https://_your_sheet_url
    GOOGLE_SHEET_URL_PARENTS=https://_your_sheet_url
    GOOGLE_SHEET_URL_TEACHERS=https://_your_sheet_url
    GOOGLE_SHEET_URL_ACTIVITIES=https://_your_sheet_url
    GOOGLE_SHEET_URL_HEALTH=https://_your_sheet_url
    SERVICE_ACCOUNT_FILE=.credentials.json
    ```
3. Update your Google Sheets permissions by allowing the *service account email* to **edit** each sheet or set the permissions to *"Anyone with the link"* can edit.

### Step 4: Create a Snowflake Warehouse and Configure Airflow Connection
1. Set up a Snowflake warehouse and database in your [Snowflake account](https://signup.snowflake.com/).
2. Configure the "**snowflake_default**" connection in Airflow to point to your Snowflake database.

### Step 5: Edit the Dockerfile (if using Astro CLI)
If using **Astro CLI**, update the `ENV PYTHONPATH` in the Dockerfile to your project directory.

### Step 6: Generate Data and Load into Sheets
```bash
python generate_data.py
```
This script will automatically populate the Google Sheets with sample data.

### Step 7: Start Airflow and Trigger the DAG
1. Run the following command to start Airflow locally using Astro CLI:
    ```bash
    astro dev start
    ```
2. Log into the **Airflow UI** at `http://localhost:8080` and trigger the DAG run.

### Step 8: View Data in Snowflake
Once the DAG is complete, your Snowflake warehouse database will be populated with **staging views**, **fact table**, and **dimension tables**.

### Bonus: Generate ERD
From the dbt project root, run the following commands:
```bash
dbt docs generate
dbterd run -ad target/
```
Copy the content of target/output.dbml and paste it into [dbdiagram.io](https://dbdiagram.io) to create an ERD.
