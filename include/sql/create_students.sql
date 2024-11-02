CREATE OR REPLACE TABLE {{ params.schema_name }}.{{ params.table_name }} (
    student_id STRING PRIMARY KEY,
    first_name STRING,
    middle_name STRING,
    last_name STRING,
    gender STRING,
    date_of_birth DATE,
    stream STRING,
    grade_level STRING,
    blood_group STRING,
    genotype STRING,
    state_of_origin STRING,
    address TEXT,
    parent_id STRING,
    registration_date DATE,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
