SELECT city, SUM(value)/COUNT(Value) AS sum_temp FROM `temperatures` GROUP BY `city` ORDER BY sum_temp DESC;
