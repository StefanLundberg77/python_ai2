DESC;

-- select all to view the data
SELECT * FROM HEMNET;

-- find out nr of rows
SELECT
	COUNT(*) AS total_rows
from
	hemnet;

-- find out 5 most expensive houses
SELECT
	"final_price",
	"address",
	"commune"
FROM
	hemnet
ORDER BY
	"final_price" DESC
LIMIT 5;

-- find out 5 least expensive
SELECT
	"final_price",
	"address",
	"commune"
FROM
	hemnet
ORDER BY
	"final_price" ASC
LIMIT 5;

-- summary statistics for this dataset
SELECT 
	MIN(final_price) AS min_price,
	MAX(final_price) AS max_price,
	AVG(final_price) AS avg_price,
	MEDIAN(final_price) AS median_price
FROM hemnet

-- sumary stats for price per area
SELECT 
	MIN(price_per_area) AS min_price,
	MAX(price_per_area) AS max_price,
	AVG(price_per_area) AS avg_price,
	MEDIAN(price_per_area) AS median_price
FROM hemnet

-- find unique value for commune column
SELECT COUNT(DISTINCT commune)
FROM hemnet


-- find unique value for commune
SELECT
	COUNT(DISTINCT trim(split_part(commune, ',', 2))) AS kommun
FROM
	hemnet;


-- Common Table Expression (CTE)
-- % of houses that cost more than 10m 
	--1. calc nr of houses
	--2. calc nr of >10m houses
	--3. using calculated numbers to calc a %
-- ref for CTE: https://www.geeksforgeeks.org/cte-in-sql/

WITH all_houses AS (SELECT COUNT(*) AS total_count FROM hemnet),
	expensive_houses AS (SELECT COUNT(*) AS expensive_count FROM hemnet WHERE final_price > 10000000)
SELECT(eh.expensive_count*100/ah.total_count) AS percentage_expensive_houses
FROM all_houses ah, expensive_houses eh;







