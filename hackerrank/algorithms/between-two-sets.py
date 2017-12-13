# https://www.hackerrank.com/challenges/between-two-sets

import sys


def between_two_sets(A, B):
    count = 0
    for x in range(max(A), min(B) + 1):
        count += all(x % a == 0 for a in A) and all(b % x == 0 for b in B)
    return count


if __name__ == '__main__':
    f = sys.stdin
    n, m = list(map(int, f.readline().split()))
    A = set(map(int, f.readline().split()))
    B = set(map(int, f.readline().split()))
    print(between_two_sets(A, B))
