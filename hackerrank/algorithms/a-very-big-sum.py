# https://www.hackerrank.com/challenges/a-very-big-sum

import sys


if __name__ == '__main__':
    f = sys.stdin
    N = int(f.readline())
    numbers = map(int, f.readline().strip().split())
    print(sum(numbers))
