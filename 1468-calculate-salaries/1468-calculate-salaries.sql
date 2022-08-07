/* Write your T-SQL query statement below */

with cte as
(select company_id, 
(case when maxsal<1000 then 0
      when (maxsal>=1000 and maxsal<=10000) then 0.24
      when maxsal>10000 then 0.49 end) as tax from 
(select company_id, max(salary) maxsal from Salaries
group by company_id) t)

select s.company_id, s.employee_id, s.employee_name, round(cast(s.salary as float)*(1-cte.tax),0) as salary
from Salaries s left join cte
on s.company_id = cte.company_id


