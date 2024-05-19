/* Write your T-SQL query statement below */
select prices.product_id, isnull(round(cast(sum(units*price) as float) / sum(units), 2),0) as average_price from  prices 
left join unitssold on unitssold.product_id = prices.product_id and purchase_date >= start_date and purchase_date <= end_date
group by prices.product_id;