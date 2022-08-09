/* Write your T-SQL query statement below */


select driver_id, (case when ride_id = null then 0 else count(ride_id) end) cnt
from
(select t1.driver_id, Rides.ride_id
from
Rides right join 
(select distinct driver_id from Rides)t1
on Rides.passenger_id = t1.driver_id)t2
group by driver_id