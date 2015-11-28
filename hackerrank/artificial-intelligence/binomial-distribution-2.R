# https://www.hackerrank.com/challenges/binomial-distribution-2

n <- 6
p <- 1.09 / (1.09 + 1)
digits <- 3

ans <- sum(dbinom(3:n, n, p))
cat(round(ans, digits), "\n")
