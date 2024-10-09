{{ config(materialized='view') }}

WITH source_data AS (
    SELECT *
    FROM {{ source('bronze', 'extracurricular_activities') }}
)

SELECT * FROM source_data
