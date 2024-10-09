WITH subject_grades AS (
    SELECT
        student_id,
        name,
        stream,
        academic_year,
        class_arm,
        grade_level,
        term,
        {{ generate_subject_fields([
            'english_language', 
            'mathematics', 
            'civic_education',
            'biology',
            'physics',
            'chemistry',
            'further_mathematics',
            'health_education',
            'computer_science',
            'technical_drawing',
            'food_and_nutrition',
            'agricultural_science',
            'financial_accounting',
            'book_keeping',
            'commerce',
            'data_processing',
            'office_practice',
            'typewriting',
            'economics',
            'government',
            'literature_in_english',
            'christian_religion_knowledge',
            'geography',
            'fine_art'
        ]) }},
        created_at,
        updated_at
    FROM {{ ref('stg_results') }}
),

final_table AS (
    SELECT
        student_id,
        name,
        stream,
        academic_year,
        class_arm,
        grade_level,
        term,
        {{ generate_subject_fields([
            'english_language', 
            'mathematics', 
            'civic_education',
            'biology',
            'physics',
            'chemistry',
            'further_mathematics',
            'health_education',
            'computer_science',
            'technical_drawing',
            'food_and_nutrition',
            'agricultural_science',
            'financial_accounting',
            'book_keeping',
            'commerce',
            'data_processing',
            'office_practice',
            'typewriting',
            'economics',
            'government',
            'literature_in_english',
            'christian_religion_knowledge',
            'geography',
            'fine_art'
        ]) }},
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
        ) }},
        created_at,
        updated_at
    FROM subject_grades
)

SELECT
    student_id,
    name,
    stream,
    academic_year,
    class_arm,
    grade_level,
    term,
    -- Dynamically expand all the subject fields generated
    {{ generate_subject_fields([
        'english_language', 
        'mathematics', 
        'civic_education',
        'biology',
        'physics',
        'chemistry',
        'further_mathematics',
        'health_education',
        'computer_science',
        'technical_drawing',
        'food_and_nutrition',
        'agricultural_science',
        'financial_accounting',
        'book_keeping',
        'commerce',
        'data_processing',
        'office_practice',
        'typewriting',
        'economics',
        'government',
        'literature_in_english',
        'christian_religion_knowledge',
        'geography',
        'fine_art'
    ]) }},
    wassce_pass,
    created_at,
    updated_at
FROM final_table