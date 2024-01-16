-- List records with a score >= 10 from the second_table in the specified database, ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
