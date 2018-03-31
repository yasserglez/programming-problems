# https://leetcode.com/problems/longest-substring-without-repeating-characters

import sys


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_length = 1
        for start in range(len(s)):
            chars = set([s[start]])
            end = len(s) - 1
            for i in range(start + 1, len(s)):
                if s[i] in chars:
                    end = i - 1
                    break
                else:
                    chars.add(s[i])
            length = end - start + 1
            if length > max_length:
                max_length = length
        return max_length


if __name__ == '__main__':
    sol = Solution()
    for line in sys.stdin:
        s = line.strip()
        length = sol.lengthOfLongestSubstring(s)
        print(length)
