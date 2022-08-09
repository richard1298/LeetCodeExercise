/* Write your T-SQL query statement below */

--cte has three columns: city_id, day, maxdegree
with cte as
(select w.city_id, w.day,t.maxdegree from
Weather w inner join
(select city_id, max(degree) maxdegree
from Weather group by city_id)t
on w.city_id = t.city_id
and w.degree = t.maxdegree)


select city_id, day, maxdegree degree
from
(select city_id, day, maxdegree, row_number() over(partition by city_id order by day) row
from cte)t2
where row = 1