-- https://leetcode.com/problems/trips-and-users/

SELECT
  T.Request_at AS Date,
  round(SUM(T.Status LIKE "cancelled_%") / (1.0 * COUNT(*)), 2)
    AS `Cancellation Rate`
FROM
  Trips AS T
  INNER JOIN Users AS U
    ON T.Client_Id = U.Users_Id
WHERE
  U.Banned = "No" AND
  T.Request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY
  T.Request_at;
