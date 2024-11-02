{% macro calculate_average_score_per_term(subject_list) %}
ROUND(
    AVG(
        {% for subject in subject_list %}
            COALESCE({{ subject }}_total, 0)
            {% if not loop.last %} + {% endif %}
{% endfor %}
    ) / NULLIF(
        COUNT(
            CASE
                {% for subject in subject_list %}
                    WHEN COALESCE({{ subject }}_total, NULL) IS NOT NULL THEN '{{ subject }}'
                {% endfor %}
                ELSE NULL
            END
        ), 0), 2
)
{% endmacro %}


{% macro calculate_total_term_score(subject_list) %}

(
    COALESCE(
        {% for subject in subject_list %}
            SUM({{ subject }}_total){% if not loop.last %} + {% endif %}
    {% endfor %}
    , 0)
)
{% endmacro %}


{% macro count_subjects_registered(subject_list) %}
COUNT(DISTINCT (
    CASE
        {% for subject in subject_list %}
            WHEN COALESCE({{ subject }}_total, NULL) IS NOT NULL THEN '{{ subject }}'
        {% endfor %}
        ELSE NULL
    END
))
{% endmacro %}


{% macro count_subjects_passed(subject_pass_list) %}
COUNT(DISTINCT (
    CASE
        {% for subject in subject_pass_list %}
            WHEN {{ subject }} = 'Pass' THEN '{{ subject | replace('_pass', '') }}'
        {% endfor %}
        ELSE NULL
    END
))
{% endmacro %}


{% macro cumulative_term_average(subject_pass_list) %}

ROUND(
    SUM(
        {% for subject in subject_pass_list %}
            CASE
                WHEN COALESCE({{ subject }}, NULL) IS NOT NULL THEN 1
                ELSE 0
            END
            {% if not loop.last %} + {% endif %}
    {% endfor %}
    ) / NULLIF(COUNT(*), 0), 2
)
{% endmacro %}
