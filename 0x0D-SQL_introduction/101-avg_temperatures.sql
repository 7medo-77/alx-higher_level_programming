-- Lists all the average temperatures per city by descending order
SELECT city, SUM(value)/COUNT(Value) AS avg_temp FROM `temperatures` GROUP BY `city` ORDER BY sum_temp DESC;
