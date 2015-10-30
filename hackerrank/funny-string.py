# https://www.hackerrank.com/challenges/funny-string

import sys


def is_funny(string):
    n = len(string)
    s = [ord(c) for c in string]
    return all(abs(s[i] - s[i-1]) == abs(s[n-i-1] - s[n-i])
               for i in range(1, n))


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    for t in range(T):
        string = f.readline().rstrip()
        print(('' if is_funny(string) else 'Not ') + 'Funny')
