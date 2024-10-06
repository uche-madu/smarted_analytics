CREATE OR REPLACE TABLE {{ params.schema_name }}.parents (
    parent_id STRING PRIMARY KEY,                -- Unique identifier for each parent
    first_name STRING NOT NULL,                  -- Parent's first name
    middle_name STRING,                          -- Parent's middle name
    last_name STRING NOT NULL,                   -- Parent's last name
    gender STRING,                               -- Parent's gender
    marital_status STRING,                       -- Marital status (e.g., 'Married', 'Single')
    phone_number STRING UNIQUE,                  -- Contact phone number
    email STRING UNIQUE,                         -- Email address
    address STRING,                              -- Home address
    occupation STRING,                           -- Parent's occupation
    relationship_to_student STRING,              -- Relationship to student (e.g., 'Father', 'Mother')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for last update
);
