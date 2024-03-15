-- Script that lists all shows with their genres
SELECT tv_shows.title, tv_genres.name FROM tv_shows, tv_genres
JOIN `tv_show_genres` ON tv_show_genres.show_id = tv_shows.id 
LEFT OUTER JOIN `tv_genres` AS `genres` ON `genres`.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC;
