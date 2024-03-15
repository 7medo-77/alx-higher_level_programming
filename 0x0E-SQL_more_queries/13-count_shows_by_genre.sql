-- Script that lists all shows contained in database 
-- that have at least one genre liked
USE hbtn_0d_tvshows;
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS `number_of_shows`
FROM `tv_genres` JOIN `tv_show_genres` ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY tv_genres.id DESC;