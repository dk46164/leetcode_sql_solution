/* Write your T-SQL query statement below */
select department , employee , salary 
from (
  select e.name employee , e.salary salary, d.name department, dense_rank() over (partition by d.id order by e.salary desc) ranking
  from employee e inner join Department d
  on e.departmentId = d.id
) newTable
where ranking <= 3;