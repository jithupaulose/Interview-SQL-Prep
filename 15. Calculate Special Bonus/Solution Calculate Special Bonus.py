Kurach chindikkendi varumm.

No groupby ellam venam
CASE vech aaa cheyendae 
% ariyanam

10%2 = 0 aanuu NOT LIKE % VENAM





SELECT 
employee_id ,
(CASE WHEN employee_id%2 = 1 AND name NOT LIKE 'M%' THEN salary ELSE 0 END
) AS bonus 
FROM 
Employees 

