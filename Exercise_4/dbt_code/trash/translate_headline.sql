{% macro translate_headline(title_column) %}
    case
        when {{ title_column }} = 'Senior Data Engineer'
        then 'Lead Data Engineer'
        when {{ title_column }} = 'Data Engineer'
        then 'Junior Data Engineer'
        else {{ title_column }}
    end
{% endmacro %}
