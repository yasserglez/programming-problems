# https://leetcode.com/problems/edit-distance/

import sys
# import random


class Solution(object):

    def _memoize(f):
        memo = {}
        def wrapper(self, *args):
            if args not in memo:
                memo[args] = f(self, *args)
            return memo[args]
        return wrapper

    @_memoize
    def minDistance(self, w1, w2):
        l1, l2 = len(w1), len(w2)
        i = next((i for i in range(min(l1, l2)) if w1[i] != w2[i]), None)
        if i is None:
            # i) w1 and w2 are equal => 0
            # ii) w1 is shorter than w2 => insert missing chars
            # iii) w2 is longer than w2 => delete extra chars
            return abs(l1 - l2)
        else:
            operations = [
                lambda: self.minDistance(w1[i:],   w2[i+1:]),  # insert
                lambda: self.minDistance(w1[i+1:], w2[i:]),    # delete
                lambda: self.minDistance(w1[i+1:], w2[i+1:]),  # replace
            ]
            # random.shuffle(operations)
            d = max(l1, l2)
            for op in operations:
                d = min(d, 1 + op())
                if d == 1:
                    break
            return d


if __name__ == '__main__':
    s = Solution()
    f = sys.stdin
    num_test_cases = int(f.readline())
    for i in range(num_test_cases):
        w1 = f.readline().rstrip()
        w2 = f.readline().rstrip()
        print(s.minDistance(w1, w2))
