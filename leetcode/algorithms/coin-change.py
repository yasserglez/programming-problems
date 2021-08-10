# https://leetcode.com/problems/coin-change/

import fileinput
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        m = [0 if i == 0 else float("inf") for i in range(amount + 1)]
        for current_amount in range(1, amount + 1):
            for i in range(len(coins)):
                if coins[i] <= current_amount:
                    m[current_amount] = min(m[current_amount], 1 + m[current_amount - coins[i]])
        return -1 if m[amount] == float("inf") else m[amount]


if __name__ == "__main__":
    s = Solution()
    for line in fileinput.input():
        nums = list(map(int, line.rstrip().split()))
        amount = nums[0]
        coins = nums[1:]
        print(s.coinChange(coins, amount))
