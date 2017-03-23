-- https://www.hackerrank.com/challenges/average-population-of-each-continent

SELECT
  country.continent,
  CAST(AVG(city.population) AS INTEGER)
FROM
  city INNER JOIN country ON city.countrycode = country.code
GROUP BY
  country.continent;
