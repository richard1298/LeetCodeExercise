/* Write your T-SQL query statement below */

select p1, p2, abs(pp1x-pp2x) * abs(pp1y - pp2y) as area
from
(select pp1.id p1, pp1.x_value pp1x, pp1.y_value pp1y,
pp2.id p2, pp2.x_value pp2x, pp2.y_value pp2y
from Points pp1 full outer join Points pp2
on (pp1.x_value != pp2.x_value and pp1.y_value != pp2.y_value and pp2.id >pp1.id))t
where p1 is not null and p2 is not null
order by area desc, p1, p2