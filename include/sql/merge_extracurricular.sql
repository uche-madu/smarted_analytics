MERGE INTO {{ params.schema_name }}.extracurricular_activities AS target
USING @{{ params.schema_name }}.{{ params.stage_name }}/{{ params.file_name }} AS source
ON target.activity_id = source.$1
WHEN MATCHED THEN
   UPDATE SET
       target.activity_name = source.$2,
       target.student_id = source.$3,
       target.participation_level = source.$4,
       target.teacher_id = source.$5,
       target.date_joined = source.$6,
       target.updated_at = CURRENT_TIMESTAMP  -- Updates timestamp for modifications
WHEN NOT MATCHED THEN
   INSERT (activity_id, activity_name, student_id, participation_level, teacher_id, date_joined, created_at, updated_at)
   VALUES (source.$1, source.$2, source.$3, source.$4, source.$5, source.$6, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);  -- Sets created_at and updated_at for new records
