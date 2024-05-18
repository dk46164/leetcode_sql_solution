# Write your MySQL query statement below
SELECT 
s.name as name
FROM Company c  
    join  Orders o on o.com_id = c.com_id  and c.name = 'RED'
    right join  SalesPerson s on s.sales_id = o.sales_id
where o.sales_id is null
;
