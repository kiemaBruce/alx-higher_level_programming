-- Creates a database and creates a new user.
-- Create the database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user.
CREATE USER IF NOT EXISTS user_0d_2 IDENTIFIED BY 'user_0d_2_pwd';
-- Grant SELECT privileges.
GRANT SELECT ON *.* TO 'user_0d_2';
