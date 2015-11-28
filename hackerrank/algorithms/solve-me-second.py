# https://www.hackerrank.com/challenges/solve-me-second

import sys


def solve_me_second(a, b):
    return a + b


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    for t in range(T):
        a, b = map(int, f.readline().strip().split())
        print(solve_me_second(a, b))
