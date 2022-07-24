/* Write your T-SQL query statement below */


select a.sell_date,count(products) num_sold, string_agg(products,',')
within group (order by products) as products
from
(select distinct sell_date,product products from Activities) a
group by a.sell_date