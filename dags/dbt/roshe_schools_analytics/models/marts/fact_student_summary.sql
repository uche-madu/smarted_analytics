WITH results_summary AS (
    SELECT
        student_id,

        -- Average score across all subjects over all terms
        {{ calculate_average_score_per_term([
            'english_language', 'mathematics', 'civic_education', 'biology', 'chemistry', 
            'physics', 'further_mathematics', 'health_education', 'computer_science', 
            'technical_drawing', 'food_and_nutrition', 'agricultural_science', 
            'financial_accounting', 'book_keeping', 'commerce', 'data_processing', 
            'office_practice', 'typewriting', 'economics', 'government', 'literature_in_english', 
            'christian_religion_knowledge', 'geography', 'fine_art'
        ]) }} AS cumulative_average_subject_score,

        -- Total score for all subjects over all terms
        {{ calculate_total_term_score([
            'english_language', 'mathematics', 'civic_education', 'biology', 'chemistry', 
            'physics', 'further_mathematics', 'health_education', 'computer_science', 
            'technical_drawing', 'food_and_nutrition', 'agricultural_science', 
            'financial_accounting', 'book_keeping', 'commerce', 'data_processing', 
            'office_practice', 'typewriting', 'economics', 'government', 'literature_in_english', 
            'christian_religion_knowledge', 'geography', 'fine_art'
        ]) }} AS cumulative_overall_term_score,

        -- Total subjects taken over all terms
        {{ count_subjects_registered([
            'english_language', 'mathematics', 'civic_education', 'biology', 'chemistry', 
            'physics', 'further_mathematics', 'health_education', 'computer_science', 
            'technical_drawing', 'food_and_nutrition', 'agricultural_science', 
            'financial_accounting', 'book_keeping', 'commerce', 'data_processing', 
            'office_practice', 'typewriting', 'economics', 'government', 'literature_in_english', 
            'christian_religion_knowledge', 'geography', 'fine_art'
        ]) }} AS cumulative_subjects_taken,

        -- Total subjects passed over all terms
        {{ count_subjects_passed([
            'english_language_pass', 'mathematics_pass', 'civic_education_pass', 'biology_pass', 
            'chemistry_pass', 'physics_pass', 'further_mathematics_pass', 'health_education_pass', 
            'computer_science_pass', 'technical_drawing_pass', 'food_and_nutrition_pass', 
            'agricultural_science_pass', 'financial_accounting_pass', 'book_keeping_pass', 
            'commerce_pass', 'data_processing_pass', 'office_practice_pass', 'typewriting_pass', 
            'economics_pass', 'government_pass', 'literature_in_english_pass', 
            'christian_religion_knowledge_pass', 'geography_pass', 'fine_art_pass'
        ]) }} AS cumulative_subjects_passed,

        -- Cumulative average over all terms
        {{ cumulative_term_average([
            'english_language_pass', 'mathematics_pass', 'civic_education_pass', 'biology_pass', 
            'chemistry_pass', 'physics_pass', 'further_mathematics_pass', 'health_education_pass', 
            'computer_science_pass', 'technical_drawing_pass', 'food_and_nutrition_pass', 
            'agricultural_science_pass', 'financial_accounting_pass', 'book_keeping_pass', 
            'commerce_pass', 'data_processing_pass', 'office_practice_pass', 'typewriting_pass', 
            'economics_pass', 'government_pass', 'literature_in_english_pass', 
            'christian_religion_knowledge_pass', 'geography_pass', 'fine_art_pass'
        ]) }} AS overall_cumulative_average,

        -- Calculate WASSCE pass likelihood based on pass percentage over all terms
        100
        * SUM(CASE WHEN wassce_pass = 'Pass' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0) AS wassce_pass_likelihood
    FROM {{ ref('dim_results') }}
    GROUP BY student_id
),

student_info AS (
    SELECT
        student_id,
        gender,
        CONCAT_WS(' ', first_name, middle_name, last_name) AS student_name,
        age,
        state_of_origin,
        blood_group,
        genotype,
        registration_year
    FROM {{ ref('dim_students') }}
),

health_event_details AS (
    SELECT
        student_id,
        COUNT(record_id) AS total_health_checkups,
        COUNT(CASE WHEN admitted = 'Yes' THEN 1 ELSE 0 END) AS total_admissions,
        COUNT(DISTINCT health_issues) AS unique_health_issues,
        MIN(admission_date) AS first_admission_date,
        MAX(discharge_date) AS most_recent_discharge_date,
        DATEDIFF('day', MIN(admission_date), MAX(discharge_date)) AS total_days_admitted
    FROM {{ ref('dim_health_records') }}
    GROUP BY student_id
),

student_activity_summary AS (
    SELECT
        student_id,
        COUNT(DISTINCT activity_id) AS num_activities,
        SUM(CASE WHEN participation_level = 'Beginner' THEN 1 ELSE 0 END) AS beginner_activities,
        SUM(CASE WHEN participation_level = 'Intermediate' THEN 1 ELSE 0 END)
            AS intermediate_activities,
        SUM(CASE WHEN participation_level = 'Advanced' THEN 1 ELSE 0 END) AS advanced_activities
    FROM {{ ref('dim_extracurricular_activities') }}
    GROUP BY student_id
)

-- Final Fact Table
SELECT
    rs.student_id,
    si.student_name,
    si.gender,
    si.age,
    si.state_of_origin,
    si.blood_group,
    si.genotype,
    si.registration_year,
    rs.cumulative_average_subject_score,
    rs.cumulative_overall_term_score,
    rs.cumulative_subjects_taken,
    rs.cumulative_subjects_passed,
    rs.overall_cumulative_average,
    rs.wassce_pass_likelihood,
    he.total_health_checkups,
    he.total_admissions,
    he.unique_health_issues,
    he.total_days_admitted,
    sa.num_activities,
    sa.beginner_activities,
    sa.intermediate_activities,
    sa.advanced_activities,
    CURRENT_TIMESTAMP AS created_at,
    CURRENT_TIMESTAMP AS updated_at
FROM results_summary AS rs
LEFT JOIN student_info AS si ON rs.student_id = si.student_id
LEFT JOIN health_event_details AS he ON rs.student_id = he.student_id
LEFT JOIN student_activity_summary AS sa ON rs.student_id = sa.student_id
