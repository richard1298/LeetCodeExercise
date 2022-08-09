/* Write your T-SQL query statement below */


select user_id, 
isnull(round(cast(confirmed as float)/cast(timeout+confirmed as float),2),0) as confirmation_rate
from
(select s.user_id, t.timeout, t.confirmed
from
(select user_id, 
sum(case when action = 'timeout' then 1 else 0 end) timeout,
sum(case when action = 'confirmed' then 1 else 0 end) confirmed
from Confirmations
group by user_id) t
right join Signups s
on s.user_id = t.user_id)t2
