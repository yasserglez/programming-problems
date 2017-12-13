# https://www.hackerrank.com/challenges/picking-numbers

import sys
from collections import Counter


def picking_numbers(integers):
    freq = Counter(integers)
    max_count = -1
    for number in freq:
        max_count = max(max_count, freq[number] + freq[number + 1])
    return max_count


if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    integers = list(map(int, f.readline().split()))
    print(picking_numbers(integers))
