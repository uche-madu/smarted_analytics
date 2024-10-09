{{ config(materialized='view') }}

WITH source_data AS (
    SELECT *
    FROM {{ source('bronze', 'results') }}
)

SELECT * FROM source_data
