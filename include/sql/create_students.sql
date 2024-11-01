CREATE OR REPLACE TABLE {{ params.schema_name }}.{{ params.table_name }} (
    student_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(100),
    middle_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(10),
    date_of_birth DATE,
    stream VARCHAR(50),
    grade_level VARCHAR(20),
    blood_group VARCHAR(5),
    genotype VARCHAR(5),
    state_of_origin VARCHAR(50),
    address TEXT,
    parent_id VARCHAR(20),
    registration_date DATE,
    created_at TIMESTAMP,  
    updated_at TIMESTAMP
);
