/* Write your T-SQL query statement below */
SELECT Visits.customer_id, count(Visits.visit_id) count_no_trans
FROM Visits 
LEFT JOIN Transactions
on Visits.visit_id = Transactions.visit_id
where Transactions.transaction_id is null
group by customer_id 
