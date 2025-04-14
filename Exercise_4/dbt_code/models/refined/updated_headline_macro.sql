with staging_data as (select * from {{ ref("original_headline") }})
select {{ translate_headline("headline") }} as updated_job_title
from staging_data
