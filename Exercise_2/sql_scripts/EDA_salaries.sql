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

DROP TABLE cleaned_salaries;

-- testing
SELECT * FROM cleaned_salaries;

-- update values for column with new names
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

