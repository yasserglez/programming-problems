# https://www.hackerrank.com/challenges/mini-max-sum

import sys


def mini_max_sum(numbers):
    s = sum(numbers)
    m = M = s - numbers[0]
    for i in numbers[1:]:
        m = min(m, s - i)
        M = max(M, s - i)
    return m, M


if __name__ == '__main__':
    f = sys.stdin
    numbers = list(map(int, f.read().split()))
    result = mini_max_sum(numbers)
    print('{} {}'.format(*result))
