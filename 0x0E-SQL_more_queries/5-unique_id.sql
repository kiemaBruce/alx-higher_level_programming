-- Create table with unique data type that also has a default value
CREATE TABLE IF NOT EXISTS unique_id(
    id   INT          UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
