{% macro generate_subject_fields(subjects) %}
    {% set subject_fields = [] %}

    {% for subject in subjects %}
        {% set ca1 = subject ~ '_ca1' %}
        {% set ca2 = subject ~ '_ca2' %}
        {% set total = subject ~ '_total' %}
        {% set grade = subject ~ '_grade' %}
        {% set pass_field = subject ~ '_pass' %}
        {% set attendance = subject ~ '_attendance' %}
        {% set teacher_remarks = subject ~ '_teacher_remarks' %}

        {% set fields = [
            ca1,
            ca2,
            total,
            "CASE WHEN " ~ total ~ " IS NULL THEN NULL " ~
            "WHEN " ~ total ~ " >= 75 THEN 'A1' " ~
            "WHEN " ~ total ~ " >= 70 THEN 'B2' " ~
            "WHEN " ~ total ~ " >= 65 THEN 'B3' " ~
            "WHEN " ~ total ~ " >= 60 THEN 'C4' " ~
            "WHEN " ~ total ~ " >= 55 THEN 'C5' " ~
            "WHEN " ~ total ~ " >= 50 THEN 'C6' " ~
            "WHEN " ~ total ~ " >= 45 THEN 'D7' " ~
            "WHEN " ~ total ~ " >= 40 THEN 'E8' " ~
            "ELSE 'F9' END AS " ~ grade,
            "CASE WHEN " ~ total ~ " IS NULL THEN NULL " ~
            "WHEN " ~ total ~ " >= 50 THEN 'Pass' ELSE 'Fail' END AS " ~ pass_field,
            attendance,
            teacher_remarks
        ] %}

        {% for field in fields %}
            {% do subject_fields.append(field) %}
        {% endfor %}
    {% endfor %}

    {{ return(subject_fields | join(',\n    ')) }}
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


