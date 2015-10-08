# Interview Question 18.7

import fileinput


def longest_word(words):
    word_set = set(words)
    for word in sorted(words, reverse=True):
        if can_be_formed(word, word_set, True):
            return word
    return ''


def can_be_formed(s, word_set, force_split=False):
    if not s:
        return not force_split
    max_i = len(s) - 1 if force_split else len(s)
    for i in range(max_i, 0, -1):
        if s[:i] in word_set and can_be_formed(s[i:], word_set):
            return True
    return False


if __name__ == '__main__':
    words = []
    for line in fileinput.input():
        words.append(line.strip())
    print(longest_word(words))
