/* Write your T-SQL query statement below */

select today.id
from Weather today
left join Weather yesterday
on DATEADD(day,-1,today.recordDate) = yesterday.recordDate
where today.temperature > yesterday.temperature