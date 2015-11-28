# https://www.hackerrank.com/challenges/normal-distribution-2

mu <- 20
sigma <- 2
digits <- 3

# a) less than 19.5 hours?
ans <- pnorm(19.5, mu, sigma)
cat(round(ans, digits), "\n")

# b) between 20 and 22 hours?
ans <- pnorm(22, mu, sigma) - pnorm(20, mu, sigma)
cat(round(ans, digits), "\n")
