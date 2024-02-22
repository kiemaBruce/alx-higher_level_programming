-- List all genres of the show 'Dexter'
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
WHERE tv_show_genres.show_id = 8
ORDER BY tv_genres.name DESC;
