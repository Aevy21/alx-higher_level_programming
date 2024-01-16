-- List the number of records with the same score in the second_table of the specified database
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC, score;
