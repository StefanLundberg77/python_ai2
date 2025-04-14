{% macro to_lowercase(column) %} lower({{ column }}) {% endmacro %}
