-- Script that lists all cities of california sorted by city id
SELECT `id`, `name` FROM `cities` WHERE state_id = (
	SELECT `id` FROM `states` WHERE `name` = "California"
) ORDER BY `id` DESC;
