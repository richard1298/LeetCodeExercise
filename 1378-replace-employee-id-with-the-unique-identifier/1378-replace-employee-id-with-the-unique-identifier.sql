/* Write your T-SQL query statement below */
SELECT unique_id, name
from Employees e left join EmployeeUNI b
on e.id = b.id