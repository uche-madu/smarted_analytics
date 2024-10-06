CREATE OR REPLACE TABLE {{ params.schema_name }}.{{ params.table_name }} (
    student_id STRING,  -- Unique identifier for each student
    name STRING,  -- Full name of the student
    stream STRING,  -- Academic stream the student belongs to
    academic_year STRING,  -- Academic year (e.g., '2022/2023')
    class_arm STRING,  -- Class arm (e.g., 'A', 'B')
    grade_level STRING,  -- Grade level (e.g., 'SS1', 'JS2')
    term STRING,  -- Academic term (e.g., 'First', 'Second')

    -- English Language fields
    english_language_ca1 FLOAT,  -- English Language Continuous Assessment 1 score
    english_language_ca2 FLOAT,  -- English Language Continuous Assessment 2 score
    english_language_exam FLOAT,  -- English Language Exam score
    english_language_total FLOAT,  -- Total English Language score
    english_language_attendance FLOAT,  -- Attendance percentage
    english_language_teacher_remarks TEXT,  -- Teacher's remarks

    -- Mathematics fields
    mathematics_ca1 FLOAT,  
    mathematics_ca2 FLOAT,  
    mathematics_exam FLOAT,  
    mathematics_total FLOAT,  
    mathematics_attendance FLOAT,  
    mathematics_teacher_remarks TEXT,  

    -- Civic Education fields
    civic_education_ca1 FLOAT,  
    civic_education_ca2 FLOAT,  
    civic_education_exam FLOAT,  
    civic_education_total FLOAT,  
    civic_education_attendance FLOAT,  
    civic_education_teacher_remarks TEXT,  

    -- Biology fields
    biology_ca1 FLOAT,  
    biology_ca2 FLOAT,  
    biology_exam FLOAT,  
    biology_total FLOAT,  
    biology_attendance FLOAT,  
    biology_teacher_remarks TEXT,  

    -- Physics fields
    physics_ca1 FLOAT,  
    physics_ca2 FLOAT,  
    physics_exam FLOAT,  
    physics_total FLOAT,  
    physics_attendance FLOAT,  
    physics_teacher_remarks TEXT,  

    -- Chemistry fields
    chemistry_ca1 FLOAT,  
    chemistry_ca2 FLOAT,  
    chemistry_exam FLOAT,  
    chemistry_total FLOAT,  
    chemistry_attendance FLOAT,  
    chemistry_teacher_remarks TEXT,  

    -- Further Mathematics fields
    further_mathematics_ca1 FLOAT,  
    further_mathematics_ca2 FLOAT,  
    further_mathematics_exam FLOAT,  
    further_mathematics_total FLOAT,  
    further_mathematics_attendance FLOAT,  
    further_mathematics_teacher_remarks TEXT,  

    -- Health Education fields
    health_education_ca1 FLOAT,  
    health_education_ca2 FLOAT,  
    health_education_exam FLOAT,  
    health_education_total FLOAT,  
    health_education_attendance FLOAT,  
    health_education_teacher_remarks TEXT,  

    -- Computer Science fields
    computer_science_ca1 FLOAT,  
    computer_science_ca2 FLOAT,  
    computer_science_exam FLOAT,  
    computer_science_total FLOAT,  
    computer_science_attendance FLOAT,  
    computer_science_teacher_remarks TEXT,  

    -- Technical Drawing fields
    technical_drawing_ca1 FLOAT,  
    technical_drawing_ca2 FLOAT,  
    technical_drawing_exam FLOAT,  
    technical_drawing_total FLOAT,  
    technical_drawing_attendance FLOAT,  
    technical_drawing_teacher_remarks TEXT,  

    -- Food and Nutrition fields
    food_and_nutrition_ca1 FLOAT,  
    food_and_nutrition_ca2 FLOAT,  
    food_and_nutrition_exam FLOAT,  
    food_and_nutrition_total FLOAT,  
    food_and_nutrition_attendance FLOAT,  
    food_and_nutrition_teacher_remarks TEXT,  

    -- Agricultural Science fields
    agricultural_science_ca1 FLOAT,  
    agricultural_science_ca2 FLOAT,  
    agricultural_science_exam FLOAT,  
    agricultural_science_total FLOAT,  
    agricultural_science_attendance FLOAT,  
    agricultural_science_teacher_remarks TEXT,  

    -- Financial Accounting fields
    financial_accounting_ca1 FLOAT,  
    financial_accounting_ca2 FLOAT,  
    financial_accounting_exam FLOAT,  
    financial_accounting_total FLOAT,  
    financial_accounting_attendance FLOAT,  
    financial_accounting_teacher_remarks TEXT,  

    -- Book Keeping fields
    book_keeping_ca1 FLOAT,  
    book_keeping_ca2 FLOAT,  
    book_keeping_exam FLOAT,  
    book_keeping_total FLOAT,  
    book_keeping_attendance FLOAT,  
    book_keeping_teacher_remarks TEXT,  

    -- Commerce fields
    commerce_ca1 FLOAT,  
    commerce_ca2 FLOAT,  
    commerce_exam FLOAT,  
    commerce_total FLOAT,  
    commerce_attendance FLOAT,  
    commerce_teacher_remarks TEXT,  

    -- Data Processing fields
    data_processing_ca1 FLOAT,  
    data_processing_ca2 FLOAT,  
    data_processing_exam FLOAT,  
    data_processing_total FLOAT,  
    data_processing_attendance FLOAT,  
    data_processing_teacher_remarks TEXT,  

    -- Office Practice fields
    office_practice_ca1 FLOAT,  
    office_practice_ca2 FLOAT,  
    office_practice_exam FLOAT,  
    office_practice_total FLOAT,  
    office_practice_attendance FLOAT,  
    office_practice_teacher_remarks TEXT,  

    -- Typewriting fields
    typewriting_ca1 FLOAT,  
    typewriting_ca2 FLOAT,  
    typewriting_exam FLOAT,  
    typewriting_total FLOAT,  
    typewriting_attendance FLOAT,  
    typewriting_teacher_remarks TEXT,  

    -- Economics fields
    economics_ca1 FLOAT,  
    economics_ca2 FLOAT,  
    economics_exam FLOAT,  
    economics_total FLOAT,  
    economics_attendance FLOAT,  
    economics_teacher_remarks TEXT,  

    -- Government fields
    government_ca1 FLOAT,  
    government_ca2 FLOAT,  
    government_exam FLOAT,  
    government_total FLOAT,  
    government_attendance FLOAT,  
    government_teacher_remarks TEXT,  

    -- Literature in English fields
    literature_in_english_ca1 FLOAT,  
    literature_in_english_ca2 FLOAT,  
    literature_in_english_exam FLOAT,  
    literature_in_english_total FLOAT,  
    literature_in_english_attendance FLOAT,  
    literature_in_english_teacher_remarks TEXT,  

    -- Christian Religion Knowledge fields
    christian_religion_knowledge_ca1 FLOAT,  
    christian_religion_knowledge_ca2 FLOAT,  
    christian_religion_knowledge_exam FLOAT,  
    christian_religion_knowledge_total FLOAT,  
    christian_religion_knowledge_attendance FLOAT,  
    christian_religion_knowledge_teacher_remarks TEXT,  

    -- Geography fields
    geography_ca1 FLOAT,  
    geography_ca2 FLOAT,  
    geography_exam FLOAT,  
    geography_total FLOAT,  
    geography_attendance FLOAT,  
    geography_teacher_remarks TEXT,  

    -- Fine Art fields
    fine_art_ca1 FLOAT,  
    fine_art_ca2 FLOAT,  
    fine_art_exam FLOAT,  
    fine_art_total FLOAT,  
    fine_art_attendance FLOAT,  
    fine_art_teacher_remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);
