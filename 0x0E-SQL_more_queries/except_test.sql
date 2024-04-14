USE hbtn_0d_tvshows;
SELECT id FROM tv_shows
EXCEPT
SELECT id FROM tv_shows WHERE id = 2

