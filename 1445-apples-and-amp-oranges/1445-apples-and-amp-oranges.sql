/* Write your T-SQL query statement below */

select sale_date,sum(sold_num) diff from
(select sale_date,
fruit,
case
    when fruit = 'apples' then sold_num
    when fruit = 'oranges' then -sold_num
end as sold_num
from Sales) t
group by sale_date
