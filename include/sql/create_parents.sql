CREATE OR REPLACE TABLE {{ params.schema_name }}.{{ params.table_name }} (
    parent_id STRING PRIMARY KEY,                    -- Unique identifier for each parent
    first_name STRING NOT NULL,                      -- Parent's first name
    middle_name STRING,                              -- Parent's middle name
    last_name STRING NOT NULL,                       -- Parent's last name
    gender STRING,                                   -- Parent's gender
    marital_status STRING,                           -- Marital status (e.g., 'Married', 'Single', 'Separated', etc.)
    phone_number STRING UNIQUE,                      -- Contact phone number
    email STRING UNIQUE,                             -- Email address
    address STRING,                                  -- Home address
    relationship_to_student STRING,                  -- Relationship type (e.g., 'Parent', 'Guardian')
    income_bracket STRING,                           -- Income bracket in Naira terms (e.g., 'Low', 'Middle', 'High')
    education_level STRING,                          -- Highest level of education (e.g., 'Secondary School', 'Bachelor', 'Master')
    occupation STRING,                               -- Parent's occupation
    employment_type STRING,                          -- Employment type (e.g., 'Full-Time', 'Part-Time', 'Unemployed')
    industry STRING,                                 -- Industry sector (e.g., 'Education', 'Healthcare')
    engagement_level INT,                            -- Measure of engagement with school
    home_language STRING,                            -- Primary language spoken at home
    number_of_children INT,                          -- Total number of children in the household
    alternate_contact_number STRING,                 -- Secondary phone number
    parent_teacher_meeting_attendance INT,           -- Number of parent-teacher meetings attended
    volunteer_activities_count INT,                  -- Number of volunteer activities participated in
    recent_interaction_date TIMESTAMP,               -- Date of last interaction with the school
    created_at TIMESTAMP,                            -- Timestamp when the record was created
    updated_at TIMESTAMP                             -- Timestamp for last update
);
