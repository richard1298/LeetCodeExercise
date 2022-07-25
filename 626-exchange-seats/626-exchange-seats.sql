/* Write your T-SQL query statement below */

select 
t.id,
case
when t.id % 2 = 0 then (select student from Seat where Seat.id = t.id - 1)
when t.id %2 = 1 then ISNULL((select student from Seat where Seat.id = t.id + 1), student)             
end as student
from
(select s1.id,s1.student,s2.id swapid, s2.student nameswap from 
Seat s1 inner join Seat s2
on s1.id = s2.id) t
