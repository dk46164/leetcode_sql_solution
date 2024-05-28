-- Write your PostgreSQL query statement below
SELECT e.employee_id , e.name , COUNT(e2.reports_to) reports_count, ROUND(AVG(e2.age)) average_age
FROM Employees e
LEFT JOIN Employees e2
ON e.employee_id = e2.reports_to
GROUP BY 1, 2
HAVING COUNT(e2.reports_to) >=1
ORDER BY employee_id;