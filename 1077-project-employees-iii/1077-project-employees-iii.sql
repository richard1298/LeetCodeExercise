/* Write your T-SQL query statement below */

with cte as 
(select p.project_id, p.employee_id, e.name, e.experience_years from 
Project p left join Employee e
on p.employee_id = e. employee_id)

select cte.project_id, cte.employee_id 
from
(select distinct project_id, (max(experience_years) over(partition by project_id)) maxyear
from cte) t
inner join cte 
on t.project_id = cte.project_id and cte.experience_years = t.maxyear
