# Interview Question 7.6

import collections
import decimal
import fileinput
import itertools


def fit_line(x, y):
    x1, x2 = map(decimal.Decimal, x)
    y1, y2 = map(decimal.Decimal, y)
    try:
        m = (y2 - x2) / (y1 - x1)
        b = y2 - m * y1
    except decimal.DivisionByZero:
        m = decimal.Decimal('Inf')
        b = None
    return m, b


def find_best_line(points):
    counter = collections.Counter()
    for x, y in itertools.combinations(points, 2):
        line = fit_line(x, y)
        counter[line] += 1
    return counter.most_common(1)[0][0]


if __name__ == '__main__':
    points = []
    for line in fileinput.input():
        point = tuple(map(float, line.split()))
        points.append(point)
    m, b = find_best_line(points)
    print(m, b)
