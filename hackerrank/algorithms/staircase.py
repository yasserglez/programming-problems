# https://www.hackerrank.com/challenges/staircase

import sys


def print_staircase(n):
    for i in range(n - 1, -1, -1):
        print(' ' * i + '#' * (n - i))


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print_staircase(n)
