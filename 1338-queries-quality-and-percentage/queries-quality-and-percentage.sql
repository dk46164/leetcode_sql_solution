/* Write your T-SQL query statement below */
SELECT 
QUERY_NAME,
ROUND(AVG(RATING*1.0/POSITION),2) AS quality,
ROUND(AVG(CASE WHEN RATING<3 THEN 1.0 ELSE 0 END)*100.0,2) AS poor_query_percentage
FROM Queries where query_name is not null
GROUP BY QUERY_NAME;
