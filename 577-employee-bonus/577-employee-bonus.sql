/* Write your T-SQL query statement below */

select * from 
(SELECT e.name,b.bonus
from Employee e left join Bonus b
on e.empId = b.empId) t
where t.bonus is Null or t.bonus < 1000