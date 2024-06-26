-- Script that lists all genres not of the show Dexter
USE hbtn_0d_tvshows;
SELECT tv_genres.name FROM `tv_genres`
JOIN `tv_show_genres` ON tv_show_genres.genre_id = tv_genres.id 
JOIN `tv_shows` ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
EXCEPT DISTINCT
	SELECT tv_genres.name FROM `tv_genres`
	JOIN `tv_show_genres` ON tv_show_genres.genre_id = tv_genres.id 
	JOIN `tv_shows` ON tv_shows.id = tv_show_genres.show_id;
