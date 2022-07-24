/* Write your T-SQL query statement below */
SELECT ct.name Customers
FROM Customers ct
LEFT JOIN Orders od
ON ct.id = od.customerId
where od.id is null




