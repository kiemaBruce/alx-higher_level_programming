-- Creates a table and adds multiple rows into it.
-- Create the table
CREATE TABLE IF NOT EXISTS second_table (
id INT,
name VARCHAR(256),
score INT
);
-- Add rows into the table.
INSERT INTO second_table
VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8)
;
