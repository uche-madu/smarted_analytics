WITH teacher_data AS (
    SELECT
        t.teacher_id,
        t.first_name,
        t.middle_name,
        t.last_name,
        t.gender,
        t.date_of_birth,
        t.phone_number,
        t.email,
        t.address,
        t.hire_date,
        t.subject,
        t.qualification,
        t.years_of_experience,
        t.created_at,
        t.updated_at,
        DATEDIFF(YEAR, t.date_of_birth, CURRENT_DATE) AS age,
        COUNT(a.activity_id) AS number_of_activities,
        LISTAGG(a.activity_name, ', ')
        WITHIN GROUP (ORDER BY a.activity_name) AS activities_list
    FROM {{ ref('stg_teachers') }} AS t
    LEFT JOIN {{ ref('stg_extracurricular_activities') }} AS a
        ON t.teacher_id = a.teacher_id
    GROUP BY
        t.teacher_id, t.first_name, t.middle_name, t.last_name, t.gender,
        t.date_of_birth, t.phone_number, t.email, t.address, t.hire_date,
        t.subject, t.qualification, t.years_of_experience, t.created_at,
        t.updated_at
)

SELECT
    teacher_id,
    first_name,
    middle_name,
    last_name,
    gender,
    date_of_birth,
    phone_number,
    email,
    address,
    hire_date,
    subject,
    qualification,
    years_of_experience,
    created_at,
    updated_at,
    age,
    number_of_activities,
    activities_list
FROM teacher_data
