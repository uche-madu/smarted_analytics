MERGE INTO {{ params.schema_name }}.{{ params.table_name }} AS target
USING @{{ params.schema_name }}.{{ params.stage_name }}/{{ params.file_name }}
(FILE_FORMAT => 'csv_format_with_quotes') AS source
ON target.student_id = source.$1
WHEN MATCHED THEN
   UPDATE SET
       target.first_name = source.$2,
       target.middle_name = source.$3,
       target.last_name = source.$4,
       target.gender = source.$5,
       target.date_of_birth = source.$6,
       target.stream = source.$7,
       target.grade_level = source.$8,
       target.blood_group = source.$9,
       target.genotype = source.$10,
       target.state_of_origin = source.$11,
       target.address = source.$12,
       target.parent_id = source.$13,
       target.registration_date = source.$14,
       target.updated_at = source.$16
WHEN NOT MATCHED THEN
   INSERT (student_id, first_name, middle_name, last_name, gender, date_of_birth, stream, grade_level, blood_group, genotype, state_of_origin, address, parent_id, registration_date, created_at, updated_at)
   VALUES (source.$1, source.$2, source.$3, source.$4, source.$5, source.$6, source.$7, source.$8, source.$9, source.$10, source.$11, source.$12, source.$13, source.$14, source.$15, source.$16);
