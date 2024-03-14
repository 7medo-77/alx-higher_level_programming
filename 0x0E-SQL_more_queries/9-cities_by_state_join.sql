-- Script that lists all cities of california sorted by city id
SELECT cities.id, cities.name, states.name FROM `cities` JOIN `states` ON cities.state_id = states.id ORDER BY cities.id ASC;
