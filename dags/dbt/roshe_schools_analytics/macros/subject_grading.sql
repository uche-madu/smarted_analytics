{% macro get_columns_by_suffix(model_name, suffix) %}
    {%- set columns = adapter.get_columns_in_relation(ref(model_name)) -%}

    {# Initialize an empty list to store matching columns #}
    {%- set filtered_cols = [] -%}

    {# Loop through each column and use slicing to check for the suffix #}
    {%- for col in columns -%}
        {% if (col.name[-(suffix | length):] | lower) == (suffix | lower) %}
            {% do filtered_cols.append(col.name) %}
        {% endif %}
    {%- endfor -%}

    {{ return(filtered_cols) }}
{% endmacro %}



{% macro generate_subject_case_statements(model_name) %}
    {# Retrieve the subject total columns dynamically #}
    {% set subject_totals = get_columns_by_suffix(model_name, '_total') %}
    {% set case_statements = [] %}

    {# Loop through the total columns to generate all related fields dynamically #}
    {% for total_column in subject_totals %}
        {% set subject = total_column[:-6] %}  {# Extract the subject name by removing '_total' #}

        {# Define all field variations for the subject #}
        {% set ca1 = subject ~ '_ca1' %}
        {% set ca2 = subject ~ '_ca2' %}
        {% set exam = subject ~ '_exam' %}
        {% set grade = subject ~ '_grade' %}
        {% set pass_field = subject ~ '_pass' %}
        {% set attendance = subject ~ '_attendance' %}
        {% set teacher_remarks = subject ~ '_teacher_remarks' %}
        {% set teacher_id = subject ~ '_teacher_id' %}

        {# Generate the grade case statement #}
        {% set grade_case = "CASE WHEN \"" ~ total_column ~ "\" IS NULL THEN NULL " ~
            "WHEN \"" ~ total_column ~ "\" >= 75 THEN 'A1' " ~
            "WHEN \"" ~ total_column ~ "\" >= 70 THEN 'B2' " ~
            "WHEN \"" ~ total_column ~ "\" >= 65 THEN 'B3' " ~
            "WHEN \"" ~ total_column ~ "\" >= 60 THEN 'C4' " ~
            "WHEN \"" ~ total_column ~ "\" >= 55 THEN 'C5' " ~
            "WHEN \"" ~ total_column ~ "\" >= 50 THEN 'C6' " ~
            "WHEN \"" ~ total_column ~ "\" >= 45 THEN 'D7' " ~
            "WHEN \"" ~ total_column ~ "\" >= 40 THEN 'E8' " ~
            "ELSE 'F9' END AS " ~ grade %}

        {# Generate the pass/fail case statement #}
        {% set pass_case = "CASE WHEN \"" ~ total_column ~ "\" IS NULL THEN NULL " ~
            "WHEN \"" ~ total_column ~ "\" >= 50 THEN 'Pass' ELSE 'Fail' END AS " ~ pass_field %}

        {# Collect all fields to include in the select statement #}
        {% set fields = [
            ca1,
            ca2,
            exam,
            total_column,
            grade_case,
            pass_case,
            attendance,
            teacher_remarks,
            teacher_id
        ] %}

        {# Append each field to the case statements #}
        {% for field in fields %}
            {% do case_statements.append(field) %}
        {% endfor %}
    {% endfor %}

    {# Join all the case statements with commas and return the result #}
    {{ return(case_statements | join(',\n    ')) }}
{% endmacro %}


{% macro generate_average(model_name, field_suffix) %}
    {% set columns = get_columns_by_suffix(model_name, field_suffix) %}

    ROUND(
        (
            {% for col in columns %}
                COALESCE({{ col }}, 0)
                {% if not loop.last %} + {% endif %}
            {% endfor %}
        ) / NULLIF(
            (
                {% for col in columns %}
                    CASE WHEN {{ col }} IS NOT NULL THEN 1 ELSE 0 END
                    {% if not loop.last %} + {% endif %}
                {% endfor %}
            ),
            0
        ),
        2
    )
{% endmacro %}




{% macro generate_wassce_pass_logic(core_subjects, elective_subjects) %}
    CASE
        WHEN {{ core_subjects[0] }} = 'Pass'
            AND {{ core_subjects[1] }} = 'Pass'
            AND (
                {% for subject in elective_subjects %}
                    (CASE WHEN {{ subject }} = 'Pass' THEN 1 ELSE 0 END)
                    {% if not loop.last %} + {% endif %}
                {% endfor %}
            ) >= 3 THEN 'Pass'
        ELSE 'Fail'
    END AS wassce_pass
{% endmacro %}


{% macro generate_teacher_joins(model_name) %}
    {%- set teacher_id_columns = get_columns_by_suffix(model_name, '_teacher_id') -%}
    {%- set join_statements = [] -%}

    {%- for teacher_id_column in teacher_id_columns %}
        {%- set subject = teacher_id_column[:-11] -%}

        {%- set join_statement -%}
        LEFT JOIN {{ ref('dim_teachers') }} t_{{ subject }}
            ON f.{{ teacher_id_column }} = t_{{ subject }}.teacher_id
        {%- endset %}

        {%- do join_statements.append(join_statement) -%}
    {%- endfor -%}

    {{ join_statements | join('\n') }}
{% endmacro %}



{% macro generate_teacher_selects(model_name) %}
    {%- set teacher_id_columns = get_columns_by_suffix(model_name, '_teacher_id') -%}
    {%- set select_statements = [] -%}

    {%- for teacher_id_column in teacher_id_columns %}
        {%- set subject = teacher_id_column[:-11] -%}

        {%- set select_statement -%}
            {{ teacher_id_column }},
            f.{{ subject }}_ca1,
            f.{{ subject }}_ca2,
            f.{{ subject }}_exam,
            f.{{ subject }}_total,
            f.{{ subject }}_grade,
            f.{{ subject }}_pass,
            f.{{ subject }}_attendance,
            f.{{ subject }}_teacher_remarks,
            t_{{ subject }}.qualification AS {{ subject }}_teacher_qualification,
            t_{{ subject }}.age AS {{ subject }}_teacher_age,
            t_{{ subject }}.gender AS {{ subject }}_teacher_gender,
            t_{{ subject }}.years_of_experience AS {{ subject }}_teacher_years_of_experience,
            t_{{ subject }}.qualification_category AS {{ subject }}_teacher_qualification_category
        {%- endset %}

        {%- do select_statements.append(select_statement) -%}
    {%- endfor -%}

    {{ select_statements | join(',\n    ') }}
{% endmacro %}

