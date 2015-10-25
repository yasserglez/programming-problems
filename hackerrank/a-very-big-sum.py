# https://www.hackerrank.com/challenges/a-very-big-sum

import fileinput


if __name__ == '__main__':
    with fileinput.input() as fi:
        N = int(fi.readline())
        numbers = map(int, fi.readline().strip().split())
        print(sum(numbers))
