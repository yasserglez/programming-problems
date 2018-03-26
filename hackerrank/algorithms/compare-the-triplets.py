# https://www.hackerrank.com/challenges/compare-the-triplets

import sys


def compare_the_triplets(a, b):
    score = lambda t1, t2: sum(t1[i] > t2[i] for i in range(3))
    return score(a, b), score(b, a)


if __name__ == '__main__':
    f = sys.stdin
    a = tuple(map(int, f.readline().split()))
    b = tuple(map(int, f.readline().split()))
    print(' '.join(map(str, compare_the_triplets(a, b))))
