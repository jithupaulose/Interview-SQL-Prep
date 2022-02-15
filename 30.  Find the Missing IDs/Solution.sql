With recursive cte as

(
Select 1 AS ids 
    UNION ALL
    SELECT ids+1 from cte where ids < (select max(customer_id ) from Customers)
)

select ids from cte
where ids not in (select customer_id from Customers )

order by ids;


