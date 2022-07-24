/* Write your T-SQL query statement below */

SELECT t.Department, ee.name Employee, t.Salary 
FROM 
(SELECT d.name Department,d.id departmentId, max(e.salary) Salary
FROM Employee e
inner join Department d
on e.departmentId = d.id
group by d.name,d.id) t
left join Employee ee
on ee.departmentId = t.departmentId and ee.salary = t.Salary


