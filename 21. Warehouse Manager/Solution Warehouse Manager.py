With CTE AS
(

SELECT product_id, (Width * Length * Height) AS volume1     
    FROM Products GROUP BY product_id 

)

SELECT name AS warehouse_name ,sum(C.volume1 * W.units)  as      volume     
FROM Warehouse W
LEFT JOIN CTE C 
ON W.product_id   = C.product_id   

GROUP BY W.name;