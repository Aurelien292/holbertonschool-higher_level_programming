-- script lists number of records with same score
SELECT score, COUNT(*) AS score_count
FROM second_table
GROUP BY score;