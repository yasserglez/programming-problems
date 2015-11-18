SELECT *
FROM
  TableA AS A
  LEFT JOIN TableB AS B
    ON A.name = B.name;
