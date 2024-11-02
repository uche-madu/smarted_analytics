WITH subject_grades AS (
    SELECT
        student_id,
        academic_year,
        term,
        grade_level,
        {{ generate_subject_case_statements('stg_results') }},
        {{ generate_average('stg_results', '_ca1') }} AS average_ca1,
        {{ generate_average('stg_results', '_ca2') }} AS average_ca2,
        {{ generate_average('stg_results', '_exam') }} AS average_exam,
        {{ generate_average('stg_results', '_total') }} AS average_total_score,
        {{ generate_average('stg_results', '_attendance') }} AS aggregate_attendance_percentage,
        ARRAY_SIZE(SPLIT(extracurricular_activities, ';')) AS extracurricular_activities_count,
        extracurricular_activities,
        extracurricular_activity_feedback,
        health_incidences,
        health_remarks
    FROM {{ ref('stg_results') }}
),

final_table AS (
    SELECT
        *,
        {{ generate_wassce_pass_logic(
            ['english_language_pass', 'mathematics_pass'],
            [
                'civic_education_pass',
                'biology_pass',
                'physics_pass',
                'chemistry_pass',
                'further_mathematics_pass',
                'health_education_pass',
                'computer_science_pass',
                'technical_drawing_pass',
                'food_and_nutrition_pass',
                'agricultural_science_pass',
                'financial_accounting_pass',
                'book_keeping_pass',
                'commerce_pass',
                'data_processing_pass',
                'office_practice_pass',
                'typewriting_pass',
                'economics_pass',
                'government_pass',
                'literature_in_english_pass',
                'christian_religion_knowledge_pass',
                'geography_pass',
                'fine_art_pass'
            ]
        ) }}
    FROM subject_grades
)

SELECT
    student_id,
    academic_year,
    term,
    grade_level,
    {{ generate_subject_case_statements('stg_results') }},
    extracurricular_activities,
    extracurricular_activities_count,
    extracurricular_activity_feedback,
    health_incidences,
    health_remarks,
    average_ca1,
    average_ca2,
    average_exam,
    average_total_score,
    aggregate_attendance_percentage,
    wassce_pass
FROM final_table
