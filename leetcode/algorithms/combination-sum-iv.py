# https://leetcode.com/problems/combination-sum-iv/

from typing import List


class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = {}
        def _solve(t):
            if t < 0:
                return 0
            elif t == 0:
                return 1
            else:
                if t not in mem:
                    mem[t] = 0
                    for n in nums:
                        mem[t] += _solve(t - n)
                return mem[t]
        return _solve(target)


# nums = [1, 2, 3]
# target = 4
nums = [4, 2, 1]
target = 32
s = Solution()
r = s.combinationSum4(nums, target)
print(r)
