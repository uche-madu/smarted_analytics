-- macros/tests/nullable_relationships.sql

{% test nullable_relationships(model, column_name, to, field='id') %}

with filtered_data as (
    -- Select rows where the foreign key (column_name) is NOT NULL
    select *
    from {{ model }}
    where {{ column_name }} is not null
),

exceptions as (
    -- Identify rows where the foreign key does not have a matching primary key in the related model
    select
        f.*
    from filtered_data f
    left join {{ ref(to) }} r
    on f.{{ column_name }} = r.{{ field }}
    where r.{{ field }} is null
)

-- Return rows that fail the nullable_relationships test
select *
from exceptions

{% endtest %}
