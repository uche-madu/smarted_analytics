{{ config(materialized='view') }}

WITH source_data AS (
    SELECT *
    FROM {{ source('bronze', 'parents') }}
)

SELECT * FROM source_data
