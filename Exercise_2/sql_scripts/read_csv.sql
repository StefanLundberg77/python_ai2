-- ingest dataset hemnet from csv
-- Create TABLE 
--     hemnet AS 
-- SELECT
-- * 
-- FROM 
--     read_csv_auto("data/hemnet_data_clean.csv");

-- ingest another dataset salaries from csv
Create TABLE 
    salaries AS 
SELECT
* 
FROM 
    read_csv_auto("data/salaries.csv");