MERGE INTO {{ params.schema_name }}.parents AS target
USING @{{ params.schema_name }}.{{ params.stage_name }}/{{ params.file_name }} AS source
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
       target.occupation = source.$10,
       target.relationship_to_student = source.$11,
       target.updated_at = CURRENT_TIMESTAMP  -- Updates timestamp for modifications
WHEN NOT MATCHED THEN
   INSERT (parent_id, first_name, middle_name, last_name, gender, marital_status, phone_number, email, address, occupation, relationship_to_student, created_at, updated_at)
   VALUES (source.$1, source.$2, source.$3, source.$4, source.$5, source.$6, source.$7, source.$8, source.$9, source.$10, source.$11, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);  -- Sets created_at and updated_at for new records
