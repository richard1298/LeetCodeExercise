/* Write your T-SQL query statement below */

select t.member_A, t.member_B, c.student_name member_C
from
(select a.student_id member_Aid, a.student_name member_A, 
       b.student_id member_Bid, b.student_name member_B
from SchoolA a cross join SchoolB b
where a.student_id != b.student_id and a.student_name!= b.student_name) t
cross join SchoolC c
where t.member_Aid != c.student_id and t.member_Bid !=c.student_id
and t.member_A != c.student_name and t.member_B !=c.student_name