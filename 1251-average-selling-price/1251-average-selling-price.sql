/* Write your T-SQL query statement below */

with cte as
(select u.product_id, u.purchase_date, u.units, p.price*u.units total from 
Prices p right join  UnitsSold u
on (u.purchase_date between p.start_date and p.end_date)
and p.product_id = u.product_id)



select product_id, round(cast(sum(total) as float)/cast(sum(units) as float),2) average_price 
from cte 
group by product_id
/*

select a.product_id,

round(cast(sum(a.price*b.units)as float)/sum(b.units),2) as average_price
from
prices a
join
unitssold b
on
a.product_id = b.product_id and
b.purchase_date between a.start_date and a.end_date
group by
a.product_id
*/