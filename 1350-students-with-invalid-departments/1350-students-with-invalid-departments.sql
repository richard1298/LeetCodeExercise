/* Write your T-SQL query statement below */
select id,name from Students 
where department_id not in (select id from Departments)