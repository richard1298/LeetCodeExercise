/* Write your T-SQL query statement below */

with t1 as
(select * From
(select person_id, person_name, turn, weight,
sum(weight) over(order by turn) as cumsum
from Queue) t
where t.cumsum <=1000)


select person_name from t1
where turn = (select max(turn) from t1)