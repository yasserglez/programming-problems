# https://www.hackerrank.com/challenges/binomial-distribution-1

n <- 4
p <- 4/5
digits <- 3

# a) more than 2 hits?
ans <- 1 - pbinom(2, n, p)
cat(round(ans, digits), "\n")

# b) at least 3 misses?
ans <- sum(dbinom(n - 3:n, n, p))
cat(round(ans, digits), "\n")
