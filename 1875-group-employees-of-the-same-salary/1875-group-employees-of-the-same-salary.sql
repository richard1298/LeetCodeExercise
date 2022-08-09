/* Write your T-SQL query statement below */

with cte as (select salary from 
(SELECT salary, count(salary) salary_num from Employees
group by salary) t
where salary_num >1)

select *, dense_rank() over(order by salary) team_id
from
(select e.employee_id, e.name, e.salary from Employees e
right join cte
on e.salary = cte.salary)t2
order by team_id, employee_id
