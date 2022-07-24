/* Write your T-SQL query statement below */


/*select piv.id, 
piv.Jan 'Jan_Revenue',
piv.Feb 'Feb_Revenue',
piv.Mar 'Mar_Revenue',
piv.Apr 'Apr_Revenue',
piv.May 'May_Revenue',
piv.Jun 'Jun_Revenue',
piv.Jul 'Jul_Revenue',
piv.Aug 'Aug_Revenue',
piv.Sep 'Sep_Revenue',
piv.Oct 'Oct_Revenue',
piv.Nov 'Nov_Revenue',
piv.Dec 'Dec_Revenue' 
from(*/

select piv.id, 
piv.Jan 'Jan_Revenue',
piv.Feb 'Feb_Revenue',
piv.Mar 'Mar_Revenue',
piv.Apr 'Apr_Revenue',
piv.May 'May_Revenue',
piv.Jun 'Jun_Revenue',
piv.Jul 'Jul_Revenue',
piv.Aug 'Aug_Revenue',
piv.Sep 'Sep_Revenue',
piv.Oct 'Oct_Revenue',
piv.Nov 'Nov_Revenue',
piv.Dec 'Dec_Revenue' 
from department
PIVOT(
sum(revenue)
for month in(
"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
) as piv

