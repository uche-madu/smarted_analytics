WITH source_data AS (
    SELECT *
    FROM {{ source('bronze', 'teachers') }}
)

SELECT * FROM source_data
