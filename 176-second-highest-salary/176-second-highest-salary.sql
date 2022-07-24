/* Write your T-SQL query statement below */


/*
with temp as (select * from Employee)

select temp.id,(case when temp.salary = @mx then null else temp salary end) SecondHightestSalary from temp group by id,salary

*/

declare @mx as int
set @mx = (select max(salary) from Employee)
select top 1 (case when temp.salary = @mx then null else temp.salary end) SecondHighestSalary from 
(select * from Employee) temp 
order by SecondHighestSalary desc