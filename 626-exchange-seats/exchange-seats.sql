/* Write your T-SQL query statement below */
    SELECT 
    CASE 
        WHEN MAX(ID) OVER()=ID AND ID%2=1 THEN  ID 
        WHEN ID%2=0 THEN ID-1 
        ELSE ID+1 
    END AS ID,
    STUDENT
    FROM SEAT
    ORDER BY ID ;