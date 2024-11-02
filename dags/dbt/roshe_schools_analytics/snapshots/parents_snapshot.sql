{% snapshot parents_snapshot %}

{{
    config(
        target_schema='snapshots',
        unique_key='parent_id',
        strategy='timestamp',
        updated_at='updated_at',
        invalidate_hard_deletes=True
    )
}}

    SELECT
        parent_id,
        first_name,
        middle_name,
        last_name,
        gender,
        marital_status,
        phone_number,
        email,
        address,
        relationship_to_student,
        income_bracket,
        education_level,
        occupation,
        employment_type,
        industry,
        engagement_level,
        home_language,
        number_of_children,
        alternate_contact_number,
        parent_teacher_meeting_attendance,
        volunteer_activities_count,
        recent_interaction_date,

        -- Education Category
        created_at,

        -- Income Bracket Category
        updated_at,

        CASE
            WHEN education_level IN ('Primary School', 'Secondary School') THEN 'Basic'
            WHEN education_level IN ('Technical/Vocational', 'Diploma') THEN 'Intermediate'
            WHEN education_level = 'Bachelor' THEN 'Undergraduate'
            WHEN education_level IN ('Master', 'PhD') THEN 'Postgraduate'
            ELSE education_level
        END AS education_category,
        CASE
            WHEN income_bracket = 'Below 50,000 Naira' THEN 'Low'
            WHEN income_bracket = '50,000 - 200,000 Naira' THEN 'Lower-Middle'
            WHEN income_bracket = '200,000 - 500,000 Naira' THEN 'Middle'
            WHEN income_bracket = '500,000 - 1,000,000 Naira' THEN 'Upper-Middle'
            WHEN income_bracket = 'Above 1,000,000 Naira' THEN 'High'
            ELSE income_bracket
        END AS income_bracket_category

    FROM {{ ref('stg_parents') }}



{% endsnapshot %}
