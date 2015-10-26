# https://www.hackerrank.com/challenges/two-strings

import sys


def have_common_substring(A, B):
    Aset, Bset = set(A), set(B)
    return any(c in Aset for c in Bset)


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    for t in range(T):
        A = f.readline().rstrip()
        B = f.readline().rstrip()
        print('YES' if have_common_substring(A, B) else 'NO')
