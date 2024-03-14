-- Script that lists all shows contained in database 
-- that have at least one genre liked
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, "NULL") AS `NULL`
FROM `tv_shows` FULL JOIN `tv_show_genres`
ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
