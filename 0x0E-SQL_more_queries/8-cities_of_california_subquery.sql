-- Replace 'your_database_name' with the actual database name passed as an argument
USE hbtn_0d_usa;

-- Find the state_id for California in the states table
SET @california_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities of California sorted by cities.id
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = @california_id
ORDER BY cities.id ASC;
