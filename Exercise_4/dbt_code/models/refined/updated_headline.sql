with staging_data as (select * from {{ ref("original_headline") }})

select
    case
        when headline = 'Data engineer' then 'Junior data engineer' else headline
    end as job_title
from staging_data
