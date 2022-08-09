/* Write your T-SQL query statement below */

with cte as
(SELECT order_id, 
count(distinct product_id) as num_prods, 
sum(quantity) as totalquantity, 
max(quantity) as maxquantity
FROM OrdersDetails
group by order_id)



select order_id
from cte
where maxquantity > (select max(cast(totalquantity as float)/(cast(num_prods as float))) from cte)
