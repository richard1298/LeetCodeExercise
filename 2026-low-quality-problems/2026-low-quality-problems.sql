/* Write your T-SQL query statement below */
select problem_id from (
select problem_id, 
    cast(likes as float)/(cast(likes as float)+cast(dislikes as float)) ratio
from Problems) t
where t.ratio <0.6
order by problem_id 