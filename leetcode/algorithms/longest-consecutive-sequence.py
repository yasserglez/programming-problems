# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import Set, List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s: Set[int] = set(nums)
        longest: int = 0
        for x in s:
            if x - 1 in s:
                continue
            else:
                count = 1
                x += 1
                while x in s:
                    count += 1
                    x += 1
                if longest is None:
                    longest = count
                elif count > longest:
                    longest = count
        return longest


s = Solution()
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(s.longestConsecutive(nums))
