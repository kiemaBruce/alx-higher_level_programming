-- Counts the number of records with same score in second_table
SELECT score,
COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
