/* Write your T-SQL query statement below */

select month,count(distinct(order_id)) order_count, count(distinct(customer_id)) customer_count
from
(select order_id,
       concat(year(order_date),'-',
             (case when month(order_date)<10 then '0' else '' end),month(order_date)) month,
        customer_id,invoice
from Orders) t
where invoice >20
group by month
