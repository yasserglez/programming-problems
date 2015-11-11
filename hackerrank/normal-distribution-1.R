# https://www.hackerrank.com/challenges/normal-distribution-1

mu <- 30
sigma <- 4
digits <- 3

# a) P(x < 40)
ans <- pnorm(40, mu, sigma)
cat(round(ans, digits), "\n")

# b) P(x > 21)
ans <- 1 - pnorm(21, mu, sigma)
cat(round(ans, digits), "\n")

# c) P(30 < x < 35)
ans <- pnorm(35, mu, sigma) - pnorm(30, mu, sigma)
cat(round(ans, digits), "\n")
