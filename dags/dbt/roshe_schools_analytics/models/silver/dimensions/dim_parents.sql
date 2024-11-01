WITH current_parents AS (
    SELECT *
    FROM {{ ref('parents_snapshot') }}  
    WHERE dbt_valid_to IS NULL
)

SELECT *
FROM current_parents
