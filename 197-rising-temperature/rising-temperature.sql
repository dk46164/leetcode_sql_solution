/* Write your T-SQL query statement below */
Select 
distinct c.id
from Weather c join Weather p on DATEADD(day,1,p.recordDate) = c.recordDate
and c.temperature>p.temperature ;
