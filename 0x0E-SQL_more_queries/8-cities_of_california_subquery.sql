-- Lists all cities of California in hbtn_0d_usa database.
SELECT cities.id, cities.name
    FROM cities
    WHERE cities.state_id = 
    (SELECT states.id
         FROM states
	 WHERE states.name = 'California')
ORDER BY cities.id ASC;
