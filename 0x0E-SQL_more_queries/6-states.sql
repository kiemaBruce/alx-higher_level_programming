-- Creates a database and a table within that database.
-- Create database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select that database.
USE hbtn_0d_usa;
-- Create table within that database.
CREATE TABLE IF NOT EXISTS states(
    id   INT          PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
