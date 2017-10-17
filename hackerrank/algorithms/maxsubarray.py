# https://www.hackerrank.com/challenges/maxsubarray

import sys


def maxsubarray_contiguous(numbers):
    max_ending_here = numbers[0]
    max_so_far = numbers[0]
    for n in numbers[1:]:
        max_ending_here = max(n, max_ending_here + n)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


def maxsubarray_noncontiguous(numbers):
    max_number = numbers[0]
    max_positive_sum = max(0, numbers[0])
    for n in numbers[1:]:
        max_number = max(n, max_number)
        max_positive_sum += max(n, 0)
    return max_positive_sum if max_positive_sum > 0 else max_number


def maxsubarray(numbers):
    return maxsubarray_contiguous(numbers), maxsubarray_noncontiguous(numbers)


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        numbers = list(map(int, f.readline().rstrip().split()))
        print(' '.join(map(str, maxsubarray(numbers))))
