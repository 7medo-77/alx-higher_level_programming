-- SQL query to display average of all the student scores
SELECT score, COUNT(score) AS number FROM `second_table` GROUP BY score ORDER BY number DESC;
