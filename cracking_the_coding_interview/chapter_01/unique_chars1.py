# Interview Question 1.1

# Time complexity: O(n)
# Auxiliary space complexity: O(n)

def unique_chars1(s):
    return len(s) == len(set(s))


if __name__ == '__main__':
    print(unique_chars1(""))
    print(unique_chars1("a"))
    print(unique_chars1("aa"))
    print(unique_chars1("abc"))
    print(unique_chars1("abca"))
    print(unique_chars1("abcb"))
    print(unique_chars1("abcc"))
