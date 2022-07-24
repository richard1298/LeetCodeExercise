/* Write your T-SQL query statement below */

select * from (
select product_id, (case when store1 is not null then 'store1' else null end) store, (case when store1 is not null then store1 end) price from Products
union
select product_id, (case when store2 is not null then 'store2' else null end) store, (case when store2 is not null then store2 end) price from Products
union
select product_id, (case when store3 is not null then 'store3'  else null end) store, (case when store3 is not null then store3 end) price from Products)a
where price is not null