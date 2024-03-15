-- Script that lists all genres of the show Dexter
USE hbtn_0d_tvshows;
SELECT tv_shows.title FROM tv_shows 
JOIN `tv_show_genres` ON tv_show_genres.genre_id = tv_genres.id 
JOIN `tv_shows` ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
