MERGE INTO {{ params.schema_name }}.{{ params.table_name }} AS target
USING @{{ params.schema_name }}.{{ params.stage_name }}/{{ params.file_name }}
(FILE_FORMAT => 'csv_format_with_quotes') AS source
ON target.student_id = source.$1
   AND target.grade_level = source.$5
   AND target.term = source.$6
WHEN MATCHED THEN
   UPDATE SET
       target.name = source.$2,
       target.stream = source.$3,
       target.academic_year = source.$4,

       -- English Language fields
       target.english_language_ca1 = source.$7,
       target.english_language_ca2 = source.$8,
       target.english_language_exam = source.$9,
       target.english_language_total = source.$10,
       target.english_language_attendance = source.$11,
       target.english_language_teacher_remarks = source.$12,
       target.english_language_teacher_id = source.$13,

       -- Mathematics fields
       target.mathematics_ca1 = source.$14,
       target.mathematics_ca2 = source.$15,
       target.mathematics_exam = source.$16,
       target.mathematics_total = source.$17,
       target.mathematics_attendance = source.$18,
       target.mathematics_teacher_remarks = source.$19,
       target.mathematics_teacher_id = source.$20,

       -- Civic Education fields
       target.civic_education_ca1 = source.$21,
       target.civic_education_ca2 = source.$22,
       target.civic_education_exam = source.$23,
       target.civic_education_total = source.$24,
       target.civic_education_attendance = source.$25,
       target.civic_education_teacher_remarks = source.$26,
       target.civic_education_teacher_id = source.$27,

       -- Biology fields
       target.biology_ca1 = source.$28,
       target.biology_ca2 = source.$29,
       target.biology_exam = source.$30,
       target.biology_total = source.$31,
       target.biology_attendance = source.$32,
       target.biology_teacher_remarks = source.$33,
       target.biology_teacher_id = source.$34,

       -- Physics fields
       target.physics_ca1 = source.$35,
       target.physics_ca2 = source.$36,
       target.physics_exam = source.$37,
       target.physics_total = source.$38,
       target.physics_attendance = source.$39,
       target.physics_teacher_remarks = source.$40,
       target.physics_teacher_id = source.$41,

       -- Chemistry fields
       target.chemistry_ca1 = source.$42,
       target.chemistry_ca2 = source.$43,
       target.chemistry_exam = source.$44,
       target.chemistry_total = source.$45,
       target.chemistry_attendance = source.$46,
       target.chemistry_teacher_remarks = source.$47,
       target.chemistry_teacher_id = source.$48,

       -- Further Mathematics fields
       target.further_mathematics_ca1 = source.$49,
       target.further_mathematics_ca2 = source.$50,
       target.further_mathematics_exam = source.$51,
       target.further_mathematics_total = source.$52,
       target.further_mathematics_attendance = source.$53,
       target.further_mathematics_teacher_remarks = source.$54,
       target.further_mathematics_teacher_id = source.$55,

       -- Health Education fields
       target.health_education_ca1 = source.$56,
       target.health_education_ca2 = source.$57,
       target.health_education_exam = source.$58,
       target.health_education_total = source.$59,
       target.health_education_attendance = source.$60,
       target.health_education_teacher_remarks = source.$61,
       target.health_education_teacher_id = source.$62,

       -- Computer Science fields
       target.computer_science_ca1 = source.$63,
       target.computer_science_ca2 = source.$64,
       target.computer_science_exam = source.$65,
       target.computer_science_total = source.$66,
       target.computer_science_attendance = source.$67,
       target.computer_science_teacher_remarks = source.$68,
       target.computer_science_teacher_id = source.$69,

       -- Technical Drawing fields
       target.technical_drawing_ca1 = source.$76,
       target.technical_drawing_ca2 = source.$77,
       target.technical_drawing_exam = source.$78,
       target.technical_drawing_total = source.$79,
       target.technical_drawing_attendance = source.$80,
       target.technical_drawing_teacher_remarks = source.$81,
       target.technical_drawing_teacher_id = source.$82,

       -- Food and Nutrition fields
       target.food_and_nutrition_ca1 = source.$83,
       target.food_and_nutrition_ca2 = source.$84,
       target.food_and_nutrition_exam = source.$85,
       target.food_and_nutrition_total = source.$86,
       target.food_and_nutrition_attendance = source.$87,
       target.food_and_nutrition_teacher_remarks = source.$88,
       target.food_and_nutrition_teacher_id = source.$89,

       -- Agricultural Science fields
       target.agricultural_science_ca1 = source.$90,
       target.agricultural_science_ca2 = source.$91,
       target.agricultural_science_exam = source.$92,
       target.agricultural_science_total = source.$93,
       target.agricultural_science_attendance = source.$94,
       target.agricultural_science_teacher_remarks = source.$95,
       target.agricultural_science_teacher_id = source.$96,

       -- Financial Accounting fields
       target.financial_accounting_ca1 = source.$97,
       target.financial_accounting_ca2 = source.$98,
       target.financial_accounting_exam = source.$99,
       target.financial_accounting_total = source.$100,
       target.financial_accounting_attendance = source.$101,
       target.financial_accounting_teacher_remarks = source.$102,
       target.financial_accounting_teacher_id = source.$103,

       -- Book Keeping fields
       target.book_keeping_ca1 = source.$104,
       target.book_keeping_ca2 = source.$105,
       target.book_keeping_exam = source.$106,
       target.book_keeping_total = source.$107,
       target.book_keeping_attendance = source.$108,
       target.book_keeping_teacher_remarks = source.$109,
       target.book_keeping_teacher_id = source.$110,

       -- Commerce fields
       target.commerce_ca1 = source.$111,
       target.commerce_ca2 = source.$112,
       target.commerce_exam = source.$113,
       target.commerce_total = source.$114,
       target.commerce_attendance = source.$115,
       target.commerce_teacher_remarks = source.$116,
       target.commerce_teacher_id = source.$117,

       -- Data Processing fields
       target.data_processing_ca1 = source.$118,
       target.data_processing_ca2 = source.$119,
       target.data_processing_exam = source.$120,
       target.data_processing_total = source.$121,
       target.data_processing_attendance = source.$122,
       target.data_processing_teacher_remarks = source.$123,
       target.data_processing_teacher_id = source.$124,

       -- Office Practice fields
       target.office_practice_ca1 = source.$125,
       target.office_practice_ca2 = source.$126,
       target.office_practice_exam = source.$127,
       target.office_practice_total = source.$128,
       target.office_practice_attendance = source.$129,
       target.office_practice_teacher_remarks = source.$130,
       target.office_practice_teacher_id = source.$131,

       -- Typewriting fields
       target.typewriting_ca1 = source.$132,
       target.typewriting_ca2 = source.$133,
       target.typewriting_exam = source.$134,
       target.typewriting_total = source.$135,
       target.typewriting_attendance = source.$136,
       target.typewriting_teacher_remarks = source.$137,
       target.typewriting_teacher_id = source.$138,

       -- Economics fields
       target.economics_ca1 = source.$139,
       target.economics_ca2 = source.$140,
       target.economics_exam = source.$141,
       target.economics_total = source.$142,
       target.economics_attendance = source.$143,
       target.economics_teacher_remarks = source.$144,
       target.economics_teacher_id = source.$145,

       -- Government fields
       target.government_ca1 = source.$146,
       target.government_ca2 = source.$147,
       target.government_exam = source.$148,
       target.government_total = source.$149,
       target.government_attendance = source.$150,
       target.government_teacher_remarks = source.$151,
       target.government_teacher_id = source.$152,

       -- Literature in English fields
       target.literature_in_english_ca1 = source.$153,
       target.literature_in_english_ca2 = source.$154,
       target.literature_in_english_exam = source.$155,
       target.literature_in_english_total = source.$156,
       target.literature_in_english_attendance = source.$157,
       target.literature_in_english_teacher_remarks = source.$158,
       target.literature_in_english_teacher_id = source.$159,

       -- Christian Religion Knowledge fields
       target.christian_religion_knowledge_ca1 = source.$160,
       target.christian_religion_knowledge_ca2 = source.$161,
       target.christian_religion_knowledge_exam = source.$162,
       target.christian_religion_knowledge_total = source.$163,
       target.christian_religion_knowledge_attendance = source.$164,
       target.christian_religion_knowledge_teacher_remarks = source.$165,
       target.christian_religion_knowledge_teacher_id = source.$166,

       -- Geography fields
       target.geography_ca1 = source.$167,
       target.geography_ca2 = source.$168,
       target.geography_exam = source.$169,
       target.geography_total = source.$170,
       target.geography_attendance = source.$171,
       target.geography_teacher_remarks = source.$172,
       target.geography_teacher_id = source.$173,

       -- Fine Art fields
       target.fine_art_ca1 = source.$174,
       target.fine_art_ca2 = source.$175,
       target.fine_art_exam = source.$176,
       target.fine_art_total = source.$177,
       target.fine_art_attendance = source.$178,
       target.fine_art_teacher_remarks = source.$179,
       target.fine_art_teacher_id = source.$180,

       -- Extracurricular and Health data
       target.extracurricular_activities = source.$70,
       target.extracurricular_activity_feedback = source.$71,
       target.health_incidences = source.$72,
       target.health_remarks = source.$73,

       target.updated_at = source.$75

WHEN NOT MATCHED THEN
   INSERT (student_id, name, stream, academic_year, grade_level, term,
           english_language_ca1, english_language_ca2, english_language_exam, english_language_total,
           english_language_attendance, english_language_teacher_remarks, english_language_teacher_id,
           mathematics_ca1, mathematics_ca2, mathematics_exam, mathematics_total,
           mathematics_attendance, mathematics_teacher_remarks, mathematics_teacher_id,
           civic_education_ca1, civic_education_ca2, civic_education_exam, civic_education_total,
           civic_education_attendance, civic_education_teacher_remarks, civic_education_teacher_id,
           biology_ca1, biology_ca2, biology_exam, biology_total,
           biology_attendance, biology_teacher_remarks, biology_teacher_id,
           physics_ca1, physics_ca2, physics_exam, physics_total,
           physics_attendance, physics_teacher_remarks, physics_teacher_id,
           chemistry_ca1, chemistry_ca2, chemistry_exam, chemistry_total,
           chemistry_attendance, chemistry_teacher_remarks, chemistry_teacher_id,
           further_mathematics_ca1, further_mathematics_ca2, further_mathematics_exam, further_mathematics_total,
           further_mathematics_attendance, further_mathematics_teacher_remarks, further_mathematics_teacher_id,
           health_education_ca1, health_education_ca2, health_education_exam, health_education_total,
           health_education_attendance, health_education_teacher_remarks, health_education_teacher_id,
           computer_science_ca1, computer_science_ca2, computer_science_exam, computer_science_total,
           computer_science_attendance, computer_science_teacher_remarks, computer_science_teacher_id,
           technical_drawing_ca1, technical_drawing_ca2, technical_drawing_exam, technical_drawing_total,
           technical_drawing_attendance, technical_drawing_teacher_remarks, technical_drawing_teacher_id,
           food_and_nutrition_ca1, food_and_nutrition_ca2, food_and_nutrition_exam, food_and_nutrition_total,
           food_and_nutrition_attendance, food_and_nutrition_teacher_remarks, food_and_nutrition_teacher_id,
           agricultural_science_ca1, agricultural_science_ca2, agricultural_science_exam, agricultural_science_total,
           agricultural_science_attendance, agricultural_science_teacher_remarks, agricultural_science_teacher_id,
           financial_accounting_ca1, financial_accounting_ca2, financial_accounting_exam, financial_accounting_total,
           financial_accounting_attendance, financial_accounting_teacher_remarks, financial_accounting_teacher_id,
           book_keeping_ca1, book_keeping_ca2, book_keeping_exam, book_keeping_total,
           book_keeping_attendance, book_keeping_teacher_remarks, book_keeping_teacher_id,
           commerce_ca1, commerce_ca2, commerce_exam, commerce_total,
           commerce_attendance, commerce_teacher_remarks, commerce_teacher_id,
           data_processing_ca1, data_processing_ca2, data_processing_exam, data_processing_total,
           data_processing_attendance, data_processing_teacher_remarks, data_processing_teacher_id,
           office_practice_ca1, office_practice_ca2, office_practice_exam, office_practice_total,
           office_practice_attendance, office_practice_teacher_remarks, office_practice_teacher_id,
           typewriting_ca1, typewriting_ca2, typewriting_exam, typewriting_total,
           typewriting_attendance, typewriting_teacher_remarks, typewriting_teacher_id,
           economics_ca1, economics_ca2, economics_exam, economics_total,
           economics_attendance, economics_teacher_remarks, economics_teacher_id,
           government_ca1, government_ca2, government_exam, government_total,
           government_attendance, government_teacher_remarks, government_teacher_id,
           literature_in_english_ca1, literature_in_english_ca2, literature_in_english_exam, literature_in_english_total,
           literature_in_english_attendance, literature_in_english_teacher_remarks, literature_in_english_teacher_id,
           christian_religion_knowledge_ca1, christian_religion_knowledge_ca2, christian_religion_knowledge_exam, christian_religion_knowledge_total,
           christian_religion_knowledge_attendance, christian_religion_knowledge_teacher_remarks, christian_religion_knowledge_teacher_id,
           geography_ca1, geography_ca2, geography_exam, geography_total,
           geography_attendance, geography_teacher_remarks, geography_teacher_id,
           fine_art_ca1, fine_art_ca2, fine_art_exam, fine_art_total,
           fine_art_attendance, fine_art_teacher_remarks, fine_art_teacher_id,
           extracurricular_activities, extracurricular_activity_feedback, health_incidences, health_remarks,
           created_at, updated_at)
   VALUES (
         source.$1,  -- student_id
         source.$2,  -- name
         source.$3,  -- stream
         source.$4,  -- academic_year
         source.$5,  -- grade_level
         source.$6,  -- term
         source.$7,  -- english_language_ca1
         source.$8,  -- english_language_ca2
         source.$9, -- english_language_exam
         source.$10, -- english_language_total
         source.$11, -- english_language_attendance
         source.$12, -- english_language_teacher_remarks
         source.$13, -- english_language_teacher_id
         source.$14, -- mathematics_ca1
         source.$15, -- mathematics_ca2
         source.$16, -- mathematics_exam
         source.$17, -- mathematics_total
         source.$18, -- mathematics_attendance
         source.$19, -- mathematics_teacher_remarks
         source.$20, -- mathematics_teacher_id
         source.$21, -- civic_education_ca1
         source.$22, -- civic_education_ca2
         source.$23, -- civic_education_exam
         source.$24, -- civic_education_total
         source.$25, -- civic_education_attendance
         source.$26, -- civic_education_teacher_remarks
         source.$27, -- civic_education_teacher_id
         source.$28, -- biology_ca1
         source.$29, -- biology_ca2
         source.$30, -- biology_exam
         source.$31, -- biology_total
         source.$32, -- biology_attendance
         source.$33, -- biology_teacher_remarks
         source.$34, -- biology_teacher_id
         source.$35, -- physics_ca1
         source.$36, -- physics_ca2
         source.$37, -- physics_exam
         source.$38, -- physics_total
         source.$39, -- physics_attendance
         source.$40, -- physics_teacher_remarks
         source.$41, -- physics_teacher_id
         source.$42, -- chemistry_ca1
         source.$43, -- chemistry_ca2
         source.$44, -- chemistry_exam
         source.$45, -- chemistry_total
         source.$46, -- chemistry_attendance
         source.$47, -- chemistry_teacher_remarks
         source.$48, -- chemistry_teacher_id
         source.$49, -- further_mathematics_ca1
         source.$50, -- further_mathematics_ca2
         source.$51, -- further_mathematics_exam
         source.$52, -- further_mathematics_total
         source.$53, -- further_mathematics_attendance
         source.$54, -- further_mathematics_teacher_remarks
         source.$55, -- further_mathematics_teacher_id
         source.$56, -- health_education_ca1
         source.$57, -- health_education_ca2
         source.$58, -- health_education_exam
         source.$59, -- health_education_total
         source.$60, -- health_education_attendance
         source.$61, -- health_education_teacher_remarks
         source.$62, -- health_education_teacher_id
         source.$63, -- computer_science_ca1
         source.$64, -- computer_science_ca2
         source.$65, -- computer_science_exam
         source.$66, -- computer_science_total
         source.$67, -- computer_science_attendance
         source.$68, -- computer_science_teacher_remarks
         source.$69, -- computer_science_teacher_id
         source.$76, -- technical_drawing_ca1
         source.$77, -- technical_drawing_ca2
         source.$78, -- technical_drawing_exam
         source.$79, -- technical_drawing_total
         source.$80, -- technical_drawing_attendance
         source.$81, -- technical_drawing_teacher_remarks
         source.$82, -- technical_drawing_teacher_id
         source.$83, -- food_and_nutrition_ca1
         source.$84, -- food_and_nutrition_ca2
         source.$85, -- food_and_nutrition_exam
         source.$86, -- food_and_nutrition_total
         source.$87, -- food_and_nutrition_attendance
         source.$88, -- food_and_nutrition_teacher_remarks
         source.$89, -- food_and_nutrition_teacher_id
         source.$90, -- agricultural_science_ca1
         source.$91, -- agricultural_science_ca2
         source.$92, -- agricultural_science_exam
         source.$93, -- agricultural_science_total
         source.$94, -- agricultural_science_attendance
         source.$95, -- agricultural_science_teacher_remarks
         source.$96, -- agricultural_science_teacher_id
         source.$97, -- financial_accounting_ca1
         source.$98, -- financial_accounting_ca2
         source.$99, -- financial_accounting_exam
         source.$100, -- financial_accounting_total
         source.$101, -- financial_accounting_attendance
         source.$102, -- financial_accounting_teacher_remarks
         source.$103, -- financial_accounting_teacher_id
         source.$104, -- book_keeping_ca1
         source.$105, -- book_keeping_ca2
         source.$106, -- book_keeping_exam
         source.$107, -- book_keeping_total
         source.$108, -- book_keeping_attendance
         source.$109, -- book_keeping_teacher_remarks
         source.$110, -- book_keeping_teacher_id
         source.$111, -- commerce_ca1
         source.$112, -- commerce_ca2
         source.$113, -- commerce_exam
         source.$114, -- commerce_total
         source.$115, -- commerce_attendance
         source.$116, -- commerce_teacher_remarks
         source.$117, -- commerce_teacher_id
         source.$118, -- data_processing_ca1
         source.$119, -- data_processing_ca2
         source.$120, -- data_processing_exam
         source.$121, -- data_processing_total
         source.$122, -- data_processing_attendance
         source.$123, -- data_processing_teacher_remarks
         source.$124, -- data_processing_teacher_id
         source.$125, -- office_practice_ca1
         source.$126, -- office_practice_ca2
         source.$127, -- office_practice_exam
         source.$128, -- office_practice_total
         source.$129, -- office_practice_attendance
         source.$130, -- office_practice_teacher_remarks
         source.$131, -- office_practice_teacher_id
         source.$132, -- typewriting_ca1
         source.$133, -- typewriting_ca2
         source.$134, -- typewriting_exam
         source.$135, -- typewriting_total
         source.$136, -- typewriting_attendance
         source.$137, -- typewriting_teacher_remarks
         source.$138, -- typewriting_teacher_id
         source.$139, -- economics_ca1
         source.$140, -- economics_ca2
         source.$141, -- economics_exam
         source.$142, -- economics_total
         source.$143, -- economics_attendance
         source.$144, -- economics_teacher_remarks
         source.$145, -- economics_teacher_id
         source.$146, -- government_ca1
         source.$147, -- government_ca2
         source.$148, -- government_exam
         source.$149, -- government_total
         source.$150, -- government_attendance
         source.$151, -- government_teacher_remarks
         source.$152, -- government_teacher_id
         source.$153, -- literature_in_english_ca1
         source.$154, -- literature_in_english_ca2
         source.$155, -- literature_in_english_exam
         source.$156, -- literature_in_english_total
         source.$157, -- literature_in_english_attendance
         source.$158, -- literature_in_english_teacher_remarks
         source.$159, -- literature_in_english_teacher_id
         source.$160, -- christian_religion_knowledge_ca1
         source.$161, -- christian_religion_knowledge_ca2
         source.$162, -- christian_religion_knowledge_exam
         source.$163, -- christian_religion_knowledge_total
         source.$164, -- christian_religion_knowledge_attendance
         source.$165, -- christian_religion_knowledge_teacher_remarks
         source.$166, -- christian_religion_knowledge_teacher_id
         source.$167, -- geography_ca1
         source.$168, -- geography_ca2
         source.$169, -- geography_exam
         source.$170, -- geography_total
         source.$171, -- geography_attendance
         source.$172, -- geography_teacher_remarks
         source.$173, -- geography_teacher_id
         source.$174, -- fine_art_ca1
         source.$175, -- fine_art_ca2
         source.$176, -- fine_art_exam
         source.$177, -- fine_art_total
         source.$178, -- fine_art_attendance
         source.$179, -- fine_art_teacher_remarks
         source.$180, -- fine_art_teacher_id
         source.$70,  -- extracurricular_activities
         source.$71,  -- extracurricular_activity_feedback
         source.$72,  -- health_incidences
         source.$73,  -- health_remarks
         source.$74,  -- created_at
         source.$75   -- updated_at
   );
