MERGE INTO {{ params.schema_name }}.health_records AS target
USING @{{ params.schema_name }}.{{ params.stage_name }}/{{ params.file_name }} AS source
ON target.record_id = source.$1
WHEN MATCHED THEN
   UPDATE SET
       target.student_id = source.$2,
       target.checkup_date = source.$3,
       target.health_issues = source.$4,
       target.treatment = source.$5,
       target.admitted = source.$6,
       target.admission_date = source.$7,
       target.discharge_date = source.$8,
       target.doctor = source.$9,
       target.follow_up_date = source.$10,
       target.updated_at = CURRENT_TIMESTAMP  -- Updates timestamp for modifications
WHEN NOT MATCHED THEN
   INSERT (record_id, student_id, checkup_date, health_issues, treatment, admitted, admission_date, discharge_date, doctor, follow_up_date, created_at, updated_at)
   VALUES (source.$1, source.$2, source.$3, source.$4, source.$5, source.$6, source.$7, source.$8, source.$9, source.$10, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);  -- Sets created_at and updated_at for new records
