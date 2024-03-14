-- SQL script that creates a user "user_0d_1" and grants them all previliges
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED WITH 'user_0d_1_pwd';
GRANT ALL PRIVILIGES ON *.* TO `user_0d_1`@`localhost`;
