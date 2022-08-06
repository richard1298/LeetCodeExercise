/* Write your T-SQL query statement below */

select account_id, day, sum(amount) over (partition by account_id order by day) as balance
from
(select account_id, day, (case when type = 'Deposit' then amount else -amount end) amount
from Transactions)t
