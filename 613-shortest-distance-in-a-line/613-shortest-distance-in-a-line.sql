/* Write your T-SQL query statement below */


select min(diff) as shortest from
(select 
x,
lag(x) over(order by x) as laggedx,
abs(x - lag(x) over(order by x)) as diff
from Point) t
where t.diff is not null
