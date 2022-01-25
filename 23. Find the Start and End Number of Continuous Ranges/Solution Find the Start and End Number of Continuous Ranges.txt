With ranking as


(
select 
log_id , log_id - dense_rank() over(order by log_id) as rnkorder
from   
Logs 

order by log_id  
)

Select min(log_id) as start_id   , max(log_id) as end_id from ranking

group by rnkorder