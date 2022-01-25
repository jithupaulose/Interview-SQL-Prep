Kidullan question aaanu..



Evde customerID udae ordertype 0 aanenghil adth maatram print cheykka 
Baki scne illaaa


Oru ezhuppa vazhi undddd........

UNION vekkamm
first order type 0 aaki SELECT cheyukkaaa
then adth UNION ittuuu second select where orderype = 1 and ordertype not in (inner select ordertype = 0)

Solution 1 :


SELECT order_id, customer_id, order_type 
FROM Orders 
WHERE order_type = 0
    UNION
SELECT order_id, customer_id, order_type 
FROM Orders 
WHERE order_type = 1 AND customer_id 
NOT IN (SELECT customer_id FROM Orders WHERE order_type = 0)


Solution 2 :

