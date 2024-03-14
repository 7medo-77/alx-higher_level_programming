-- SQL script that creates a user "user_0d_1" and grants them all previliges
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost`;