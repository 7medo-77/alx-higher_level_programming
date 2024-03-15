-- Script that lists all shows with their genres
SELECT tv_shows.title AS `title` FROM , tv_genres.name AS `name` FROM tv_shows
LEFT JOIN `tv_show_genres` ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC;
