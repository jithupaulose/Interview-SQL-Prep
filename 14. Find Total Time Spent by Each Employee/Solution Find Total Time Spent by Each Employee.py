Idth scene illaa.


Group by cheyanno ennu nokkuka
venam so which one okkae venam 

day and emp_id ittu group by cheyanam


SUM vech differnce of out and in time cehythal output kittum

SELECT event_day AS day , emp_id , SUM(out_time -in_time) AS total_time 

FROM Employees 

GROUP BY event_day, emp_id
order by event_day;