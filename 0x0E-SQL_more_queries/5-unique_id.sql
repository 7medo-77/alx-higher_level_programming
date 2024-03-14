-- Script that creates a table
CREATE TABLE IF NOT EXISTS `unique_id`(
		`id` INT NOT NULL AND UNIQUE,
		`name` VARCHAR(256)
);
