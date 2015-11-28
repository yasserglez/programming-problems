# https://www.hackerrank.com/challenges/countingsort2

import sys


def countingsort1(numbers):
    counts = [0] * 100
    for number in numbers:
        counts[number] += 1
    return counts


def printnumbers(counts):
    first = True
    for i in range(len(counts)):
        for c in range(counts[i]):
            print('' if first else ' ', i, sep='', end='')
            first = False
    print()


if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    numbers = list(map(int, f.readline().rstrip().split()))
    assert len(numbers) == n
    counts = countingsort1(numbers)
    printnumbers(counts)
