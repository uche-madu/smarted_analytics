WITH current_students AS (
    SELECT *
    FROM {{ ref('students_snapshot') }} 
    WHERE dbt_valid_to IS NULL
),

results AS (
    SELECT
        DISTINCT student_id,
        stream
    FROM {{ ref('stg_results') }}
)

SELECT 
    cs.*, 
    r.stream
FROM current_students cs
JOIN results r
ON cs.student_id = r.student_id
