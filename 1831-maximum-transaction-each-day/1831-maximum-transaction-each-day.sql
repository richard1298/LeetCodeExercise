/* Write your T-SQL query statement below */

with cte as
(select 
distinct day,
max(amount) over(partition by day) as maxamt
from
(select transaction_id,convert(date,day) day,amount
from Transactions) t)

select transaction_id from 
Transactions inner join cte 
on convert(date,Transactions.day) = cte.day
and Transactions.amount = cte.maxamt
order by transaction_id

