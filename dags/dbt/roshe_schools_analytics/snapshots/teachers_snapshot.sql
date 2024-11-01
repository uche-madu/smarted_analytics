{% snapshot teachers_snapshot %}

{{
    config(
        target_schema='snapshots',
        unique_key='teacher_id',
        strategy='timestamp',
        updated_at='updated_at',
        invalidate_hard_deletes=True
    )
}}

SELECT 
    teacher_id,
    first_name,
    middle_name,
    last_name,
    gender,
    date_of_birth,
    
    -- Calculate age based on date_of_birth
    DATE_PART('year', CURRENT_DATE) - DATE_PART('year', date_of_birth) AS age,

    phone_number,
    email,
    address,
    hire_date,
    subject,
    qualification,
    years_of_experience,
    
    -- Qualification Category: Simplifies qualification for potential aggregation
    CASE 
        WHEN qualification IN ('M.Sc.', 'PhD', 'Ed.D.') THEN 'Advanced'
        WHEN qualification IN ('B.Ed.', 'B.Sc.', 'HND') THEN 'Undergraduate'
        ELSE 'Basic'
    END AS qualification_category,
    
    created_at,
    updated_at

FROM {{ ref('stg_teachers') }}

{% endsnapshot %}
