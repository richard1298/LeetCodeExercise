CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        select isnull(
        (select distinct salary from    
        (select dense_rank() over (order by salary desc) as rnk,
            salary from employee )t
        where rnk = @N),Null)
        

               
    );
END