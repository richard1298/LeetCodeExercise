/* Write your T-SQL query statement below */


with t1 as 
(select user_id, max(amt) maxamt
 from (select s.user_id, s.product_id, sum(s.quantity*p.price) amt from
Sales s inner join Product p
on s.product_id = p.product_id
group by s.user_id, s.product_id) a
group by user_id)


select t1.user_id, t2.product_id
from t1 right join 
(select s.user_id, s.product_id, sum(s.quantity*p.price) amt from
Sales s inner join Product p
on s.product_id = p.product_id
group by s.user_id, s.product_id) t2
on t1.user_id = t2.user_id
where t2.amt = t1.maxamt



