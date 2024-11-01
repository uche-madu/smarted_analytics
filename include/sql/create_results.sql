CREATE OR REPLACE TABLE {{ params.schema_name }}.{{ params.table_name }} (
    student_id STRING,  -- Unique identifier for each student
    name STRING,  -- Full name of the student
    stream STRING,  -- Academic stream the student belongs to
    academic_year STRING,  -- Academic year (e.g., '2022/2023')
    grade_level STRING,  -- Grade level (e.g., 'SS1', 'JS2')
    term STRING,  -- Academic term (e.g., 'First', 'Second')

    -- English Language fields
    english_language_ca1 FLOAT,  
    english_language_ca2 FLOAT,  
    english_language_exam FLOAT,  
    english_language_total FLOAT,  
    english_language_attendance FLOAT,  
    english_language_teacher_remarks TEXT,  
    english_language_teacher_id STRING,  -- Teacher ID for English Language

    -- Mathematics fields
    mathematics_ca1 FLOAT,  
    mathematics_ca2 FLOAT,  
    mathematics_exam FLOAT,  
    mathematics_total FLOAT,  
    mathematics_attendance FLOAT,  
    mathematics_teacher_remarks TEXT,  
    mathematics_teacher_id STRING,  -- Teacher ID for Mathematics

    -- Civic Education fields
    civic_education_ca1 FLOAT,  
    civic_education_ca2 FLOAT,  
    civic_education_exam FLOAT,  
    civic_education_total FLOAT,  
    civic_education_attendance FLOAT,  
    civic_education_teacher_remarks TEXT,  
    civic_education_teacher_id STRING,  -- Teacher ID for Civic Education

    -- Biology fields
    biology_ca1 FLOAT,  
    biology_ca2 FLOAT,  
    biology_exam FLOAT,  
    biology_total FLOAT,  
    biology_attendance FLOAT,  
    biology_teacher_remarks TEXT,  
    biology_teacher_id STRING,  -- Teacher ID for Biology

    -- Physics fields
    physics_ca1 FLOAT,  
    physics_ca2 FLOAT,  
    physics_exam FLOAT,  
    physics_total FLOAT,  
    physics_attendance FLOAT,  
    physics_teacher_remarks TEXT,  
    physics_teacher_id STRING,  -- Teacher ID for Physics

    -- Chemistry fields
    chemistry_ca1 FLOAT,  
    chemistry_ca2 FLOAT,  
    chemistry_exam FLOAT,  
    chemistry_total FLOAT,  
    chemistry_attendance FLOAT,  
    chemistry_teacher_remarks TEXT,  
    chemistry_teacher_id STRING,  -- Teacher ID for Chemistry

    -- Further Mathematics fields
    further_mathematics_ca1 FLOAT,  
    further_mathematics_ca2 FLOAT,  
    further_mathematics_exam FLOAT,  
    further_mathematics_total FLOAT,  
    further_mathematics_attendance FLOAT,  
    further_mathematics_teacher_remarks TEXT,  
    further_mathematics_teacher_id STRING,  -- Teacher ID for Further Mathematics

    -- Health Education fields
    health_education_ca1 FLOAT,  
    health_education_ca2 FLOAT,  
    health_education_exam FLOAT,  
    health_education_total FLOAT,  
    health_education_attendance FLOAT,  
    health_education_teacher_remarks TEXT,  
    health_education_teacher_id STRING,  -- Teacher ID for Health Education

    -- Computer Science fields
    computer_science_ca1 FLOAT,  
    computer_science_ca2 FLOAT,  
    computer_science_exam FLOAT,  
    computer_science_total FLOAT,  
    computer_science_attendance FLOAT,  
    computer_science_teacher_remarks TEXT,  
    computer_science_teacher_id STRING,  -- Teacher ID for Computer Science

    -- Technical Drawing fields
    technical_drawing_ca1 FLOAT,  
    technical_drawing_ca2 FLOAT,  
    technical_drawing_exam FLOAT,  
    technical_drawing_total FLOAT,  
    technical_drawing_attendance FLOAT,  
    technical_drawing_teacher_remarks TEXT,  
    technical_drawing_teacher_id STRING,  -- Teacher ID for Technical Drawing

    -- Food and Nutrition fields
    food_and_nutrition_ca1 FLOAT,  
    food_and_nutrition_ca2 FLOAT,  
    food_and_nutrition_exam FLOAT,  
    food_and_nutrition_total FLOAT,  
    food_and_nutrition_attendance FLOAT,  
    food_and_nutrition_teacher_remarks TEXT,  
    food_and_nutrition_teacher_id STRING,  -- Teacher ID for Food and Nutrition

    -- Agricultural Science fields
    agricultural_science_ca1 FLOAT,  
    agricultural_science_ca2 FLOAT,  
    agricultural_science_exam FLOAT,  
    agricultural_science_total FLOAT,  
    agricultural_science_attendance FLOAT,  
    agricultural_science_teacher_remarks TEXT,  
    agricultural_science_teacher_id STRING,  -- Teacher ID for Agricultural Science

    -- Financial Accounting fields
    financial_accounting_ca1 FLOAT,  
    financial_accounting_ca2 FLOAT,  
    financial_accounting_exam FLOAT,  
    financial_accounting_total FLOAT,  
    financial_accounting_attendance FLOAT,  
    financial_accounting_teacher_remarks TEXT,  
    financial_accounting_teacher_id STRING,  -- Teacher ID for Financial Accounting

    -- Book Keeping fields
    book_keeping_ca1 FLOAT,  
    book_keeping_ca2 FLOAT,  
    book_keeping_exam FLOAT,  
    book_keeping_total FLOAT,  
    book_keeping_attendance FLOAT,  
    book_keeping_teacher_remarks TEXT,  
    book_keeping_teacher_id STRING,  -- Teacher ID for Book Keeping

    -- Commerce fields
    commerce_ca1 FLOAT,  
    commerce_ca2 FLOAT,  
    commerce_exam FLOAT,  
    commerce_total FLOAT,  
    commerce_attendance FLOAT,  
    commerce_teacher_remarks TEXT,  
    commerce_teacher_id STRING,  -- Teacher ID for Commerce

    -- Data Processing fields
    data_processing_ca1 FLOAT,  
    data_processing_ca2 FLOAT,  
    data_processing_exam FLOAT,  
    data_processing_total FLOAT,  
    data_processing_attendance FLOAT,  
    data_processing_teacher_remarks TEXT,  
    data_processing_teacher_id STRING,  -- Teacher ID for Data Processing

    -- Office Practice fields
    office_practice_ca1 FLOAT,  
    office_practice_ca2 FLOAT,  
    office_practice_exam FLOAT,  
    office_practice_total FLOAT,  
    office_practice_attendance FLOAT,  
    office_practice_teacher_remarks TEXT,  
    office_practice_teacher_id STRING,  -- Teacher ID for Office Practice

    -- Typewriting fields
    typewriting_ca1 FLOAT,  
    typewriting_ca2 FLOAT,  
    typewriting_exam FLOAT,  
    typewriting_total FLOAT,  
    typewriting_attendance FLOAT,  
    typewriting_teacher_remarks TEXT,  
    typewriting_teacher_id STRING,  -- Teacher ID for Typewriting

    -- Economics fields
    economics_ca1 FLOAT,  
    economics_ca2 FLOAT,  
    economics_exam FLOAT,  
    economics_total FLOAT,  
    economics_attendance FLOAT,  
    economics_teacher_remarks TEXT,  
    economics_teacher_id STRING,  -- Teacher ID for Economics

    -- Government fields
    government_ca1 FLOAT,  
    government_ca2 FLOAT,  
    government_exam FLOAT,  
    government_total FLOAT,  
    government_attendance FLOAT,  
    government_teacher_remarks TEXT,  
    government_teacher_id STRING,  -- Teacher ID for Government

    -- Literature in English fields
    literature_in_english_ca1 FLOAT,  
    literature_in_english_ca2 FLOAT,  
    literature_in_english_exam FLOAT,  
    literature_in_english_total FLOAT,  
    literature_in_english_attendance FLOAT,  
    literature_in_english_teacher_remarks TEXT,  
    literature_in_english_teacher_id STRING,  -- Teacher ID for Literature in English

    -- Christian Religion Knowledge fields
    christian_religion_knowledge_ca1 FLOAT,  
    christian_religion_knowledge_ca2 FLOAT,  
    christian_religion_knowledge_exam FLOAT,  
    christian_religion_knowledge_total FLOAT,  
    christian_religion_knowledge_attendance FLOAT,  
    christian_religion_knowledge_teacher_remarks TEXT,  
    christian_religion_knowledge_teacher_id STRING,  -- Teacher ID for Christian Religion Knowledge

    -- Geography fields
    geography_ca1 FLOAT,  
    geography_ca2 FLOAT,  
    geography_exam FLOAT,  
    geography_total FLOAT,  
    geography_attendance FLOAT,  
    geography_teacher_remarks TEXT,  
    geography_teacher_id STRING,  -- Teacher ID for Geography

    -- Fine Art fields
    fine_art_ca1 FLOAT,  
    fine_art_ca2 FLOAT,  
    fine_art_exam FLOAT,  
    fine_art_total FLOAT,  
    fine_art_attendance FLOAT,  
    fine_art_teacher_remarks TEXT,  
    fine_art_teacher_id STRING,  -- Teacher ID for Fine Art

    -- Extracurricular Activities
    extracurricular_activities TEXT,           -- List of activities participated in during the term
    extracurricular_activity_feedback TEXT,    -- Aggregated feedback on each activity

    -- Health Records
    health_incidences INT,                     -- Count of health-related incidences in the term
    health_remarks TEXT,                       -- Remarks related to health records for the term

    created_at TIMESTAMP,
    updated_at TIMESTAMP  
);
