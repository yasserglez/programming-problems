SELECT
  s.Name AS Student_Name
FROM
  Friends AS f
  INNER JOIN Students AS s ON f.ID = s.ID
  INNER JOIN Packages AS sp ON s.ID = sp.ID
  INNER JOIN Packages AS fp ON f.Friend_ID = fp.ID
WHERE
  fp.Salary > sp.Salary
ORDER BY fp.Salary;
