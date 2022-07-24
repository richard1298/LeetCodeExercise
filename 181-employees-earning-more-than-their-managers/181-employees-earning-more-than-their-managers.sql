/* Write your T-SQL query statement below */


SELECT empl1.name Employee
FROM Employee empl1
LEFT JOIN Employee empl2
on empl2.id = empl1.managerId
where empl1.salary > empl2.salary
