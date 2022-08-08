/* Write your T-SQL query statement below */






declare @td as date = '2021-1-1'

select user_id, (case when window >=windowtoday then window else windowtoday end) biggest_window
from
(select user_id, 
max(datediff(day,lag_visit_date,visit_date)) as window,
datediff(day,max(visit_date),@td) windowtoday
from 
(select user_id, 
visit_date,
lag(visit_date) over(partition by user_id order by visit_date) as lag_visit_date
from UserVisits) aa
group by user_id) bb
order by user_id