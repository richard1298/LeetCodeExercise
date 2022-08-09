/* Write your T-SQL query statement below */

with cte as 
(select member_id, 
100*cast(sum(case when charged_amount != 0 then 1 else 0 end) as float)/cast(count(visit_id) as float) conv,
count(visit_id) visits
from
(select visit_id, member_id, visit_date,isnull(charged_amount,0) charged_amount
from
(select v.visit_id, v.member_id, v.visit_date,p.charged_amount from 
Visits v left join Purchases p
on v.visit_id = p.visit_id) t)t1
group by member_id)

select member_id, name,
(case when visits is null then 'Bronze'
      when conv < 50 and visits is not null then 'Silver'
      when conv>= 50 and conv<80 and visits is not null then 'Gold'
      when conv>=80 and visits is not null then 'Diamond'
end) as category
from
(select m.member_id, m.name,cte.visits, cte.conv
from Members m left join cte
on m.member_id = cte.member_id) t2
