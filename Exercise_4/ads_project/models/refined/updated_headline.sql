with staging_data as (select * from {{ ref("original_headline") }})

select
    case
        when headline = 'Data Engineer' then 'Junior data engineer' else headline
    end as job_title,
    description__text as description
from staging_data
