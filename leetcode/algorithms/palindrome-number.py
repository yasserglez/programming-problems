# https://leetcode.com/problems/palindrome-number/

import math


def isPalindrome(x):
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        i = 0
        j = int(math.log(x, 10))
        digit = lambda k: (x // 10 ** k) % 10
        while i < j:
            if digit(i) != digit(j):
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    print(isPalindrome(-1))
    print(isPalindrome(0))
    print(isPalindrome(1))
    print(isPalindrome(11))
    print(isPalindrome(12))
    print(isPalindrome(121))
    print(isPalindrome(123))
