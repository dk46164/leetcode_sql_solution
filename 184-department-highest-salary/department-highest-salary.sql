/* Write your T-SQL query statement below */
WITH CTE AS (
        SELECT 
        E.NAME AS NAME,
        E.SALARY AS SALARY,
        D.NAME  AS Department,
        DENSE_RANK() OVER(PARTITION BY D.NAME ORDER BY E.SALARY DESC) AS RNK
        FROM 
            EMPLOYEE E JOIN DEPARTMENT D ON D.ID = E.departmentId
)
SELECT 
Department, NAME AS EMPLOYEE , SALARY
FROM CTE WHERE RNK=1 ;