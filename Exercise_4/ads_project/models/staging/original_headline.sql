with staging_data as (select * from ads.staging.data_field_job_ads)

select headline, description__text
from staging_data
