/* Write your T-SQL query statement below */


with cte as
(select distinct visited_on, 
(sum(amount) over (partition by visited_on)) as amount
from Customer)


select visited_on,amount,average_amount from
(select visited_on, 
sum(amount) over(order by visited_on rows between 6 preceding and current row) as amount,
round(cast(sum(amount) over(order by visited_on rows between 6 preceding and current row ) as float)/7,2) as average_amount,
rownum
from
(select *,row_number() over (order by visited_on) as rownum
from cte) t) t1
where rownum>=7
