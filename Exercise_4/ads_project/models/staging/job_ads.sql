with staging_data as (select * from ads.staging.data_field_job_ads)
select
    id as job_id,
    headline as job_title,
    employer__name as company_name,
    workplace_address__city as city,
    workplace_address__region as region,
    employment_type__label as employment_type,
    salary_type__label as salary_type,
    scope_of_work__min as min_hours,
    scope_of_work__max as max_hours,
    publication_date,
    application_details__email as contact_email,
    application_details__reference as contact_name,
    application_details__other as contact_phone,
    description__text as job_description
from staging_data


