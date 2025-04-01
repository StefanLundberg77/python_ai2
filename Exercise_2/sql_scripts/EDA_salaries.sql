-- describe the table
DESC;

-- select all to view the data
SELECT * FROM salaries;

-- determine nr of rows
SELECT COUNT(*) AS total_rows
FROM salaries;

-- find out nr of employment types
SELECT COUNT(DISTINCT employment_type)
FROM salaries;

-- find out the different values
SELECT DISTINCT employment_type
FROM salaries;

-- create a new table from salaries
CREATE TABLE cleaned_salaries AS
    SELECT *
    FROM salaries;

-- testing
SELECT * FROM cleaned_salaries;

-- transform column value abbreviations
	-- ref: https://www.w3schools.com/sql/sql_case.asp
UPDATE cleaned_salaries
SET employment_type = CASE
    WHEN employment_type = 'FT' THEN 'Full time'
    WHEN employment_type = 'CT' THEN 'Contract'
    WHEN employment_type = 'PT' THEN 'Part time'
    WHEN employment_type = 'FL' THEN 'Freelance'
    ELSE employment_type
END;

-- checking to ensure correct result
SELECT DISTINCT employment_type
FROM cleaned_salaries;

-- continue to transform column company size
-- list abbreviations in column
-- find out the different values
SELECT DISTINCT company_size
FROM cleaned_salaries;

-- transform column value abbreviations
UPDATE cleaned_salaries
SET company_size = CASE
    WHEN company_size = 'S' THEN 'Small'
    WHEN company_size = 'M' THEN 'Medium'
    WHEN company_size = 'L' THEN 'Large'
    ELSE company_size
END;

-- create a salary column with Swedish currency for yearly salary.
ALTER TABLE cleaned_salaries
ADD salary_in_sek FLOAT;

-- convert values from usd to sek values
UPDATE cleaned_salaries
SET salary_in_sek = salary_in_usd * 10;

-- add a column for monthly salary in sek
ALTER TABLE cleaned_salaries
ADD salary_in_sek_monthly FLOAT;

-- set values to monthly
UPDATE cleaned_salaries
SET salary_in_sek_monthly = salary_in_sek /12;

select * from cleaned_salaries
ORDER BY salary_in_sek_monthly DESC;


-- getting summary statistics
SELECT 	
	MIN(salary_in_sek_monthly) AS min_salary,
	MAX(salary_in_sek_monthly) AS max_salary,
	AVG(salary_in_sek_monthly) AS avg_salary,
	MEDIAN(salary_in_sek_monthly) AS median_salary
FROM cleaned_salaries;

ALTER TABLE cleaned_salaries
ADD salary_level VARCHAR;

-- Make a salary_level column with the following categories: low, medium, high, insanely_high.
-- Decide your thresholds for each category.
-- Make it base on the monthly salary in SEK.

UPDATE cleaned_salaries
SET salary_level = CASE
	WHEN salary_in_sek_monthly < 50000 THEN 'low'
	WHEN salary_in_sek_monthly >= 50000 AND salary_in_sek_monthly < 200000 THEN 'medium'
	WHEN salary_in_sek_monthly >= 200000 AND salary_in_sek_monthly < 300000 THEN 'high'
	WHEN salary_in_sek_monthly >= 300000 THEN 'insanely_high'
END;

-- f) Choose the following columns to include in your table: 
-- experience_level, employment_type, job_title, salary_annual_sek, salary_monthly_sek, 
-- remote_ratio, company_size, salary_level

SELECT
	job_title, 
	employment_type, 
	experience_level, 
	salary_in_sek,
	salary_in_sek_monthly,
	salary_level,
	remote_ratio,
	company_size
FROM
	cleaned_salaries
WHERE
	salary_level = 'insanely_high'
ORDER BY 
	salary_level;

--  a) Count number of Data engineers jobs. For simplicity just go for job_title Data Engineer.

SELECT
	COUNT(*) AS num_data_engineers
FROM
	cleaned_salaries
WHERE
	job_title = 'Data Engineer';

--  b) Count number of unique job titles in total.

SELECT 
	COUNT(DISTINCT job_title) AS num_titles
FROM
	cleaned_salaries;	

--  c) Find out how many jobs that goes into each salary level.

SELECT
	DISTINCT (salary_level) AS salary_levels,
	COUNT(*) AS num_jobs
FROM
	cleaned_salaries
GROUP BY
	salary_level
ORDER BY
	num_jobs  ASC; 

--  d) Find out the median and mean salaries for each seniority levels.

SELECT
	DISTINCT(experience_level),
	AVG(salary_in_sek_monthly) AS avg_salary,
	MEDIAN(salary_in_sek_monthly) AS median_salary
FROM
	cleaned_salaries
GROUP BY
	experience_level


--  e) Find out the top earning job titles based on their median salaries and how much they earn.

SELECT
	DISTINCT(job_title),
	MEDIAN(salary_in_sek_monthly) AS median_salary
FROM
	cleaned_salaries
GROUP BY
	job_title
ORDER BY median_salary DESC
LIMIT 5;
	
--  f) How many percentage of the jobs are fully remote, 50 percent remote and fully not remote.

SELECT
	remote_ratio, --DISTINCT(remote_ratio),
	ROUND(COUNT(*)*100 / (SELECT COUNT(*) FROM cleaned_salaries)) || '%'AS percentage
FROM cleaned_salaries
GROUP BY remote_ratio;


--  g) Pick out a job title of interest and figure out if company size affects the salary. Make a simple analysis as a comprehensive one requires causality investigations which are much harder to find



select COUNT(salary_level) from cleaned_salaries;
select * from cleaned_salaries
DESC
