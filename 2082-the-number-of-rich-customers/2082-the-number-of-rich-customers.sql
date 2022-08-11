/* Write your T-SQL query statement below */

select count(rich_count) rich_count 
from
(select distinct customer_id as rich_count
from Store
group by customer_id
having max(amount)>500) t
