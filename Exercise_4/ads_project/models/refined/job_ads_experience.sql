with
    staging_data as (select * from {{ ref("job_ads") }}),

    experience_data as (
        select job_id, label
        from ads.staging.data_field_job_ads__must_have__work_experiences
    )
select s.*, {{ to_lowercase("e.label") }} as required_experience
from staging_data s
join experience_data e on s.job_id = e.job_id
