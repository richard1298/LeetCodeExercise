/* Write your T-SQL query statement below */

select name from Customer c where not exists(
select * from Customer d where c.referee_id = 2)