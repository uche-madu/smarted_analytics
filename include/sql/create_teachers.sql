CREATE OR REPLACE TABLE {{ params.schema_name }}.{{ params.table_name }} (
    teacher_id STRING PRIMARY KEY,                -- Unique identifier for each teacher
    first_name STRING NOT NULL,                   -- Teacher's first name
    middle_name STRING,                           -- Teacher's middle name
    last_name STRING NOT NULL,                    -- Teacher's last name
    gender STRING,                                -- Gender of the teacher
    date_of_birth DATE,                           -- Date of birth of the teacher
    phone_number STRING UNIQUE,                   -- Contact phone number
    email STRING UNIQUE,                          -- Email address of the teacher
    address STRING,                               -- Residential address
    hire_date DATE,                               -- Date the teacher was hired
    subject STRING,                               -- Subject the teacher teaches
    qualification STRING,                         -- Teacher's qualifications (e.g., B.Ed., M.Sc.)
    years_of_experience INT,                      -- Number of years of teaching experience
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for last update
);
