SELECT score, COUNT(*) AS score_count
FROM second_table
GROUP BY score;