# https://leetcode.com/problems/contains-duplicate/

import fileinput


def containsDuplicate(numbers):
    return len(numbers) != len(set(numbers))


if __name__ == '__main__':
    for line in fileinput.input():
        numbers = list(map(int, line.rstrip().split()))
        print(containsDuplicate(numbers))
