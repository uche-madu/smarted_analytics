-- Added: Ensured all relevant attendance fields are present in subject_grades
WITH subject_grades AS (
    SELECT
        student_id,
        name,
        stream,
        academic_year,
        class_arm,
        grade_level,
        term,
        {{ generate_subject_case_statements('stg_results') }},
        {{ generate_aggregate_attendance('stg_results') }} AS aggregate_attendance_percentage,
        {{ calculate_average_total_score('stg_results') }}  AS average_total_score,
        created_at,
        updated_at
    FROM {{ ref('stg_results') }}
),

final_table AS (
    SELECT
        *,  -- Pull all fields from subject_grades
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

-- Final ordered SELECT, visible generated fields for clarity
SELECT
    student_id,
    name,
    stream,
    academic_year,
    class_arm,
    grade_level,
    term,
    {{ generate_subject_case_statements('stg_results') }},
    wassce_pass,
    aggregate_attendance_percentage,
    average_total_score,
    created_at,
    updated_at
FROM final_table
