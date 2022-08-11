/* Write your T-SQL query statement below */

with cte as
(select product_id, new_price, change_date 
from
(select *, row_number() over(partition by product_id order by change_date desc) rn
from Products
where change_date <= '2019-08-16') t
where rn = 1)

select t1.product_id, isnull(cte.new_price,10) price from
(select distinct product_id as product_id
from Products) t1
left join cte on t1.product_id = cte.product_id

