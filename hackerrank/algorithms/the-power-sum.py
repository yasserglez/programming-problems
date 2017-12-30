# https://www.hackerrank.com/challenges/the-power-sum

import sys
import math


def memoize(f):
    memory = {}

    def ff(*args):
        if args not in memory:
            memory[args] = f(*args)
        return memory[args]

    return ff


def the_power_sum(x, n):
    max_base = int(math.floor(x ** (1 / n)))
    terms = [base ** n for base in range(1, max_base + 1)]

    @memoize
    def count_ways(target, i):
        if i == len(terms):
            return 0
        elif target == terms[i]:
            return 1
        else:  # target > terms[i]
            including_term = count_ways(target - terms[i], i + 1)
            not_including_it = count_ways(target, i + 1)
            return including_term + not_including_it

    return count_ways(x, 0)


if __name__ == '__main__':
    x = int(sys.stdin.readline())
    assert 1 <= x <= 1000
    n = int(sys.stdin.readline())
    assert 2 <= n <= 10
    print(the_power_sum(x, n))
