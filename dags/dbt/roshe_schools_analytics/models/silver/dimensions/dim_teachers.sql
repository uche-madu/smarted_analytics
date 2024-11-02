WITH current_teachers AS (
    SELECT *
    FROM {{ ref('teachers_snapshot') }}
    WHERE dbt_valid_to IS NULL
)

SELECT *
FROM current_teachers
