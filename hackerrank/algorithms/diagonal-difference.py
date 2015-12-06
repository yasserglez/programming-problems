# https://www.hackerrank.com/challenges/diagonal-difference

import sys


def diagonal_difference(matrix):
    assert len(matrix) == len(matrix[0])
    n = len(matrix)
    diag1_sum = sum(matrix[i][j] for i, j in zip(range(n), range(n)))
    diag2_sum = sum(matrix[i][j] for i, j in zip(reversed(range(n)), range(n)))
    abs_diff = abs(diag1_sum - diag2_sum)
    return abs_diff


if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    matrix = []
    for i in range(n):
        row = list(map(int, f.readline().split()))
        matrix.append(row)
    print(diagonal_difference(matrix))
