# https://www.hackerrank.com/challenges/normal-distribution-3

mu <- 70
sigma <- 10
digits <- 2

# a) scored higher than 80?
ans <- 100 * (1 - pnorm(80, mu, sigma))
cat(round(ans, digits), "\n")

# b) should pass the test (grades >= 60)?
ans <- 100 * (1 - pnorm(60, mu, sigma))
cat(round(ans, digits), "\n")

# c) should fail the test (grades < 60)?
ans <- 100 * pnorm(60, mu, sigma)
cat(round(ans, digits), "\n")
