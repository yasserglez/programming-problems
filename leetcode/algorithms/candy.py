# https://leetcode.com/problems/candy/

import fileinput


class Solution(object):

    def candy(self, r):
        n = len(r)
        c = [1] * n
        changed = True
        while changed:
            changed = False
            for i in range(1, n):
                if r[i] > r[i-1] and not c[i] > c[i-1]:
                    c[i] = c[i-1] + 1
                    changed = True
            for i in range(n-2, -1, -1):
                if r[i] > r[i+1] and not c[i] > c[i+1]:
                    c[i] = c[i+1] + 1
                    changed = True
        return sum(c)


if __name__ == '__main__':
    s = Solution()
    for line in fileinput.input():
        ratings = list(map(int, line.rstrip().split()))
        print(s.candy(ratings))
