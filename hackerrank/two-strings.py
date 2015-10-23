# https://www.hackerrank.com/challenges/two-strings

import fileinput


def have_common_substring(A, B):
    Aset, Bset = set(A), set(B)
    return any(c in Aset for c in Bset)


if __name__ == '__main__':
    with fileinput.FileInput() as fi:
        T = int(fi.readline())
        for t in range(T):
            A = fi.readline().rstrip()
            B = fi.readline().rstrip()
            print('YES' if have_common_substring(A, B) else 'NO')
