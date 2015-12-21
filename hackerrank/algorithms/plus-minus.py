# https://www.hackerrank.com/challenges/plus-minus

import sys
import math
import collections


def sign(n):
    return 0 if n == 0 else math.copysign(1, n)


if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    numbers = list(map(int, f.readline().strip().split()))
    counter = collections.Counter()
    for number in numbers:
        counter[sign(number)] += 1
    format_fraction = lambda s: '%.6f' % round(counter[s] / n, 6)
    print(format_fraction(1))
    print(format_fraction(-1))
    print(format_fraction(0))
