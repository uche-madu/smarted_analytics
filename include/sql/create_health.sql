CREATE OR REPLACE TABLE {{ params.schema_name }}.health_records (
    record_id STRING PRIMARY KEY,                   -- Unique identifier for each health record
    student_id STRING,                              -- Foreign key referencing the student
    checkup_date DATE,                              -- Date of health check-up
    health_issues STRING,                           -- Any health issues identified
    treatment STRING,                               -- Treatment recommended or administered
    admitted STRING,                                -- Whether or not there was a hospital/clinic admission
    admission_date DATE,                            -- If applicable, date of hospital admission
    discharge_date DATE,                            -- If applicable, date of discharge
    doctor STRING,                                  -- Name of the doctor or medical personnel
    follow_up_date DATE,                            -- Follow-up date, if applicable
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for last update
);
