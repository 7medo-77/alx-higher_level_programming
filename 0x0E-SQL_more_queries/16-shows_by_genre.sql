-- Script that lists all shows with their genres
SELECT tv_shows.title AS `title`, tv_genres.name AS `name` FROM tv_shows, tv_genres
LEFT JOIN `tv_show_genres` ON tv_show_genres.show_id = tv_shows.id
JOIN `tv_genres` AS `genres` ON `genres`.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC;
