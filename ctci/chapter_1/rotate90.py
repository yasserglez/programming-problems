# Interview Question 1.6

import pprint


def rotate90(image):
    n = len(image)
    for i in range(n // 2):
        for j in range(i, i + (n - 2 * i) - 1):
            tmp = (i, j), image[i][j]
            for _ in range(4):
                orig, val = tmp
                dest = (orig[1], n - orig[0] - 1)
                tmp = dest, image[dest[0]][dest[1]]
                image[dest[0]][dest[1]] = val


if __name__ == '__main__':
    for n in range(6):
        image = image = [[None] * n for i in range(n)]
        k = 1
        for i in range(n):
            for j in range(n):
                image[i][j] = k
                k += 1
        rotate90(image)
        pprint.pprint(image)
