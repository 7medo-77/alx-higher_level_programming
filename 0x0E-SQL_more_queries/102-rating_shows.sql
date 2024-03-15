-- Script that lists all shows with their genres
SELECT title, SUM(tv_show_ratings.rate) FROM tv_shows
LEFT JOIN `tv_show_ratings` ON tv_show_ratings.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_genres.name ASC;
