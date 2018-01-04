# Interview Question 9.1

import sys


def count_ways(steps_left, memory=None):
    if memory is None:
        memory = [None] * steps_left

    if steps_left == 0:
        return 1
    else:
        ways = 0
        for k in {1, 2, 3}:
            if steps_left - k >= 0:
                if memory[steps_left - k] is None:
                    memory[steps_left - k] = count_ways(steps_left - k, memory)
                ways += memory[steps_left - k]
        return ways


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(count_ways(n))
