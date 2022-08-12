/* Write your T-SQL query statement below */

select distinct account_id as account_id
from
(select l1.account_id, l1.ip_address ip1, l1.login login1, l1.logout logout1,
l2.ip_address ip2, l2.login login2, l2.logout logout2
from 
LogInfo l1 full outer join LogInfo l2
on 
(l1.account_id = l2.account_id) and
(l1.ip_address < l2.ip_address) and
((l1.logout between l2.login and l2.logout) or (l2.logout between l1.login and l1.logout))) t2
where login1 is not null and login2 is not null
