# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/

import sys


def min_abs_diff(numbers):
    numbers_sorted = list(sorted(set(numbers)))
    if len(numbers_sorted) != len(numbers):
        return 0
    min_diff = None
    for i in range(len(numbers_sorted) - 1):
        j = i + 1
        diff = abs(numbers_sorted[i] - numbers_sorted[j])
        min_diff = diff if min_diff is None else min(min_diff, diff)
    return min_diff


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    print(min_abs_diff(numbers))
