/* Write your T-SQL query statement below */

select * from Orders where
   (customer_id  in (select customer_id from Orders
group by customer_id
having count(distinct order_type)=2) and order_type = 0) or 
(customer_id not in (select customer_id from Orders
group by customer_id
having count(distinct order_type)=2) )

