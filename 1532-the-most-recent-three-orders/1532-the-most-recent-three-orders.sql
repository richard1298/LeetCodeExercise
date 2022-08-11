/* Write your T-SQL query statement below */

select name as customer_name,customer_id,order_id,order_date 
from
(select c.name, o.customer_id,o.order_id,o.order_date,
row_number() over (partition by o.customer_id order by o.order_date desc) as rw
from Customers c right join Orders o
on c.customer_id = o.customer_id ) t
where rw in (1,2,3)
order by customer_name asc,customer_id asc, order_date desc
