WITH CTE AS
(
Select id, Salary,DENSE_RANK() OVER	(ORDER BY salary DESC) Rn FROM Employee
)
SELECT MAX(Salary) AS SecondHighestSalary FROM CTE WHERE rn = 2;