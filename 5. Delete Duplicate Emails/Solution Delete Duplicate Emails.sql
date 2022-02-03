
DELETE 
    P2 
FROM Person P1 
JOIN Person P2 
WHERE P1.email = P2.email AND P1.id < P2.id;
