/* Write your T-SQL query statement below */

with cte as(
select distinct user_id, 
(sum(distance) over (partition by user_id)) travelled_distance
from Rides)

select u.name,isnull(cte.travelled_distance,0) travelled_distance from
Users u left join cte 
on u.id = cte.user_id
order by travelled_distance desc, u.name asc
