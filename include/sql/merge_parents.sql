MERGE INTO {{ params.schema_name }}.{{ params.table_name }} AS target
USING @{{ params.schema_name }}.{{ params.stage_name }}/{{ params.file_name }}
(FILE_FORMAT => 'csv_format_with_quotes') AS source
ON target.parent_id = source.$1
WHEN MATCHED THEN
   UPDATE SET
       target.first_name = source.$2,
       target.middle_name = source.$3,
       target.last_name = source.$4,
       target.gender = source.$5,
       target.marital_status = source.$6,
       target.phone_number = source.$7,
       target.email = source.$8,
       target.address = source.$9,
       target.relationship_to_student = source.$10,
       target.income_bracket = source.$11,
       target.education_level = source.$12,
       target.occupation = source.$13,
       target.employment_type = source.$14,
       target.industry = source.$15,
       target.engagement_level = source.$16,
       target.home_language = source.$17,
       target.number_of_children = source.$18,
       target.alternate_contact_number = source.$19,
       target.parent_teacher_meeting_attendance = source.$20,
       target.volunteer_activities_count = source.$21,
       target.recent_interaction_date = source.$22,
       target.updated_at = source.$24
WHEN NOT MATCHED THEN
   INSERT (
       parent_id, first_name, middle_name, last_name, gender, marital_status, phone_number, email, address, 
       relationship_to_student, income_bracket, education_level, occupation, employment_type, 
       industry, engagement_level, home_language, number_of_children, alternate_contact_number, 
       parent_teacher_meeting_attendance, volunteer_activities_count, recent_interaction_date, 
       created_at, updated_at
   )
   VALUES (
       source.$1, source.$2, source.$3, source.$4, source.$5, source.$6, source.$7, source.$8, source.$9,
       source.$10, source.$11, source.$12, source.$13, source.$14, source.$15, source.$16, source.$17,
       source.$18, source.$19, source.$20, source.$21, source.$22, source.$23, source.$24
   );
