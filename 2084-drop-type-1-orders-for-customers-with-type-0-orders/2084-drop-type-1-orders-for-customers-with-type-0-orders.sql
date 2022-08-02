/* Write your T-SQL query statement below */
/*
select * from Orders where
   (customer_id  in (select customer_id from Orders
group by customer_id
having count(distinct order_type)=2) and order_type = 0) or 
(customer_id not in (select customer_id from Orders
group by customer_id
having count(distinct order_type)=2) )
*/
select order_id,customer_id,order_type from Orders a where order_type = 0
union
select order_id,customer_id,order_type from Orders b where b.customer_id not in (select customer_id from Orders where order_type = 0)


