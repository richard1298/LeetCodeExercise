# Write your MySQL query statement below

with cte as (select customer_id,
sum(case when product_name = 'A' then 1 else 0 end) countA,
sum(case when product_name = 'B' then 1 else 0 end) countB,
sum(case when product_name = 'C' then 1 else 0 end) countC
from Orders
group by customer_id)

select c.customer_id, c.customer_name
from Customers c 
inner join cte on c.customer_id = cte.customer_id
where cte.countA>0 and cte.countB>0 and cte.countC = 0