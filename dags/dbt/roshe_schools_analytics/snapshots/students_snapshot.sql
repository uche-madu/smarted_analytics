{% snapshot students_snapshot %}

{{
    config(
        target_schema='snapshots',
        unique_key='student_id',
        strategy='timestamp',
        updated_at='updated_at',
        invalidate_hard_deletes=True
    )
}}

    WITH student_base AS (
        SELECT
            student_id,
            first_name,
            middle_name,
            last_name,
            gender,
            date_of_birth,

            -- Calculate age dynamically
            grade_level,

            -- Calculate years since registration
            blood_group,

            -- Region grouping based on state of origin
            genotype,

            -- Genotype risk category
            state_of_origin,

            -- Blood group compatibility category
            address,

            -- Other fields retained as is
            parent_id,
            registration_date,
            created_at,
            updated_at,
            DATE_PART('year', CURRENT_DATE) - DATE_PART('year', date_of_birth) AS age,
            DATE_PART('year', CURRENT_DATE)
            - DATE_PART('year', registration_date) AS years_since_registration,
            CASE
                WHEN
                    state_of_origin IN ('Lagos', 'Ogun', 'Oyo', 'Ondo', 'Osun', 'Ekiti')
                    THEN 'South-West'
                WHEN
                    state_of_origin IN ('Abia', 'Anambra', 'Ebonyi', 'Enugu', 'Imo')
                    THEN 'South-East'
                WHEN
                    state_of_origin IN ('Akwa Ibom', 'Cross River', 'Bayelsa', 'Rivers')
                    THEN 'South-South'
                WHEN
                    state_of_origin IN (
                        'Benue', 'Kogi', 'Kwara', 'Nasarawa', 'Niger', 'Plateau', 'FCT'
                    )
                    THEN 'North-Central'
                WHEN
                    state_of_origin IN ('Adamawa', 'Bauchi', 'Borno', 'Gombe', 'Taraba', 'Yobe')
                    THEN 'North-East'
                WHEN
                    state_of_origin IN ('Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Sokoto', 'Zamfara')
                    THEN 'North-West'
                ELSE 'Other'
            END AS region,
            CASE
                WHEN genotype = 'SS' THEN 'High Risk'
                WHEN genotype IN ('AS', 'AC') THEN 'Carrier'
                WHEN genotype = 'AA' THEN 'Normal'
            END AS genotype_risk_category,
            CASE
                WHEN blood_group = 'O-' THEN 'Universal Donor'
                WHEN blood_group = 'AB+' THEN 'Universal Recipient'
                ELSE 'Other'
            END AS blood_group_category
        FROM {{ ref('stg_students') }}
    )

    SELECT * FROM student_base

{% endsnapshot %}
