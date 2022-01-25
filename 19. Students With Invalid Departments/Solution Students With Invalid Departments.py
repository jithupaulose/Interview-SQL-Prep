

SELECT S.id, S.name 
FROM 
Students S 
LEFT JOIN Departments D
ON S.department_id  = D.id
where D.id IS NULL




SELECT id, name
FROM Students 
WHERE department_id  NOT IN (SELECT id  FROM Departments )