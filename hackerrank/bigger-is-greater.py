# https://www.hackerrank.com/challenges/bigger-is-greater

import sys


def bigger_is_greater(word):
    word = list(word)
    min_gt = '{'  # greater than 'z'
    i = len(word) - 2
    while i >= 0:
        for j in range(i + 1, len(word)):
            if word[i] < word[j]:
                min_gt = min(word[j], min_gt)
                min_gt_index = j
        if min_gt != '{':
            break
        i -= 1
    if min_gt == '{':
        return 'no answer'
    else:
        word[i], word[min_gt_index] = word[min_gt_index], word[i]
        word[i + 1:] = sorted(word[i + 1:])
        return ''.join(word)


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline())
    for t in range(T):
        word = f.readline().rstrip()
        print(bigger_is_greater(word))
