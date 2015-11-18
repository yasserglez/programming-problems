-- SQLite does not implement RIGHT OUTER JOIN or FULL OUTER JOIN

SELECT
  A.id,
  A.name,
  B.id,
  B.name
FROM
  TableA AS A
  LEFT JOIN TableB AS B
    ON A.name = B.name
UNION
SELECT
  A.id,
  A.name,
  B.id,
  B.name
FROM
  TableB AS B
  LEFT JOIN TableA AS A
    ON A.name = B.name;
