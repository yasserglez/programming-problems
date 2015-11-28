# https://leetcode.com/problems/missing-number/


def missingNumber(numbers):
    n = len(numbers)
    s = sum(numbers)
    return n * (n + 1) // 2 - s


if __name__ == '__main__':
    numbers = [0, 1, 3]
    print(missingNumber(numbers))
