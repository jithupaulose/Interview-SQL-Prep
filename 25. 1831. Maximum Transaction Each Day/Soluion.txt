
with cte as (
    
SELECT  
transaction_id,
 dense_rank()  over(partition by date(day) order by amount desc ) as max_value

FROM 
Transactions 
)

select transaction_id   from cte  where max_value = 1 
order by transaction_id