# https://www.hackerrank.com/challenges/simple-array-sum

import sys


if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    numbers = list(map(int, f.readline().strip().split()))
    print(sum(numbers))
