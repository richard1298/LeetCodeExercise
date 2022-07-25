/* Write your T-SQL query statement below */


select 
(case when e.employee_id is not null then e.employee_id
      else s.employee_id
end) employee_id
from 
Employees e full outer join Salaries s
on e.employee_id = s.employee_id
where e.name is null or s.salary is null
order by employee_id
