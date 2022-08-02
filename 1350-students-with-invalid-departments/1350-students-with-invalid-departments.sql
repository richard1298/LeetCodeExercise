/* Write your T-SQL query statement below */
/*select id,name from Students 
where department_id not in (select id from Departments)
*/
select id,name from Students s
where not exists
(select id from Departments d where s.department_id = d.id)