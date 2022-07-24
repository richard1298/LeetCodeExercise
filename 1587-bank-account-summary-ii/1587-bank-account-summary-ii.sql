/* Write your T-SQL query statement below */

SELECT Users.name,a.balance FROM 
Users
inner join 
(select account, sum(amount) balance from Transactions group by account) a
on a.account = Users.account
where a.balance >10000