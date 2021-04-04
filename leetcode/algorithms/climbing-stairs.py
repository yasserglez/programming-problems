# https://leetcode.com/problems/climbing-stairs/

import sys
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        results: List[int] = [0, 1, 2] + [-1] * max(0, n - 2)
        for i in range(3, n + 1):
            results[i] = results[i - 1] + results[i - 2]
        return results[n]


if __name__ == '__main__':
    s = Solution()
    f = sys.stdin
    test_cases = int(f.readline())
    for i in range(test_cases):
        print(s.climbStairs(int(f.readline())))
