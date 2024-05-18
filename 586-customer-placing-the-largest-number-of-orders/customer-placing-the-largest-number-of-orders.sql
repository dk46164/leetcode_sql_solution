# Write your MySQL query statement below
with cte_cnt_order as (
    select customer_number, row_number() over(order by count(order_number) desc) as cnt from Orders group by customer_number
)
select customer_number from cte_cnt_order where  cnt = 1;
