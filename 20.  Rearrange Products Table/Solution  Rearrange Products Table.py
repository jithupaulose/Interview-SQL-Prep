Idth oru new patern question aannu. COLUMN row aaakki  maatnam

Enk logic ariyillaaa . But union all vech sub query ezhuthiyal pattumm





SELECT product_id, store, price

FROM

(
SELECT product_id, 'store1' AS store  , store1 AS price FROM Products 
UNION ALL

SELECT product_id, 'store2' AS store  , store2 AS price FROM Products 

UNION ALL
SELECT product_id, 'store3' AS store  , store3 AS price FROM Products 

) A where price is not null



(
SELECT product_id, 'store1' AS store  , store1 AS price FROM Products 
WHERE store1 IS NOT NULL
UNION ALL

SELECT product_id, 'store2' AS store  , store2 AS price FROM Products 
WHERE store2 IS NOT NULL

UNION ALL
SELECT product_id, 'store3' AS store  , store3 AS price FROM Products 
WHERE store3 IS NOT NULL

) A