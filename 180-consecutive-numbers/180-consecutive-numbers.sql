/* Write your T-SQL query statement below */
WITH Sel AS
(
    SELECT 
        Num,
        LAG(Num, 1) OVER (ORDER BY Id) AS Prev,
        LEAD(Num, 1) OVER (ORDER BY Id) AS Next
    FROM Logs
)

select distinct Num  as ConsecutiveNums from Sel
where Prev = Num and Next = Num