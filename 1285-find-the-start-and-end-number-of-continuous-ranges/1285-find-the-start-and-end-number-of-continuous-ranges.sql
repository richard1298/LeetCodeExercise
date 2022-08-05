/* Write your T-SQL query statement below */

select min(log_id) start_id, max(log_id) end_id 
from
(select log_id,
log_id - row_number() over(order by log_id) flag
from Logs) t
group by flag