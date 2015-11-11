# https://www.hackerrank.com/challenges/binomial-distribution-3

n <- 10
p <- 0.12
digits <- 3

# a) no more than 2 rejects?
ans <- pbinom(2, n, p)
cat(round(ans, digits), "\n")

# b) at least 2 rejects?
ans <- sum(dbinom(2:n, n, p))
cat(round(ans, digits), "\n")
