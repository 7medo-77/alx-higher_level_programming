-- Script that creates a table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities`(
		`id` INT PRIMARY KEY AUTO_INCREMENT,
		FOREIGN KEY (state_id) REFERENCES state(`state_id`) NOT NULL,
		`name` VARCHAR(256) NOT NULL
);
