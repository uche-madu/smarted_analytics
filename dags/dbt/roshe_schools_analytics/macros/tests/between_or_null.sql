{% test between_or_null(model, column_name, lower_bound, upper_bound) %}
SELECT *
FROM {{ model }}
WHERE {{ column_name }} IS NOT NULL
AND ({{ column_name }} < {{ lower_bound }} OR {{ column_name }} > {{ upper_bound }})
{% endtest %}
