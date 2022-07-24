/* Write your T-SQL query statement below */
select user_id, MAX(time_stamp) last_stamp
from Logins where time_stamp is not null and year(time_stamp) = 2020
group by user_id