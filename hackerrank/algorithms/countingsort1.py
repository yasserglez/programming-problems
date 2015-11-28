# https://www.hackerrank.com/challenges/countingsort1

import sys


def countingsort1(numbers):
    counts = [0] * 100
    for number in numbers:
        counts[number] += 1
    return counts


if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    numbers = list(map(int, f.readline().rstrip().split()))
    assert len(numbers) == n
    counts = countingsort1(numbers)
    print(' '.join(map(str, counts)))
