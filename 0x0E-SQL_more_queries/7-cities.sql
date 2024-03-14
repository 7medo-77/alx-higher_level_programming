-- Script that creates a table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities`(
		`id` INT PRIMARY KEY AUTO_INCREMENT,
		`state_id` INT NOT NULL FOREIGN KEY (state_id) REFERENCES state(id),
		`name` VARCHAR(256) NOT NULL
);
