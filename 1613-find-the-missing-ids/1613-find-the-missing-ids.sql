/* Write your T-SQL query statement below */
DECLARE @startnum INT=1
DECLARE @endnum INT=100
;
WITH gen AS (
    SELECT @startnum AS num
    UNION ALL
    SELECT num+1 FROM gen WHERE num+1<=@endnum
    )


SELECT G.NUM AS ids
FROM GEN AS G
WHERE G.NUM <=
    (SELECT MAX(C.CUSTOMER_ID)
    FROM CUSTOMERS AS C)
    AND G.NUM NOT IN
    (SELECT C1.CUSTOMER_ID
    FROM CUSTOMERS AS C1)
