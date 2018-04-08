# Interview Question 9.8

import sys


def count_ways(n):

    def _count_ways(amount, denoms, i, memory):
        if i == len(denoms) - 1:
            return 1
        else:
            key = (amount, i)
            if key not in memory:
                ways = 0
                coin = denoms[i]
                for count in range(amount // coin + 1):
                    new_amount = amount - (coin * count)
                    ways += _count_ways(new_amount, denoms, i + 1, memory)
                memory[key] = ways
            return memory[key]

    memory = {}
    denoms = [25, 10, 5, 1]
    return _count_ways(n, denoms, 0, memory)


if __name__ == '__main__':
    for line in sys.stdin.readlines():
        n = int(line.strip())
        print(count_ways(n))
