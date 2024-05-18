/* Write your T-SQL query statement below */

-- SELECT 
-- DISTINCT 
-- E.NAME AS EMPLOYEE
-- FROM EMPLOYEE  E JOIN EMPLOYEE M ON E.MANAGERID = M.ID
-- AND E.SALARY>M.SALARY;

SELECT e.Name AS Employee
FROM Employee e
JOIN Employee m
ON e.ManagerId = m.Id AND e.Salary > m.Salary;