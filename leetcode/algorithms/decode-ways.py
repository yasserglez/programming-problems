# https://leetcode.com/problems/decode-ways/

import string
import fileinput
from typing import Dict


class Solution:

    MAPPING = dict(zip(map(str, range(1, 28)), string.ascii_uppercase))

    def _numDecodings(self, s: str, mem: Dict[str, int]) -> int:
        if s in mem:
            return mem[s]

        mem[s] = 0
        if len(s) >= 1 and s[:1] in self.MAPPING:
            mem[s] += self._numDecodings(s[1:], mem)
        if len(s) >= 2 and s[:2] in self.MAPPING:
            mem[s] += self._numDecodings(s[2:], mem)
        return mem[s]

    def numDecodings(self, s: str) -> int:
        mem = {"": 1}
        return self._numDecodings(s, mem)


if __name__ == "__main__":
    s = Solution()
    for line in fileinput.input():
        print(s.numDecodings(line.strip()))
