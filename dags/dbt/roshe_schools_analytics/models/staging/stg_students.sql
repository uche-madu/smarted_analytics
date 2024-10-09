{{ config(materialized='view') }}

WITH source_data AS (
    SELECT *
    FROM {{ source('bronze', 'students') }}
)

SELECT * FROM source_data
