/* Write your T-SQL query statement below */

select user_id,gender from 
(SELECT user_id, gender, dense_rank() over(partition by gender order by user_id) rnk FROM Genders) t
order by rnk,
case when gender = 'female' then 1
when gender = 'other' then 2
when gender = 'male' then 3
end
