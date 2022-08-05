/* Write your T-SQL query statement below */

select * from
(select gender, day, sum(total) over(order by day) total 
from 
(select gender, day, sum(score_points) total
from Scores
where gender = 'F'
group by gender, day) cte1

UNION

select gender, day, sum(total) over(order by day) total 
from 
(select gender, day, sum(score_points) total
from Scores
where gender = 'M'
group by gender, day) cte2) cte3
order by gender, day

