--  a script that lists the number of records with the same score in th-- e table second_table of the database hbtn_0c_0 in your MySQL serverS

SELECT score, COUNT(*) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY score DESC;

