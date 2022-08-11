/* Write your T-SQL query statement below */


select school_id, score
from
(select s.school_id,isnull(e.score,-1) score,
s.capacity,e.student_count, 
row_number() over(partition by s.school_id order by e.score) rn
from
Schools s left join Exam e
on s.capacity >=e.student_count) t
where (rn = 1 or rn = -1)
