-- https://leetcode.com/problems/second-highest-salary/

SELECT (
  SELECT DISTINCT Salary
  FROM Employee
  ORDER BY Salary DESC
  LIMIT 1
  OFFSET 1
);
