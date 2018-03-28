# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):

    def longestCommonPrefix(self, strs):
        prefix = []
        min_len = min((len(s) for s in strs), default=0)
        for pos in range(min_len):
            chars = set(s[pos] for s in strs)
            if len(chars) == 1:
                prefix.append(strs[0][pos])
            else:
                break
        return ''.join(prefix)


if __name__ == '__main__':
    s = Solution()

    strs = []
    print(s.longestCommonPrefix(strs))

    strs = ['', 'b']
    print(s.longestCommonPrefix(strs))

    strs = ['a', 'b', 'c']
    print(s.longestCommonPrefix(strs))

    strs = ['abcc', 'ab', 'aa']
    print(s.longestCommonPrefix(strs))

    strs = ['abc', 'abc']
    print(s.longestCommonPrefix(strs))
