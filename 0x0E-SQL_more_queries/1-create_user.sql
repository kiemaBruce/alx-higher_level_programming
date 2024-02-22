-- Creates a user for MySQL server and grants them all privileges.
CREATE USER IF NOT EXISTS user_0d_1 IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
