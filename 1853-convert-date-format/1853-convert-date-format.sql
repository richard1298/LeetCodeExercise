/* Write your T-SQL query statement below */
select concat(datename(weekday,day),', ',datename(month,day),' ',day(day),', ',year(day)) day
from Days