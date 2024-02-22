-- Lists all cities of California in hbtn_0d_usa database.
USE hbtn_0d_usa;
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = 1
ORDER BY cities.id ASC;
