# https://www.hackerrank.com/challenges/solve-me-second

import fileinput


def solve_me_second(a, b):
    return a + b


if __name__ == '__main__':
    with fileinput.input() as fi:
        T = int(fi.readline())
        for t in range(T):
            a, b = map(int, fi.readline().strip().split())
            print(solve_me_second(a, b))
