/* Write your T-SQL query statement below */
SELECT psn.firstName, psn.lastName, ads.city, ads.state
from Address ads 
right join Person psn
on ads.personId = psn.personId

