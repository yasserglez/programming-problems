-- https://leetcode.com/problems/exchange-seats

SELECT
    s1.id as id,
    COALESCE(s2.student, s1.student) as student
FROM 
    seat AS s1 LEFT JOIN seat AS s2 
    ON (CASE s1.id % 2 WHEN 1 THEN s1.id + 1 ELSE s1.id - 1 END) = s2.id
ORDER BY id;