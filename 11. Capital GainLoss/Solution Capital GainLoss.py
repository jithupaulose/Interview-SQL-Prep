Idthum oru good question annu


first output analyse cheyukka

group by  and order by yum vename for stock_name

evarkk sell - buy differnce aaa vendath


sum and case fuction ittu cheyyam idth 



SELECT stock_name,

SUM(
    (CASE WHEN operation = 'Buy' THEN -price 
     WHEN operation = 'Sell' THEN price END)
)
 AS capital_gain_loss 

FROM Stocks 

GROUP BY stock_name
ORDER BY stock_name