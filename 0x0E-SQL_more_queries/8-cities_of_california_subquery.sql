-- Selecting cities in California from the hbtn_0d_usa database
SELECT cities.id, cities.name
FROM cities
-- Subquery to get the state_id of 'California' from the states table
WHERE cities.state_id IN
    (SELECT states.id
     FROM states
     WHERE states.name = 'California')
-- Ordering the results by cities.id
ORDER BY cities.id;
