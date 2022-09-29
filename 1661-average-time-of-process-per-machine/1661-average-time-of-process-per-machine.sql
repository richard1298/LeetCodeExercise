/* Write your T-SQL query statement below */

with cte as
(select machine_id, process_id,
(case when activity_type = 'start' then -timestamp else timestamp end) timestamp
from Activity)

select machine_id, round(sum(timestamp)/count(distinct process_id),3) processing_time
from cte
group by machine_id
order by machine_id