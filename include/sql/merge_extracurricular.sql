MERGE INTO {{ params.schema_name }}.{{ params.table_name }} AS target
USING @{{ params.schema_name }}.{{ params.stage_name }}/{{ params.file_name }}
(FILE_FORMAT => 'csv_format_with_quotes') AS source
ON target.activity_id = source.$1
   AND target.student_id = source.$3
WHEN MATCHED THEN
   UPDATE SET
       target.activity_name = source.$2,
       target.participation_level = source.$4,
       target.teacher_id = source.$5,
       target.activity_type = source.$6,
       target.activity_frequency = source.$7,
       target.role_in_activity = source.$8,
       target.achievement = source.$9,
       target.attendance_percentage = source.$10,
       target.instructor_feedback = source.$11,
       target.activity_status = source.$12,
       target.date_joined = source.$13,
       target.updated_at = source.$15
WHEN NOT MATCHED THEN
   INSERT (activity_id, activity_name, student_id, participation_level, teacher_id, activity_type, activity_frequency, role_in_activity, achievement, attendance_percentage, instructor_feedback, activity_status, date_joined, created_at, updated_at)
   VALUES (source.$1, source.$2, source.$3, source.$4, source.$5, source.$6, source.$7, source.$8, source.$9, source.$10, source.$11, source.$12, source.$13, source.$14, source.$15);
