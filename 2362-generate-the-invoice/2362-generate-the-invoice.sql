/* Write your T-SQL query statement below */

with 
cte as
(select p2.invoice_id, sum(p1.price*p2.quantity) price from 
Products p1 right join Purchases p2 
on p1.product_id = p2.product_id
group by p2.invoice_id),

cte1 as
(select p2.invoice_id, 
sum(p1.price*p2.quantity) price from 
Products p1 right join Purchases p2 
on p1.product_id = p2.product_id
group by p2.invoice_id
having sum(p1.price*p2.quantity) = (select max(price) from cte))

select b.product_id, b.quantity, b.quantity*a.price price
from Products a inner join 
(select * from Purchases where invoice_id = (select min(invoice_id) from cte1))b
on a.product_id = b.product_id


