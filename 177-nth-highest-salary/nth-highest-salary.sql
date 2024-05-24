CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
       select max(salary) from(
      select dense_rank() over(order by salary desc) as rank, salary from Employee)a
      where rank = @N

    );
END