-- Script that lists all shows with their genres
SELECT title, name FROM tv_shows
LEFT JOIN `tv_show_genres` ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN `tv_genres` ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC;
