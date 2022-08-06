/* Write your T-SQL query statement below */

select c.country_name, 
(case when t.av <= 15 then 'Cold'
 when t.av >= 25 then 'Hot'
 else 'Warm' end) weather_type
from
(select distinct country_id,
    avg(cast(weather_state as float)) over (partition by country_id) av from Weather 
where year(day) = 2019 and month(day) = 11) t
left join Countries c
on t.country_id = c.country_id