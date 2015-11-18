-- SQLite does not implement RIGHT OUTER JOIN

SELECT
  A.id,
  A.name,
  B.id,
  B.name
FROM
  TableB AS B
  LEFT JOIN TableA AS A
    ON A.name = B.name;
