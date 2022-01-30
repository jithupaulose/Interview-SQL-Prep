With CTE as



(

SELECT U.name, SUM(T.amount) as balance 
from 
Users U 
JOIN Transactions T ON 
U.account = T.account 
GROUP BY U.name
)

select * from CTE where balance > 10000
