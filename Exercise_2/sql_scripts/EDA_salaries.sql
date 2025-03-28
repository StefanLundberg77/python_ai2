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

-- Make a salary_level column with the following categories: low, medium, high, insanely_high.
-- Decide your thresholds for each category.
-- Make it base on the monthly salary in SEK.

-- getting summary statistics
SELECT 
	
	MIN(salary_in_sek_monthly) AS min_salary,
	MAX(salary_in_sek_monthly) AS max_salary,
	AVG(salary_in_sek_monthly) AS avg_salary,
	MEDIAN(salary_in_sek_monthly) AS median_salary
FROM cleaned_salaries;

ALTER TABLE cleaned_salaries
ADD salary_level VARCHAR;


UPDATE cleaned_salaries
SET salary_level = CASE
	WHEN salary_in_sek_monthly < 50000 THEN 'low'
	WHEN salary_in_sek_monthly > 50000 AND salary_in_sek_monthly < 200000 THEN 'medium'
	WHEN salary_in_sek_monthly > 200000 AND salary_in_sek_monthly < 300000 THEN 'high'
	WHEN salary_in_sek_monthly > 300000 THEN 'insanely_high'
END;

select salary_level from cleaned_salaries;
select * from cleaned_salaries
DESC
