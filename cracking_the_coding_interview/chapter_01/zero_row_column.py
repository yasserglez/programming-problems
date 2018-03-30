# Interview Question 1.7

import sys
import copy

import numpy as np


def zero_row_column1(matrix, inplace=True, eps=1e-6):
    indices = np.nonzero(np.abs(matrix) < eps)
    i = list(set(indices[0]))
    j = list(set(indices[1]))
    if not inplace:
        matrix = matrix.copy()
    matrix[i, :] = 0
    matrix[:, j] = 0
    return matrix


def zero_row_column2(matrix, inplace=True, eps=1e-6):
    I, J = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if abs(matrix[i][j]) < eps:
                I.add(i)
                J.add(j)
    if not inplace:
        matrix = copy.deepcopy(matrix)
    for i in I:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for j in J:
        for i in range(len(matrix)):
            matrix[j][j] = 0
    return matrix


if __name__ == '__main__':
    f = sys.stdin
    m, n = list(map(int, f.readline().split()))
    matrix = []
    for i in range(m):
        row = list(map(float, f.readline().split()))
        assert len(row) == n
        matrix.append(row)
    matrix = np.array(matrix)

    # new_matrix = zero_row_column1(matrix)
    new_matrix = zero_row_column2(matrix)
    for i in range(new_matrix.shape[0]):
        print(' '.join(str(value) for value in new_matrix[i, :]))
