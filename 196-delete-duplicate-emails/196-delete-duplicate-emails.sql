/* 
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your T-SQL query statement below
 */
DELETE FROM Person
WHERE ID NOT IN 
(SELECT MIN(id) FROM Person group by email)