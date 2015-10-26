# https://leetcode.com/problems/two-sum/

import collections
import sys


def twoSum(numbers, target):
    n = len(numbers)
    complements = collections.defaultdict(list)
    for i in range(n):
        complements[numbers[i]].append(i)
    for i in range(n):
        complement = target - numbers[i]
        if complement in complements:
            for j in complements[complement]:
                if i < j:
                    return [i + 1, j + 1]


if __name__ == '__main__':
    f = sys.stdin
    test_cases = int(f.readline())
    for i in range(test_cases):
        numbers = list(map(int, f.readline().strip().split()))
        target = int(f.readline())
        index1, index2 = twoSum(numbers, target)
        print(index1, index2)
