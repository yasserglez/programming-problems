# https://leetcode.com/problems/two-sum/

import fileinput
import collections


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
    with fileinput.input() as fi:
        test_cases = int(fi.readline())
        for i in range(test_cases):
            numbers = list(map(int, fi.readline().strip().split()))
            target = int(fi.readline())
            index1, index2 = twoSum(numbers, target)
            print(index1, index2)
