SELECT DISTINCT
  f1.X AS X,
  f1.Y AS Y
FROM
  Functions f1
  INNER JOIN Functions f2 ON
    f1.X = f2.Y AND
    f2.X = f1.Y AND
    f1.ROWID != f2.ROWID
WHERE
    f1.X <= f1.Y
ORDER BY f1.X;
