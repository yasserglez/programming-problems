SELECT *
FROM
  TableA AS A
  LEFT JOIN TableB as B
    ON A.name = B.name
WHERE
  B.name IS NULL;
