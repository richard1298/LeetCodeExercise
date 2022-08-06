/* Write your T-SQL query statement below */

select customer_number from 
(select customer_number, count(order_number) cnt from Orders
group by customer_number) t
where cnt = (select max(cnt) from (select customer_number, count(order_number) cnt from Orders
group by customer_number) t2)