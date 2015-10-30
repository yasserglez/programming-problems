# https://www.hackerrank.com/challenges/computing-the-correlation

import math
import sys


def computing_the_correlation(n, x, y, z):

    Sxi = Sxi2 = 0
    Syi = Syi2 = 0
    Szi = Szi2 = 0
    Sxiyi = Syizi = Szixi = 0

    for i in range(n):
        Sxi += x[i]
        Sxi2 += x[i] ** 2

        Syi += y[i]
        Syi2 += y[i] ** 2

        Szi += z[i]
        Szi2 += z[i] ** 2

        Sxiyi += x[i] * y[i]
        Syizi += y[i] * z[i]
        Szixi += z[i] * x[i]

    compute = lambda Sai, Sai2, Sbi, Sbi2, Saibi: \
        ((n * Saibi - Sai * Sbi) /
         (math.sqrt(n * Sai2 - Sai ** 2) *
          math.sqrt(n * Sbi2 - Sbi ** 2)))

    rho_xy = compute(Sxi, Sxi2, Syi, Syi2, Sxiyi)
    rho_yz = compute(Syi, Syi2, Szi, Szi2, Syizi)
    rho_zx = compute(Szi, Szi2, Sxi, Sxi2, Szixi)

    return rho_xy, rho_yz, rho_zx


if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    M, P, C = [], [], []
    for i in range(n):
        m, p, c = list(map(int, f.readline().rstrip().split()))
        M.append(m); P.append(p); C.append(c)
    rho_MP, rho_PC, rho_CM = computing_the_correlation(n, M, P, C)
    print(round(rho_MP, 2))
    print(round(rho_PC, 2))
    print(round(rho_CM, 2))
