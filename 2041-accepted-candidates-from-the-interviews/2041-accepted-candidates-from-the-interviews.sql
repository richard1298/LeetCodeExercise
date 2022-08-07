/* Write your T-SQL query statement below */

select c.candidate_id from
Candidates c left join
(select interview_id, sum(score) total_score from Rounds group by interview_id) s
on c.interview_id = s.interview_id
where c.years_of_exp >= 2 and s.total_score > 15