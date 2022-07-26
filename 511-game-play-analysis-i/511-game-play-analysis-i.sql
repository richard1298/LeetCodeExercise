/* Write your T-SQL query statement below */

/*
SELECT player_id, min(event_date) as first_login
from Activity 
group by player_id
*/
SELECT distinct(player_id) player_id,
        min(event_date) over(partition by player_id) as first_login
FROM Activity