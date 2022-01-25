
Idth oru kidullan question aaanu. sooshichu vaayichu nookanam.... Illenghil mansilavullaaa

ivarkk vendath  team size ill common etra undthintae count adth ella employeeid columnillum idanam


COUNT(teamsize) OVER(PARTITION BY teamsize) ittal ready aaakaam





SELECT employee_id, COUNT(team_id) OVER (PARTITION BY team_id) AS team_size
FROM Employee;