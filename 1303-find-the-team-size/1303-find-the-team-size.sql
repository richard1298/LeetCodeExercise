/* Write your T-SQL query statement below */

select e.employee_id,a.team_size
from Employee e left join
(SELECT team_id, count(team_id) team_size
FROM Employee e
group by team_id) a
on a.team_id = e.team_id
