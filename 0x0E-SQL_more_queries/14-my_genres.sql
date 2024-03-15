-- Script that lists all shows contained in database 
-- that have at least one genre liked
SELECT tv_genres.name
FROM `tv_genres` 
JOIN `tv_show_genres`
JOIN `tv_shows`
ON tv_show_genres.genre_id = tv_genres.id AND tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.name = "Dexter";
