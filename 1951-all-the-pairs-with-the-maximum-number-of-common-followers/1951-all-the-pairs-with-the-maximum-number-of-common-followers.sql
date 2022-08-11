/* Write your T-SQL query statement below */

with a as (select a1.user_id as user1_id , a2.user_id as user2_id, count(*) cnt
from Relations  a1 
join Relations  a2 on a1.follower_id  = a2.follower_id and a1.user_id < a2.user_id
group by a1.user_id, a2.user_id
) 


select user1_id, user2_id from a
where cnt = (select max(cnt) from a)
