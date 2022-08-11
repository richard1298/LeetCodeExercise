/* Write your T-SQL query statement below */


with cte1 as
(select distinct departure_airport, 
sum(flights_count) over(partition by departure_airport) as flightsout
from Flights),
cte2 as
(select distinct arrival_airport, 
sum(flights_count) over(partition by arrival_airport) as flightsin
from Flights)

select airport_id from
(select airport_id, rank() over(order by cnt desc) rnk
from
(select 
(case when cte1.departure_airport is null then cte2.arrival_airport else cte1.departure_airport end)
as airport_id,
((case when cte1.flightsout is null then 0 else cte1.flightsout end)
+(case when cte2.flightsin is null then 0 else cte2.flightsin end)) cnt
from 
cte1 full outer join cte2
on cte1.departure_airport = cte2.arrival_airport) t3)t4
where rnk = 1