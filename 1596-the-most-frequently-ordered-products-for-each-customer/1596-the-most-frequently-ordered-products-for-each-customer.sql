/* Write your T-SQL query statement below */

with cte as
(select o.order_id, o.customer_id,o.product_id,p.product_name
from Orders o left join Products p on o.product_id = p.product_id)

select customer_id,product_id,product_name from
(select customer_id, product_id, product_name,dense_rank() over(partition by customer_id order by product_cnt desc) rnk from
(select distinct customer_id,product_name,product_id,count(product_id) over(partition by product_id, customer_id) product_cnt
from cte) a) b
where rnk = 1
