/* Write your T-SQL query statement below */
SELECT email from Person 
group by email
having count(email) >1