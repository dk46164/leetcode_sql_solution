-- Write your PostgreSQL query statement below
WITH cte AS(

SELECT 
    id,
    visit_date,
    people,
    COUNT(id) OVER(ORDER BY id RANGE BETWEEN 2 PRECEDING AND CURRENT ROW) AS count1,
    COUNT(id) OVER(ORDER BY id RANGE BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS count2,
    COUNT(id) OVER(ORDER BY id RANGE BETWEEN CURRENT ROW AND 2 FOLLOWING) AS count3
    FROM (SELECT * FROM Stadium WHERE people >= 100)
)
SELECT     id,
    visit_date,
    people
    FROM cte WHERE count1 = 3 OR count2 = 3 OR count3 = 3;