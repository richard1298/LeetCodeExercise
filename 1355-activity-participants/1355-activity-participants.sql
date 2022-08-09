/* Write your T-SQL query statement below */

with t as 
(select activity,count(activity) participants from Friends
group by activity)

select activity from t
where (participants != (select max(participants) from t)
and participants!= (select min(participants) from t))