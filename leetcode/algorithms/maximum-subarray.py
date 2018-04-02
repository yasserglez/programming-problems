# https://leetcode.com/problems/maximum-subarray/

import sys
import math


class Solution1(object):

    def maxSubArray(self, arr):
        max_sum = arr[0]
        for start in range(0, len(arr)):
            acum = 0
            for end in range(start, len(arr)):
                acum += arr[end]
                max_sum = max(max_sum, acum)
        return max_sum


class Solution2(object):

    def maxSubArray(self, arr):
        max_global = max_local = arr[0]
        for value in arr[1:]:
            max_local = max(value, max_local + value)
            max_global = max(max_local, max_global)
        return max_global


if __name__ == '__main__':
    sol = Solution2()
    for line in sys.stdin.readlines():
        arr = list(map(int, line.strip().split()))
        max_sum = sol.maxSubArray(arr)
        print(max_sum)
