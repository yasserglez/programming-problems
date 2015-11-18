-- SQLite does not implement FULL OUTER JOIN

SELECT
  A.id,
  A.name,
  B.id,
  B.name
FROM
  TableA AS A
  LEFT JOIN TableB as B
    ON A.name = B.name
WHERE
  B.name IS NULL
UNION
SELECT
  A.id,
  A.name,
  B.id,
  B.name
FROM
  TableB AS B
  LEFT JOIN TableA as A
    ON A.name = B.name
WHERE
  A.name IS NULL;
