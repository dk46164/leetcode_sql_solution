-- Write your PostgreSQL query statement below
WITH CTE_1 as (select COUNT(*) over(partition by lat,lon) as ct,tiv_2016,tiv_2015,COUNT(*) over(partition by tiv_2015) as ct_1 from insurance)
select ROUND(SUM(tiv_2016)::decimal,2) as tiv_2016 from CTE_1 where ct=1 and ct_1 != 1;