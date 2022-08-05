/* Write your T-SQL query statement below */

with cte as 
(SELECT p.player_id, p.player_name, c.year, c.Wimbledon, c.Fr_open, c.Us_open, c.Au_open
FROM Players p inner join Championships c
on p.player_id = c.Wimbledon
or p.player_id = c.Fr_open
or p.player_id = c.US_open
or p.player_id = c.Au_open)

select player_id, player_name,
sum((case when Wimbledon = player_id then 1 else 0 end)
   +(case when Fr_open = player_id then 1 else 0 end)
   +(case when Us_open = player_id then 1 else 0 end)
   +(case when Au_open = player_id then 1 else 0 end)) grand_slams_count
from cte group by player_id,player_name
