# https://www.hackerrank.com/challenges/angry-professor

import sys


def class_cancelled(arrival_time, threshold):
    return sum(map(lambda t: t <= 0, arrival_time)) < threshold


if __name__ == '__main__':
    f = sys.stdin
    test_cases = int(f.readline())
    for i in range(test_cases):
        first_line = f.readline().strip().split()
        num_students, threshold = int(first_line[0]), int(first_line[1])
        second_line = f.readline().strip().split()
        arrival_time = list(map(int, second_line))
        print('YES' if class_cancelled(arrival_time, threshold) else 'NO')
