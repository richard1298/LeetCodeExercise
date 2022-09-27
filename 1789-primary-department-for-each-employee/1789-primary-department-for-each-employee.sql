/* Write your T-SQL query statement below */
/*
select employee_id, department_id from Employee e1 where primary_flag = 'Y'

union
*/

with cte as
(select employee_id, department_id,
count(department_id) over (partition by employee_id) num_dep
from Employee e2 )

select employee_id, department_id from Employee e1 where primary_flag = 'Y'
union
select employee_id, department_id from cte where num_dep = 1


