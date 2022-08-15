/* Write your T-SQL query statement below */

/*
with cte as
(select 
(case when user1_id = 1 then user2_id 
     when user2_id = 1 then user1_id
     end) user1_friendid 
from Friendship
where user1_id = 1 or user2_id = 1)

select distinct(l.page_id) recommended_page
from cte left join Likes l
on cte.user1_friendid = l.user_id
where l.page_id not in (select isnull(page_id,'') from Likes where user_id = 1)*/


/*

select distinct page_id as recommended_page
from Likes
where user_id in
(select distinct
(case when user1_id = 1 then user2_id 
else user1_id end) as friends from Friendship
where user1_id = 1 or user2_id = 1)
and page_id not in (select page_id from Likes where user_id =1 )

*/


select distinct page_id as recommended_page from Likes where
user_id in (select case when user1_id = 1 then user2_id else user1_id end as user1_friend from Friendship where user1_id = 1 or user2_id=1)
and page_id not in (select page_id from Likes where user_id =1)
and user_id ! = 1









