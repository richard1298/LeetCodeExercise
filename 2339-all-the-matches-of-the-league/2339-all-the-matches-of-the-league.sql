/* Write your T-SQL query statement below */
select a.team_name home_team, b.team_name away_team
from Teams a cross join Teams b
where a.team_name != b.team_name