/* Write your T-SQL query statement below */

with cte as (select t.box_id, appleBox + isnull(appleChest,0) as applecnt, orangeBox + isnull(orangeChest,0) as orangecnt
from
(select b.box_id,
b.chest_id, 
b.apple_count as appleBox,
c.apple_count as appleChest,
b.orange_count as orangeBox,
c.orange_count as orangeChest
from
Boxes b left join Chests c
on b.chest_id = c.chest_id) t) 

select sum(applecnt) apple_count, sum(orangecnt) orange_count
from cte