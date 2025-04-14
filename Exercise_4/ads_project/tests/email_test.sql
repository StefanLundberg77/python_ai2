select *
from {{ ref("job_ads") }}
where contact_email not like '%@%'
