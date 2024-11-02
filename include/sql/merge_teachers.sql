MERGE INTO {{ params.schema_name }}.{{ params.table_name }} AS target
USING @{{ params.schema_name }}.{{ params.stage_name }}/{{ params.file_name }}
(FILE_FORMAT => 'csv_format_with_quotes') AS source
ON target.teacher_id = source.$1
WHEN MATCHED THEN
   UPDATE SET
       target.first_name = source.$2,
       target.middle_name = source.$3,
       target.last_name = source.$4,
       target.gender = source.$5,
       target.date_of_birth = source.$6,
       target.phone_number = source.$7,
       target.email = source.$8,
       target.address = source.$9,
       target.hire_date = source.$10,
       target.subject = source.$11,
       target.qualification = source.$12,
       target.years_of_experience = source.$13,
       target.updated_at = source.$15
WHEN NOT MATCHED THEN
   INSERT (teacher_id, first_name, middle_name, last_name, gender, date_of_birth, phone_number, email, address, hire_date, subject, qualification, years_of_experience, created_at, updated_at)
   VALUES (source.$1, source.$2, source.$3, source.$4, source.$5, source.$6, source.$7, source.$8, source.$9, source.$10, source.$11, source.$12, source.$13, source.$14, source.$15);
