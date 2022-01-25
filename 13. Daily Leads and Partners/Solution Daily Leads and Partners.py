First namml output nooki structure manasilakukaa.


Group by cheyanam 2 ennathil date_id, make_name pinnae distinct lead and partnerid COUNT aayi ittal answer kittum



SELECT date_id, make_name , 
COUNT(DISTINCT lead_id ) AS unique_leads , 
COUNT(DISTINCT partner_id ) AS unique_partners 
FROM DailySales 
GROUP BY date_id, make_name 
