With cte as
(
select Wimbledon as play from Championships 
    UNION ALL
select Fr_open as play from Championships 
    UNION ALL
select US_open as play from Championships 
    UNION ALL
select Au_open as play from Championships 

)
SELECT player_id,player_name, count(*) as grand_slams_count  FROM Players P
JOIN CTE C ON P.player_id = C.play
group by P.player_id 