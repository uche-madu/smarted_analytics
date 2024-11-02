-- depends_on: {{ ref('dim_teachers') }}

WITH fact_results AS (
    SELECT *
    FROM {{ ref('fact_results') }}
),

student_data AS (
    SELECT
        student_id,
        parent_id,
        first_name,
        middle_name,
        last_name,
        gender,
        age,
        years_since_registration,
        stream,
        grade_level,
        region,
        genotype_risk_category,
        blood_group_category
    FROM {{ ref('dim_students') }}
),

parent_metrics AS (
    SELECT
        parent_id,
        income_bracket AS parent_income_bracket_category,
        education_category AS parent_education_category,
        occupation AS parent_occupation,
        engagement_level AS parent_engagement_level,
        parent_teacher_meeting_attendance,
        volunteer_activities_count AS parent_volunteer_activities_count,
        recent_interaction_date AS parent_recent_interaction_date,
        home_language,
        number_of_children AS parent_number_of_children,
        marital_status AS parent_marital_status
    FROM {{ ref('dim_parents') }}
)

SELECT
    p.*,
    f.student_id,
    f.academic_year,
    f.term,
    f.grade_level,
    s.first_name,
    s.middle_name,
    s.last_name,
    s.gender,
    s.age,
    s.years_since_registration,
    s.stream,
    s.grade_level AS current_grade_level,
    s.region,
    s.genotype_risk_category,
    s.blood_group_category,

    -- Include dynamically generated subject-specific fields and teacher details
    {{ generate_teacher_selects('fact_results') }},

    -- Include additional columns from fact_results
    f.extracurricular_activities,
    f.extracurricular_activities_count,
    f.extracurricular_activity_feedback,
    f.health_incidences,
    f.health_remarks,
    f.average_ca1,
    f.average_ca2,
    f.average_exam,
    f.average_total_score,
    f.aggregate_attendance_percentage,
    f.wassce_pass

FROM fact_results AS f
LEFT JOIN student_data AS s ON f.student_id = s.student_id
LEFT JOIN parent_metrics AS p ON s.parent_id = p.parent_id

-- Include dynamically generated teacher joins
{{ generate_teacher_joins('fact_results') }}
