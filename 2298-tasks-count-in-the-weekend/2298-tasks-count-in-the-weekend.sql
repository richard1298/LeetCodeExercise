/* Write your T-SQL query statement below */

select weekend_cnt, working_cnt from
(select count(task_id) cnt,flag  
from
(select *,
(case when datename(weekday,submit_date) = 'Saturday' or datename(weekday,submit_date) = 'Sunday' then 'weekend_cnt' else 'working_cnt' end) flag
from Tasks) t
group by flag) tmp
pivot
(max(cnt)
 for flag in (weekend_cnt,working_cnt)
)pvt
