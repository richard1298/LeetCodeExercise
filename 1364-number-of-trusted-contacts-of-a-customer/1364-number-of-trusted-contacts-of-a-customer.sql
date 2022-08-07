/* Write your T-SQL query statement below */

with cte as
(select c.customer_id, c.customer_name,isnull(t2.contacts_cnt,0) contacts_cnt, isnull(t2.trusted_contacts_cnt,0) trusted_contacts_cnt
from
(select user_id, count(contact_name) contacts_cnt, sum(is_trusted) trusted_contacts_cnt
from
(select user_id, contact_name,
(case when contact_name in (select customer_name from Customers) then 1 else 0 end) is_trusted
from Contacts) t 
group by user_id) t2
right join Customers c
on c.customer_id = t2.user_id)

select i.invoice_id, cte.customer_name, i.price, cte.contacts_cnt, cte.trusted_contacts_cnt
from Invoices i left join cte 
on i.user_id = cte.customer_id
order by i.invoice_id


