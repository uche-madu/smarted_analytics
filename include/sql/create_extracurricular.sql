CREATE OR REPLACE TABLE {{ params.schema_name }}.{{ params.table_name }} (
    activity_id STRING PRIMARY KEY,                -- Unique identifier for each extracurricular activity
    activity_name STRING,                          -- Name of the activity (e.g., 'Soccer', 'Debate Club')
    student_id STRING,                             -- Foreign key referencing the student
    participation_level STRING,                    -- Participation level: 'Beginner', 'Intermediate', 'Advanced'
    teacher_id STRING,                             -- Teacher overseeing the activity
    date_joined DATE,                              -- Date the student joined the activity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for last update
);
