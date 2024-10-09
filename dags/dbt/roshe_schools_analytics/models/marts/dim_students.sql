WITH student_data AS (
    SELECT
        *,
        DATEDIFF(YEAR, date_of_birth, CURRENT_DATE) AS age,
        DATE_PART('year', registration_date) AS registration_year
    FROM {{ ref('stg_students') }}
)

SELECT * FROM student_data
