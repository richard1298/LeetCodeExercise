/* Write your T-SQL query statement below */

select round(100*cast(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) as float)/
cast(count(delivery_id) as float),2) immediate_percentage
from Delivery