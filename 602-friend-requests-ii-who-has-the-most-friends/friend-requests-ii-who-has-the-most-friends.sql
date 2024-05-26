/* Write your T-SQL query statement below */
WITH CTE  AS (
    SELECT 
    REQUESTER_ID AS ID1 ,ACCEPTER_ID  AS ID2
    FROM RequestAccepted
    UNION ALL
    SELECT 
    ACCEPTER_ID AS ID1 ,REQUESTER_ID  AS ID2
    FROM RequestAccepted

)

SELECT TOP 1 ID1 AS ID,COUNT(ID2) AS NUM
FROM CTE GROUP BY ID1
ORDER BY  NUM DESC ;