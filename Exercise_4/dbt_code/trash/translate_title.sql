{% macro translate_title(title_column) %}
    case
        when {{ title_column }} = 'Data Engineer'
        then 'Junior Data Engineer'
        else {{ title_column }}
    end
{% endmacro %}
