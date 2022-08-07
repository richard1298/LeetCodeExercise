/* Write your T-SQL query statement below */

with cte as
(select t.left_operand, t.left_value, t.operator,t.right_operand,v2.value right_value
from 
(select e.left_operand, v.value left_value, e.operator, e.right_operand from
Expressions e left join Variables v
on e.left_operand = v.name) t
left join Variables v2
on t.right_operand = v2.name)

select left_operand, operator, right_operand,
(case when operator = '>' then (case when left_value >right_value then 'true' else 'false' end)
      when operator = '<' then (case when left_value <right_value then 'true' else 'false' end)
      when operator = '=' then (case when left_value =right_value then 'true' else 'false' end)    end) as value
from cte