/* Write your T-SQL query statement below */

with cte as 
(select from_id, to_id, 
 (case when from_id<to_id then from_id else to_id end) new_from_id,
 (case when from_id<to_id then to_id else from_id end) new_to_id,
 duration
 from Calls
)
select new_from_id person1,new_to_id person2,count(*) call_count,sum(duration) total_duration
from cte
group by new_from_id, new_to_id