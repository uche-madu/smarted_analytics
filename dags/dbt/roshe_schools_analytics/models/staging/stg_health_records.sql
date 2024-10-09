{{ config(materialized='view') }}

WITH source_data AS (
    SELECT *
    FROM {{ source('bronze', 'health_records') }}
)

SELECT * FROM source_data
