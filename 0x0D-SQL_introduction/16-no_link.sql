-- List all records from the second_table in the specified database with a non-null name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
