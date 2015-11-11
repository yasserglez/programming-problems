# Interview Question 5.1

import fileinput


def num_bit_flips(a, b):
    bit_flips = 0
    c = a ^ b
    while c > 0:
        bit_flips += c & 1
        c = c >> 1
    return bit_flips


if __name__ == '__main__':
    for line in fileinput.input():
        a, b = map(int, line.rstrip().split())
        print(num_bit_flips(a, b))
