-- https://www.hackerrank.com/challenges/asian-population

SELECT
  sum(city.population)
FROM
  city INNER JOIN country ON city.countrycode = country.code
WHERE
  country.continent = 'Asia';
