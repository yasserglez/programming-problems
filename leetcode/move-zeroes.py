# https://leetcode.com/problems/move-zeroes/

import fileinput


class Solution(object):

    def moveZeroes(self, nums):
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                if i != j:
                    nums[j] = 0
                i += 1
            j += 1


if __name__ == '__main__':
    s = Solution()
    for line in fileinput.input():
        nums = list(map(int, line.rstrip().split()))
        s.moveZeroes(nums)
        print(' '.join(map(str, nums)))
