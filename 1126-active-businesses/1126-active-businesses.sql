/* Write your T-SQL query statement below */

with cte as
(select e.business_id, e.event_type, e.occurences, t.avg_activity
from Events e left join 
(select event_type, avg(cast(occurences as float)) avg_activity
from Events
group by event_type) t
on e.event_type = t.event_type)


select distinct business_id as business_id from cte
group by business_id
having sum(case when occurences > avg_activity then 1 else 0 end)>1
