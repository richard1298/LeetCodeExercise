select count(*) as accounts_count
from(
select sbs.account_id,
sum (case when stream_date between '2021-01-01' and '2021-12-31' then 1 else 0 end) as ct
from
Subscriptions sbs inner join
Streams  stm on sbs.account_id = stm.account_id
where end_date>='2021-01-01'
group by sbs.account_id ) A where ct=0