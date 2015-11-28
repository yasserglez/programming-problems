# https://leetcode.com/problems/reverse-integer/

import math
import fileinput


class Solution(object):

    def reverse1(self, x):
        if x == 0:
            return 0
        else:
            s = 1 if x > 0 else -1
            x = abs(x)
            d = int(math.log(x, 10) + 1)
            r = 0
            for k in range(d):
                r += (x % 10) * 10 ** (d - k - 1)
                x //= 10
            return s * r if r < 2 ** 31 else 0

    def reverse2(self, x):
        s = 1 if x > 0 else -1
        r = int(''.join(reversed(str(abs(x)))))
        return s * r if r < 2 ** 31 else 0

    reverse = reverse1


if __name__ == '__main__':
    s = Solution()
    for line in fileinput.input():
        x = int(line)
        print(s.reverse(x))
