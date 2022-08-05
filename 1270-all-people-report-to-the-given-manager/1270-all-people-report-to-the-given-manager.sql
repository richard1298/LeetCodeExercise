/* Write your T-SQL query statement below */
select employee_id from
(select e1.employee_id, e1.manager_id manager1, e2.manager_id manager2, e3.manager_id manager3 from
Employees e1 left join Employees e2
on e1.manager_id = e2.employee_id
left join Employees e3
on e2.manager_id = e3.employee_id)t
where (manager1 = 1 or manager2 = 1 or manager3 = 1) and employee_id != 1