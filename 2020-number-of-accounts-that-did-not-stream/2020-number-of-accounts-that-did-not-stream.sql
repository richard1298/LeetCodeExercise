/* Write your T-SQL query statement below */

with cte as
(select s.account_id,s.start_date, s.end_date,t2.stream2021
from Subscriptions s 
left join
(select account_id, (case when sum(stream2021)>=1 then 1 else 0 end) stream2021
from
(select account_id, 
(case when stream_date between '2021-1-1' and '2021-12-31' then 1 else 0 end) stream2021
from Streams) t
group by account_id)t2
on s.account_id = t2.account_id)


select sum(case when subs2021 = 1 and stream2021 = 0 then 1 else 0 end) as accounts_count
from
(select account_id, 
(case when ((start_date between '2021-1-1' and '2021-12-31') or (end_date between '2021-1-1' and '2021-12-31')) then 1 else 0 end) as subs2021,
isnull(stream2021,0) stream2021
from cte) t3
